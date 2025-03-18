def sum(a, b):
	return (a + b)

def rest(a, b):
	return (a - b)
    
def mult(a, b):
	return (a * b)
    
def div(a, b):
	return (a / b)

a = int(input('Primer valor: '))
b = int(input('Segon valor: '))
op = input('Operacio a  realitzar (s,r,m,d): ')

if op == 's':
	print('Resultat: '+str(sum(a, b)))
elif op == 'r':
	print('Resultat: '+str(rest(a, b)))
elif op == 'm':
	print('Resultat: '+str(mult(a, b)))
elif op == 'd':
	print('Resultat: '+str(div(a, b)))
else:
	print('Invalid...')
