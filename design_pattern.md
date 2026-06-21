
# 🧩 Python Design Patterns with Real Examples
 
---

# 🧩 Deep Dive into Python Design Patterns

## 1. **Singleton Pattern**
- **What:** Guarantees only one instance of a class exists.  
- **Why:** Shared resources like DB connections, cache managers, or configuration should not be duplicated.  
- **When to Use:**  
  - Database connection pools  
  - Logging systems  
  - Global configuration  

**Code Example: Logger**
```python
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = open("app.log", "a")
        return cls._instance

    def log(self, message):
        self.log_file.write(message + "\n")

# Usage
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True
```

**Real Example:** In a **microservices system**, you don’t want multiple loggers writing to different files — one global logger ensures consistency.

---

## 2. **Factory Pattern**
- **What:** Centralizes object creation logic.  
- **Why:** Avoids hardcoding `new` everywhere, makes code flexible.  
- **When to Use:**  
  - Payment gateways  
  - File parsers (JSON, XML, CSV)  
  - Notification systems  

**Code Example: Payment Factory**
```python
class Payment:
    def pay(self, amount): pass

class CreditCard(Payment):
    def pay(self, amount): print(f"Paid {amount} via Credit Card")

class PayPal(Payment):
    def pay(self, amount): print(f"Paid {amount} via PayPal")

class PaymentFactory:
    @staticmethod
    def get_payment(method):
        if method == "credit": return CreditCard()
        if method == "paypal": return PayPal()
        raise ValueError("Unknown method")

# Usage
payment = PaymentFactory.get_payment("paypal")
payment.pay(500)
```

**Real Example:** In **e-commerce**, you can add new payment methods without touching existing code.

---

## 3. **Observer Pattern**
- **What:** One object’s change triggers updates in others.  
- **Why:** Decouples event producers from consumers.  
- **When to Use:**  
  - Notifications (email, SMS, push)  
  - Real-time dashboards  
  - Pub/Sub systems  

**Code Example: Order Notifications**
```python
class Observer:
    def update(self, msg): pass

class EmailNotifier(Observer):
    def update(self, msg): print(f"Email: {msg}")

class SMSNotifier(Observer):
    def update(self, msg): print(f"SMS: {msg}")

class OrderSystem:
    def __init__(self):
        self.observers = []

    def attach(self, obs): self.observers.append(obs)

    def new_order(self, order_id):
        for obs in self.observers:
            obs.update(f"Order {order_id} placed")

system = OrderSystem()
system.attach(EmailNotifier())
system.attach(SMSNotifier())
system.new_order(101)
```

**Real Example:** In a **food delivery app**, when an order is placed, both customer and restaurant get notified.

---

## 4. **Decorator Pattern**
- **What:** Add new behavior without modifying original code.  
- **Why:** Keeps code clean, reusable, and flexible.  
- **When to Use:**  
  - Logging  
  - Authentication  
  - Caching  

**Code Example: Logging Decorator**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def checkout(order_id):
    print(f"Checking out order {order_id}")

checkout(200)
```

**Real Example:** In **Django/Flask**, decorators are used for authentication (`@login_required`) or caching.

---

## 5. **Strategy Pattern**
- **What:** Define multiple algorithms and switch between them easily.  
- **Why:** Avoids hardcoding logic, makes behavior flexible.  
- **When to Use:**  
  - Sorting algorithms  
  - Payment calculation strategies  
  - Recommendation engines  

**Code Example: Sorting**
```python
class Strategy:
    def execute(self, data): pass

class Ascending(Strategy):
    def execute(self, data): return sorted(data)

class Descending(Strategy):
    def execute(self, data): return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy): self.strategy = strategy
    def run(self, data): return self.strategy.execute(data)

context = Context(Descending())
print(context.run([5, 1, 9]))
```

**Real Example:** In **analytics pipelines**, you might switch between algorithms depending on dataset size.

---

## 6. **Adapter Pattern**
- **What:** Bridges old and new interfaces.  
- **Why:** Helps integrate legacy systems with modern APIs.  
- **When to Use:**  
  - Migrating old systems  
  - Integrating third-party APIs  
  - Handling backward compatibility  

**Code Example: Printer Adapter**
```python
class OldPrinter:
    def print_text(self, text): print(f"Old: {text}")

class NewPrinter:
    def print(self, text): print(f"New: {text}")

class PrinterAdapter:
    def __init__(self, old_printer): self.old_printer = old_printer
    def print(self, text): self.old_printer.print_text(text)

