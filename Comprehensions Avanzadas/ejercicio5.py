"""
Ejercicio 5 — Medio
Dado el texto de un párrafo, genera estadísticas usando comprehensions y funciones de alto orden.
python
texto = Python es un lenguaje de programacion poderoso y versatil.
Es muy popular en ciencia de datos inteligencia artificial y desarrollo web.
Python tiene una sintaxis clara y facil de aprender.

word_count        → 37
unique_words      → 30
longest_word      → "programacion"
most_common_3     → [("y", 3), ("de", 3), ("Python", 2)]
words_over_5      → ["lenguaje", "programacion", "poderoso", ...]
avg_word_length   → 5.24
"""
texto = """Python es un lenguaje de programacion poderoso y versatil.
Es muy popular en ciencia de datos inteligencia artificial y desarrollo web.
Python tiene una sintaxis clara y facil de aprender."""

words = texto.split()    # sin lower() para preservar mayúsculas

word_count    = len(words)
unique_words  = len(set(words))
longest_word  = max(words, key=len)
words_over_5  = [w for w in words if len(w) > 5]
avg_word_len  = round(sum(len(w) for w in words) / len(words), 2)

freq          = {w: words.count(w) for w in set(words)}
most_common_3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]

print(f"word_count:    {word_count}")
print(f"unique_words:  {unique_words}")
print(f"longest_word:  {longest_word}")
print(f"most_common_3: {most_common_3}")
print(f"words_over_5:  {words_over_5}")
print(f"avg_word_len:  {avg_word_len}")

#SOLUCION OPTIMA
"""
from collections import Counter

texto = Python es un lenguaje de programacion poderoso y versatil.
Es muy popular en ciencia de datos inteligencia artificial y desarrollo web.
Python tiene una sintaxis clara y facil de aprender.

words = texto.split()
freq  = Counter(words)    # más eficiente que {w: words.count(w) for w in set(words)}

word_count    = len(words)
unique_words  = len(freq)
longest_word  = max(words, key=len)
most_common_3 = freq.most_common(3)    # método directo de Counter
words_over_5  = [w for w in words if len(w) > 5]
avg_word_len  = round(sum(len(w) for w in words) / len(words), 2)

print(f"word_count:    {word_count}")
print(f"unique_words:  {unique_words}")
print(f"longest_word:  {longest_word}")
print(f"most_common_3: {most_common_3}")
print(f"words_over_5:  {words_over_5}")
print(f"avg_word_len:  {avg_word_len}")
"""