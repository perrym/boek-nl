from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ToolPolicy:
    name: str
    scope: str
    write_action: bool
    allowed_parameters: set[str]
    approval_required: bool


POLICIES = {
    "document_search": ToolPolicy(
        name="document_search",
        scope="documents.read",
        write_action=False,
        allowed_parameters={"query", "max_results"},
        approval_required=False,
    ),
    "ticket_create": ToolPolicy(
        name="ticket_create",
        scope="tickets.write",
        write_action=True,
        allowed_parameters={"title", "description", "idempotency_key"},
        approval_required=True,
    ),
    "account_status_update": ToolPolicy(
        name="account_status_update",
        scope="accounts.status.write",
        write_action=True,
        allowed_parameters={"account_id", "status", "idempotency_key"},
        approval_required=True,
    ),
}


@dataclass
class RequestContext:
    user_scopes: set[str]
    approved: bool = False
    source_is_untrusted: bool = False
    log: list[str] = field(default_factory=list)


def authorize_tool_call(
    tool_name: str,
    arguments: dict[str, Any],
    context: RequestContext,
) -> tuple[bool, str]:
    policy = POLICIES.get(tool_name)
    if policy is None:
        return False, "Onbekende tool"

    if policy.scope not in context.user_scopes:
        return False, "Ontbrekende scope"

    unexpected = set(arguments) - policy.allowed_parameters
    if unexpected:
        return False, f"Niet-toegestane parameters: {sorted(unexpected)}"

    if policy.write_action and "idempotency_key" not in arguments:
        return False, "Idempotency-key ontbreekt"

    if policy.approval_required and not context.approved:
        return False, "Menselijke goedkeuring vereist"

    # Content uit documenten is data, geen autorisatie-instructie.
    if context.source_is_untrusted and policy.write_action:
        return False, "Schrijfactie mag niet rechtstreeks uit onbetrouwbare content volgen"

    context.log.append(f"ALLOW {tool_name}")
    return True, "Toegestaan"


if __name__ == "__main__":
    ctx = RequestContext(
        user_scopes={"documents.read", "tickets.write"},
        approved=False,
        source_is_untrusted=True,
    )

    ok, reason = authorize_tool_call(
        "ticket_create",
        {
            "title": "Controleer account",
            "description": "Afkomstig uit document",
            "idempotency_key": "demo-001",
        },
        ctx,
    )
    print(ok, reason)
