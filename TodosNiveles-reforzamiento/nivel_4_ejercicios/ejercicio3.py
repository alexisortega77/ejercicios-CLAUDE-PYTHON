# ------------------------------------------------------------
# EJERCICIO 3 — Fácil
# Dado un diccionario de países y sus capitales,
# implementa búsqueda en ambas direcciones.
# ------------------------------------------------------------
paises = {
    "México": "Ciudad de México",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Australia": "Canberra"
}

# Output esperado:
# capital_de("México")    → Ciudad de México
# capital_de("Italia")    → País no encontrado
# pais_de("Tokio")        → Japón
# pais_de("Londres")      → Capital no encontrada
def normalizar(texto):
    texto = texto.lower()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"
    }
    for a, b in reemplazos.items():
        texto = texto.replace(a, b)
    return texto


def capital_de(pais):
    pais = normalizar(pais)
    for p, c in paises.items():
        if normalizar(p) == pais:
            return c
    return "País no encontrado"


def pais_de(capital):
    capital = normalizar(capital)
    for p, c in paises.items():
        if normalizar(c) == capital:
            return p
    return "Capital no encontrada"

print(capital_de("MexICO"))
print(pais_de("Tokio"))