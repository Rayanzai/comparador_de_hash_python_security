import hashlib

arquivo_1 = "a.txt"
arquivo_2 = "b.txt"

hash1 = hashlib.new("ripemd160") #tipo de chave hash
hash1.update(open(arquivo_1, "rb").read()) #Abertura do arquivo em modo binária, leitura e 

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo_2, "rb").read())

if hash1.digest() != hash2.digest(): #.digest() resume os bytes do metodo .Update
    print(f"O arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}.")
    print(f"O hash do arquivo {arquivo_1} é:", hash1.hexdigest()) #.hexdigest() mostra o hash em haxadecimal
    print(f"O hash do arquivo {arquivo_2} é:", hash2.hexdigest())
else:
    print(f"O arquivo: {arquivo_1} é igual ao arquivo: {arquivo_2}.")
    print(f"O hash do arquivo {arquivo_1} é:", hash1.hexdigest())
    print(f"O hash do arquivo {arquivo_2} é:", hash2.hexdigest())
