from conversor_letras_numeros import ConversorLetrasNumeros
from generador import GeneradorSolitario


def main():
    # Objeto que usaremos para pasar de letras a
    # números (A a 1, B a 2, ...) y viceversa
    conversor = ConversorLetrasNumeros()

    # Objeto que contiene la baraja y los algoritmos
    # para seguir cada uno de los pasos necesarios
    # para generar la clave de cifrado / descifrado
    generador = GeneradorSolitario(conversor)

    cifrar_o_descifrar = input_cifrar_o_descifrar()
    if cifrar_o_descifrar == 'C':
        texto = input('Introduce el texto a cifrar: ')
        clave = generador.generar_letras_secuencia_de_clave(len(texto))
        cifrado = cifrar(texto, clave, conversor)
        print(f'El texto {texto} cifrado es:')
        mostrar_en_bloques(cifrado)
    else:
        texto = input('Introduce el texto a descifrar: ')
        clave = generador.generar_letras_secuencia_de_clave(len(texto))
        descifrado = descifrar(texto, clave, conversor)
        print(f'El texto {texto} descifrado es:')
        mostrar_en_bloques(descifrado)


def input_cifrar_o_descifrar():
    # Función que recibe una C (para indicar cifrar)
    # o D (para indicar que el usuario desea decifrar)
    cifrar_o_descifrar = ''
    while cifrar_o_descifrar != 'C' and cifrar_o_descifrar != 'D':
        cifrar_o_descifrar = input(
            "Introduce C para cifrar o D para descifrar: ")
        cifrar_o_descifrar = cifrar_o_descifrar.upper()
    return cifrar_o_descifrar


def mostrar_en_bloques(texto):
    # Función que muestra las letras separadas en bloques
    # de 5
    for posicion, letra in enumerate(texto):
        print(letra, end='')
        if (posicion + 1) % 5 == 0:
            print(' ', end='')
    print()


def cifrar(texto, clave, conversor):
    # Pasos a seguir para el cifrado, siendo estos convertir a
    # numeros tanto el texto original como la clave, sumarlos
    # y convertir el resultado en texto otra vez
    numeros_original = lista_numerica_desde_texto(texto, conversor)
    numeros_clave = lista_numerica_desde_texto(clave, conversor)
    numeros_combinados = sumar_numeros(numeros_original, numeros_clave)
    texto_cifrado = texto_desde_lista_numerica(numeros_combinados, conversor)
    return texto_cifrado


def descifrar(texto, clave, conversor):
    # Pasos a seguir para el descifrado, siendo estos convertir a
    # números tanto el texto cifrado como la clave, restarlos
    # y convertir el resultado en texto otra vez
    numeros_original = lista_numerica_desde_texto(texto, conversor)
    numeros_clave = lista_numerica_desde_texto(clave, conversor)
    numeros_combinados = restar_numeros(numeros_original, numeros_clave)
    texto_cifrado = texto_desde_lista_numerica(numeros_combinados, conversor)
    return texto_cifrado


def texto_desde_lista_numerica(numeros, conversor):
    # Convierte en un String una lista de números, utilizando
    # un objeto de tipo ConversorLetrasNumeros
    resultado = ''
    for numero in numeros:
        letra = conversor.transformar_valor_a_letra(numero)
        resultado += letra
    return resultado


def lista_numerica_desde_texto(texto, conversor):
    # Convierte una lista de números a un String, utilizando
    # un objeto de tipo ConversorLetrasNumeros
    resultado = []
    for letra in texto:
        if letra != ' ':
            resultado.append(conversor.transformar_letra_a_valor(letra))
    return resultado


def sumar_numeros(lista1, lista2):
    # Función que recibe dos listas y devuelve una con la
    # suma de cada uno de los elementos
    resultado = []
    i = 0
    while i < len(lista1):
        valor = (lista1[i] + lista2[i]) % 26
        resultado.append(valor)
        i += 1
    return resultado


def restar_numeros(lista1, lista2):
    # Función que recibe dos listas y devuelve una con la
    # resta de cada uno de los elementos
    resultado = []
    i = 0
    while i < len(lista1):
        if lista1[i] < lista2[i]:
            lista1[i] += 26
        valor = lista1[i] - lista2[i]
        resultado.append(valor)
        i += 1
    return resultado


if __name__ == "__main__":
    main()
