
# 🔄 Generators

## 📖 What
- A **generator** is a function that uses `yield` to produce values one at a time.  
- Unlike lists, generators don’t store everything in memory — they compute values lazily.

```python
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()   # yields one line at a time
```

👉 Each call to `next()` gives the next line, without loading the entire file.

---

## 💡 Why
- **Memory efficiency**: Handles huge datasets without exhausting RAM.  
- **Performance**: Faster for streaming pipelines.  
- **Flexibility**: Can represent infinite sequences.

---

## 🕒 When
- Reading **large log files**.  
- Streaming **database rows**.  
- Handling **real-time data feeds** (Kafka, sockets).

---

# 🧰 Itertools

## 📖 What
- A Python module with **optimized iteration tools**.  
- Provides utilities for **combinatorics, infinite sequences, grouping, slicing**.

---

## 🔑 Key Functions

### Infinite Iterators
```python
import itertools
for i in itertools.count(10, 2):   # start=10, step=2
    if i > 20: break
    print(i)
```

👉 Output: `10 12 14 16 18 20`

---

### Combinatorics
```python
import itertools
items = ['A', 'B', 'C']
print(list(itertools.combinations(items, 2)))
```

👉 Output: `[('A','B'), ('A','C'), ('B','C')]`

---

### Grouping
```python
import itertools
data = [("ERROR", "Disk full"), ("ERROR", "File not found"), ("INFO", "User login")]
for key, group in itertools.groupby(sorted(data, key=lambda x: x[0]), key=lambda x: x[0]):
    print(key, list(group))
```

👉 Output:
```
ERROR [('ERROR', 'Disk full'), ('ERROR', 'File not found')]
INFO [('INFO', 'User login')]
```

---

# 📊 Generators vs Itertools

| Feature        | Generators                        | Itertools                          |
|----------------|-----------------------------------|------------------------------------|
| Definition     | Functions with `yield`            | Module with iteration utilities    |
| Purpose        | Lazy evaluation, custom iteration | Prebuilt iteration patterns        |
| Memory         | Very efficient                    | Very efficient                     |
| Example Use    | Streaming logs, DB rows           | Combinatorics, infinite sequences  |

---

# 🚀 Real-Time Example: Log Analyzer

Imagine you’re building a **log processing system**:

### Step 1: Stream logs with a Generator
```python
def read_logs(file_path):
    with open(file_path) as f:
        for line in f:
            level, message = line.strip().split(":", 1)
            yield (level, message)
```

👉 Reads logs line by line, memory-efficient.

---

### Step 2: Group logs with Itertools
```python
import itertools

logs = [
    ("ERROR", "Disk full"),
    ("ERROR", "File not found"),
    ("INFO", "User login"),
    ("INFO", "Page loaded"),
    ("WARNING", "Low memory"),
]

for level, group in itertools.groupby(sorted(logs, key=lambda x: x[0]), key=lambda x: x[0]):
    print(level, list(group))
```

👉 Groups logs by severity.

---

### Step 3: Analyze Error Combinations
```python
error_types = ["Disk full", "File not found", "Permission denied"]
pairs = list(itertools.combinations(error_types, 2))
print("Error combinations:", pairs)
```

👉 Helps detect co-occurrence patterns in errors.

---

# 🎯 Real-World Mapping
- **Generator** → stream logs line by line (efficient memory usage).  
- **Itertools.groupby** → categorize logs by severity.  
- **Itertools.combinations** → analyze error co-occurrence patterns.  

