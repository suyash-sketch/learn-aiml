class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sweetness'],
            order_data['size'],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(
            tea_type, sweetness, size
        )
    

order_one = ChaiOrder.from_dict({"tea_type" : "Masala", "sweetness":"medium", "size" : "small"})

order_two = ChaiOrder.from_string("ginger-low-large")

order_three = ChaiOrder("Motchaa", "mild", "large")

print(order_one)
print(order_one.__dict__)
print(order_two.__dict__)
print(order_three.__dict__)