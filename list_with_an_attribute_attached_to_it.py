class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_attribute = "Hello, world!"

# Usage
my_list = MyList([1, 2, 4])
print(my_list.my_attribute)  # Outputs: "Hello, world!"
