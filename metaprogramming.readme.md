
# Metaprogramming in Python — Complete Guide
## 📖 Introduction
Metaprogramming means writing code that modifies or controls other code.
In Python, the main tools are:

- Decorators → wrap functions/classes with extra behavior.

- Descriptors → control attribute access.

- Context Managers → manage setup/teardown around code blocks.

- Metaclasses → control how classes are created (covered separately).

These features power frameworks like Django, FastAPI, SQLAlchemy, and Dataclasses.

# 🐍 Python Decorators — Complete Guide

## 📖 Introduction
A **decorator** in Python is a function that takes another function or class, **wraps it with extra behavior**, and returns it.  
They are applied using the `@` symbol and are a cornerstone of **metaprogramming**.

---

## 🔑 Basics

### Simple Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Rengaraj")
```

👉 **Explanation**:  
- `@my_decorator` wraps `greet`.  
- When `greet` is called, the wrapper runs first, then the original function, then the wrapper finishes.

---

## ⚡ Advanced Concepts

### 1. Decorators with Arguments
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
```

👉 **Explanation**:  
- `repeat(3)` configures the decorator to run the function 3 times.  
- Useful for configurable behaviors like retries, timeouts, or logging levels.

---

### 2. Class-Based Decorators
```python
class MathDecorator:
    def __init__(self, func):
        self.func = func
        self.calls = 0
        self.results = []  # store results of each call

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Call #{self.calls} to {self.func.__name__}")
        result = self.func(*args, **kwargs)
        self.results.append(result)
        print(f"Result: {result}")
        return result

@MathDecorator
def add(a, b):
    return a + b

@MathDecorator
def subtract(a, b):
    return a - b

# Usage
print(add(10, 5))       # Call #1 → Result: 15
print(add(20, 7))       # Call #2 → Result: 27
print(subtract(10, 5))  # Call #1 → Result: 5
print(subtract(20, 7))  # Call #2 → Result: 13

# Access stored results
print("Add results:", add.results)         # [15, 27]
print("Subtract results:", subtract.results) # [5, 13]

```

👉 **Explanation**:  
- `__init__` stores the function and initializes counters/results.
- `__call__` makes the class behave like a function:
  - Tracks how many times the function was called.
  - Executes the original function (add or subtract).
  - Stores the result in a list for later inspection.
- Each decorated function (add, subtract) has its own independent state.

---

### 3. Stacking Multiple Decorators
```python
def deco1(func):
    def wrapper(*args, **kwargs):
        print("deco1 before")
        result = func(*args, **kwargs)
        print("deco1 after")
        return result
    return wrapper

def deco2(func):
    def wrapper(*args, **kwargs):
        print("deco2 before")
        result = func(*args, **kwargs)
        print("deco2 after")
        return result
    return wrapper

@deco1
@deco2
def main():
    print("Main function runs")

main()
```

👉 **Explanation**:  
- Execution order:  
  - Before parts: `deco1 → deco2`  
  - Main function runs once  
  - After parts: `deco2 → deco1`  
- Think of it like nested boxes: open outer → inner → gift → close inner → close outer.

---

### 4. Preserving Metadata with `functools.wraps`
```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    """Greets a person"""
    print(f"Hello, {name}")

print(greet.__name__)  # greet ✅
print(greet.__doc__)   # "Greets a person" ✅
```

👉 **Explanation**:  
- Without `wraps`, decorated functions lose their name/docstring.  
- `@wraps` preserves metadata, making debugging and documentation consistent.

---

### 5. Class Decorators
```python
def add_repr(cls):
    cls.__repr__ = lambda self: f"<{cls.__name__} object>"
    return cls

@add_repr
class MyClass:
    pass

print(MyClass())  # <MyClass object>
```

👉 **Explanation**:  
- Decorators can modify entire classes.  
- Here, `__repr__` is injected automatically.  
- Libraries like `dataclasses` use this technique to auto-generate methods.

---

### 6. Error Handling in Decorators
```python
def safe_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error caught: {e}")
            return None
    return wrapper

@safe_decorator
def risky_division(a, b):
    return a / b

print(risky_division(10, 0))  # Error caught: division by zero
```

👉 **Explanation**:  
- If a decorator fails, the chain breaks.  
- Wrapping logic in `try/except` makes decorators resilient.  
- Frameworks use this to return controlled error responses instead of crashing.

---

## 🎯 Real-World Usage
- **Django** → `@login_required` for authentication  
- **Flask/FastAPI** → `@app.route("/path")`, `@app.get("/items")` for routing  
- **functools** → `@lru_cache` for caching results  
- **pytest** → decorators for marking tests  

---

## 🧠 Key Takeaways
- Decorators wrap functions/classes to add behavior.  
- Use `functools.wraps` to preserve metadata.  
- You can stack multiple decorators — order matters.  
- Decorators can be function-based, class-based, or applied to classes.  
- Always handle errors gracefully in production decorators.  

