import json
from collections import abc

class RegAcidente(object):
   def __init__(self, id, condutoresVeiculos, passageiros, acidentes, peoes):
      self.id = id
      self.condutoresVeiculos = condutoresVeiculos
      self.passageiros = passageiros
      self.acidentes = acidentes
      self.peoes = peoes