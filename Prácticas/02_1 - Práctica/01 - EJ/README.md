# Práctica 2-1 - IFD

## TP2_quien_lo_firmo

Se entrega::

* mensaje.txt
* mensaje.txt.sig
* clave-publica.asc

## Enunciado

Durante una investigación se recuperó un mensaje acompañado por una firma digital y una clave pública.
Determinar si el contenido fue alterado y verificar quién generó la firma.
El fingerprint puede contener información útil para continuar la investigación.
Encontrar la flag.

## Solución

Si abrimos el archivo mensaje.txt podemos ver que está escrito lo siguiente:

> Informe preliminar de evidencia
> La evidencia fue recibida y verificada correctamente.
> IFD{una_firma_tambien_es_evidencia}

Para verificar si el contenido fue modificado tenemos que importar la clave publica:

> gpg --import clave-publica.asc

Luego tenemos que verificar que el archivo mensaje.txt no se haya modificado:

> gpg --verify mensaje-txt.sig mensaje.txt

Respuesta:

> gpg: Firmado el 08/11/26 11:46:34 Hora est ndar de Argentina
gpg:                usando RSA clave 42A6B1A7F774EFF6CF8A3145C6A20F635A433C31
gpg: Firma correcta de "Perito IFD (IFD desafio CTF) <perito@ifd.ctf>" [desconocido]
gpg: ATENCIÓN: ¡Esta clave no está certificada por una firma de confianza!
gpg:          No hay indicios de que la firma pertenezca al propietario.
      42A6B1A7F774EFF6CF8A3145C6A20F635A433C31

Como verificamos que el contenido no fue modificado, podemos confiar en la flag.

## Flag: IFD{una_firma_tambien_es_evidencia}