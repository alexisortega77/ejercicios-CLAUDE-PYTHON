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

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name    = name
        self.hp      = hp
        self.attack  = attack
        self.defense = defense

    def take_damage(self, damage):
        real_damage = max(0, damage - self.defense)
        self.hp     = max(0, self.hp - real_damage)
        return real_damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} | HP: {self.hp}"


class Warrior(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)
        self.bonus_attack = 10

    def attack_target(self, target):
        damage = self.attack + self.bonus_attack
        real   = target.take_damage(damage)
        return f"{self.name} attacks {target.name} for {real} damage. {target.name} HP: {target.hp}"


class Mage(Character):
    def __init__(self, name, hp, attack, defense, magic):
        super().__init__(name, hp, attack, defense)
        self.magic = magic

    def attack_target(self, target):
        damage = self.attack + self.magic
        real   = target.take_damage(damage)
        return f"{self.name} casts spell on {target.name} for {real} damage. {target.name} HP: {target.hp}"


class Battle:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def start(self):
        turn = 1
        print(f"⚔️  {self.fighter1.name} vs {self.fighter2.name}")
        print("=" * 40)

        while self.fighter1.is_alive() and self.fighter2.is_alive():
            print(f"\n--- Turn {turn} ---")
            print(self.fighter1.attack_target(self.fighter2))
            if self.fighter2.is_alive():
                print(self.fighter2.attack_target(self.fighter1))
            turn += 1

        winner = self.fighter1 if self.fighter1.is_alive() else self.fighter2
        print(f"\n{'=' * 40}")
        print(f"🏆 {winner.name} wins in {turn - 1} turns!")


warrior = Warrior("Arthas", hp=100, attack=25, defense=10)
mage    = Mage("Jaina", hp=80, attack=15, defense=5, magic=20)

battle  = Battle(warrior, mage)
battle.start()