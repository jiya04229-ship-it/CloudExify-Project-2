from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

print("===== Fernet Encryption Demo =====")
print("\nSecret Key:")
print(key.decode())

# Sensitive data
data = b"Credit Card: 1234-5678-9012-3456"

print("\nOriginal Data:")
print(data.decode())

# Encrypt data
encrypted_data = cipher.encrypt(data)

print("\nEncrypted Data:")
print(encrypted_data.decode())

# Decrypt data
decrypted_data = cipher.decrypt(encrypted_data)

print("\nDecrypted Data:")
print(decrypted_data.decode())