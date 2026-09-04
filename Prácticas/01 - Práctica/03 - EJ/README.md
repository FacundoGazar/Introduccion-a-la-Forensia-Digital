# Práctica 1 - IFD

## TP1_el_hash_no_se_descifra

Se entregan dos archivos:
- hash_idf.txt
- diccionario_ifd.txt

Contenido de hash_ifd.txt:
> 72d1e5db5fe55a4d10d26aecc20afbe95cd8a2f8ebd9559b9a05b1da9428de1f

## Enunciado

Durante una adquisición se recuperó un hash SHA-256 y un pequeño diccionario utilizado por el usuario. 
Determinar qué entrada del diccionario corresponde al hash. 
La flag deberá construirse utilizando el texto encontrado: IFD{texto_encontrado}

## Solución

Para encontrar qué entrada del diccionario corresponde al hash vamos aplicarle hash SHA-256 a todas las entradas y verificar cuál coincide con el resumen recuperado. 

```Python
import hashlib

hash_recuperado = "72d1e5db5fe55a4d10d26aecc20afbe95cd8a2f8ebd9559b9a05b1da9428de1f"

with open("diccionario_ifd.txt", "r", encoding="utf-8") as f:
    for linea in f:
        palabra = linea.strip()
        if hashlib.sha256(palabra.encode()).hexdigest() == hash_recuperado:
            print(palabra)
```

## Flag: IFD{CadenaDeCustodia}