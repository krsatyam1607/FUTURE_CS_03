# Secure File Upload/Download Portal with AES Encryption

## Project Overview

A simple web app that lets users upload and download files securely. Every file is **AES-256 encrypted** before being saved and decrypted when downloaded — keeping your data safe at rest.

---

## Features

- AES-256 encryption for secure file storage.
- Flask backend with upload and download functionality.
- Web-based interface using HTML forms with Dark and Light theme toggle switch.
- Encryption done using PyCryptodome.
- Key is stored in a separate `key.bin` file (not to store in code repo).
- Basic error handling for missing files or bad requests.

---

## Setup Instructions

1. **Clone the repository**
    
    - `git clone https://github.com/kumar1607/FUTURE_CS_O3.git`
    - `cd FUTURE_CS_03`
2. **Installation of python**
	1. **Download Python**
	    - Go to [python.org/downloads](https://www.python.org/downloads)
	    - Click **“Download Python 3.x.x”**
	2. **Install Python**
	    - Run the installer
	    - Check **“Add Python to PATH”**
	    - Click **“Install Now”**
	3. **Verify Installation**
	    - Open Command Prompt
	    - Run: `python --version`
	    - Run: `pip --version`
3. **Install required packages**
    - :`pip install flask pycryptodome`
4. **Generate the AES encryption key**
    - Run: `python generate_key.py`
    - This creates a `key.bin` file — keep it safe and **never share** it.
5. **Create folders if missing**
    - `mkdir storage`
    - `mkdir templates`
6. **Start the Flask app**
    - `python app.py`
    - App will run at: [http://localhost:5000](http://localhost:5000/)

---

## Usage

- Go to `/upload` to select and upload a file
- Go to `/download` to retrieve a file by name (Make sure the name consist the extension of the required file too).
- Encrypted files are saved in the `storage/` folder with a `.enc` extension.

---

## Important Notes

- The `key.bin` file is critical for encryption/decryption and must be kept **private**.
- There’s **no login system** — use only in trusted environments or for learning purposes.
- HTTPS is **not set up by default** — use SSL for secure file transfer in production.
- Temporary decrypted files may remain — improve cleanup in future updates.

---

## Technologies Used

- Python
- Flask
- PyCryptodome

---
