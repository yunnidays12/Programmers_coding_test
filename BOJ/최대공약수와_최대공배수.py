
def gcd(a, b) :

    if b == 0 : return a
    if b == 1 : return 1

    else :
        return gcd(b, a%b)

def lcd(a, b) :
    the_gcd = gcd(a,b)
    return (the_gcd * (a//the_gcd) * (b//the_gcd))

a, b = map(int, input().split())

print(gcd(a,b))
print(lcd(a,b))