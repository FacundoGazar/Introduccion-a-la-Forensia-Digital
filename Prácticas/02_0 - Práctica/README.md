# Práctica 2-0 - IFD

## PGP: firma digital y cifrado

## Enunciado

1. Conformación del grupo

Cada grupo podrá estar integrado por hasta tres estudiantes
Cada integrante deberá informar en el correo:

- Apellido y nombre. 
- Número de alumno/a. 
- Usuario de GitHub. 
- Usuario utilizado en el CTF. 
- Nombre del grupo utilizado en el CTF.

Aunque los datos del grupo sean los mismos, cada integrante deberá realizar individualmente el procedimiento de firma y cifrado y enviar su propio correo.
No se considerará válido el simple reenvío de un mensaje generado por otro integrante.

2. Generación de claves PGP

Cada estudiante deberá generar su propio par de claves PGP compuesto por:
- Una clave privada, que deberá conservar bajo su exclusivo control;
- Una clave pública, que podrá distribuir entre sus compañeros y la cátedra.

La clave privada no deberá enviarse, compartirse ni adjuntarse bajo ninguna circunstancia.
Una vez generado el par de claves, deberán identificar el fingerprint completo de la clave pública.

3. Intercambio de claves públicas

Antes de enviar el correo deberán:
- Exportar su propia clave pública. 
- Intercambiar las claves públicas entre los integrantes del grupo. 
- Importar las claves públicas de sus compañeros. 
- Importar la clave pública de la cátedra. 
- Verificar el fingerprint de la clave de la cátedra antes de utilizarla

Fingerprint de la clave PGP de la cátedra

- Sandra Zilla: 
> E20A 4D40 B889 6B9F 7B41 C867 8F1D B90B 6B8F 9DD4 
- Einar Lanfranco: 
>699B 5CD9 4C66 19BC DCE6 893D E4ED C070 3DB4 692E

La verificación del fingerprint es parte del ejercicio: no debe asumirse que una clave es correcta únicamente por el nombre o dirección de correo asociada a ella.

4. Preparación del correo

Cada integrante deberá enviar un correo electrónico que contenga los datos de todos los miembros del grupo.
El mensaje deberá incluir también el fingerprint PGP de cada integrante
Ejemplo de estructura:

Integrante 1
- Apellido y nombre:
- Número de alumno:
- Usuario de GitHub:
- Usuario CTF:
- Grupo CTF:
- Fingerprint PGP:

Integrante 2...

Además, deberán adjuntarse las claves públicas PGP de todos los integrantes del grupo.

5. Firma digital

Antes de enviar el mensaje, cada estudiante deberá firmarlo digitalmente utilizando su propia clave privada PGP.
La firma deberá permitir verificar:
- quién generó el mensaje;
- que el mensaje no fue modificado luego de ser firmado.

La firma deberá corresponder a la clave pública adjuntada por el estudiante que realiza el envío.

6. Cifrado del mensaje

Una vez firmado, el correo deberá ser cifrado mediante PGP.
El mensaje deberá poder ser descifrado por:

- todos los integrantes del grupo;
- la cátedra.

Por lo tanto, deberán seleccionarse como destinatarios de cifrado las claves públicas correspondientes a todas las personas que necesiten acceder al mensaje.
El correo deberá enviarse a las direcciones indicadas por la cátedra.

7. Respuesta de la cátedra

Una vez recibido el correo, la cátedra verificará:
- los datos informados;
-  la firma digital; 
-  la clave pública del remitente; 
-  el fingerprint informado; 
-  que el mensaje haya sido correctamente cifrado;
-  que pueda ser descifrado utilizando la clave privada correspondiente.

Si el procedimiento es correcto, el estudiante recibirá una respuesta relacionada con el desafío del CTF:

- Parece que tu equipo cumplió

La respuesta podrá encontrarse protegida mediante PGP.
Para obtener la flag será necesario:

1. descifrar el mensaje recibido;
2. verificar la firma digital de la cátedra; 
3. recuperar la flag correspondiente.

Las flags del CTF utilizan la siguiente sintaxis:

IFD{texto_de_la_flag}

## Solución

Ya tenía clave PGP creada así que ese paso no lo hago.

Exporto mi clave pública de esta manera:

> gpg --armor --export facundobarciabarate@gmail.com > facugazar.asc

Y obtengo mi fingerprint PGP para pasarsela a mis compañeros:

> gpg --fingerprint facundobarciabarate@gmail.com

> 24E5 A2AD 51EC 7648 CE18  4E69 A7AC CB44 3A88 AF1C

Importo las claves públicas de Einar y de Sandra. Para eso voy a la pagina: 
> https://keyserver.ubuntu.com/

Y pego cada fingerprint para descargar la clave pública e importarlas.

> gpg --import sandra.asc

> gpg --import einar.asc

**TERMINAR...**

## Flag: IFD{}