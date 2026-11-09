from datetime import datetime, timezone, timedelta


class AnomalyDetector:

    def __init__(self):
        self.request_history = {}
        self.previous_scopes = {}
        self.expired_tokens = set()

    # Print anomaly alert
    def alert(self, identity, event_type, reason):
        print("\n🚨 ANOMALY DETECTED")
        print("Timestamp:", datetime.now(timezone.utc).isoformat())
        print("Identity:", identity)
        print("Event Type:", event_type)
        print("Reason:", reason)

    # 1. Detect unusual API request volume
    def check_api_volume(self, identity, current_time):
        if identity not in self.request_history:
            self.request_history[identity] = []

        self.request_history[identity].append(current_time)

        # Keep requests from the last 60 seconds
        recent_requests = [
            timestamp
            for timestamp in self.request_history[identity]
            if current_time - timestamp <= timedelta(seconds=60)
        ]

        self.request_history[identity] = recent_requests

        if len(recent_requests) > 20:
            self.alert(
                identity,
                "API_VOLUME_SPIKE",
                f"{len(recent_requests)} requests detected within 60 seconds"
            )

    # 2. Detect unexpected permission scope changes
    def check_scope_change(self, identity, current_scope):
        if identity in self.previous_scopes:
            old_scope = self.previous_scopes[identity]

            if old_scope != current_scope:
                self.alert(
                    identity,
                    "SCOPE_CHANGE",
                    f"Scope changed from {old_scope} to {current_scope}"
                )

        self.previous_scopes[identity] = current_scope

    # 3. Detect reuse of an expired token
    def check_token_reuse(
        self, identity, token_id, expiry_time, current_time
    ):
        if token_id in self.expired_tokens:
            self.alert(
                identity,
                "EXPIRED_TOKEN_REUSE",
                "Previously expired token was reused"
            )
            return

        if current_time >= expiry_time:
            self.expired_tokens.add(token_id)
            print("Token expired:", token_id)


# Run demonstration tests
detector = AnomalyDetector()

identity = "agent-001"
now = datetime.now(timezone.utc)

# TEST 1: API volume spike
print("\nTEST 1: API volume spike")

for i in range(21):
    detector.check_api_volume(
        identity,
        now + timedelta(seconds=i)
    )

# TEST 2: Scope change
print("\nTEST 2: Scope change")

detector.check_scope_change(identity, "read:data")
detector.check_scope_change(identity, "read:data write:admin")

# TEST 3: Expired token reuse
print("\nTEST 3: Expired token reuse")

token_id = "mock-token-001"
expiry_time = now + timedelta(seconds=5)

# First, mark the token as expired
detector.check_token_reuse(
    identity,
    token_id,
    expiry_time,
    now + timedelta(seconds=10)
)

# Then, simulate reuse of the same expired token
detector.check_token_reuse(
    identity,
    token_id,
    expiry_time,
    now + timedelta(seconds=11)
)

