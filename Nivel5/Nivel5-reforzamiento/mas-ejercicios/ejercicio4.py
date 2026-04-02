"""
Ejercicio 4 — Medio
Crea una clase Playlist que gestione canciones. Cada canción tiene título, artista y duración en segundos. Métodos: add_song(), remove_song(), total_duration(), longest_song() y __str__.
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