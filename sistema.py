aparelhos = []
def listar_aparelhos():
  for i aparelho in enumerate(aparelhos)
  print(f"[{i}] {aparelho['nome']}")

def calcular_consumo(aparelhos, tarifa):
   if not aparelhos:
      print("Nenhum aparelho cadastrado.")
      return
   for aparelho in aparelhos:
      potencia = aparelhos["potencia"]
      horas = aparelhos["horas"]
      nome = aparelhos["nome"]

      consumo = (potencia * horas) / 1000
      custo_dia = consumo * tarifa
      custo_mes = custo_dia * 30

       print(f"\n{nome}")
       print(f"Consumo: {consumo:.2f} kWh/dia")
       print(f"Custo diário: R$ {custo_dia:.2f}")
       print(f"Custo mensal: R$ {custo_mes:.2f}")
       print("-" * 30)

def identificar_vilao(aparelhos):
    if not aparelhos:
        print("Nenhum aparelho cadastrado.")
        return

    # Lógica de comparação: assume o primeiro como maior e testa os outros
    vilao = aparelhos[0]
    for aparelho in aparelhos:
        consumo_atual = aparelho["potencia"] * aparelho["horas"]
        consumo_vilao = vilao["potencia"] * vilao["horas"]

        if consumo_atual > consumo_vilao:
            vilao = aparelho

    print("\n" + "=" * 30)
    print(f"O VILÃO ENERGÉTICO: {vilao['nome'].upper()}")
    print(f"Consumo: {(vilao['potencia'] * vilao['horas']) / 1000:.2f} kWh/dia")
    print("=" * 30)
    # Definição geral de meta de economia


def definir_meta_economia(aparelhos, tarifa):
    if not aparelhos:
        print("Cadastre aparelhos antes de definir uma meta.")
        return

    try:
        meta = float(input("Quanto você deseja pagar no máximo por mês (R$)? "))
    except ValueError:
        print("Valor inválido.")
        return

    # 1. Calcular o gasto total atual
    gasto_total_mensal = 0
    vilao = aparelhos[0]

    for ap in aparelhos:
        consumo_mensal = (ap["potencia"] * ap["horas"] * 30) / 1000
        custo_mensal = consumo_mensal * tarifa
        gasto_total_mensal += custo_mensal

        if (ap["potencia"] * ap["horas"]) > (vilao["potencia"] * vilao["horas"]):
            vilao = ap

    print(f"\nSeu gasto atual estimado: R$ {gasto_total_mensal:.2f}")

    # 2. Comparar com a meta
    if gasto_total_mensal <= meta:
        print("Parabéns! Seus gastos já estão dentro da meta.")
    else:
        diferenca = gasto_total_mensal - meta
        print(f"Atenção! Você está gastando R$ {diferenca:.2f} acima da sua meta.")

        # 3. Gerar sugestão inteligente baseada no vilão
        consumo_vilao_kwh = (vilao["potencia"] * vilao["horas"] * 30) / 1000
        custo_vilao_mensal = consumo_vilao_kwh * tarifa

        print(f"\n--- PLANO DE AÇÃO ---")
        print(f"Para economizar, foque no aparelho: {vilao['nome']}")

        # Cálculo de quanto tempo reduzir (aproximado)
        if custo_vilao_mensal > 0:
            reducao_horas = (diferenca / custo_vilao_mensal) * vilao["horas"]
            print(f"Sugestão: Reduza o uso do {vilao['nome']} em aproximadamente {reducao_horas:.1f} horas por dia.")


# --- FLUXO PRINCIPAL ---

while True:
    print("\n== SISTEMA DE ENERGIA ===")
    print("[1] Cadastrar aparelhos")
    print("[2] Listar aparelhos")
    print("[3] Calcular consumo")
    print("[4] Identificar Vilão")
    print("[5] Definir meta de Economia")
    print("[6] Editar")
    print("[7] Excluir")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aparelho: ")
        while True:
            try:
                potencia = float(input("Potência (W): "))
                break
            except ValueError:
                print("Digite um número válido.")

        while True:
            try:
                horas = float(input("Quantas horas por dia: "))
                break
            except ValueError:
                print("Digite um número válido.")

        # Salva os dados em um dicionário dentro da lista
        aparelho = {"nome": nome, "potencia": potencia, "horas": horas}
        aparelhos.append(aparelho)
        print("Aparelho cadastrado com sucesso.")

    elif opcao == "2":
        if not aparelhos:
            print("Nenhum aparelho cadastrado.")
        else:
            # Lista de forma simples para visualização
            for aparelho in aparelhos:
                print(f"Nome: {aparelho['nome']} | {aparelho['potencia']}W")

    elif opcao == "3":
        while True:
            try:
                tarifa = float(input("Digite o preço da tarifa: "))
                break
            except ValueError:
                print("Digite um número válido.")
        calcular_consumo(aparelhos, tarifa)
    # VER QUAL APARELHO CONSUME MAIS
    elif opcao == "4":
        identificar_vilao(aparelhos)

    elif opcao == "5":
        # Precisamos da tarifa para calcular a meta
        try:
            tarifa = float(input("Confirme o preço da tarifa (R$): "))
            definir_meta_economia(aparelhos, tarifa)
        except ValueError:
            print("Tarifa inválida.")

    elif opcao == "6":
        if not aparelhos:
            print("Nenhum aparelho cadastrado.")
        else:
            listar_aparelhos(aparelhos)
            try:
                indice = int(input("Digite o número do aparelho: "))
                aparelhos[indice]["nome"] = input("Novo nome: ")
                aparelhos[indice]["potencia"] = float(input("Nova potência (W): "))
                aparelhos[indice]["horas"] = float(input("Novas horas: "))
                print("Aparelho atualizado!")
            except:
                print("Erro ao editar.")
    # REMOVER APARELHO DA LISTA
    elif opcao == "7":
        if not aparelhos:
            print("Nenhum aparelho cadastrado.")
        else:
            listar_aparelhos(aparelhos)
            try:
                indice = int(input("Digite o número do aparelho: "))
                removido = aparelhos.pop(indice)
                print(f"{removido['nome']} removido!")
            except:
                print("Índice inválido.")
    # OPÇÂO PARA SAIR DO PROGRAMA
    elif opcao == "0":
        print("Saindo...")
        break
  




    
  
