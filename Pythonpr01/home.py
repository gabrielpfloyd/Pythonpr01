import os
import ingresar
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26 abr. 2017

@author: gasantil
'''
def menu():
    print("1- Agregar persona")
    print("2- Borrar persona")
    print("3- Imprimir lista ordenada por  nombre")
    print("4- Imprimir grafico de edades")
    
    print("5- Salir")
    
    sel_ect = input('Ingrese seleccionar opcion: ')

    if sel_ect == "1":
            os.system ("cls")
            nuevo = ingresar.persona()
            nuevo.ingresar()
    elif sel_ect == "2":
        print("opcion 2")
    elif sel_ect == "3":
        print("opcion 3")
    elif sel_ect == "4":
        print("opcion 4")
        
menu()