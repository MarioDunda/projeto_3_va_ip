from championschip.simulation.index import simulation
simulation = simulation()

def main_champ():
    print("""
[ 1 ] - Simular campeonato
[ 2 ] - Ver tabela de classificação
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        simulation.games()
        main_champ()
    elif(menu == "2"):
        simulation.ranking()
        main_champ()
    elif(menu == "0"):
        print("exit")
    else:
        print("""

Digite uma opção valida

        """)
