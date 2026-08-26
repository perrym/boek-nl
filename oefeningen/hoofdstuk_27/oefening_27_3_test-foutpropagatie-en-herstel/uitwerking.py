from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class Failure(str, Enum):
    TIMEOUT = "timeout"
    INVALID_RESPONSE = "invalid_response"
    NO_EVIDENCE = "no_evidence"


@dataclass
class Trace:
    trace_id: str = field(default_factory=lambda: str(uuid4()))
    events: list[dict] = field(default_factory=list)

    def add(self, step: str, action: str, detail: str) -> None:
        self.events.append(
            {
                "trace_id": self.trace_id,
                "step": step,
                "action": action,
                "detail": detail,
            }
        )


def recovery_action(failure: Failure, retry_count: int) -> str:
    if failure == Failure.TIMEOUT:
        return "retry" if retry_count < 2 else "human_review"
    if failure == Failure.INVALID_RESPONSE:
        return "retry_with_schema" if retry_count < 1 else "stop"
    if failure == Failure.NO_EVIDENCE:
        return "human_review"
    return "stop"


def simulate(failure: Failure) -> Trace:
    trace = Trace()
    retry_count = 0
    max_steps = 5

    for step_number in range(1, max_steps + 1):
        action = recovery_action(failure, retry_count)
        trace.add(
            step=f"agent_step_{step_number}",
            action=action,
            detail=f"failure={failure.value}, retry={retry_count}",
        )

        if action.startswith("retry"):
            retry_count += 1
            continue

        if action in {"human_review", "stop"}:
            break

    return trace


if __name__ == "__main__":
    for failure in Failure:
        trace = simulate(failure)
        print(f"\nTrace {trace.trace_id} - {failure.value}")
        for event in trace.events:
            print(event)
