from main_champ import main_champ
from main_clubs import main_clubs

def main():
    print("""
[ 1 ] - Gerenciar Clubes
[ 2 ] - Gerenciar Campeonato
[ 0 ] - Sair
    """)
    menu = input("Digite uma opção: ")

    if(menu == "1"):
        main_clubs()
    elif(menu == "2"):
        main_champ()
    elif(menu == "0"):
        print('exit')
    else:
        print("Digite um comando valido")
        main()
main()
