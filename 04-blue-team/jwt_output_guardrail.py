import re

# Simulated model response containing a fake JWT
model_response = """
The generated response contains this test token:
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0LXVzZXIifQ.dGhpcy1pcy1hLWZha2Utc2lnbmF0dXJl
"""

# Pattern to detect JWT-shaped strings
jwt_pattern = r'(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])'

def redact_jwt(text):
    return re.sub(jwt_pattern, "[REDACTED]", text)

print("===== OUTPUT GUARDRAIL TEST =====")
print("\nOriginal Model Response:")
print(model_response)

safe_response = redact_jwt(model_response)

print("\nProtected Model Response:")
print(safe_response)

if "[REDACTED]" in safe_response:
    print("\nStatus: JWT DETECTED AND REDACTED")
else:
    print("\nStatus: NO JWT DETECTED")
