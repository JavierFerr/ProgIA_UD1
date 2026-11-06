# Fai unha función que recolla como parámetro unha lista de números e nos indique que elementos son primos.

# Para iso, parte inicialmente dunha función que indique se un número é primo ou non e posteriormente aplica esa función a cada membro da lista
# (co mecanismo que prefiras).

def primo(num):
    
        primo = True;
        for i in range(2,(num//2)+1):
            if num % i == 0:
                primo = False
                break
        return primo

def primos(lista):
    for num in lista:
         if primo(num):
              print(f"O numero {num} e primo")

if __name__ == '__main__':
    
    lista = [1,2,3,4,5,6,7,8,9,10,93,45,78,13,11]
    primos(lista)