# Observatorio Astronómico <img src="https://camo.githubusercontent.com/cd122cf1a24b8e8ccb81d65d3995ce9b80cc22d315c9409e09d80aad389006a3/68747470733a2f2f656d6f6a69732e736c61636b6d6f6a69732e636f6d2f656d6f6a69732f696d616765732f313537393231363131312f373535302f70696b616368755f776176652e6769663f31353739323136313131" data-canonical-src="https://emojis.slackmojis.com/emojis/images/1579216111/7550/pikachu_wave.gif?1579216111" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage"></strong></h1>

Este proyecto simula un observatorio astronómico que puede gestionar planetas y sus satélites naturales. Está compuesto por tres clases principales: `SateliteNatural`, `Planeta` y `Observatorio`.

## Clases y Métodos

### Clase `SateliteNatural`

Representa un satélite natural con nombre, excentricidad e inclinación orbital.

#### Métodos

- **`__init__(self, nombre, excentricidad, inclinacionOrbital)`**: Constructor para inicializar los atributos del satélite.
- **`getNombre(self)`**: Devuelve el nombre del satélite.
- **`getExcentricidad(self)`**: Devuelve la excentricidad del satélite.
- **`getInclinacion(self)`**: Devuelve la inclinación orbital del satélite.
- **`setExcentricidad(self, nExcentricidad)`**: Establece una nueva excentricidad para el satélite.
- **`setInclinacion(self, nInclinacion)`**: Establece una nueva inclinación orbital para el satélite.

### Clase `Planeta`

Representa un planeta con nombre, distancia media al Sol, excentricidad, periodo orbital sinódico, velocidad orbital e inclinación. Además, puede tener una lista de satélites naturales.

#### Métodos

- **`__init__(self, nombre, distanciaMediaSol, excentricidad, PeriodoOrbitalSinodico, velocidadOrbital, inclinacion)`**: Constructor para inicializar los atributos del planeta.
- **`getNombre(self)`**: Devuelve el nombre del planeta.
- **`getDistanciaMediaSol(self)`**: Devuelve la distancia media al Sol del planeta.
- **`getInclinacion(self)`**: Devuelve la inclinación del planeta.
- **`agregarSateliteNatural(self, satelite)`**: Agrega un satélite natural a la lista de satélites del planeta.
- **`eliminarSatelite(self, nombre)`**: Elimina un satélite de la lista de satélites del planeta por su nombre.
- **`editarSatelite(self, nombre, valorModificar, nuevoValor)`**: Edita un atributo específico de un satélite del planeta.
- **`getCantidadSatelites(self)`**: Devuelve la cantidad de satélites del planeta.
- **`getSatelites(self)`**: Devuelve la lista de satélites del planeta.
- **`buscarSatelite(self, nombre)`**: Busca un satélite por su nombre y lo devuelve.

### Clase `Observatorio`

Gestiona una lista de planetas y sus satélites.

#### Métodos

- **`__init__(self)`**: Constructor que inicializa un observatorio con capacidad para 8 planetas.
- **`getNombrePlanetas(self)`**: Imprime y devuelve los nombres de los planetas en el observatorio.
- **`getSateliteNatural(self, nombre)`**: Busca y devuelve un satélite natural por su nombre en todos los planetas.
- **`getPlanetaPorDistancia(self, distancia)`**: Devuelve un planeta por su distancia media al Sol.
- **`getPlanetaPorInclinacion(self, inclinacion)`**: Devuelve un planeta por su inclinación.
- **`agregarSateliteNatural(self, planetaDelSatelite, satelite)`**: Agrega un satélite natural a un planeta específico.
- **`eliminarSatelite(self, planetaDelSatelite, sateliteRemover)`**: Elimina un satélite natural de un planeta específico.
- **`editarSatelite(self, nombrePlaneta, nombreSatelite, valor_a_Modificar, nuevoValor)`**: Edita un satélite natural en un planeta específico.
- **`agregarPlaneta(self, Planeta)`**: Agrega un planeta al observatorio.
- **`eliminarPlaneta(self, planeta)`**: Elimina un planeta del observatorio.

## Uso

Aquí hay un ejemplo de cómo utilizar las clases para gestionar un observatorio astronómico:

```python
from SateliteNatural import SateliteNatural
from Planeta import Planeta
from Observatorio import Observatorio

# Instanciamos el observatorio
observatorio_sanJuan = Observatorio()

# Instanciar los planetas
mercurio = Planeta("Mercurio", 2, 2, 2, 2, 2)
venus = Planeta("Venus", 4, 4, 4, 4, 4)
tierra = Planeta("Tierra", 6, 6, 6, 6, 6)
marte = Planeta("Marte", 8, 8, 8, 8, 8)
jupiter = Planeta("Jupiter", 10, 10, 10, 10, 10)
saturno = Planeta("Saturno", 12, 12, 12, 12, 12)
urano = Planeta("Urano", 14, 14, 14, 14, 14)
neptuno = Planeta("Neptuno", 16, 16, 16, 16, 16)
pluton = Planeta("Pluton", 18, 18, 18, 18, 18)  # Planeta a eliminar

# Agregamos los planetas
observatorio_sanJuan.agregarPlaneta(mercurio)
observatorio_sanJuan.agregarPlaneta(venus)
observatorio_sanJuan.agregarPlaneta(tierra)
observatorio_sanJuan.agregarPlaneta(jupiter)
observatorio_sanJuan.agregarPlaneta(saturno)
observatorio_sanJuan.agregarPlaneta(urano)
observatorio_sanJuan.agregarPlaneta(neptuno)

observatorio_sanJuan.agregarPlaneta(pluton)  # Esto debería fallar al exceder el límite

# Instanciamos algunos satélites
luna = SateliteNatural("Luna", 1, 1)
metis = SateliteNatural("Metis", 2, 2)
fogos = SateliteNatural("Fogos", 5, 5)

# Agregamos los satélites a los planetas correspondientes
observatorio_sanJuan.agregarSateliteNatural("Tierra", luna)
observatorio_sanJuan.agregarSateliteNatural("Marte", fogos)
observatorio_sanJuan.agregarSateliteNatural("Jupiter", metis)

# Mostramos los planetas
observatorio_sanJuan.getNombrePlanetas()

# Eliminamos un planeta
observatorio_sanJuan.eliminarPlaneta("Pluton")

# Mostramos nuevamente los planetas
observatorio_sanJuan.getNombrePlanetas()

# Editar satélite
observatorio_sanJuan.editarSatelite("Tierra", "Luna", "excentricidad", 0.0549)
