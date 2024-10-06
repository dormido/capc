import os, sys
from capc.functions import get_translations
def main():
    print("Selecciona el idioma:")
    print("1. Español\n2. Inglés\n3. Francés")
    
    option = input("Ingresa el número del idioma que deseas (1/2/3): ")
    
    if option == '1':
        Language = "es"
    elif option == '2':
        Language = "en"
    elif option == '3':
        Language = "fr"
    else:
        print("Opción no válida. Se seleccionará el idioma por defecto: Inglés.")
        Language = "es"

    messages = get_translations(Language)

    print(messages["gender"])

if __name__ == "__main__":
    main()
