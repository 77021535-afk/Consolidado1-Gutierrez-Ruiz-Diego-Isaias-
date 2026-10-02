class CuentaBancaria:

  def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
   

  def depositar(self, monto: float):
    

  def retirar(self, monto: float):
   

  def consultar_saldo(self) -> float:
    

  def __str__(self) -> str:
    


class CuentaAhorros(CuentaBancaria):

 
  def calcular_interes(self) -> float:
    

  def __str__(self) -> str:
    


class CuentaCorriente(CuentaBancaria):

  

  def retirar(self, monto: float):
   

  def permite_sobregiro(self) -> bool:
    
  def __str__(self) -> str:
    



  
