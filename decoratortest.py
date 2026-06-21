

# def mydecorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function '{func.__name__}' returned {result}")
#         return result
#     return wrapper



from functools import wraps


def mydectrator(callbackfuntion):
	def wrapper(*a, **k):
		print(f"({callbackfuntion.__name__}) function called with arguments: {a} and keyword arguments: {k}")
		result = callbackfuntion(*a, **k)
		print(f"({callbackfuntion.__name__}) function returned: {result}")
		return result   
	return wrapper


def mywarpdectrator(callbackfuntion):
	@wraps(callbackfuntion)
	def wrapper(*a, **k):
		print(f"({callbackfuntion.__name__}) function called with arguments: {a} and keyword arguments: {k}")
		result = callbackfuntion(*a, **k)
		print(f"({callbackfuntion.__name__}) function returned: {result}")
		return result   
	return wrapper


@mydectrator
def add(x, y):
	"""This function adds two numbers."""
	return x + y

added = add(5, 3)
print(f"Function name: {add.__name__}")
print(f"Function docstring: {add.__doc__}")



@mywarpdectrator
def addwithwraps(x, y):
	"""This function adds two numbers."""
	return x + y

added = addwithwraps(5, 3)

print(f"Function name: {addwithwraps.__name__}")
print(f"Function docstring: {addwithwraps.__doc__}")
print(f"Added result: {added}")

def validate_attributes(cls):
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        if not hasattr(self, "name"):
            raise ValueError("Class must have a 'name' attribute")
    cls.__init__ = new_init
    return cls

@validate_attributes
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Rengaraj")  # ✅ works
# q = Person()            # ❌ raises ValueError