adapter = PrinterAdapter(OldPrinter())
adapter.print("Hello World")
```

**Real Example:** In **banking systems**, adapters connect legacy COBOL services to modern REST APIs.

---

# 🎯 Big Picture
- **Singleton** → One instance (DB, Logger).  
- **Factory** → Object creation abstraction (Payments, Parsers).  
- **Observer** → Event-driven notifications (Orders, Stocks).  
- **Decorator** → Add features dynamically (Logging, Auth).  
- **Strategy** → Switch algorithms easily (Sorting, Pricing).  
- **Adapter** → Bridge old & new (Legacy migration).  



# ⚙️ Django Design Patterns

### 1. **MVC / MTV Pattern**
- Django follows **MTV (Model–Template–View)** which is a variation of MVC.
- **Example:**  
  - **Model:** `User` table in `models.py`  
  - **Template:** HTML file for rendering user profile  
  - **View:** Function/class in `views.py` that fetches data and passes it to template  

👉 This enforces **separation of concerns**.

---

### 2. **Singleton Pattern (Settings & Config)**
- Django’s **settings.py** acts like a singleton — one global configuration object.
- Example: Database settings, middleware, installed apps.

---

### 3. **Factory Pattern (ORM QuerySets)**
- Django ORM acts like a factory:  
  ```python
  User.objects.create(username="rengaraj")
  ```
  - You don’t instantiate SQL directly; ORM generates objects for you.

---

### 4. **Observer Pattern (Signals)**
- Django **signals** (e.g., `post_save`, `pre_delete`) notify subscribers when events happen.
- Example: Send email after user registration:
  ```python
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from django.contrib.auth.models import User

  @receiver(post_save, sender=User)
  def send_welcome_email(sender, instance, created, **kwargs):
      if created:
          print(f"Welcome email sent to {instance.username}")
  ```

---

### 5. **Decorator Pattern (Middleware & View Decorators)**
- Django uses decorators for authentication, caching, CSRF protection.
- Example:
  ```python
  from django.contrib.auth.decorators import login_required

  @login_required
  def dashboard(request):
      return HttpResponse("Welcome to dashboard")
  ```

---

# ⚡ FastAPI Design Patterns

### 1. **Dependency Injection Pattern**
- FastAPI’s **Depends** is a built-in DI system.
- Example: Injecting DB session:
  ```python
  from fastapi import Depends

  def get_db():
      db = SessionLocal()
      try:
          yield db
      finally:
          db.close()

  @app.get("/users/")
  def read_users(db: Session = Depends(get_db)):
      return db.query(User).all()
  ```

👉 This makes testing and scaling easier.

---

### 2. **Factory Pattern (Routers)**
- FastAPI uses **APIRouter** as a factory for endpoints.
- Example:
  ```python
  from fastapi import APIRouter

  user_router = APIRouter()

  @user_router.get("/profile")
  def profile():
      return {"msg": "User profile"}
  ```

---

### 3. **Observer Pattern (Event Handlers)**
- FastAPI supports **startup/shutdown events**.
- Example:
  ```python
  @app.on_event("startup")
  async def startup_event():
      print("App started, connecting to DB...")

  @app.on_event("shutdown")
  async def shutdown_event():
      print("App shutting down, closing DB...")
  ```

---

### 4. **Decorator Pattern (Middleware)**
- FastAPI middleware wraps requests/responses.
- Example:
  ```python
  from fastapi import Request

  @app.middleware("http")
  async def log_requests(request: Request, call_next):
      print(f"Incoming request: {request.url}")
      response = await call_next(request)
      return response
  ```

---

### 5. **Strategy Pattern (Response Models)**
- FastAPI lets you define multiple response strategies using **Pydantic models**.
- Example:
  ```python
  from pydantic import BaseModel

  class SuccessResponse(BaseModel):
      message: str

  class ErrorResponse(BaseModel):
      error: str

  @app.get("/status", response_model=SuccessResponse)
  def status():
      return {"message": "All good"}
  ```

---

# 🎯 Summary

| Pattern        | Django Example                  | FastAPI Example                  |
|----------------|---------------------------------|----------------------------------|
| Singleton      | `settings.py`                   | Global config objects            |
| Factory        | ORM QuerySets                   | Routers/APIRouter                |
| Observer       | Signals (`post_save`)           | Startup/Shutdown events          |
| Decorator      | Middleware, `@login_required`   | Middleware, custom decorators    |
| Strategy       | Template rendering              | Pydantic response models         |
| Dependency Injection | Not native (manual services) | Built-in `Depends` system        |


