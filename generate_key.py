import os

key = os.urandom(32)  # Generate a 256-bit AES key
with open('key.bin', 'wb') as f:
    f.write(key)
print("AES key generated and saved to key.bin")
