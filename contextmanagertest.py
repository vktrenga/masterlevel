
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")

def add(a, b):
    result = 0
    with my_context_manager() as cm:
        result = a + b
        print(f"Using {result}")
    return result


result = add(2, 3)
print(f"Result: {result}")  

# result = add_new(2, 3)
# print(f"Result: {result}")  

