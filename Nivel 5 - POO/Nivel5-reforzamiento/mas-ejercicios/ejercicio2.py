"""
Ejercicio 2 — Fácil
Crea una clase Counter con un valor inicial. Métodos: increment(), decrement(), reset(), value() y __str__.
c = Counter(0)
c.increment()
c.increment()
c.increment()
c.value()      → 3
c.decrement()
c.value()      → 2
c.reset()
c.value()      → 0
print(c)       → Counter: 0
"""
class Counter:
    def __init__(self,start_value):
       self._initial = start_value      # guardas el inicial
       self.current  = start_value 
    def increment(self):
         self.current += 1
    
    def decrement(self):
         self.current -= 1
    
    def reset(self):
         self.current = self._initial

    def value(self):
        return self.current
    
    def __str__(self):
        return f"Counter: {self.current}"
    
c = Counter(10)
c.increment()
c.increment()
c.increment()
print(c.value())     # → 3
c.decrement()
print(c.value() )    # → 2
c.reset()
print(c.value())     # → 0
print(c)      # → Counter: 0