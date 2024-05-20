from SateliteNatural import SateliteNatural
from Planeta import Planeta
from Observatorio import Observatorio

# instanciamos el observatorio
observatorio_sanJuan = Observatorio()

# instanciar los planetas
mercurio = Planeta("Mercurio", 2, 2, 2, 2, 2)
venus = Planeta("Venus", 4, 4, 4, 4, 4)
tierra = Planeta("Tierra", 6, 6, 6, 6, 6)
marte = Planeta("Marte", 8, 8, 8, 8, 8)
jupiter = Planeta("Jupiter", 10, 10, 10, 10, 10)
saturno = Planeta("Saturno", 12, 12, 12, 12, 12)
urano = Planeta("Urano", 14, 14, 14, 14, 14)
neptuno = Planeta("Neptuno", 16, 16, 16, 16, 16)
# planeta a eliminar
pluton = Planeta("Pluton", 18, 18, 18, 18, 18)

# agregamos los planetas
observatorio_sanJuan.agregarPlaneta(mercurio)
observatorio_sanJuan.agregarPlaneta(venus)
observatorio_sanJuan.agregarPlaneta(tierra)
observatorio_sanJuan.agregarPlaneta(jupiter)
observatorio_sanJuan.agregarPlaneta(saturno)
observatorio_sanJuan.agregarPlaneta(urano)
observatorio_sanJuan.agregarPlaneta(neptuno)

observatorio_sanJuan.agregarPlaneta(pluton)

# instanciamos algunos satelites
luna = SateliteNatural("Luna", 1, 1)
metis = SateliteNatural("Metis", 2, 2)
fogos = SateliteNatural("Fogos", 5, 5)

# agregamos las lunas a los palenas correspondientes
observatorio_sanJuan.agregarSateliteNatural(tierra, luna)
observatorio_sanJuan.agregarSateliteNatural(marte, fogos)
observatorio_sanJuan.agregarSateliteNatural(jupiter, metis)

# mostamos los planetas
print(observatorio_sanJuan.getNombrePlanetas())

# eliminamos un planeta
observatorio_sanJuan.eliminarPlaneta(pluton)

# mostramos nuevamente los planetas
observatorio_sanJuan.getNombrePlanetas()

# editar satelite
observatorio_sanJuan.editarSatelite(tierra, "Luna", 1, 41)

