def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

inputs = list(map(int,input().split()))
breads = inputs[0]
people = inputs[1]
if breads % people == 0:
    print(0)
else:
    first_gcd = gcd(breads, people)
    breads /= first_gcd
    people /= first_gcd
    slices = people - 1
    slices *= first_gcd
    print(int(slices))
    
        
    