import hashlib

hash_recuperado = "72d1e5db5fe55a4d10d26aecc20afbe95cd8a2f8ebd9559b9a05b1da9428de1f"

with open("diccionario_ifd.txt", "r", encoding="utf-8") as f:
    for linea in f:
        palabra = linea.strip()
        if hashlib.sha256(palabra.encode()).hexdigest() == hash_recuperado:
            print(palabra)