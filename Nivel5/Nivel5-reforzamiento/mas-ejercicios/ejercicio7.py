"""
Ejercicio 7 — Medio
Crea una clase TextAnalyzer que analice un texto. Métodos: word_count(), char_count(), most_common(n), longest_word() y __str__.
ta = TextAnalyzer("el gato y el perro y el gato son amigos")
ta.word_count()     → 9
ta.char_count()     → 38
ta.most_common(3)   → [("el", 3), ("gato", 2), ("y", 2)]
ta.longest_word()   → "amigos"
print(ta)
→ Text: "el gato y el perro..."
→ Words: 9 | Chars: 38 | Unique: 7
"""

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def char_count(self):
        return len(self.text)

    def most_common(self, n):
        frequencies = {}
        for word in self.text.split():
            frequencies[word] = frequencies.get(word, 0) + 1
        return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:n]

    def longest_word(self):
        return max(self.text.split(), key=len)

    def __str__(self):
        preview = self.text[:20] + "..." if len(self.text) > 20 else self.text
        unique  = len(set(self.text.split()))
        return (f'Text: "{preview}"\n'
                f'Words: {self.word_count()} | Chars: {self.char_count()} | Unique: {unique}')
ta = TextAnalyzer("el gato y el perro y el gato son amigos")
print(ta.word_count() )
print(ta.char_count() )
print(ta.most_common(3))
print(ta.longest_word())
print(ta)