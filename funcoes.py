def receberValidarEntrada(tipo):
    """
    Função criada para receber a entrada do usuário e validar que ela foi digitada corretamente
    de acordo com o tipo definido no parâmetro quando a função for chamada. Caso dê erro ou exceção,
    o loop de repetição continuará até que a entrada seja adequada.
    :param tipo: 1 - inteiro, 2 - real, 3 - string
    :return:
    """
    validandoEntrada = 1
    while validandoEntrada == 1:
        match tipo:
            case 1:
                try:
                    entrada = int(input("<<< "))
                except:
                    print(f'>>> Você digitou uma entrada inválida. Por favor, tente novamente!')
                else:
                    validandoEntrada = 0
                    return entrada
            case 2:
                try:
                    entrada = float(input("<<< "))
                except:
                    print(f'>>> Você digitou uma entrada inválida. Por favor, tente novamente!')
                else:
                    validandoEntrada = 0
                    return entrada
            case 3:
                try:
                    entrada = str(input("<<< "))
                except:
                    print(f'>>> Você digitou uma entrada inválida. Por favor, tente novamente!')
                else:
                    validandoEntrada = 0
                    return entrada

def verificarIdadePulseira():
    validandoIdade = 1
    print(f'--- Idade da pessoa:')
    while validandoIdade == 1:
        idade = receberValidarEntrada(1)
        if idade <= 0:
            print(f'>>> A idade inserida está inválida. Por favor, tente novamente.')
        if idade >= 1 and idade <= 9:
            print(f'>>> Ingresso gratuito / Pulseira: amarela.')
            validandoIdade = 0
        if idade >= 10 and idade <= 17:
            print(f'>>> Ingresso adolescente: R$15 / Pulseira: laranja.')
            validandoIdade = 0
        if idade >= 18 and idade <= 130:
            estudante = verificarEstudante()
            if estudante:
                print(f'>>> INGRESSO É 20 PORRRAAAAA PULSEIRA ROXA')
                validandoIdade = 0
            else:
                print(f'>>> PASSA OS 40 FILHO DA PUTA PULSEIRA VERMEIA')
                validandoIdade = 0
        if idade > 130:
            print(f'>>> Para de mentir... Inválido, tente novamente.')

def validarMatricula():
    '''
    função para verificar se a matrícula do estudante é válida
    :return: True se for validada
    '''
    validandoMatricula = 1
    print(f'--- Informe o número da matricula de 9 dígitos [000 para abandonar a validação de matrícula]: ')
    while validandoMatricula == 1:
        matricula = receberValidarEntrada(3)
        if matricula.isdigit() and len(matricula) == 9:
            print(f'>>> Matrícula validada com sucesso!')
            return True
        elif matricula == "000":
            return False
        else:
            print(f'>>> Matrícula inválida. Por favor, digite novamente. [digite 000 caso não seja aluno]')

def verificarEstudante():
    '''
    Checa se a pessoa estuda na UEFS ou não. Se estuda, chama a função
    que verifica e valida a matrícula.
    :return: status/True se for estudante, False se não for
    '''
    verificandoEstudante = 1
    print(f'--- A pessoa estuda na UEFS? [1 - SIM | 2 - NÃO]')
    while verificandoEstudante == 1:
        escolha = receberValidarEntrada(1)
        match escolha:
            case 1:
                status = validarMatricula()
                return status
            case 2:
                return False
            case _:
                print(f'>>> Opção inválida. Por favor, tente novamente.')

'''def processarCompra(ingressos):

    for i in range(ingressos):
        verificarIdadePulseira()'''

