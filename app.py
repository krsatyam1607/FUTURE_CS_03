from flask import Flask, request, send_file, render_template, redirect, url_for
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)

# Load the AES key
with open('key.bin', 'rb') as f:
    key = f.read()

def encrypt_file(file_data, key):
    iv = get_random_bytes(16)  # Initialization vector
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted = iv + cipher.encrypt(file_data)
    return encrypted

def decrypt_file(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(encrypted_data[16:])

@app.route('/')
def home():
    return redirect(url_for('upload_form'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        files = request.files.getlist('file')
        uploaded_filenames = []
        for f in files:
            data = f.read()
            encrypted = encrypt_file(data, key)
            save_path = os.path.join('storage', f"{f.filename}.enc")
            with open(save_path, 'wb') as out_file:
                out_file.write(encrypted)
            uploaded_filenames.append(f.filename)
        return render_template('upload_success.html', filenames=uploaded_filenames)
    return render_template('upload.html')

@app.route('/download', methods=['GET'])
def download_form():
    filename = request.args.get('filename')
    if not filename:
        return render_template('download.html', error=None)
    try:
        enc_path = os.path.join('storage', f"{filename}.enc")
        with open(enc_path, 'rb') as in_file:
            encrypted = in_file.read()
        decrypted = decrypt_file(encrypted, key)
        tmp_path = os.path.join('storage', f"{filename}.tmp")
        with open(tmp_path, 'wb') as tmp_file:
            tmp_file.write(decrypted)
        return send_file(tmp_path, as_attachment=True, download_name=filename)
    except FileNotFoundError:
        return render_template('download.html', error='File not found!')
if __name__ == '__main__':
    app.run()
