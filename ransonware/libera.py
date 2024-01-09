import os
import pyaes

## abre o arquivo  infectado
file_name = "teste.txt.ranswareteste"
file = open(filne_name, 'rb' )
file_data = file.read()
file.close()

## Chave  para remocao

key = b'testeransoware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data =aes.decrypt(file_data)

##cria novo arquivo depois de inserir a chave correta

new_file = "teste.txt"
new_file = open(f'{new_file}' , "wb")
new_file .write(decrypt_data)
new_file.close()
