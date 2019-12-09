from clubs.club.club import *
from clubs.players.index import *
from clubs.managers.index import *
class_club = class_club()
player = player()
manager = manager()


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
        main_manager()
    elif(menu == "0"):
        from main import main
        main()
    else:
        print("""

Digite uma opção valida

        """)
        main_clubs()


def main_player():
    print("""
[ 1 ] - Cadastrar novo jogador
[ 2 ] - Deletar jogador
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        player.createPlayer()
        main_clubs()
    elif(menu == "2"):
        player.deletePlayerID()
        main_clubs()
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
[ 2 ] - Deletar clube
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        class_club.createClub()
        main_clubs()
    elif(menu == "2"):
        print("""

[ 1 ] - Deletar por ID
[ 2 ] - Deletar por nome
[ 0 ] - Voltar

    """)
        opcao = input("Digite uma opção: ")
        if(opcao == "1"):
            class_club.deleteClubByID()
            main_clubs()
        elif(opcao == "2"):
            class_club.deleteClubByName()
            main_clubs()
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
        manager.creatManager()
        main_clubs()
    elif(menu == "2"):
        print("alterar")
        main_clubs()
    elif(menu == "0"):
        main_clubs()
    else:
        print("""

Digite uma opção valida

        """)
        main_clubs()

