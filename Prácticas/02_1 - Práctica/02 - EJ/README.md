
# Práctica 2-1 - IFD

## TP2_la_clave_equivocada

Se entrega::

* mensaje.txt
* mensaje.txt.sig
* README.txt

claves/ ├── investigacion1.asc ├── investigacion-old.asc └── investigacion-fake.asc

## Enunciado

Durante el análisis de una evidencia se recuperó un documento acompañado por una firma digital.
En el mismo directorio aparecieron varias claves públicas asociadas aparentemente a la misma identidad.
Sin embargo, que una clave tenga el nombre o la dirección de correo esperados no significa necesariamente que sea la correcta.
La documentación interna de la organización contiene un dato que puede ayudarte a identificar la clave legítima.
Analiza las claves disponibles, identifica cuál corresponde a la identidad esperada y verifica la autenticidad del mensaje.
Si la firma es válida, revisa el contenido del documento.
Encontrar la flag.

## Solución

El archivo mensaje.txt tiene la siguiente información:

>INFORME DE INVESTIGACION

>La autenticidad de este documento debe verificarse antes
de considerar su contenido válido.

>IFD{el_nombre_no_identifica_una_clave}

El archivo README.txt tiene la siguiente información:

>Durante la investigación se recuperaron tres claves públicas
asociadas a la misma identidad.

>La documentación interna indica que la firma válida corresponde
a la clave cuyo fingerprint termina en:

>CAAC 386B C89D 093C

Para ver los fingerprints de las claves tenemos que usar este comando:

> gpg --show-keys investigacion1.asc

> gpg --show-keys investigacion-old.asc

> gpg --show-keys investigacion-fake.asc

El fingerprint de investigacion1.asc termina como nos dijieron en el archivo README.txt.

Para verificar la integridad de de mensaje.txt tenemos que importar esa clave publica y verificar que coincidan las firmas.

> gpg --import investigacion1.asc

> gpg --verify mensaje.txt.sig mensaje.txt

Nos devuelve lo siguiente:

> gpg: Firmado el 08/11/26 14:42:47 Hora est ndar de Argentina
gpg:                usando RSA clave 95A0DD7DEB4C6ABCF215F3E7CAAC386BC89D093C
gpg: Firma correcta de "Unidad de Investigacion <investigacion@ifd.ctf>" [desconocido]
gpg: ATENCIÓN: ¡Esta clave no está certificada por una firma de confianza!
gpg:          No hay indicios de que la firma pertenezca al propietario.
      95A0DD7DEB4C6ABCF215F3E7CAAC386BC89D093C

Como ya verificamos que el contenido de mensaje.txt es válido, entonces podemos confiar y mandar la flag.

## Flag: IFD{el_nombre_no_identifica_una_clave}