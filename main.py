import os           # for generating random bytes
import argparse     # for handling command-line arguments

class OneTimePad:
    def __init__(self, text:str = None, key:int = None):   

        # Either a key or text has to be provided
        # if both text and key are provided, the text is not used to generate a key, rather the provided key is used
        if not (text or key):
            raise ValueError("either text or key has to be provided!!")
        
        elif isinstance(key, bytes):
            self.key = key

        elif isinstance(key, int):               
            self.key = key.to_bytes(len(str(key)), byteorder = 'big')   #'big' -> converts int to big endian byte

        else:               
            # if text is only provided, generates a truly random key, same length as the text
            self.key = os.urandom(len(text))    # os.urandom() returns a byte object with random bytes

    def encrypt(self, text:str):
        encrypted = []
        # convert each character in the text and key into integers and XOR them
        for char, k_byte in zip(text, self.key):
            char_ascii = ord(char)          # Convert character to ASCII integer
            # Encrypt the text using XOR
            enc_val = char_ascii ^ k_byte   # k_byte already an integer
            encrypted.append(enc_val) 
        
        return encrypted
    
    def decrypt(self, encrypted):
        decrypted = ""
        # Decrypt the text by XORing the encrypted values with the same key
        # XORing again with the same key gives back the original character
        for enc_val, k_byte in zip(encrypted, self.key):
            decrypted_ascii = enc_val ^ k_byte 
            decrypted += chr(decrypted_ascii)    # Join all decrypted characters into a string

        return decrypted

def main():
    parser = argparse.ArgumentParser(description="One Time Pad Encryptor/Decryptor")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Encrypt Command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a string")
    encrypt_parser.add_argument("text", help="Text to encrypt")
    encrypt_parser.add_argument("--key", required=False, help="Key to use for encryption")
    # Decrypt Command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt an encrypted integers")
    decrypt_parser.add_argument("encrypted", help="Encrypted integers (space-separated)")
    decrypt_parser.add_argument("--key", required=True, help="Key used to encrypt (space-separated)")

    args = parser.parse_args()

    if args.command == "encrypt":
        if args.key:
            key_bytes = bytes(map(int, args.key.split()))
            pad = OneTimePad(text=args.text, key=key_bytes)
        else:
            pad = OneTimePad(text=args.text)

        encrypted = pad.encrypt(args.text)

        #converts all the elements in the list into strings and join them
        print("No key provided. Generated a random one time pad.")
        print("Encrypted:", ' '.join(map(str, encrypted)))  
        print("Key:      ", ' '.join(map(str, pad.key)))

    elif args.command == "decrypt":
        encrypted_list = list(map(int, args.encrypted.split()))
        key_bytes = bytes(map(int, args.key.split()))
        pad = OneTimePad(key=key_bytes)
        decrypted = pad.decrypt(encrypted_list)
        print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     x = OneTimePad("aStringwith20letters")
#     print("key in byte(s): ", x.key)
    
#     enc = x.encrypt("Exaaaaactly20letters")
#     print("\nencrypted list of integers: ", enc)

#     dec = x.decrypt(enc)
#     print("\ndecrypted string: ", dec)