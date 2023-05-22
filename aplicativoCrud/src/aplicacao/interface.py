from validacoes import validacoes


def menu_inicial():
    print("qual funcao deseja acessar?")
    print("[0] sair")
    print("[1] marcar consulta")
    print("[2] acessar todas consultas")
    print("[3] acessar consulta por id")
    print("[4] atualizar uma consulta")
    print("[5] deletar consulta")
    print("[6] medidas de tendencia central das idades dos pacientes")
    print()

    try:
        valor = validacoes.validar_inteiro()
    except TypeError as e:
        print(e)
        menu_inicial()
    else:
        if valor < 0 or valor > 6:
            print("O valor deve ser maior ou igual a 0 e menor que 7, digite novamente. ")
            menu_inicial()
        else:
            return valor
