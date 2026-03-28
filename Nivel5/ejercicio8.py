"""

**Ejercicio 8 — Desafío**
Crea un juego RPG con clases `Character`, `Warrior` y `Mage`. Implementa un sistema de combate por turnos.
```
warrior = Warrior("Arthas", hp=100, attack=25, defense=10)
mage    = Mage("Jaina", hp=80, attack=15, defense=5, magic=20)

battle  = Battle(warrior, mage)
battle.start()
→ Turn 1: Arthas attacks Jaina for 20 damage. Jaina HP: 60
→ Turn 1: Jaina casts spell on Arthas for 35 damage. Arthas HP: 65
→ ...
→ Arthas wins in X turns!
"""