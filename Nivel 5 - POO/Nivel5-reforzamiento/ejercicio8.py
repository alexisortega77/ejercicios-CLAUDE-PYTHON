"""
Ejercicio 8 — Desafío
Crea un sistema de torneo con clases Player, Match y Tournament. 
Los jugadores tienen nombre y puntos (0 inicial). 
Cada partido tiene dos jugadores y un resultado.
El torneo gestiona partidos y genera una tabla de posiciones.
tournament = Tournament("Python Cup")
p1 = Player("Ana")
p2 = Player("Luis")
p3 = Player("María")

tournament.add_player(p1)
tournament.add_player(p2)
tournament.add_player(p3)

tournament.play_match(p1, p2, "Ana")      # Ana gana → 3 pts
tournament.play_match(p2, p3, "draw")     # Empate → 1 pt cada uno
tournament.play_match(p1, p3, "Ana")      # Ana gana → 3 pts

tournament.standings()
→ Python Cup Standings:
→ 1. Ana   → 6 pts
→ 2. Luis  → 1 pts
→ 3. María → 1 pts

💡 Victoria = 3 puntos, Empate = 1 punto cada uno, Derrota = 0 puntos.
"""
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
    def add_points(self, pts):
        self.points+= pts
    
    def __str__(self):
        return f"{self.name} -> {self.points} pts"
        

class Match:
    def __init__(self, player1, player2, result):
        self.player1 = player1
        self.player2 = player2
        self.result = result
    
    # ✅ Agrega un else para resultados no reconocidos
    def apply_result(self):
     if self.result == "draw":
        self.player1.add_points(1)
        self.player2.add_points(1)
     elif self.result == self.player1.name:
        self.player1.add_points(3)
     elif self.result == self.player2.name:
        self.player2.add_points(3)
     else:
         return f"Invalid result: '{self.result}'"
    
    def __str__(self):
     return f"{self.player1.name} vs {self.player2.name} → {self.result}"



class Tournament:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.matches = []

    def add_player(self, player):
        self.players.append(player)
    
    def play_match(self, player1, player2, result):
        match = Match(player1, player2, result)
        match.apply_result()
        self.matches.append(match)
    
    def standings(self):
        ordenados = sorted(self.players, key=lambda p: p.points, reverse=True)
        print(f"\n {self.name} Standings:")
        for i, player in enumerate(ordenados, start=1):
            print(f"{i}. {player}")

    def match_history(self):
        print(f"\n{self.name} Match History:")
        for match in self.matches:
            print(f" {match}")




tournament = Tournament("Python Cup")
p1 = Player("Ana")
p2 = Player("Luis")
p3 = Player("María")

tournament.add_player(p1)
tournament.add_player(p2)
tournament.add_player(p3)

tournament.play_match(p1, p2, "Ana")    # Ana gana → 3 pts
tournament.play_match(p2, p3, "draw")   # Empate → 1 pt cada uno
tournament.play_match(p1, p3, "Ana")    # Ana gana → 3 pts

tournament.standings()
tournament.match_history()