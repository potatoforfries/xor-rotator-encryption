# Simple One Time Pad
> ⚠️ WARNING: This is a **toy/demo implementation** of a One Time Pad cipher.  
> Reusing keys, using non-random keys, or using keys shorter than the message breaks the security completely.


A python class with simple implementation of One Time Pad encryption using bitwise XOR operations.

## Usage
```python
import OneTimePad 

# create the class object and insert the secret
# text to generate a random key of the same length as your text
otp = OneTimePad('secret text!') 

# returns an encrypted list of your text
encrypted = otp.encrypt('secret text!')

# returns a decrypted text again
decrypted = otp.decrypt(encrypted)
```
### OR (NOT RECOMMENDED)

```python
import OneTimePad

# random key input by user
Key = 123456789       #has to be an integer, byte or bit

# no need to mention text to encrypt in the class object
# parameter as its only used to generate random key
otp = OneTimePad(key=Key)  

# returns an encrypted list of your text using your custom Key
encrypted = otp.encrypt('secret text!')

# returns a decrypted text again
decrypted = otp.decrypt(encrypted)
```
### OR
by using argparse 

```bash
python main.py encrypt "aStringwith20letters"
```
Output(might be different for you as its key is randomly generated):
```
No key provided. Generated a random one time pad.
Encrypted: 122 0 102 94 150 78 72 53 166 245 98 163 24 163 166 227 170 1 61 77
Key:       27 83 18 44 255 32 47 66 207 129 10 145 40 207 195 151 222 100 79 62
```
a custom key(bytes or integers) can also be provided for encryption
**(NOT RECOMMENDED)**
```bash
python main.py encrypt --key "aStringwith20letters" "27 83 18 44 255 32 47 66 207 129 10 145 40 207 195 151 222 100 79 62"
```
decryption
```bash
python main.py decrypt --key "122 0 102 94 150 78 72 53 166 245 98 163 24 163 166 227 170 1 
61 77" "27 83 18 44 255 32 47 66 207 129 10 145 40 207 195 151 222 100 79 62" 
```
Output:
```
Decrypted: aStringwith20letters
```

+ please check the code to see how random bytes are generated and how the function works for custom usage. 

## Contributing

Pull requests are welcome. This is just a hobby project which I plan to slowly expand. 

## Explanation
```python
class OneTimePad:
    def __init__(self, text:str = None, key:int = None):   
```
* Accepts either a plaintext `text` to generate a random `key`, or an integer key if decrypting.

```python
if not (text or key):
    raise ValueError("either text or key has to be provided!!")
```
* Ensures atleast one input(text or key) is provided.
```python
elif key:
    self.key = key.to_bytes(len(str(key)), byteorder='big')
```
* Converts the integer key into a byte sequence (e.g. `12345` -> `b'\x00\x00...'`)
```pythonelse:
    self.key = os.urandom(len(text))
```
* If no key is given, generates truly random bytes of same length as `text`.
* urandom returns raw bytes — each `k_byte` is an int already.

### encrypt() Method
```python
for char, k_byte in zip(text, self.key):
    char_ascii = ord(char)
    enc_val = char_ascii ^ k_byte
    encrypted.append(enc_val)
```
* `ord(char)` converts each letter to its ASCII value.

* `k_byte` is each byte from the random key.

* XORing `char_ascii ^ k_byte` encrypts it.

* Returns a list of integers.

### decrypt() Method
```python
for enc_val, k_byte in zip(encrypted, self.key):
    decrypted_ascii = enc_val ^ k_byte
    decrypted += chr(decrypted_ascii)
```
* Repeats XOR with same key to recover original ASCII.

* `chr()` converts ASCII back to character.

* Joins decrypted string.

## Flaws
* pass integers like `1234` to use as keys but:
    * `1234` as an int becomes `b'\x04\xd2'` - too short for most texts

    * Converting int → bytes with `len(str(key))` is risky and inconsistent

## License

Not Licensed as of now

## Security Notes

This tool is a **learning project**. A true One Time Pad is secure **only if**:
- The key is truly random
- The key is as long as the plaintext
- The key is used **only once**
- The key is kept completely secret

Violating any of these rules reduces it to simple XOR encryption, which is **not secure**.