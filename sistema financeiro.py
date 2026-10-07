print("Sistema financeiro")
print()

opcao = 0
reserva_mensal = 0.0
valor = 0.0
opcao_categoria = 0
descricao_gasto = ""
soma_gastos = 0.0

gastos_por_categoria = []

lista_gastos = []
lista_descricoes_gastos = []
lista_categorias_gastos = []

while True:

    print()
    print("opções")
    print("1- informar reserva mensal")
    print("2- cadastrar o gasto")
    print("3- consultar gastos")
    print("4- consultar situação financeira")
    print("5- ver estatísticas")
    print("6- sair")

    print()
    while True:
        opcao = int(input("opção desejada: "))

        if opcao < 1 or opcao > 6:
            print("erro: opção não listada, informe entre 1 e 6")
        else:
            break

    match opcao:
        case 1:
            print()
            reserva_mensal = float(input("informe sua reserva mensal:\n "))
            print('reserva cadastrada com sucesso!')

        case 2:
            print()
            descricao_gasto = input("informe a descrição do gasto: ")
            lista_descricoes_gastos.append(descricao_gasto)

            valor = float(input("informar gasto: "))

            print("informe uma dentre as categorias abaixo:")
            print("1- Alimentação")
            print("2- Transporte")
            print("3- Lazer")
            print("4- Saúde")
            print("5- Outro")

            opcao_gasto = int(input("categoria: "))

            match opcao_gasto:
                case 1:
                    lista_categorias_gastos.append("Alimentação")
                case 2:
                    lista_categorias_gastos.append("Transporte")
                case 3:
                    lista_categorias_gastos.append("Lazer")
                case 4:
                    lista_categorias_gastos.append("Saúde")
                case 5:
                    lista_categorias_gastos.append("Outro")
                case _:
                    print("erro: categoria inválido, saindo do programa...")
                    break

            lista_gastos.append(valor)

        case 3:
            print()
            if len(lista_gastos) == 0:
                print("nenhum gasto cadastrado ainda")
            else:
                print("gastos: ")
                print("indice do gasto\t|\tdescricao\t|\tcategoria\t|\tvalor gasto")
                for i in range(len(lista_gastos)):
                    print(f"{i + 1}\t\t|\t{lista_descricoes_gastos[i]}\t\t|\t{lista_categorias_gastos[i]}\t|\tR$ {lista_gastos[i]:.2f}")

                print(f"soma dos gastos: R$ {soma_gastos:.2f}")

        case 4:
            print()
            print("situação financeira:")
            print(f"reserva inicial: R$ {reserva_mensal:.2f}")
            print(f"soma dos gastos: R$ {soma_gastos:.2f}")
            print(f"reserva atual: R$ {(reserva_mensal - soma_gastos):.2f}")

            if soma_gastos > reserva_mensal:
                print("atenção: você ultrapassou a sua reserva mensal!")
            else:
                print("atenção: você está dentro da reserva mensal")

        case 5:
            print()
            if len(lista_gastos) == 0:
                print("aviso: nenhum gasto cadastrado ainda")
            else:
                print("soma dos gastos em cada categoria:")

                categorias = ["Alimentação", "Transporte", "Lazer", "Saúde", "Outro"]

                for categoria in categorias:
                    soma_categoria = 0.0

                    for i in range(len(lista_gastos)):
                        if lista_categorias_gastos[i] == categoria:
                            soma_categoria += lista_gastos[i]

                    percentual = soma_categoria / soma_gastos * 100

                    print(f"{categoria}: R$ {soma_categoria:.2f} ({percentual:.1f}%)")

                indice_maior = 0
                for i in range(len(lista_gastos)):
                    if lista_gastos[i] > lista_gastos[indice_maior]:
                        indice_maior = i

                print()
                print(f"maior gasto: {lista_descricoes_gastos[indice_maior]} "
                        f"({lista_categorias_gastos[indice_maior]}) - R$ {lista_gastos[indice_maior]:.2f}")


        case 6:
            print("aviso: saindo do programa...")
            break
        case _:
            print("erro: opção não listada")
            print("aviso: saindo do programa...")
            break

    soma_gastos = sum(lista_gastos)
