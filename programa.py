from funcoes import *

'''print("~"*30)
print("{:^30}".format('TOTEM DE INGRESSOS'))
print("~"*30)
print(f'--- Boas vindas ao sistema de ingressos da Game-Con Bahia Pocket!!!'
      f'--- Os ingressos são pulseiras que representam cada tipo de participante'
      f'--- de acordo com a cor.'
      f'--- Amarelas: para criança, gratuita; Laranjas: para adolescentes, R$15;'
      f'--- Vermelhas: para adultos e jovens: R$40; Roxas: para universitários, R$20\n\n')

eventoAcontecendo = 1
while eventoAcontecendo == 1:
    pulseirasCompradas = {
        "amarela": 0,
        "laranja": 0,
        "vermelha": 0,
        "roxa": 0
    }
    capacidade = receberValidarEscolha("--- Defina a capacidade para esse dia:", 1)
    print(f'>>>>> VENDAS INICIADAS <<<<<\n\n')
    vendas = 1
    while vendas == 1:
        print(f'--- Seguir as vendas? [Digite 1, ou caso queira encerrar o programa, digite o código]')
        seguir = receberValidarEntrada(3)
        if seguir == "1":
            if temCapacidade(pulseirasCompradas, capacidade):
                quantIngressos = receberValidarEscolha("--- Quantos ingressos quer comprar?", 1)
                dadosCompra = processarCompra(quantIngressos)
                pulseirasCompradas = atualizarDicionarioCompras(dadosCompra, pulseirasCompradas)
            else:
                print(f'>>> O CUCA ESTÁ LOTADO! CAIXA SERÁ FECHADO E O EVENTO ENCERRADO.')
                vendas = 0
                eventoAcontecendo = 0
        elif seguir == "4thmjw94":
            print(f'>>> PROGRAMA ENCERRADO! O CAIXA SERÁ FECHADO E OS DADOS EXIBIDOS')
            vendas = 0
            eventoAcontecendo = 0
        else:
            print(f'--- Entrada inválida. Tente novamente!')'''

pulseirasCompradas = {
    "amarela": 16,
    "laranja": 43,
    "vermelha": 14,
    "roxa": 32
}

capacidade = 120
arrecadacao = somarValoresPulseiras(pulseirasCompradas)
potePremiosCosplay = tirarPotePremios(arrecadacao)
distribuicaoPremios = distribuirPremiosCosplay(potePremiosCosplay)
lucro = arrecadacao - potePremiosCosplay
dadosArrecadacao = ganhosPorPulseira(pulseirasCompradas)
mediaPagantes = arrecadacao / (somarPulseiras(pulseirasCompradas) - pulseirasCompradas['amarela'])
mediaGeral = arrecadacao / somarPulseiras(pulseirasCompradas)
vagasRestantes = capacidade - somarPulseiras(pulseirasCompradas)

print('#'*50)
print("{:^50}".format("VISÃO GERAL DO DIA DE EVENTO:\n"))
print(f'>>> O dia arrecadou R${arrecadacao}')
print(f'>>> O lucro foi de R${lucro}')
print(f'>>> Capacidade restante ao final do evento: {vagasRestantes}\n')
print(f'>>> R${potePremiosCosplay} foram destinados para a premiação do concurso cosplay')
for i, v in enumerate(distribuicaoPremios):
    print(f'>>> {i+1}º lugar: {v}')
print(f'\n>>> O ticket médio por categorias pagantes foi R${mediaPagantes:.2f}')
print(f'>>> O ticket geral foi R${mediaGeral:.2f}')
print('#'*50)