---


# 🧩 Python Descriptors — Complete Guide

## 📖 Introduction
A **descriptor** in Python is a special class that customizes how attributes are **accessed, assigned, or deleted**.  
Descriptors are the foundation of:
- `@property`
- ORM fields (Django, SQLAlchemy)
- Validation systems
- Computed attributes

They work by implementing one or more of these methods:
- `__get__(self, instance, owner)` → intercepts **reads**  
- `__set__(self, instance, value)` → intercepts **writes**  
- `__delete__(self, instance)` → intercepts **deletion**

---

## 🔑 Basic Descriptor Example
```python
class Celsius:
    def __init__(self, value=0):
        self._value = value

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._value = value

class Temperature:
    celsius = Celsius()

t = Temperature()
t.celsius = 25       # __set__ runs
print(t.celsius)     # __get__ runs
```

👉 **Explanation**:  
- `__init__` sets the initial value.  
- `__set__` validates assignments.  
- `__get__` retrieves the value.  

---

## 🔑 Transforming Values with `__set__` (×8 Example)
```python
class MultiplyByEight:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        print(f"Original value: {value}")
        self._value = value * 8
        print(f"Stored value (×8): {self._value}")

class Demo:
    number = MultiplyByEight()

d = Demo()
d.number = 5        # __set__ runs → stores 40
print(d.number)     # __get__ runs → returns 40
```

👉 **Explanation**:  
- Assigning `d.number = 5` triggers `__set__`.  
- The value is multiplied by 8 before storage.  
- Reading `d.number` triggers `__get__`, returning the transformed value.

---

## 🔑 Computed Attribute Example
```python
class Square:
    def __get__(self, instance, owner):
        return instance._value ** 2

class Number:
    def __init__(self, value):
        self._value = value
    square = Square()

n = Number(4)
print(n.square)  # 16
```

👉 **Explanation**:  
- `__get__` computes the square dynamically.  
- No redundant storage needed — value is calculated on access.

---

## 🔑 ORM-Style Descriptor Example
```python
class Field:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"Setting {self.name} = {value}")
        instance.__dict__[self.name] = value

class User:
    name = Field("name")
    age = Field("age")

u = User()
u.name = "Rengaraj"
u.age = 30
print(u.name, u.age)
```

👉 **Explanation**:  
- Mimics how Django ORM fields (`CharField`, `IntegerField`) work.  
- Each field is a descriptor controlling storage and retrieval.

---

## 📊 Types of Descriptors

| Type               | Methods Implemented              | Behavior                        |
|-------------------|----------------------------------|---------------------------------|
| Data Descriptor    | `__get__`, `__set__`, `__delete__` | Controls both read & write      |
| Non-Data Descriptor| Only `__get__`                   | Read-only or computed attributes|

---

## 🎯 Key Takeaways
- **`__init__`** → constructor for descriptor object itself.  
- **`__get__`** → intercepts **reads**.  
- **`__set__`** → intercepts **writes** (can validate or transform values).  
- **`__delete__`** → intercepts deletions.  
- Descriptors power **properties, ORM fields, and computed attributes**.  
- They give you **fine-grained control over attribute lifecycle**.

---

# 📘 Context Managers in Python — Complete Guide

## 📖 Introduction
A **Context Manager** in Python is a construct that allows you to **set up and tear down resources automatically**.  
They are used with the `with` statement and are part of Python’s **metaprogramming toolkit**, because they let you inject behavior around arbitrary blocks of code.

---

## 🔑 How Context Managers Work
A context manager implements two special methods:
- `__enter__(self)` → runs at the start of the block.  
- `__exit__(self, exc_type, exc_value, traceback)` → runs at the end of the block (even if an error occurs).  

👉 **Analogy**: Think of a library card system.  
- `__enter__` → you check out a book.  
- `__exit__` → you return the book, even if you didn’t finish reading.

---

## 🔹 Example 1: Basic Context Manager
```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside block")
```

👉 **Explanation**:  
- `__enter__` runs before the block.  
- The block executes.  
- `__exit__` runs after the block, ensuring cleanup.

---

## 🔹 Example 2: File Handling (Built-in Context Manager)
```python
with open("file.txt", "r") as f:
    data = f.read()
```

👉 **Explanation**:  
- `open()` returns a context manager.  
- File is opened at `__enter__`.  
- File is automatically closed at `__exit__`, even if an error occurs.

---

## 🔹 Example 3: Resource Management
```python
import threading

lock = threading.Lock()

with lock:
    print("Critical section")
```

👉 **Explanation**:  
- Lock is acquired at `__enter__`.  
- Code inside block runs safely.  
- Lock is released at `__exit__`.  

---

## 🔹 Example 4: Using `contextlib`
Python’s `contextlib` makes writing context managers easier.

