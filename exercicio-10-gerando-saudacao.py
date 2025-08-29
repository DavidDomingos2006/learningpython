def destinatario(nome):

    def mensagem(saudacao):

        return f'Ola {nome}, {saudacao}'

    return mensagem

saudacao_david = destinatario('David')
saudacao_wellyda = destinatario('Wellyda')

print(saudacao_david('como voce está?'))
print(saudacao_wellyda('Vocé vai hoje?'))


