# def make_group(person1, person2):
#     group = [person1, person2]
#     return group

# using a lambda
make_group = lambda person1, person2: [ person1, person2] 


person1  = "Alice"
person2 = "Bob"

group = make_group(person1, person2 )
print("Group members:")

# for person in group:
print(person1)

group2 = make_group("somebody", "anybody")
print(f"group 2: {group2}")

# for calling function
# print(f"Group1: {make_group(person1, peson2)



shopping_cart = ["kiwi", "feijoe"]
shopping_cart.append("chili")
print(shopping_cart)
shopping_cart.remove("kiwi")
print(shopping_cart)