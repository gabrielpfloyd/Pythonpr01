#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
'''

Created on 26 abr. 2017

@author: gasantil
'''

class persona:
    def __init__(self):
        self.coleccion = []
        #self.nue_nom = input("ingrese nombre: ")
        #self.nue_eda = int(input("ingresar edad: "))
        #self.nue_dni = int(input("ingresar dni: "))
        #print("el usuario %s con %s años y DNI: %s, a sido ingresado" %(self.nue_nom,self.nue_eda,self.nue_dni))
        
    def ingresar(self):
        i = 0
        while True:
            self.nue_nom = input("ingrese nombre: ")
            self.nue_eda = int(input("ingresar edad: "))
            self.nue_dni = int(input("ingresar dni: "))
            print("el usuario %s con %s años y DNI: %s, a sido ingresado INDICE: %s" %(self.nue_nom,self.nue_eda,self.nue_dni, i))
            t = [self.nue_nom,self.nue_eda,self.nue_dni]
            self.coleccion.append(t)
            select = input("¿quiere ingresar algun nuevo dato? ")
            if select == "s":
                os.system ("cls")
                i = i + 1
                continue
            elif select == "n":
                os.system ("cls")
                break
        print (len(self.coleccion), self.coleccion)
        
    def borrar(self):
        self.bus_nom = input("Ingrese el nombre para buscar: ")
        e = 0
        for self.coleccion[e] in self.coleccion:
            if self.bus_nom == self.coleccion[e][1]:
                print("es %s" % (self.coleccion[e][1]))
            else:
                continue
            e = e +1
            
        

            
            
nuevo = persona()
nuevo.ingresar()
nuevo.borrar()
#print (coleccion)
#print(nuevo.ingresar())


