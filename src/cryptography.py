import hashlib
import rsa

def hash_transaction(transaction):
    transaction_str = str(transaction)
    transaction_hash = hashlib.sha256(transaction_str.encode()).hexdigest()
    return transaction_hash

def generate_keys():
    (public_key, private_key) = rsa.newkeys(2048)
    return public_key, private_key

def encrypt_message(message, public_key):
    message = message.encode()
    encrypted_message = rsa.encrypt(message, public_key)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message
