class Automovil:

  def __init__(
      self,
      marca: str,
      modelo: str,
      velocidad_max: float,
      nivel_combustible: float,
      año_fabricacion: int,
  ):
    self.marca = marca
    self.modelo = modelo
    self.velocidad_max = velocidad_max
    self.nivel_combustible = nivel_combustible
    self.año_fabricacion = año_fabricacion

  def año_fabricacion(self) -> int:
    return self._año_fabricacion

  def año_fabricacion(self, valor: int):
    if not (1886 <= valor <= 2026):
      raise ValueError(
          f"El año de fabricación debe estar entre 1886 y 2026. Valor"
          f" ingresado: {valor}"
      )
    self._año_fabricacion = valor

  def nivel_combustible(self) -> float:
    return self._nivel_combustible

  def nivel_combustible(self, valor: float):
    if not (0.0 <= valor <= 100.0):
      raise ValueError(
          f"El nivel de combustible debe estar entre 0.0 y 100.0. Valor"
          f" ingresado: {valor}"
      )
    self._nivel_combustible = float(valor)

  def velocidad_max(self) -> float:
    return self._velocidad_max

  def velocidad_max(self, valor: float):
    if valor <= 0:
      raise ValueError(
          f"La velocidad máxima debe ser mayor a 0. Valor ingresado: {valor}"
      )
    self._velocidad_max = float(valor)

  def tiempo_llegada(self, distancia_km: float) -> float:
    """Calcula el tiempo estimado de llegada en horas."""
    return distancia_km / self.velocidad_max

  def __str__(self) -> str:
    return (
        f"Automóvil: {self.marca} {self.modelo} | Año: {self.año_fabricacion} |"
        f" Vel. Máx: {self.velocidad_max} km/h | Combustible:"
        f" {self.nivel_combustible}%"
    )



auto = Automovil(
      marca="Toyota",
      modelo="Corolla",
      velocidad_max=180.0,
      nivel_combustible=85.0,
      año_fabricacion=2022,
  )
print(auto)

distancia = 360.0
print(
      f"Tiempo para recorrer {distancia} km:"
      f" {auto.tiempo_llegada(distancia):.2f} horas"
  )

  # Prueba de validaciones
print("\n--- Demostración de captura de errores ---")
try:
    auto.año_fabricacion = 1800
except ValueError as e:
    print(f"Excepción capturada con éxito: {e}")