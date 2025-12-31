class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")
    

class MasalaChai(BaseChai):

    def add_spices(self):
        print("Adding cardamom, ginger and cloves")

class ChaiShop:

    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")
    
    def server(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
    
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()

fancy_chai = FancyChaiShop()

shop.server()

fancy_chai.chai.add_spices()