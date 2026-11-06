# Unha inmobiliaria dunha cidade manexa unha lista de inmobles como a seguinte:

# [{'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe':  True, 'zona': 'A'},
# {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe':  True, 'zona': ' B'},
# {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe':  False, 'zona': 'A'},
# {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe':  True, 'zona': ' B'},
# {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe':  False, 'zona': 'A'}]

# Construír unha función que permita facer a procura de inmobles en función dun orzamento dado.
# A función recibirá como entrada a lista de inmobles e un prezo, e devolverá outra lista cos inmobles onde o prezo sexa menor ou igual que o dado.
# Os inmobles da lista que se devolva deben incorporar un novo atributo do a cada dicionario co prezo do inmoble,
# onde o prezo dun inmoble calcúlase coa seguinte fórmula en función da zona:

# Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
# Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5

# Para isto, parte inicialmente dunha función que a partires dun diccionario que representa a un dos inmobles obteña o seu prezo.
# A partires desa función e as ferramentas que Python podes ir construíndo o resto.

from datetime import date


if __name__ == '__main__':

    inmuebles = [
        {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
        {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': ' B'},
        {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A'},
        {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': ' B'},
        {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A'},
    ]

    calcular_prezo = lambda inmueble: (
        inmueble["metros"] * 1000
        + inmueble["habitacións"] * 5000
        + inmueble["garaxe"] * 15000
    ) * (1 - (date.today().year - inmueble["ano"]) / 100) if inmueble["zona"] == "A" else (
        inmueble["metros"] * 1000
        + inmueble["habitacións"] * 5000
        + inmueble["garaxe"] * 15000
    ) * (1 - (date.today().year - inmueble["ano"]) / 100) * 1.5

    buscar_inmobles = lambda inmuebles, prezodado: [
        dict(inmueble, prezo=calcular_prezo(inmueble))
        for inmueble in inmuebles
        if (calcular_prezo(inmueble)) <= prezodado
    ]
    
    print(f"\n{buscar_inmobles(inmuebles, 100000)}\n")