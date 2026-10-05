from itertools import product

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
U = set(range(1, 9))

print("Union          :", A | B) 
print("Intersection   :", A & B) 
print("Difference     :", A - B) 
print("Complement     :", U - A) 
print("Cardinality    :", len(A)) 
print("Subset?        :", A <= U) 
print("A x B          :", set(product(A, B)))




