def main_clubs():
    print("""
[ 1 ] - Jogadores
[ 2 ] - Clubes
[ 3 ] - Técnicos
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")

    if(menu == "1"):
        main_player()
    elif(menu == "2"):
        main_club()
    elif(menu == "3"):
        main_manager
    else:
        print("""

Digite uma opção valida

        """)
        main_clubs()


def main_player():
    print("""
[ 1 ] - Cadastrar novo jogador
[ 2 ] - Alterar jogador
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        print("cadastrar")
    elif(menu == "2"):
        print("alterar")
    elif(menu == "0"):
        main_clubs()
    else:
        print("""

Digite uma opção valida

        """)
        main_player()


def main_club():
    print("""
[ 1 ] - Cadastrar novo clube
[ 2 ] - Alterar clube
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        print("cadastrar")
    elif(menu == "2"):
        print("alterar")
    elif(menu == "0"):
        main_clubs()
    else:
        print("""

Digite uma opção valida

        """)
        main_club()


def main_manager():
    print("""
[ 1 ] - Cadastrar novo técnico
[ 2 ] - Alterar técnico
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        print("cadastrar")
    elif(menu == "2"):
        print("alterar")
    elif(menu == "0"):
        main_clubs()
    else:
        print("""

Digite uma opção valida

        """)
        main_clubs()


main_clubs()
