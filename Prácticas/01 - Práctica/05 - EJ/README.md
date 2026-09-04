# Práctica 1 - IFD

## TP1_no_confies_en_la_extension

Se entrega:
- evidenciaDesafio5.dat

## Enunciado

El archivo fue recuperado de espacio no asignado.
El sistema operativo no consigue identificarlo y aparentemente está dañado.
El nombre y la extensión fueron asignados automáticamente durante la recuperación.
Determinar qué tipo de archivo era y recuperar su contenido

## Solución

Tenemos que ver los primeros bytes para ver qué tipo de archivo es.

```Python
print(open('evidenciaDesafio5.dat','rb').read(16).hex())
```

Eso nos devuelve estos bytes en hex:
> 00 00 00 00 00 00 00 00 00 00 00 0d 49 48 44 52

49 48 44 52 es el chunk IHDR, el primer data block de un PNG. Con esto ya podemos identificar que se trata de un PNG. La firma fue reemplazada por 00 así que hay que reconstruirla. Normalmente siempre arranca con: 

> 89 50 4E 47 0D 0A 1A 0A
```Python
with  open("evidenciaDesafio5.dat", "rb") as  f:
	data  =  f.read()
	fixed  =  bytes([0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A]) + data[8:] 

with  open("recuperado.png", "wb") as  f:
	f.write(fixed)
```

Si abrimos el archivo que creamos ("recuperado.png"), podemos ver que es una imagen con un texto que dice IFD{magic_bytes_reveal_truth}

## Flag: IFD{magic_bytes_reveal_truth}