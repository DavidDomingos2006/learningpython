
def mult(*args):
    num =1
    for numero in args:
        num*= numero
    
    return num

def par_impar(numero):
    return(f'par' if numero%2 ==0 else 'impar')

print(mult(5,4,100))
print(par_impar(5))