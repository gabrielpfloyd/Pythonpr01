'''
Created on 26 abr. 2017

@author: gasantil
'''

#CREAR la clase ANIMAL
class animal:
    def __init__(self, alimento):
        self.alimento = alimento
        print("tenemos", alimento, "kilos")
        
    def caminar(self):
        if self.alimento > 0:
            return("Camina!")
        else:
            return("Parar!")
            
    def correr(self):
        if self.alimento > 0:
            self.alimento -= 1
            return ("quedan", self.alimento,"kilos")
        else:
            return("se paro")
            
#Crear los objetos

humano = animal(30)
print (humano.alimento)
print (humano.caminar())
#humano.correr()

while humano.caminar() == "Camina!":
    print(humano.correr())
    

print(humano.correr())