# Práctica 1 - IFD

## TP1_la_clave_está_cerca

Se recuperó un pequeño mensaje de una aplicación:
> 1c08082b2d213e0f3b2b293426112d0f3e2b352d

Del mismo directorio se recuperó una nota:
> “No era necesario inventar una clave complicada. Cuatro letras alcanzaban. La universidad siempre estuvo presente.”

Recuperar el mensaje.

## Solución

En la nota nos están dando como pista que "UNLP" es una key. Primero la paso a hex:

> 75 6e 6c 70

Y ahora pruebo haciendole un XOR al mensaje que se recibió usando como key unlp en hex:

> IFD{xor_needs_a_key}

## Flag: IFD{xor_needs_a_key}