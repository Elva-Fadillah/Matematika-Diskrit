nilai = [True, False]

print("P     Q     P and Q   P or Q   not P")
for p in nilai:
    for q in nilai:
         print(f"{p!s:<5} {q!s:<5} {p and q!s:<8} {p or q!s:<8} {not p!s}")
