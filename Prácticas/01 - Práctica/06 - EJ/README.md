# Práctica 1 - IFD

## TP1_integridad_comprometida

Se entrega:
- caso.zip

Dentro

Caso/ 
├── evidencia01.dat 
├── evidencia02.dat 
├── evidencia03.dat 
├── evidencia04.dat 
└── hashes.sha256

## Enunciado

Durante la transferencia de una evidencia se generaron hashes SHA-256 de todos los archivos.
Al recibirla en el laboratorio existe la sospecha de que uno de ellos fue modificado.
Identificar el archivo cuya integridad está comprometida.
Luego analizarlo: puede contener información adicional relacionada con la alteración.
Recuperar la flag

## Solución

Primero identificamos el archivo cuya integridad está comprometida, para eso corremos:
```bash
$ sha256sum -c hashes.sha256
evidencia01.dat: OK
evidencia02.dat: OK
evidencia03.dat: FAILED
evidencia04.dat: OK
sha256sum: WARNING: 1 computed checksum did NOT match
```

Si abrimos el archivo comprometido con un editor de texto podemos ver que en la ultima linea dice:

> HIDDEN_DATA:SUZEe2ludGVncml0eV9iZWZvcmVfYW5hbHlzaXN9

Si decodificamos en base64, nos devuelve:

> IFD{integrity_before_analysis}


## Flag: IFD{integrity_before_analysis}