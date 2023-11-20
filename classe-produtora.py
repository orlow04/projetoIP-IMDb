class Produtora:
  def __init__(self,nome,pais):
    self.__nome = nome
    self.__pais = pais

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @property
  def pais(self):
    return self.__pais

  @pais.setter
  def pais(self,pais):
    self.__pais = pais
