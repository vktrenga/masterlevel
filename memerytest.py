from fastapi import FastAPI
import gc

app = FastAPI()

# Global memory store
GLOBAL_MEMORY = []

@app.get("/evenlist")
def evenlist(limit: int = 100_000):
    """Generate even numbers and store in global memory."""
    global GLOBAL_MEMORY
    GLOBAL_MEMORY = [n for n in range(limit) if n % 2 == 0]
    return {"status": "allocated", "size": len(GLOBAL_MEMORY)}

@app.get("/allocation")
def allocation():
    """Check current memory allocation size."""
    global GLOBAL_MEMORY
    return {"allocated_size": len(GLOBAL_MEMORY)}

@app.get("/cleanup")
def cleanup():
    """Cleanup global memory and force garbage collection."""
    global GLOBAL_MEMORY
    GLOBAL_MEMORY = []   # reset
    gc.collect()
    return {"status": "cleaned"}

@app.get("/get_list")
def getList():
    """Get the list of allocated memory."""
    global GLOBAL_MEMORY
    return {"list": GLOBAL_MEMORY}