
def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

bom_dia = saudacao('Bom dia')

print(bom_dia('David'))
print(bom_dia('Wellyda'))
print(bom_dia('Rebeka'))




