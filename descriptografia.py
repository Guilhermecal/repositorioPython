'''
treinamento learn microsoft
conceito básico do Python para criar um decodificador de mensagem secreta
Cifra de Cézar
'''
from time import sleep
def lasso_letter(letra, shift_amount):

    letra_code = ord(letra.lower()) # mostra o código ASCII do caractere
    a_ascii = ord('a')

    # calculando o caractere decodificado
    alpha_size = 26
    true_letter_code = a_ascii + (((letra_code - a_ascii) + shift_amount) % alpha_size)
    
    letra_decodificada = chr(true_letter_code)
    return letra_decodificada


def lasso_world(palavra, shift_amount):
    palavra_decodificada = ""
    for letra in palavra:
        letra_decodificada = lasso_letter(letra, shift_amount)
        palavra_decodificada = palavra_decodificada + letra_decodificada
    return palavra_decodificada
    


# principal
print('Cifra de Cézar')
while True: 

    word = str(input('código: '))
    shift = int(input('deslocamento:'))
    print(f'decodificando: "{word}" ')
    for i in range(5):
        sleep(1)
        print(' . ')

    print(lasso_world(word, shift))
    resp = str(input('decodificar outra palavra?[s/n]')).upper()[0]
    if resp == "N":
        break


#tem que adicionar linhas para salvar mensagens e mostrar todas palavras inseridas
# melhorar a amostra das cifras

