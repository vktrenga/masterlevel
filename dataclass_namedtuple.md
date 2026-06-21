
# 📖 Dataclasses

## What
- Introduced in Python 3.7 (`dataclasses` module).  
- A decorator (`@dataclass`) that auto-generates boilerplate methods:  
  - `__init__`, `__repr__`, `__eq__`, and optionally ordering methods.  
- Designed for **structured, mutable data containers**.

## Example
```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float

p = Product(1, "Laptop", 1200)
print(p)          # Product(id=1, name='Laptop', price=1200)
print(p.name)     # Laptop
p.price = 1000    # ✅ Mutable
```

👉 **Key point**: Dataclasses are **mutable** and can have methods.

---

# 📖 Namedtuple

## What
- Factory function in `collections` module.  
- Creates tuple-like objects with **named fields**.  
- Designed for **lightweight, immutable records**.

## Example
```python
from collections import namedtuple

Product = namedtuple("Product", ["id", "name", "price"])
p = Product(1, "Laptop", 1200)

print(p)          # Product(id=1, name='Laptop', price=1200)
print(p.name)     # Laptop
# p.price = 1000  # ❌ Error: Namedtuple is immutable
```

👉 **Key point**: Namedtuples are **immutable** and lightweight.

---

# ⚖️ Comparison

| Feature        | Dataclass                          | Namedtuple                        |
|----------------|------------------------------------|-----------------------------------|
| Mutability     | Mutable (can change values)        | Immutable (values fixed)          |
| Boilerplate    | Minimal, supports defaults/methods | Minimal, no methods               |
| Performance    | Slightly more overhead             | Very lightweight                  |
| Use Case       | Rich models, configs, DTOs         | Simple records, fixed data        |
| Introduced     | Python 3.7                         | Python 2.6                        |

---

# 🚀 Real-Time Example: E-Commerce Order System

### Using Dataclass
```python
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    id: int
    name: str
    price: float

@dataclass
class Order:
    id: int
    customer: str
    products: List[Product]

    def total(self) -> float:
        return sum(p.price for p in self.products)

p1 = Product(1, "Laptop", 1200)
p2 = Product(2, "Mouse", 25)
order = Order(101, "Rengaraj", [p1, p2])

print(order)
print("Total:", order.total())
```

👉 Output:
```
Order(id=101, customer='Rengaraj', products=[Product(id=1, name='Laptop', price=1200), Product(id=2, name='Mouse', price=25)])
Total: 1225
```

---

### Using Namedtuple
```python
from collections import namedtuple

Product = namedtuple("Product", ["id", "name", "price"])
Order = namedtuple("Order", ["id", "customer", "products"])

p1 = Product(1, "Laptop", 1200)
p2 = Product(2, "Mouse", 25)
order = Order(101, "Rengaraj", [p1, p2])

print(order)
# No built-in method for total, must calculate manually:
print("Total:", sum(p.price for p in order.products))
```

👉 Output:
```
Order(id=101, customer='Rengaraj', products=[Product(id=1, name='Laptop', price=1200), Product(id=2, name='Mouse', price=25)])
Total: 1225
```

---

# 🎯 Key Takeaways
- **Dataclasses** → best for **mutable, richer models** with methods (e.g., backend entities, configs).  
- **Namedtuple** → best for **immutable, lightweight records** (e.g., log entries, coordinates).  
- Both reduce boilerplate compared to traditional classes.  
- Choose based on whether you need **immutability vs mutability** and **methods vs pure data**.

---

