import os

class OneTimePad:
    def __init__(self, text:str = None, key:int = None):   

        # Either a key or text has to be provided
        # if both text and key are provided, the text is not used to generate a key, rather the provided key is used
        if not (text or key):
            raise ValueError("either text or key has to be provided!!")
        elif key:               
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


if __name__ == "__main__":
    x = OneTimePad("aStringwith20letters")
    print("key in byte(s): ", x.key)
    print(len("Exaaaaactly20letters"))
    print(len("aStringwith20letters"))
    enc = x.encrypt("Exaaaaactly20letters")
    print("\nencrypted list of integers: ", enc)

    dec = x.decrypt(enc)
    print("\ndecrypted string: ", dec)