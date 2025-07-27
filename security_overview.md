# Security Overview – Secure File Upload/Download Portal - FUTURE_CS_03

---

## 1. Encryption at Rest 

- Files are encrypted using AES-256 before saving.
- A random Initialization Vector (IV) is generated per file to ensure uniqueness.
- The IV is prepended to the encrypted file data for proper decryption later.
- PyCryptodome is used for all encryption/decryption tasks.

---

## 2. Key Management 

- A single 256-bit AES key is generated and stored in a `key.bin` file.
- The key is never committed to version control and is excluded using `.gitignore`.
- In production, the key should be stored securely using environment variables or secrets managers like AWS KMS or Vault.
- Exposure of the key compromises all encrypted files — handle with strict care.

---

## 3. Data Transmission

- Development uses HTTP for simplicity.
- In production, the application must run over HTTPS with valid SSL certificates.
- Flask supports SSL configuration for both self-signed and CA-issued certs.
- HTTPS protects against eavesdropping and tampering during file transfer.

---

## 4. Access Control 

- Currently, there is no authentication or authorization.
- Any user with access to the server can upload or download files.
- For production, implement user authentication, session handling, and access restrictions based on roles.

---

## 5. Limitations & To-Do

- File names are stored in plain text and not encrypted.
- Decrypted files are temporarily saved during download but not securely wiped.
- No upload size limit or file type validation — can lead to denial-of-service or injection risks.

**Planned Improvements:**

- Add user login and session-based access control.
- Encrypt filenames or store them with hashed identifiers.
- Implement secure deletion of temporary files.
- Validate and sanitize file inputs.
- Set upload size and type restrictions.
- Add audit logging and monitoring for security events.

---
## Summary

- Files are encrypted at rest using AES-256 with random IVs.  
- Key management is isolated from version control but needs secure production storage.  
- HTTPS must be enforced in production for safe data transfer.  
- The portal is a secure starting point but requires authentication, input validation, and better temp file handling for real-world use.
