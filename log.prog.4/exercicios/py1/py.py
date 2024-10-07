while True:
    print("/menu: ")
    print("1. diga ola")
    print("2. diga adeus")
    print("digite 'sair' para terminar o programa ")

    opcao = input("escolha uma opcao: ")

    if opcao == "1":
        print("Olá")
    elif opcao == "2":
        print("adeus")
    elif opcao.lower() == "sair":
        print("encerrando o programa. ")
        break
    else:
        print("opcao invalida, tebte novamente ")
        