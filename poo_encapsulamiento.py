# -*- coding: utf-8 -*-
"""POO_Encapsulamiento.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cdyFdteJePyTqXqF-pRlVdEaB4MZQVNS
"""

'''Restringir un atributo de nuestra clase'''
class Persona:
  def __init__(self, nombre, apellido, edad):
    self.__nombre=nombre #Se le agrega un doble guión bajo
    #Si sólo se le pusiera un guión, sería una buena práctica para sugerir que no se modifique
    self.apellido=apellido
    self.edad=edad

  def mostrar_detalle(self):
    print(f'Persona: {self.__nombre}, {self.apellido} {self.edad}')

persona1=Persona('José', 'Olmedo', 23)
persona1.__nombre='Marco Isaac'  #No marca error, pero está protegido y no se puede cambiar, solo internamente en la clase
persona1.mostrar_detalle()

'''PROTEGER o RESTRINGIR FUERTEMENTE un atributo de nuestra clase'''
class Persona:
  def __init__(self, nombre, apellido, edad):
    self._nombre=nombre #Se le agrega un guión bajo
    self.apellido=apellido
    self.edad=edad

  #Un decorador modifica el comportamiento de nuestro método
  #Método GET
  @property #Permite acceder al método como si llamara al atributo
  def nombre(self):
    print('Llamando método GET nombre')
    return self._nombre

  #Método SET
  @nombre.setter #Decorador para poder modificar el atributo del nombre
  def nombre(self, nombre):
    print('Llamando método SET nombre')
    self._nombre=nombre

  def mostrar_detalle(self):
    print(f'Persona: {self._nombre}, {self.apellido} {self.edad}')

persona1=Persona('José', 'Olmedo', 23)
persona1.nombre # Ya no es necesario poner parentesis porque accedo a ella como si fuera un atributo, cuando en realidad accedo al método
print('\n')
persona1.nombre='Marco Isaac'#Así podemos modificar el atributo "nombre" empleando un método que permite acceder al atributo
print(persona1.nombre)

'''Encapsulamiento de todos las atributos de mi clase'''
class Persona:
  def __init__(self, nombre, apellido, edad):
    self._nombre=nombre #Se le agrega un guión bajo para decir que lo encapsule
    self._apellido=apellido
    self._edad=edad

  #Un decorador modifica el comportamiento de nuestro método
  #Método GET
  @property #Permite acceder al método como si llamara al atributo
  def nombre(self):
    print('Llamando método GET nombre')
    return self._nombre

  #Método SET
  @nombre.setter #Decorador para poder modificar el atributo del nombre
  def nombre(self, nombre):
    print('Llamando método SET nombre')
    self._nombre=nombre

  #Metodo GET
  @property
  def apellido(self):
    print("Llamando método GET apellido")
    return self._apellido

  #Método SET
  @apellido.setter
  def apellido(self, apellido):
    print("LLamando método SET apellido")
    self._apellido=apellido

  #Método GET
  @property
  def edad(self):
    print("Llamando método GET edad")
    return self._edad

  #Método SET
  @edad.setter
  def edad(self, edad):
    print("Llamando método SET edad")
    self._edad=edad

  def mostrar_detalle(self):
    print(f'Persona: {self._nombre}, {self._apellido} {self._edad}')

  def __del__(self):
    print(f'Persona: {self._nombre} {self._apellido} eliminado')

persona1=Persona('José', 'Olmedo', 23)
persona1.nombre='Marco Isaac'#Así podemos modificar el atributo "nombre" empleando un método que permite acceder al atributo
print('\n')

persona1.apellido='Olmedo Guevara'
persona1.edad=30
persona1.mostrar_detalle()

# from Persona import Persona #Del archivo persona importa la clase o módulo "Persona"
'''Cuando ejecutamos el siguiente comando: print(__name__) y nos devuelve __main__ significa
que este código es el programa principal a ejecutar y será el que se ejecutará en producción.

He ahí la famosa if(__name__)=__main__ si es positivo, se ejecutará el código del archivo en el que estamos trabajando

persona1.mostrar_detalle()'''

print('Creación de objetos'.center(50,'*'))
'''El modificador .center() primero recibe el número de caracteres con los cuales quiero centrar
y  el segundo es con que carácter quieres que se rellenen esos espacios.'''
persona1.mostrar_detalle()
print('\n')
print('Eliminación de objetos'.center(50,'*'))
del persona1

