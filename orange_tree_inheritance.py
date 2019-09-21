# You should be able to measure the height of the tree.
# You should be able to find out if the tree is dead.

# A tree grows 1 meter per year until it is 10 years old. Then it stops growing.
# The orange tree cannot die until it reaches 50 years old.


# After 50 years, the probability of dying increases each year.
# No tree can live more than 100 years.

# A tree will produce 100 fruits a year once it is more than 5 years old.
# A tree will produce 200 fruits a year when it reaches 10 years old.
# A tree will not produce fruits once it reaches 15 years old.

# You should be able to pick a single fruit from the tree by calling the pick_a_fruit! method on your tree (but only if there are some left).
# You should be able to find out how many fruits are left hanging on the tree.

class OrangeTree:
 def __init__(self):
  self.age = 1
  self.height = 1
  self.living = True
  self.fruits = 0
  
  if self.age >= 100:
   self.living = False
 
 def pick_fruit():
  self.fruits -= 1     


def pass_year(tree_instance):
 tree_instance.age += 1
 if tree_instance.living is True:
  tree_instance.height += 1
 

 if tree_instance.age >= 15:
  tree_instance.fruits += 0
 elif tree_instance.age < 15 and tree_instance.age >= 10:
  tree_instance.fruits += 200
 elif tree_instance.age < 10 and tree_instance.age > 5:
  tree_instance.fruits += 100
  tree_instance.height += 1
 
 tree_instance.fruit = 0

my_tree = OrangeTree()
pass_year(my_tree)
pass_year(my_tree)
pass_year(my_tree)
pass_year(my_tree)
pass_year(my_tree)


print(my_tree.age)
print(my_tree.fruits)