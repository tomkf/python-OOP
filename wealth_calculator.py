class Trader:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives * 5
        self.tens = tens * 10
        self.twenties = twenties * 20

    def wealth(): 
         print("hi")
        # val = self.fives + self.tens + self.twenties
        # print(val)

    # def comparable(oppose_instance):
    #     if self.wealth



# class ComparableMixin(object):
#         def _compare(self, other, method):
#             try:
#                 return method(self.wealth(), other.wealth())
#             except (AttributeError, TypeError):
#                 return NotImplemented


tr1 = Trader("John", 2, 3, 1)

tr1.wealth



