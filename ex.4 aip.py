## calculadora de raizes de equação de segundo grau

a = int(input('digite o valor de a'))
if(a == 0):
    print('valor invalido')
else:
    b = int(input('digite o valor de b'))
    c = int(input('digite o valor de c'))

    if((b*b-4*a*c) < 0): 
        print('a equação não possui valores reais')
    else:
        x = (b*b-4*a*c)
        y = float((-b+x*0.5)/2*a)
        z = float((-b-x*0.5)/2*a)

        if y != 0 and z != 0: print(f'a raiz 1 é {y} e a raiz 2 é {z}')
        elif y == 0: print(f'a equação so possui uma raiz {z}')
        elif z == 0: print(f'a equação so possui uma raiz {y}')
        