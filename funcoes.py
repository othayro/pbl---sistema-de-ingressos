# Declaração de autoria
# Nome: Thayro Gabriel Alves
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.


def receberValidarEntrada(tipo):
    """
    Função criada para receber a entrada do usuário e validar que ela foi digitada corretamente
    de acordo com o tipo definido no parâmetro quando a função for chamada.

    :param tipo: 1 - inteiro, 2 - real, 3 - string
    :return: a variável com o valor do tipo do parâmetro
    """
    validandoEntrada = 1
    while validandoEntrada == 1:
        entrada = str(input('<<< '))
        # a entrada inicial é uma string, pois assim não importa o que for digitado, não dá erro.

        match tipo:
            case 1:
                # Para validar um inteiro, a função isdigit() já é suficiente.
                if entrada.isdigit():
                    entradaTransformada = int(entrada)
                    if entradaTransformada >= 0:
                        return entradaTransformada
                    else:
                        print(f'>>> Por favor, insira um valor inteiro positivo.')
                else:
                    print(f'>>> Você digitou uma entrada inválida. Por favor, tente novamente!\n')
            case 2:
                # Para validar um real, começa tirando todos os espaços da string de entrada e colocando
                # em uma nova varíavel.
                entradaSemEspacos = entrada.replace(" ", "")

                # Aqui retira o primeiro ponto da string e testa se só tem dígitos.
                if entradaSemEspacos.replace(".", "", 1).isdigit():
                    # Se tiver apenas dígitos, uma nova variável recebe a entrada tratada transformada em float
                    # e retorna.
                    entradaTransformada = float(entradaSemEspacos)
                    return entradaTransformada
                # Para o caso de digitarem vírgula ao invés de ponto, a condição abaixo
                # faz o mesmo que acima, só que com vírgula.
                elif entradaSemEspacos.replace(",", "", 1).isdigit():
                    # A diferença é que transforma a vírgula em ponto para poder transformar em float
                    # em uma nova varíavel.
                    entradaTransformada = float(entradaSemEspacos.replace(",", ".", 1))
                    return entradaTransformada
                else:
                    print(f'>>> Entrada inválida. Por favor, digite um valor real positivo.')
            case 3:
                # Se for pra retornar uma string mesmo, apenas transforma tudo em minúscula pra padronizar.
                return entrada.lower()

def receberValidarEscolha(texto, tipo):
    '''
    Ao invés de usar input, essa função é usada para receber e validar as escolhas.
    Essa função é usada quando a escolha do usuário afeta partes importantes do funcionamento
    do programa como a capacidade do evento, a quantidade de ingressos em um ciclo de venda, etc.
    Assim evita o transtorno de digitar uma entrada indesejada.

    :param texto: o texto da pergunta que seria inserido dentro das aspas do input [input('<aqui>')]
    :param tipo: o tipo de varíavel que será recebida (será usada para quando chamar a função de entrada)
    :return: a entrada que o usuário inserir e confirmar
    '''
    print(f'{texto}')

    # Loop usado para manter a validação repetindo até que o usuário insira o dado requisitado
    # e confirme a escolha. Se ele nao confirmar, pode inserir a escolha novamente.
    validando = 1
    while validando == 1:
        escolha = receberValidarEntrada(tipo)
        print(f'--- Você confirma a escolha ({escolha})? [1 - SIM | 0 - NÃO]')
        confirmando = 1
        while confirmando == 1:
            confirmacao = receberValidarEntrada(1)
            if confirmacao == 1:
                return escolha
            elif confirmacao == 0:
                print(f'{texto}')
                confirmando = 0
            else:
                print(f'>>> Opção inválida, tente novamente!!!')


