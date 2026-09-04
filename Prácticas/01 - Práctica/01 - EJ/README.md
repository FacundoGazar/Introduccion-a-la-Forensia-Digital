# Práctica 1 - IFD

## TP1_capas

Durante el análisis de un archivo de texto se encontró la siguiente cadena:
> 53555a45653256755932396b6157356e58326c7558327868655756796333303d

Sabemos que el mensaje fue ocultado aplicando más de una transformación. 
Recuperar el mensaje original

## Solución

La cadena está codificada en hex, pasandola por un decodificador nos devuelve lo siguiente:

> SUZEe2VuY29kaW5nX2luX2xheWVyc30=

Esto se ve que es base64 porque tiene el = para hacer el padding. Pasandolo por un decodificador nos devuelve lo siguiente:

> IFD{encoding_in_layers}

## Flag: IFD{encoding_in_layers}


