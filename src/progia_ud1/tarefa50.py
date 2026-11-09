# No sistema temos presente usuarios. Cada un deles ten un nome, un nome de usuario, un contrasinal e un número de tarxeta.
# O número de tarxeta segue a fórmula de Luhn. Os usuarios poden ter establecido o número de tarxeta ou non, en todo caso,
# se o teñen ten que seguir a fórmula.

# Pensa primeiramente que relación existe entre os usuarios e os números de Lunh, e logo implementa.

# O algoritmo de Luhn é unha fórmula de suma de comprobación sinxela que se usa para validar unha variedade de números de identificación,
# como os números de tarxeta de crédito e os números de seguridade social canadense.

# Na tarefa haberá comprobar se unha cadea determinada é válida. Para indicar que non é válida deberemos lanzar unha excepción.
# Validación do numero

# As cadeas de lonxitude 1 ou inferior non son válidas. Os espazos están permitidos na entrada, pero deben eliminarse antes de verificalos.
# Os únicos caracteres válidos son os números 0..9

class Usuario:

    def luhn(self, numtar):

        numtar_limpo = numtar.replace(" ", "")

        if len(numtar_limpo) <= 1:
            return False
            
        if not numtar_limpo.isdigit():
            return False
        
        # Convertemos todo o string a unha lista de enteiros
        lista = [int(dixito) for dixito in numtar_limpo]

        total = 0
        
        for i in range(len(lista) - 2, -1, -2):
                if lista[i] * 2 > 9:
                    lista[i] = lista[i] * 2 - 9
                else:
                    lista[i] = lista[i] * 2
        for num in lista:
            total += num

        if total % 10 == 0:
            return True
        else:
            return False

    
    def __init__(self, nome, user, contra, numtar=None):
        self._nome = nome
        self._user = user
        self._contra = contra
        self._numtar = None
        self.numtar = numtar

    @property
    def nome(self):
        return self._nome

    @property
    def user(self):
        return self._user

    @property
    def contra(self):
        return self._contra

    @property
    def numtar(self):
        return self._numtar

    @numtar.setter
    def numtar(self,valor):
        if valor is None or valor.strip() == "":
            self._numtar = None
        elif not self.luhn(valor):
            raise ValueError("Validación do numero")
        else:
            self._numtar = valor.replace(" ", "")

if __name__ == '__main__':
    numtar = input("Introduza o numero de tarxeta se o desexa\n")
    usuario1 = Usuario("Javier","Jriky","abc123.",numtar)
    print(usuario1.nome)
    print(usuario1.user)
    print(usuario1.contra)
    print(usuario1.numtar)
    numtar2 = input("Introduza o numero de tarxeta se o desexa\n")
    usuario1.numtar = numtar2