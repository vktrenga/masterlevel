class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        dct['created_by'] = "Meta"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # Meta
print(MyClass)  # <class '__main__.MyClass'>


class DefaultMyClass:
    pass

print(type(DefaultMyClass))  # <class 'type'>