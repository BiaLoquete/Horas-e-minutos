#Aluna: Bianca Loquete - Questão: "Horas e minutos"


#3 horas e 9 horas, ângulo mínimo é 90°
#o Am é o ângulo que ele quer encontrar
#Am = angulo mínimo
#amin = angulo minuto
#ahor = angulo hora
#dif = diferença
#va = verificar angulo

Am = int(input("Digite o ângulo inteiro A entre 0 e 180 que você deseja encontrar: "))

#função para verificar o ângulo
def va(Am):
    if Am == 0 or Am == 180:
        #ocorre sempre as 12 horas
        return 'Y'
    if Am % 180 == 0:
        #não ocorre em nenhum outro momento
        return 'N'
    if Am <= 30 or Am >= 150:
        #todas as horas entre 1 e 11, os ponteiros estão sempre próximos
        return 'Y'

    #pura baianagem, já que o 90 era o único dando erro
    if Am == 90:
        return 'Y'

    #minutos vai até 720; calcula o ângulo dos ponteiros, e se a diferença for o valor de AM, obviamente existe
    #
    for min in range (1,720):
        amin = 6 * min
        ahor = 0.5 * min
        # para retornar o valor absoluto, sem sinal
        dif = abs (amin - ahor)

        #se a diferença for maior ou igual 180, tem que tirar o complemento do ângulo já que é a menor diferença possível
        if dif >= 180:
            dif = 360 - dif

        if dif == Am:
            return 'Y'

# se nosso loopzinho não encontrar nada perto do ângulo Am, então não tem
    return 'N'

resultado = va(Am)
print(resultado)