def verificarIdadePulseira(contador):
    '''
    Aqui verifica a categoria/cor da pulseira baseada na idade da pessoa
    que receberá o ingresso.

    :param contador: qual a ordem do ingresso no loop de repetição de venda na qual essa função é chamada. para fins
    de tornar o terminal mais dinamico.
    :return: a cor da pulseira de acordo com a idade.
    '''
    print(f'--- INGRESSO {contador+1} | Digite a idade:')

    validandoIdade = 1
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
            # Se for jovem/adulto, verifica se é estudante.
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
    '''
    recebe um dicionário com o registro das pulseiras escolhidas na compra atual.
    imprime um resumo da compra e retorna o total a ser pago.

    :param pulseirasEscolhidas: dicionário com as pulseiras escolhidas na compra
    :return: total da compra
    '''
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
    '''
    recebe a entrada do usuário com o valor que irá pagar e
    calcula se é o suficiente pra ele efetuar o pagamento.

    :param total: o valor total da compra
    :return: A confirmação do pagamento e o troco (se tiver)
    '''
    efetuando = 1
    while efetuando == 1:
        if total > 0:
            print(f'--- Insira o valor do dinheiro para pagar:')
            pegarDinheiro = receberValidarEntrada(2)
            if pegarDinheiro < total:
                print(f'>>> VALOR NÃO SUFICIENTE!')
            elif pegarDinheiro >= total:
                troco = pegarDinheiro - total
                if troco == 0:
                    return print(f'>>> Pagamento efetuado!')
                elif troco > 0:
                    return print(f'>>> Pagamento efetuado! O troco é R${troco:.2f}.')
        else:
            return print(f'>>> GRATUITO. Não há o que pagar.')

def atualizarDicionarioCompras(dados, compradas):
    '''
    adiciona os dados do dicionário da compra atual ao dicionário das vendas gerais.

    :param dados: dicionário com as pulseiras vendidas na compra atual
    :param compradas: dicionário com as pulseiras gerais vendidas
    :return: dicionário com registro das vendas gerais atualizado
    '''
    for i, v in dados.items():
        compradas[i] += v
    return compradas

def somarPulseiras(dicionario):
    '''
    calcula a quantidade total de pulseiras que foram vendidas

    :param dicionario: dicionário com as vendas gerais de pulseiras
    :return: quantidade de pulseiras vendidas
    '''
    somaTotal = 0
    for v in dicionario.values():
        somaTotal += v
    return somaTotal

def somarValoresPulseiras(dicionario):
    '''
    soma o valor total de todas as pulseiras vendidas de acordo com seus
    respectivos preços.

    :param dicionario: dicionário com as vendas gerais de pulseiras
    :return: a soma total dos valores
    '''
    somaValores = int(0)
    for i, v in dicionario.items():
        if i == "laranja":
            vendasPorCor = v * 15
            somaValores += vendasPorCor
        elif i == "vermelha":
            vendasPorCor = v * 40
            somaValores += vendasPorCor
        elif i == "roxa":
            vendasPorCor = v * 20
            somaValores += vendasPorCor
    return somaValores

def tirarPotePremios(arrecadado):
    '''
    recebe o valor arrecadado no dia de evento e calcula quanto
    será destinado ao pote de prêmios do concurso cosplay.

    :param arrecadado: valor arreacadado no dia de evento
    :return: pote de premios calculado
    '''
    if arrecadado <= 300:
        pote = (10 * arrecadado) / 100
    elif arrecadado > 300 and arrecadado <= 700:
        pote = (15 * arrecadado) / 100
    elif arrecadado > 700:
        pote = (20 * arrecadado) / 100
    return pote

def distribuirPremiosCosplay(pote):
    '''
    recebe o pote de premios e calcula quanto cada uma das 3
    posicoes do pódio ganha.

    :param pote: pote de premios cosplay
    :return: lista com os premios de cada posicao.
    '''
    podio = []
    # 0 é o primeiro lugar, 1 o segundo e 3 o terceiro lugar.
    for posicao in range(3):
        if posicao == 0:
            podio.append((50 * pote) / 100)
        elif posicao == 1:
            podio.append((30 * pote) / 100)
        elif posicao == 2:
            podio.append((20 * pote) / 100)
    return podio