```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup")
    yield "Resource"
    print("Teardown")

with managed_resource() as r:
    print("Using", r)
```

👉 **Explanation**:  
- `yield` separates setup and teardown.  
- Cleaner than writing full `__enter__`/`__exit__`.

---

## 📊 Comparison: Context Managers vs Decorators

| Feature   | Decorators                          | Context Managers                |
|-----------|-------------------------------------|----------------------------------|
| Scope     | Functions/classes                   | Code blocks (`with`)            |
| Purpose   | Modify behavior at definition time  | Manage resources at runtime     |
| Example   | `@log`, `@cache`                    | `with open(...)`, `with lock`   |

---

## 🎯 Key Takeaways
- Context Managers wrap **execution blocks** with setup and teardown logic.  
- They use `__enter__` and `__exit__` methods.  
- Commonly used for **files, locks, DB connections, transactions, sockets**.  
- `contextlib` provides a simpler way to write them.  
- They are part of **metaprogramming** because they let you **inject behavior around arbitrary code**.

---

# 🏗️ Metaclasses in Python — Deep Dive

## 📖 What Are Metaclasses?
- A **metaclass** is the **class of a class**.  
- Just like objects are created from classes, classes themselves are created from metaclasses.  
- By customizing metaclasses, you can **control class creation**: inject attributes, enforce rules, auto-register classes, or generate methods dynamically.

👉 Think of it like this:
- **Object** → built from a **Class**.  
- **Class** → built from a **Metaclass**.

---

## 🔑 How They Work
- By default, Python uses `type` as the metaclass:
```python
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```
- If you define your own metaclass, you override how classes are constructed.

---

## 🔹 Example 1: Injecting Attributes
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = "Meta"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # Meta
```

👉 **Experience Insight**:  
I’ve seen this pattern in **ORM frameworks** (like Django) where metaclasses inject metadata into model classes automatically.

---

## 🔹 Example 2: Enforcing Rules (Contracts)
```python
class InterfaceMeta(type):
    def __new__(cls, name, bases, dct):
        if 'process' not in dct:
            raise TypeError(f"{name} must define a 'process' method")
        return super().__new__(cls, name, bases, dct)

class Worker(metaclass=InterfaceMeta):
    def process(self):
        print("Working...")
```

👉 **Experience Insight**:  
This is similar to how **abstract base classes (ABC)** enforce method definitions. In large teams, this prevents developers from forgetting critical methods.

---

## 🔹 Example 3: Auto-Registering Classes
```python
registry = {}

class RegistryMeta(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        registry[name] = new_cls
        return new_cls

class ServiceA(metaclass=RegistryMeta):
    pass

class ServiceB(metaclass=RegistryMeta):
    pass

print(registry)
# {'ServiceA': <class '__main__.ServiceA'>, 'ServiceB': <class '__main__.ServiceB'>}
```

👉 **Experience Insight**:  
I’ve used this in **plugin systems** — every new plugin class automatically registers itself, so you don’t need manual configuration.

---

## 🔹 Example 4: Django ORM (Real-World)
In Django, when you define a model:
```python
class User(models.Model):
    name = models.CharField(max_length=100)
```

- The `ModelBase` metaclass processes the class definition.  
- It collects all `CharField`, `IntegerField`, etc. into a `_meta` object.  
- This is how Django knows how to generate SQL tables from Python classes.

👉 **Experience Insight**:  
Metaclasses here save developers from writing repetitive SQL — the ORM builds it dynamically.

---

## 📊 Comparison with Other Metaprogramming Tools

| Tool              | Level        | Purpose                         | Example Usage                  |
|-------------------|------------|----------------------------------|--------------------------------|
| Decorators        | Function/Class | Add behavior at definition time | Logging, routing, caching      |
| Descriptors       | Attribute  | Control attribute access        | ORM fields, validation         |
| Context Managers  | Code block | Manage resources at runtime     | File handling, DB, locks       |
| Metaclasses       | Class      | Control class creation          | Django ORM, plugin systems     |

---

## 🎯 Key Takeaways
- Metaclasses let you **control class creation**.  
- They’re powerful but should be used sparingly — often decorators or descriptors are simpler.  
- Real-world frameworks (Django, SQLAlchemy) rely heavily on metaclasses for dynamic behavior.  
- Best use cases: **ORMs, plugin registries, enforcing contracts, auto-generating methods**.  

---

## 📚 Summary

Metaprogramming is a powerful set of tools in Python that allows you to write code that modifies or controls other code. The four main approaches each serve different purposes:

- **Decorators** are perfect for adding behavior to functions and classes at definition time
- **Descriptors** give fine-grained control over attribute access and manipulation
- **Context Managers** elegantly handle resource setup and teardown
- **Metaclasses** provide the deepest level of control over class creation

Mastering these tools will greatly enhance your ability to write elegant, maintainable, and powerful Python code.
