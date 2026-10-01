import math


class Planeta:

  def __init__(
      self,
      nombre: str,
      masa: float,
      radio: float,
      distancia_al_sol: float,
      tiene_vida: bool = False,
  ):
    self.nombre = nombre
    self.masa = masa
    self.radio = radio
    self.distancia_al_sol = distancia_al_sol
    self.tiene_vida = tiene_vida

  def calcular_densidad(self) -> float:
    """Calcula la densidad media en kg/m^3."""
    volumen = (4 / 3) * math.pi * (self.radio**3)
    return self.masa / volumen

  def es_planeta_exterior(self) -> bool:
    """Determina si el planeta está a más de 5.2 UA del Sol."""
    return self.distancia_al_sol > 5.2

  def __str__(self) -> str:
    densidad = self.calcular_densidad()
    tipo = "Exterior" if self.es_planeta_exterior() else "Interior"
    vida = "Sí" if self.tiene_vida else "No"
    return (
        f"Planeta: {self.nombre} | Densidad: {densidad:.2f} kg/m³ | Tipo:"
        f" {tipo} | Vida: {vida}"
    )



tierra = Planeta(
      nombre="Tierra",
      masa=5.972e24,
      radio=6371000.0,
      distancia_al_sol=1.0,
      tiene_vida=True,
  )


jupiter = Planeta(
      nombre="Júpiter",
      masa=1.898e27,
      radio=69911000.0,
      distancia_al_sol=5.204,
      tiene_vida=False,
  )

print(tierra)
print(jupiter)