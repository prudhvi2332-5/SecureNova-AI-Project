from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from pathlib import Path

# Create a folder to store the keys
key_folder = Path("keys")
key_folder.mkdir(exist_ok=True)

# Generate Ed25519 private key
private_key = Ed25519PrivateKey.generate()

# Generate public key from private key
public_key = private_key.public_key()

# Save private key
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

(key_folder / "private_key.pem").write_bytes(private_pem)

# Save public key
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

(key_folder / "public_key.pem").write_bytes(public_pem)

print("Ed25519 key pair generated successfully!")
print("Private key: keys/private_key.pem")
print("Public key: keys/public_key.pem")

