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
        entrada = str(input('<<< '))
        match tipo:
            case 1:
                if entrada.isdigit():
                    entradaTransformada = int(entrada)
                    if entradaTransformada >= 0:
                        return entradaTransformada
                    else:
                        print(f'>>> Por favor, insira um valor inteiro positivo.')
                else:
                    print(f'>>> Você digitou uma entrada inválida. Por favor, tente novamente!\n')
            case 2:
                entradaSemEspacos = entrada.replace(" ", "")
                if entradaSemEspacos.replace(".", "", 1).isdigit():
                    entradaTransformada = float(entradaSemEspacos)
                    return entradaTransformada
                elif entradaSemEspacos.replace(",", "", 1).isdigit():
                    entradaTransformada = float(entradaSemEspacos.replace(",", ".", 1))
                    return entradaTransformada
                else:
                    print(f'>>> Entrada inválida. Por favor, digite um valor real positivo.')
            case 3:
                return entrada


def verificarIdadePulseira(contador):
    validandoIdade = 1
    print(f'--- INGRESSO {contador+1} | Digite a idade:')
    while validandoIdade == 1:
        idade = receberValidarEntrada(1)
        if idade <= 0:
            print(f'>>> A idade inserida está inválida. Por favor, tente novamente.\n')
        if idade >= 1 and idade <= 9:
            print(f'>>> Ingresso gratuito / Pulseira: amarela.\n')
            return "amarela"
        if idade >= 10 and idade <= 17:
            print(f'>>> Ingresso adolescente: R$15 / Pulseira: laranja.\n')
            return "laranja"
        if idade >= 18 and idade <= 130:
            estudante = verificarEstudante()
            if estudante:
                print(f'>>> Ingresso jovem/adulto estudante: R$20 / Pulseira: roxa.\n')
                return "roxa"
            else:
                print(f'>>> Ingresso jovem/adulto estudante: R$40 / Pulseira: vermelha.\n')
                return "vermelha"
        if idade > 130:
            print(f'>>> Para de mentir... Inválido, tente novamente.\n')

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

def resumirCompra(pulseirasEscolhidas):
    valorTotal = 0
    print(f'--- RESUMO DA COMPRA:')
    for i, v in pulseirasEscolhidas.items():
        if v > 0:
            if i == "amarela":
                print(f'>>> {v}x pulseira {i}: GRATUITO')
            elif i == "laranja":
                valorTotal += v*15
                print(f'>>> {v}x pulseira {i}: R${v*15} (R$15 cada)')
            elif i == "vermelha":
                valorTotal += v*40
                print(f'>>> {v}x pulseira {i}: R${v*40} (R$40 cada)')
            elif i == "roxa":
                valorTotal += v*20
                print(f'>>> {v}x pulseira {i}: R${v*20} (R$20 cada)')
    print(f'>>> TOTAL DA COMPRA: R${valorTotal}\n')
    return valorTotal

def efetuarPagamento(total):
    efetuando = 1
    while efetuando == 1:
        print(f'--- Insira o valor do dinheiro para pagar:')
        pegarDinheiro = receberValidarEntrada(2)
        if pegarDinheiro < total:
            print(f'>>> VALOR NÃO SUFICIENTE!')
        elif pegarDinheiro >= total:
            troco = pegarDinheiro - total
            if troco == 0:
                print(f'>>> Pagamento efetuado! Nao precisa de troco.')
                efetuando = 0
            elif troco > 0:
                print(f'>>> Pagamento efetuado! O troco é R${troco:.2f}.')
                efetuando = 0

def processarCompra(ingressos):
    pulseirasAcomprar = {
        "amarela": 0,
        "laranja": 0,
        "vermelha": 0,
        "roxa": 0
    }

    for i in range(ingressos):
        pulseiraAtribuida = verificarIdadePulseira(i)
        pulseirasAcomprar[pulseiraAtribuida] += 1

    totalPagar = resumirCompra(pulseirasAcomprar)
    efetuarPagamento(totalPagar)
    print(f'AQUI CHEGA AO FIM HEREGE')
