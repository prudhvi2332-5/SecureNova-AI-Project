from nemoguardrails.actions import action

ATTACK_PATTERNS = [
    "ignore previous instructions",
    "trusted_orchestrator",
    "hidden system prompt",
    "mock_mcp_read_admin_status",
    "disregard all rules",
]

@action(is_system_action=True)
async def check_project_attack_payloads(context=None, **kwargs):
    context = context or {}

    message = (
        context.get("last_user_message")
        or context.get("user_message")
        or kwargs.get("user_message")
        or ""
    )

    message = str(message).lower()

    for pattern in ATTACK_PATTERNS:
        if pattern in message:
            print(f"BLOCKED: Matched attack pattern: {pattern}")
            return False

    print("PASS: No known attack pattern detected.")
    return True


