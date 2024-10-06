import os, sys
from functions import get_translations, data, calc
def main():
    print("Selecciona el idioma:")
    print("1. Español\n2. Inglés\n3. Català")
    
    option = input("Ingresa el número del idioma que deseas (1/2/3): ")
    
    if option == '1':
        Language = "es"
    elif option == '2':
        Language = "en"
    elif option == '3':
        Language = "ca"
    else:
        print("Opción no válida. Se seleccionará el idioma por defecto: Inglés.")
        Language = "es"

    messages = get_translations(Language)

    print(messages["gender"])
    gender = int(input())
    print(messages["weight"])
    weight = float(input())
    print(messages["tam"])
    tam = int(input())
    print(messages["drink"])
    drink = int(input())

    k, tma, wh, grad = data(gender, weight, tam, drink)  
    
    hundred = 100
    density = 0.8
    cai = calc(tma, k, wh, hundred, density, grad)

    # Imprime el resultado
    print(cai)


if __name__ == "__main__":
    main()
