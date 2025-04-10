import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys

def decrypt_aes_gcm(base64_ciphertext):
    # Read the IV and key from their respective files
    with open('./iv', 'r') as iv_file:
        iv = bytes.fromhex(iv_file.read().strip())
    with open('./key', 'r') as key_file:
        key = bytes.fromhex(key_file.read().strip())

    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(base64_ciphertext)

    # Extract the actual ciphertext and the tag (last 16 bytes)
    tag = ciphertext[-16:]
    encrypted_data = ciphertext[:-16]

    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

    # Decrypt and return the plaintext
    plaintext = cipher.decrypt_and_verify(encrypted_data, tag)
    return plaintext

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypto.py <base64_ciphertext>")
        sys.exit(1)

    base64_ciphertext = sys.argv[1]
    plaintext = decrypt_aes_gcm(base64_ciphertext)
    print(plaintext.decode('utf-8'))