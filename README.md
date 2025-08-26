# How to identify a Palindrome in Python

Un Palindromo es una palabra o frase donde sus letras leidas al derecho y al revés dicen lo mismo. Por ejemplo el nombre de Ana. En la frase "yo hago yoga hoy". Hay que tomar en cuenta que se suele ignorar espacios, puntuación y tildes.

La idea es que un programa de Python pueda evaluar la frase o palabra insertada por el usuario y retorne una respuesta indicando si es o no un palindromo.

Para este programa se deben considerar los métodos de strings lower() y replace() y la técnica de slicing de indices en listas.

Considerar:

1. El usuario debera ingresar una palabra o frase
2. La frase será evaluada por el programa. Debera mantener el orden de la frase/palabra, eliminar espacios entre caracteres y al principio y final de la palabra/frase. voltear el orden e igualarlo con el orden original. Si son exactamante igual, entoces será clasificado como palindromo, si no es asi,
3. Retornar mensaje si es o no un palindromo.

Desarrollo del programa:
```python
# function to identify a palindrome
def is_palindrome():
  word_or_phrase = input('Please write a word or a phrase: ')
  characters = word_or_phrase.lower() # convert to lower case
  characters = characters.replace(' ','').strip() # replace ' ' and remove spaces at the beginning and at the end
  # evaluates if is a palindrome
  if characters == characters[::-1]: # choose all characters and sort in reverse order
    print(f"Congrats! The submitted word(s): '{word_or_phrase}' is a palindrome")
  else:
    print(f"Sorry! The submitted word(s): '{word_or_phrase}' is NOT a palindrome")
```

Conclusion:

* El programa evalua exitosamente si la palabra de entrada es o no un Palindromo.
* Se logra la unificacion de los caracteres con los métodos de string:  lower(), replace() y split()
* La funcion lower(), convierte a cualquier caracter a minuscula
* La funcion replace(), con los parametros ' ','', remueve los espacios entre caracteres
* La funcion split() remueve espacios al inicio y al final de la palabra o frase.
* El slicing [::-1] :: indica que tome todos los caracteres y -1 que lo anterior invierta el orden. 

