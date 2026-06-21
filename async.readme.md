
# ⚡ Asyncio in Python — What, Why, When
## 📖 Introduction
Asyncio is Python’s library for asynchronous programming.
It enables concurrency using async/await, making programs efficient for I/O-bound tasks (network requests, DB queries, file I/O).

👉 Asyncio is the backbone of frameworks like FastAPI, aiohttp, asyncpg.
### 1. Event Loop
- **What**: The “traffic controller” that schedules and runs async tasks.  
- **Why**: Without an event loop, coroutines wouldn’t know when to run or pause.  
- **When**: Always — every asyncio program starts with `asyncio.run()` which creates and manages the event loop.

```python
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
```

---

### 2. Coroutines
- **What**: Functions defined with `async def`. They can pause at `await`.  
- **Why**: They allow non-blocking execution — instead of waiting, they yield control back to the event loop.  
- **When**: Use for any I/O-bound operation (network, DB, file I/O).

```python
async def greet(name):
    await asyncio.sleep(1)
    print(f"Hello, {name}")
```

---

### 3. Tasks
- **What**: Wrappers around coroutines that run concurrently.  
- **Why**: To run multiple coroutines at the same time.  
- **When**: Use when you want parallel execution of independent coroutines.

```python
task1 = asyncio.create_task(greet("A"))
task2 = asyncio.create_task(greet("B"))
await task1; await task2
```

---

### 4. Gathering Tasks
- **What**: `asyncio.gather()` runs multiple coroutines together.  
- **Why**: Cleaner than creating tasks manually.  
- **When**: Use when you want to wait for multiple coroutines and collect results.

```python
results = await asyncio.gather(greet("A"), greet("B"))
```

---

### 5. Task Cancellation
- **What**: Cancelling a running task.  
- **Why**: Prevent wasted resources when a client disconnects or deadline expires.  
- **When**: Use in long-running tasks or when implementing timeouts.

```python
task = asyncio.create_task(greet("A"))
task.cancel()
```

---

### 6. Timeouts
- **What**: Limit how long a coroutine can run.  
- **Why**: Avoid hanging forever on slow I/O.  
- **When**: Use for network calls, DB queries, or external APIs.

```python
await asyncio.wait_for(greet("A"), timeout=2)
```

---

### 7. Synchronization (Locks, Semaphores, Events)
- **What**: Async versions of threading primitives.  
- **Why**: Prevent race conditions when multiple coroutines access shared state.  
- **When**: Use when updating counters, caches, or shared resources.

```python
lock = asyncio.Lock()
async with lock:
    counter += 1
```

---

### 8. Queues (Producer–Consumer)
- **What**: Async queue for communication between tasks.  
- **Why**: Decouples producers and consumers.  
- **When**: Use in pipelines, crawlers, or message processing.

```python
queue = asyncio.Queue()
await queue.put("data")
item = await queue.get()
```

---

### 9. Running Blocking Code
- **What**: Run CPU-bound or blocking code in a thread pool.  
- **Why**: Prevents freezing the event loop.  
- **When**: Use for legacy libraries or heavy computation.

```python
loop = asyncio.get_running_loop()
await loop.run_in_executor(None, blocking_task)
```

---

### 10. Subprocess Management
- **What**: Run external commands asynchronously.  
- **Why**: Integrate with system tools or microservices.  
- **When**: Use for orchestration, automation, or pipelines.

```python
proc = await asyncio.create_subprocess_shell("echo hi")
stdout, _ = await proc.communicate()
```

---

### 11. Structured Concurrency (TaskGroup, Python 3.11+)
- **What**: Group tasks together with automatic cleanup.  
- **Why**: Safer than manual task management — if one fails, the group handles it.  
- **When**: Use when tasks are logically related (e.g., multiple API calls for one request).

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(greet("A"))
    tg.create_task(greet("B"))
```

---

### 📊 Asyncio vs Threads
- **Asyncio** → cooperative multitasking, best for I/O-bound tasks.  
- **Threads** → preemptive multitasking, better for CPU-bound tasks.  
- Asyncio has lower overhead and scales better for thousands of connections.

---

### 🎯 Key Takeaways
- **What**: Asyncio is Python’s async framework.  
- **Why**: Efficient concurrency for I/O-bound tasks.  
- **When**: Use for web servers, DB queries, crawlers, pipelines, microservices.  
- **Advanced tools**: cancellation, timeouts, locks, queues, executors, subprocesses, TaskGroups.  

