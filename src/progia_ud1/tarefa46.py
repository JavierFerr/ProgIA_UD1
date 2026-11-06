# Fai unha función que nos indique se todos os elementos dunha lista son pares ou non.

if __name__ == '__main__':

    lista = [1,2,3,4,5,6]

    function = lambda lista: ["Par" if num % 2 == 0 else "Impar" for num in lista]

    print(function(lista))
