a = 97
b = 55
c = 55
# test expression
if a < b:
    # statement to be run
    print(b)
elif b == c:
    print(c)
else:
    print(a)

    
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)
if a == 34 or b == 34:
    print (a + b)

#Operadores ternários 

imposto = 0.2
imposto = "Alto" if imposto > 0.27 else "Baixo"
print(imposto)