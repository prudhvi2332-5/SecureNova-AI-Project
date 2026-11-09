print("=" * 95)
print("SECURENOVA AI - BEFORE AND AFTER SECURITY COMPARISON")
print("=" * 95)

# BEFORE DEFENSIVE CONTROLS
# Format: Attack, Attempts, Successful Attacks
before = [
    ("Indirect Prompt Injection", 3, 3),
    ("Agent Identity Spoofing", 1, 1),
    ("System Prompt Extraction", 5, 3),
    ("RAG Poisoning and MCP Abuse", 1, 1),
    ("Suffix Injection", 1, 1)
]

# AFTER DEFENSIVE CONTROLS
# Illustrative results: replace with measured test results.
after = [
    ("Indirect Prompt Injection", 3, 0),
    ("Agent Identity Spoofing", 1, 0),
    ("System Prompt Extraction", 5, 0),
    ("RAG Poisoning and MCP Abuse", 1, 0),
    ("Suffix Injection", 1, 0)
]

print("\nBEFORE vs AFTER DEFENSIVE CONTROLS")
print("-" * 95)

print(
    f"{'ATTACK':<32}"
    f"{'BEFORE':>12}"
    f"{'AFTER':>12}"
    f"{'IMPROVEMENT':>18}"
)

print("-" * 95)

total_before_attempts = 0
total_before_success = 0
total_after_attempts = 0
total_after_success = 0

for old, new in zip(before, after):

    name, attempts_before, success_before = old
    _, attempts_after, success_after = new

    before_rate = (success_before / attempts_before) * 100
    after_rate = (success_after / attempts_after) * 100

    if before_rate > 0:
        improvement = (
            (before_rate - after_rate) / before_rate
        ) * 100
    else:
        improvement = 0

    print(
        f"{name:<32}"
        f"{before_rate:>10.1f}%"
        f"{after_rate:>10.1f}%"
        f"{improvement:>16.1f}%"
    )

    total_before_attempts += attempts_before
    total_before_success += success_before

    total_after_attempts += attempts_after
    total_after_success += success_after

print("-" * 95)

before_overall = (
    total_before_success / total_before_attempts
) * 100

after_overall = (
    total_after_success / total_after_attempts
) * 100

overall_improvement = (
    (before_overall - after_overall) / before_overall
) * 100

print(f"\nBEFORE ATTACK SUCCESS RATE: {before_overall:.1f}%")
print(f"AFTER ATTACK SUCCESS RATE: {after_overall:.1f}%")
print(f"OVERALL IMPROVEMENT: {overall_improvement:.1f}%")

print("\nNOTE: Post-defense values are illustrative.")
print("Replace them with actual measured defensive test results.")

print("\nCOMPARISON MATRIX GENERATED")
print("=" * 95)
