estoque = {"Celta": 20000.00,
          "Astra": 30000.00,
          "Gol": 45000.00,
          "Uno": 25000.00}  

def admin(login,senha):
  if login == "adm" and senha == "1234":
    while True:

      print(f"\nTodos os carros adicionados foram: {estoque}")
      print("\nVocê pode escolher \nAdd \nExcluir \nSair")
      escolha = (input("Qual sua escolha? "))
      escolha = escolha.capitalize()

      if escolha == "Sair":
        print(f"\nVocê escolheu sair, todos os carros adicionados foram: {estoque}")
        break

      elif escolha == "Excluir":
        try:
          produto = (input("\nDigite o nome do carro que deseja excluir: "))
          produto = produto.capitalize()
          estoque.pop(produto)
          print(f"\nVocê excluiu o carro: {produto}.")
        except Exception as err2:
          print(f"\n{err2} não está no estoque.")

      elif escolha == "Add":
        produto = (input("\nDigite o nome do carro: "))
        produto = produto.capitalize()

        if produto in estoque:
          print(f"\nO carro '{produto}' já existe.")
          continue
        try:
          preco = float(input("\nDigite o preço do carro: "))
          estoque[produto] = preco
          print(f"\nCarro '{produto}'adicionado")
        except ValueError as err:
          print(f"\nERRO: {err}")

  else:
      print("\nVocê não é adm")

def cliente(nomeCliente):
  total_compra = 0

  print(f"Olá, {nomeCliente},", "seja bem-vindo a nossa MarktBox, agora, iremos apresentar os carros que estão disponíveis no estoque!!")
  while True:

    if estoque  == {}:
      print("O estoque acabou!!")
      print(f"O valor total da sua compra foi: {total_compra:.2f}.")
      produto = "Finalizar"

    else:
      print(f"\n{estoque}")
      produto = input("\nVocê pode escolher: \nAdicionar o carro ao carrinho(Digitar o Nome do Carro) \nFinalizar \nSair\n")
      produto = produto.capitalize()

    if produto in estoque:
      total_compra = estoque[produto] + total_compra
      print(f"Você adicionou {produto} ao carrinho e o preço do carrinho total é {total_compra:.2f}.")
      estoque.pop(produto)


    elif produto == "Sair":
      print("Até a proxima!!")
      break

    elif produto == "Finalizar":
      finalizar(total_compra)
      break

    else:
      print("Você não selecionou nenhuma das opções.")
      continue

def finalizar(total_compra):
      if total_compra == 0:
        print("\nImpossivel finalizar a compra sem itens no carrinho.")
        return False

      print(f"Você escolheu finalizar a compra, o total é {total_compra:.2f}.")

      debOUcred = input("Débito ou Crédito? ")
      debOUcred = debOUcred.capitalize()

      if debOUcred == "Crédito" or debOUcred == "Credito":
        parcela = input("\nDeseja parcelar? Sim ou Não: ")
        parcela = parcela.capitalize()

        if parcela == "Sim":
          vezes = int(input("Quantas vezes? de 12, 24 ou 36: "))

          if vezes == 12 or vezes == 24 or vezes == 36:
            total_parcela = total_compra / vezes
            print(f"Parabens você finalizou a compra o total por cada parcela foi de {total_parcela:.2f}.")
            return False
          else:
            print("Esta opção não é aceita, não foi possivel finalizar a compra.")

        else:
          print(f"Compra finalizada!! Obrigado, volte sempre! O total foi {total_compra:.2f}.")
          return False

      else:
         print(f"Compra finalizada!! Obrigado, volte sempre! O total foi {total_compra:.2f}.")
         return False

#main
while True:
    usuario = input("Digite a sua função: (Adm ou Cliente) ")
    usuario = usuario.capitalize()

    if usuario == "Adm":
        login = input("Qual o login do adm? ")
        senha = (input("Qual a senha do adm? "))
        print("\nEssa parte é direcionada aos administradores do servidor, usada para adicionar e excluir os carros do estoque.")
        admin(login,senha)

    elif usuario == "Cliente":
        nomeCliente = input("Digite o seu nome: ")
        nomeCliente = nomeCliente.capitalize()
        cliente(nomeCliente)
    else:
        print("\nVocê não escolheu nenhuma das opções, retorne ao programa.")
    
