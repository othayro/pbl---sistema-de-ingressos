from funcoes import *
# Acima, estou importando o arquivo com as funções que eu criei e usei nesse programa.

print("~"*30)
print("{:^30}".format('TOTEM DE INGRESSOS'))
print("~"*30)
print(f'--- Boas vindas ao sistema de ingressos da Game-Con Bahia Pocket!!!')
print(f'--- Os ingressos são pulseiras que representam cada tipo de categoria por cor')
print(f'--- Amarelas: para criança, gratuita; Laranjas: para adolescentes, R$15;')
print(f'--- Vermelhas: para adultos e jovens: R$40; Roxas: para universitários, R$20\n')

# O sistema roda em um loop de repetição while com a variável eventoAcontecendo. No loop, declaro o dicionário
# das pulseiras (ingressos) e peço a entrada da capacidade para o dia de evento. (Para entender o funcionamento
# de cada função, favor ir até elas no arquivo funcoes.py da pasta e ler os comentários.)
eventoAcontecendo = 1
while eventoAcontecendo == 1:
    # Vendas gerais de pulseiras no dia de evento.
    pulseirasCompradas = {
        "amarela": 0,
        "laranja": 0,
        "vermelha": 0,
        "roxa": 0
    }

    capacidade = receberValidarEscolha("--- Defina a capacidade para esse dia:", 1)
    print(f'>>>>> VENDAS INICIADAS <<<<<\n')

    # A partir daqui começa o dia de evento de fato. A varíavel vendas controla o loop para a venda de pulseiras.
    # No começo do loop, o usuário tem a opção de seguir as vendas ou encerrar o evento.
    # Qualquer entrada além dessas duas é recusada.
    vendas = 1
    while vendas == 1:
        print(f'--- Iniciar uma venda? [Digite 1, ou caso queira encerrar o programa, digite o código]')
        seguir = receberValidarEntrada(3)
        if seguir == "1":
            # Dentro dessa condição, há outra que checa se há capacidade no evento para mais gente entrar.
            # Se tiver, mais uma venda é iniciada. Se não tiver mais capacidade, o programa é encerrado.
            if temCapacidade(pulseirasCompradas, capacidade):
                # Essa variável recebe a quantidade de ingressos que a pessoa deseja comprar.
                quantIngressos = receberValidarEscolha("--- Quantos ingressos quer comprar?", 1)

                # condição para garantir que não se tente comprar mais ingressos do que a capacidade restante.
                if quantIngressos <= (capacidade - somarPulseiras(pulseirasCompradas)):
                    # Essa variável vai chamar a função que executa a compra passando a quantidade de ingressos escolhida
                    # como parâmetro. Esse parâmetro vai ser usado em um for dentro da função. O retorno da função
                    # é um dicionário com as pulseiras adquiridas nessa venda, que é atribuído à variável dadosCompra.
                    dadosCompra = processarCompra(quantIngressos)

                    # Aqui a varíavel de vendas gerais é redefinida. A função pega como parâmetro o dicionário dessa
                    # venda e o dicionário geral das vendas do dia. Adiciona dadosCompra à pulseirasCompradas e retorna
                    # com o dicionário de vendas geral atualizado.
                    pulseirasCompradas = atualizarDicionarioCompras(dadosCompra, pulseirasCompradas)
                else:
                    print(f'>>> Quantidade excede vagas restantes ({capacidade - somarPulseiras(pulseirasCompradas)})')
            else:
                # Sem mais capacidade, as variáveis eventoAcontecendo e vendas mudam de valor.
                # Fechando o loop das vendas e do evento.
                print(f'>>> O CUCA ESTÁ LOTADO! CAIXA SERÁ FECHADO E O EVENTO ENCERRADO.')
                vendas = 0
                eventoAcontecendo = 0
        elif seguir == "4thmjw94":
            # Se a organização encerrar com o código, as varíaveis de controle dos loops mudam de valor
            # e o evento para.
            print(f'>>> PROGRAMA ENCERRADO! O CAIXA SERÁ FECHADO E OS DADOS EXIBIDOS')
            vendas = 0
            eventoAcontecendo = 0
        else:
            print(f'--- Entrada inválida. Tente novamente!')

# O programa só exibirá a visão geral do evento se forem realizadas vendas de ingressos.
# Se não tiver, um mensagem informando a ausência de dados é imprimida. Sem essa condição
# Haveriam diversos erros pela ausência de valores necessários para o fechamento do caixa
# e o cálculo das estatísticas.
if somarPulseiras(pulseirasCompradas) > 0:
    # Após as vendas encerrarem, é feito os cálculos necessário para o fechamento do caixa
    # e a exibição das estatísticas requisitadas pela organização do evento.

    # venda total de pulseiras no dia. a função retorna um número inteiro.
    arrecadacao = somarValoresPulseiras(pulseirasCompradas)

    # É retirado da arrecadação o pote destinado ao prêmio do concurso dos cosplayers.
    # A função retorna um valor real.
    potePremiosCosplay = tirarPotePremios(arrecadacao)

    # Essa varíavel chama uma função que recebe o pote de prêmios e retorna uma lista para os valores ganhos
    # nas 3 posições dos vencedores do concurso cosplay.
    distribuicaoPremios = distribuirPremiosCosplay(potePremiosCosplay)

    # É calculado o lucro para a organização baseada na arrecadação e no pote de prêmios
    lucro = arrecadacao - potePremiosCosplay

    # caso o programa seja encerrado sem arrecadacao, gerará erros de divisão por zero.
    # então o sistema só calcula as médias se tiver arrecadacao.
    if arrecadacao > 0:
        # Ticket médio dos pagantes. Aqui, eu subtraio da quantidade de pulseiras vendidas as amarelas
        # (as amarelas, das crianças)
        mediaPagantes = arrecadacao / (somarPulseiras(pulseirasCompradas) - pulseirasCompradas['amarela'])

        # Aqui o ticket médio é tirado com todas as categorias
        mediaGeral = arrecadacao / somarPulseiras(pulseirasCompradas)

        # Eu subtraio o total de pulseiras vendidas com a capacidade.
        vagasRestantes = capacidade - somarPulseiras(pulseirasCompradas)

    print('#' * 50)
    print("{:^50}".format("VISÃO GERAL DO DIA DE EVENTO:\n"))
    print(f'>>> O dia arrecadou R${arrecadacao}')
    print(f'>>> O lucro foi de R${lucro}')
    print(f'>>> Capacidade restante ao final do evento: {vagasRestantes}\n')
    print(f'>>> R${potePremiosCosplay} foram destinados para a premiação do concurso cosplay')
    for i, v in enumerate(distribuicaoPremios):
        print(f'>>> {i + 1}º lugar: R${v}')
    print(f'\n>>> O ticket médio por categorias pagantes foi R${mediaPagantes:.2f}')
    print(f'>>> O ticket geral foi R${mediaGeral:.2f}\n')
    ganhosPorPulseira(pulseirasCompradas)
    print('#' * 50)
else:
    print(f'#### NÃO FOI REALIZADA NENHUMA VENDA, LOGO, NÃO HÁ DADOS PARA PROCESSAR E EXIBIR.')

# Declaração de autoria
# Nome: [seu nome completo]
# Declaro que este código foi desenvolvido por mim, com base no meu próprio
# entendimento e esforço. Não houve plágio ou cópia integral de terceiros.
# Ferramentas de IA, quando utilizadas, foram apenas como apoio ao aprendizado
# e não para a geração integral deste código.









