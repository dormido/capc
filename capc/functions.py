import os, sys

def get_translations(language):
    translations = {
    "es": {
        "gender": "¿Cual es tu género? \n1.Hombre\n2.Mujer\n3.Hombre afeminado\n4.Dama con Rama",
        "weight": "¿Cuanto pesas?",
        "tam": "¿Tasa máxima de alcoholemia permitida? \n1. 0,5 g/L\n2. 0,3 g/L (Nóveles y profesionales)"
    },
    "en": {
        "gender": "¿What's your gender? \n1.Man\n2.Woman\n3.Tomboy\n4.Surprise girl",
        "weight": "¿What's your weight?",
        "tam": "¿Maximum alcohol tax allowed? \n1.0,5 g/L\n2.0,3 g/L (New driver and professionals)"
    },
    "ca": {
        "gender": "¿Quin es el teu génere? \n1.Home\n2.Dona\n3.Home afeminat\n4.Dona amb pirola",
        "weight": "¿Cuanto pesas?",
        "tam": "¿Tasa máxima de alcoholemia permessa? \n1.0,5 g/L\n2.0,3 g/L (Novel i professionals)"
    },
   }
    return translations.get(language, translations["es"])


def data(gender, weight, tam):
    if gender == 1 or 4:
        k = 0,7