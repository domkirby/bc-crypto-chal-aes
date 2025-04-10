import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys

# filepath: /home/domkirby/Documents/bc-crypto-chal-aes/encrypto.py

def encrypt_aes_gcm(plaintext):
    # Read the IV and key from their respective files
    with open('./iv', 'r') as iv_file:
        iv = bytes.fromhex(iv_file.read().strip())
    with open('./key', 'r') as key_file:
        key = bytes.fromhex(key_file.read().strip())

    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

    # Encrypt the plaintext
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    # Combine the ciphertext and tag, then encode in base64
    encrypted_data = base64.b64encode(ciphertext + tag)
    return encrypted_data.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encrypto.py <plaintext>")
        sys.exit(1)

    plaintext = sys.argv[1]
    encrypted_text = encrypt_aes_gcm(plaintext)
    print(encrypted_text)