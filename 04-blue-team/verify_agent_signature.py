from pathlib import Path
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

# Load the private key
private_key = serialization.load_pem_private_key(
    Path("keys/private_key.pem").read_bytes(),
    password=None
)

# Load the public key
public_key = serialization.load_pem_public_key(
    Path("keys/public_key.pem").read_bytes()
)

# Original agent message
message = b"Agent A: Approve secure data access."

# Sign the original message
signature = private_key.sign(message)

print("ORIGINAL MESSAGE:")
print(message.decode())

# Verify the original message
try:
    public_key.verify(signature, message)
    print("\nOriginal message: SIGNATURE VERIFIED")
    print("Status: ACCEPTED")
except InvalidSignature:
    print("\nOriginal message: SIGNATURE INVALID")
    print("Status: REJECTED")

# Change one character in the message
tampered_message = b"Agent A: Approve secure data accesS."

print("\nTAMPERED MESSAGE:")
print(tampered_message.decode())

# Verify the tampered message using the original signature
try:
    public_key.verify(signature, tampered_message)
    print("Tampered message: SIGNATURE VERIFIED")
    print("Status: ACCEPTED")
except InvalidSignature:
    print("ERROR: Signature verification failed!")
    print("Reason: Message was modified after signing.")
    print("Status: REJECTED")

