import hashlib
import bcrypt

password = "SecurePass123"

# SHA-256 Hash
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# bcrypt Hash
bcrypt_hash = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print("===== SHA-256 =====")
print(sha256_hash)

print("\n===== bcrypt =====")
print(bcrypt_hash.decode())