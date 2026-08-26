import hashlib
import json
import time
import uuid


def hash_tekst(tekst: str) -> str:
    return hashlib.sha256(tekst.encode("utf-8")).hexdigest()


def log_event(trace_id: str, agent: str, actie: str, duur_ms: int,
              status: str, model: str, input_tokens: int, output_tokens: int,
              input_tekst: str) -> None:
    event = {
        "trace_id": trace_id,
        "agent": agent,
        "actie": actie,
        "duur_ms": duur_ms,
        "status": status,
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_hash": hash_tekst(input_tekst),
    }
    print(json.dumps(event, ensure_ascii=False))

trace_id = str(uuid.uuid4())
start = time.perf_counter()
time.sleep(0.02)
log_event(trace_id, "policy-agent", "controleer beleid", int((time.perf_counter() - start) * 1000),
          "succes", "model-v1", 350, 90, "vertrouwelijke voorbeeldvraag")
