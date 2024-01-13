import secrets
import string
import qrcode

def otp(message):
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    inv_dict = {letter:index for index, letter in plain_dict.items()}
    message = message.lower()
    message = ''.join(letter for letter in message if letter.isalnum())
    key = []

    while len(key) < len(message):
        key.append(secrets.choice(range(0,len(plain_dict))))

    encrypt_list = [(inv_dict[let]+ind)%len(plain_dict) for let, ind in zip(message,key)]

    return [''.join([plain_dict[ind] for ind in encrypt_list]), key]
pesan = str()
otp_encryption = otp(str(pesan))
otp_cipher = otp_encryption[0]
otp_key = otp_encryption[1]
' '.join(otp_key)

print(otp_key)



print(f'The one time pad cipher text: {otp_cipher}')

def otp_decryption(cipher_text, key):
    plain_dict = {index: letter for index, letter in enumerate(string.ascii_lowercase)}
    inv_dict = {letter:index for index, letter in plain_dict.items()}
    cipher_list = [inv_dict[let] for let in cipher_text]
  
    return ''.join([plain_dict[(c_index-key_index)%26] for c_index,key_index in zip(cipher_list, key)])

ct = otp_decryption(otp_cipher, otp_key)
print(ct)
len(otp_key) == len(otp_decryption(otp_cipher, otp_key))

img = qrcode.make(otp_cipher)
img = qrcode.make(ct)
img.save('dekrip.png')
img.save('Hasil.png')
