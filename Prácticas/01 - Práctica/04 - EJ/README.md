# Práctica 1 - IFD

## TP1_la_foto_del_perito

Se entrega:
- Foto.png

## Enunciado

Durante el análisis de una computadora se recuperó el archivo Foto.png.
A simple vista, parece tratarse solamente de una captura de pantalla y no contiene información relevante para la investigación
Sin embargo, el archivo presenta algunas características que llaman la atención.
Junto a la evidencia se encontró la siguiente nota:
“No toda la información de una imagen está en lo que se ve. A veces conviene revisar qué dice el archivo sobre sí mismo.”
Analizar la evidencia y recuperar la flag

## Solución

El enunciado nos da una pista de que tenemos que revisar los metadatos de la imagen. Para eso voy a usar la herramienta exiftool. 
Corriendo exiftool Foto.png os devuelve un listado de todos los campos. Viendo el campo de User Comment encuentro lo siguiente:

> User Comment: ZXZpZGVuY2lh

Lo decodifico en base64 y nos da lo siguiente:

> evidencia

## Flag: IFD{evidencia}