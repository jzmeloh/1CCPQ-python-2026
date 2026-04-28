from sympy.codegen.ast import continue_

cp = 0
while cp < 10:
    print(f"produto {cp}")
    cp += 1
    if cp == 3:
        continue
    if cp  == 8:
            break



#while decresente de 4 ate 1
i = 4
while i > 0:
    print(i)
    i -= 1
