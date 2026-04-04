"""
Ejercicio 4 — Medio
Crea una clase Playlist que gestione canciones.
 Cada canción tiene título, artista y duración en segundos. 
 Métodos: add_song(), remove_song(), total_duration(), longest_song() y __str__.
pl = Playlist("Mis favoritas")
pl.add_song("Bohemian Rhapsody", "Queen", 354)
pl.add_song("Hotel California", "Eagles", 391)
pl.add_song("Stairway to Heaven", "Led Zeppelin", 482)
pl.total_duration()   → "20:27"
pl.longest_song()     → "Stairway to Heaven (8:02)"
print(pl)
→ Playlist: Mis favoritas (3 songs)
→   1. Bohemian Rhapsody - Queen (5:54)
→   2. Hotel California - Eagles (6:31)
→   3. Stairway to Heaven - Led Zeppelin (8:02)

💡 Para convertir segundos a mm:ss: minutos = segundos // 60, segs = segundos % 60
"""
class Song:
    def __init__(self, title, artist, duration):
        self.title    = title
        self.artist   = artist
        self.duration = duration

class Playlist:
    def __init__(self, name):
        self.name  = name
        self.songs = []

    def add_song(self, title, artist, duration):
        self.songs.append(Song(title, artist, duration))

    def remove_song(self, title):
        self.songs = [s for s in self.songs if s.title != title]

    def _format_time(self, seconds):
        return f"{seconds // 60}:{seconds % 60:02}"

    def total_duration(self):
        total = sum(s.duration for s in self.songs)
        return self._format_time(total)

    def longest_song(self):
        song = max(self.songs, key=lambda s: s.duration)
        return f"{song.title} ({self._format_time(song.duration)})"

    def __str__(self):
        lines = [f"Playlist: {self.name} ({len(self.songs)} songs)"]
        for i, s in enumerate(self.songs, 1):
            lines.append(f"  {i}. {s.title} - {s.artist} ({self._format_time(s.duration)})")
        return "\n".join(lines)

    
    """
    → Playlist: Mis favoritas (3 songs)
→   1. Bohemian Rhapsody - Queen (5:54)
→   2. Hotel California - Eagles (6:31)
→   3. Stairway to Heaven - Led Zeppelin (8:02)"""
pl = Playlist("Mis favoritas")
pl.add_song("Bohemian Rhapsody", "Queen", 354)
pl.add_song("Hotel California", "Eagles", 391)
pl.add_song("Stairway to Heaven", "Led Zeppelin", 482)
#pl.remove_song("Bohemian Rhapsody")
print(pl.total_duration() )  #→ "20:27"
print(pl.longest_song())    # → "Stairway to Heaven (8:02)"
print(pl)