def ganhosPorPulseira(pulseiras):
    '''
    Recebe o dicionário das vendas gerais de pulseiras, calcula quanto
    cada categoria/cor vendeu e coloca em um novo dicionário que contém
    os valores totais por categoria ao invés da quantidade de pulseiras
    vendidas. Também faz uma lista com o ranking de categorias por vendas.
    Ao final, imprime no terminal quanto cada categoria arrecadou e qual
    vendeu mais e menos.

    :param pulseiras: dicionário com o registro das vendas gerais do dia
    :return: nada.
    '''
    # dicionário para adicionar os valores arrecadados por categoria pagante.
    ganhosPulseiras = {}
    for i, v in pulseiras.items():
        # aqui pega a quantidade vendida de cada uma, calcula o saldo arrecadado e adiciona
        # no dicionário criado acima.
        if i == "laranja":
            ganhos = v * 15
            ganhosPulseiras[i] = ganhos
        elif i == "vermelha":
            ganhos = v * 40
            ganhosPulseiras[i] = ganhos
        elif i == "roxa":
            ganhos = v * 20
            ganhosPulseiras[i] = ganhos

    # passa por todos os itens do dicionário e checa qual a maior e a menor arrecadação
    maior = int(0)
    menor = int(9000000000)
    for indicie, ganho in ganhosPulseiras.items():
        if ganho > maior:
            maior = ganho
        if ganho < menor:
            menor = ganho

    # Primeiro pega a maior arrecadação, cruza com o dicionário e imprime as cores
    # com tal arrecadação
    print(f'>>> Arrecadou R${maior} (maior contribução):', end=" ")
    for i, v in ganhosPulseiras.items():
        if v == maior:
            print(f'{i}', end="; ")
    print(f'')

    # Mesmo processo, mas para a categoria que não vendeu nem mais, nem menos
    for i, v in ganhosPulseiras.items():
        if v < maior and v > menor:
            print(f'>>> Arrecadou R${v}: {i};')

    # Mesmo processo, mas para a categoria que menos vendeu.
    print(f'>>> Arrecadou R${menor} (menor contribução):', end=" ")
    for i, v in ganhosPulseiras.items():
        if v == menor:
            print(f'{i}', end="; ")
    print(f'')
    # Essa foi a forma que eu (Thayro, autor do código) encontrei para ranquear
    # as arrecadações por categoria sem usar funções nativas do Python que manipulam dicionários.
    # Funciona apenas para esse contexto desse programa. Não é dinâmico e não escala.
    # Se tivessem mais de 3 categorias pagas, teria de achar outra solução. É um defeito meu de lógica
    # que limita o código, mas funciona aqui nessa situação. :(


def temCapacidade(dicionarioPulseiras, capacidade):
    '''
    chama a função que soma a quantidade de pulseiras vendidas e checa se tem capacidade
    para mais gente entrar

    :param dicionarioPulseiras: dicionário com o registro das vendas gerais de pulseiras
    :param capacidade: capacidade definida pela organização antes de iniciar o evento.
    :return: True se tiver capacidade; False se não tiver.
    '''
    if somarPulseiras(dicionarioPulseiras) < capacidade:
        return True
    else:
        return False


def processarCompra(ingressos):
    '''
    função principal para a execução das vendas dos ingressos.

    :param ingressos: a quantidade de ingressos que serão comprados
    :return: dicionário com as pulseiras adquiridas na compra
    '''

    # dicionário para registrar a compra atual
    pulseirasAcomprar = {
        "amarela": 0,
        "laranja": 0,
        "vermelha": 0,
        "roxa": 0
    }

    # o loop é feito usando a quantidade de ingressos a ser comprados como range.
    for i in range(ingressos):
        # declara-se a varíável que chama a função para ver a idade da pessoa, se ela é estudante
        # e qual categoria ela pertence. se retorna uma string com a cor.
        pulseiraAtribuida = verificarIdadePulseira(i)

        # usa a cor da pulseira atribuída à pessoa como índicie ao adicionar o registro no dicionário
        # da compra atual.
        pulseirasAcomprar[pulseiraAtribuida] += 1

    # quando o loop acaba, a varíavel do total a pagar chama a função que tem como parâmetro
    # o dicionário de registro da compra atual. o que retorna é o valor total a ser pago, um valor inteiro.
    totalPagar = resumirCompra(pulseirasAcomprar)

    # função para realizar o pagamento da compra.
    efetuarPagamento(totalPagar)

    return pulseirasAcomprar

# Declaração de autoria
# Nome: [seu nome completo]
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.