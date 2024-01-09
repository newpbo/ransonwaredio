import os
import pyaes

## abrir o arquivo  infectado

file_name = "teste.txt.ransomwareteste"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave 
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado
os.remove(file_name)

## criar o novo arquivo
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
