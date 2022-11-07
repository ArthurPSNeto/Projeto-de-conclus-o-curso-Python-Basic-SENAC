#PTI SENAC Numeros de infectados covid no sudeste.
print("Calculadora de número de infectados por covid na região Sudeste\n")
infec=0
sp1=0
sp2=0
rj1=0
rj2=0
es1=0
es2=0
mg1=0
mg2=0
while infec!=6:
    print("\nPressione 1 para adicionar números de infectados em São Paulo: ")
    print("\nPressione 2 para adicionar números de infectados no Rio de Janeiro: ")
    print("\nPressione 3 para adicionar números de infectados no Espirito Santo: ")
    print("\nPressione 4 para adicionar números de infectados em Minas Gerais: ")
    print("\nPressione 5 para consultar situação atual de toda região Sudeste: ")
    print("\nPressione 6 para encerrar o programa: ")
    infec=int(input("\nQual opção você deseja?: "))
    if infec==1:
        sp1=int(input("\nAdicionar número de profissionais de saúde infectados em São Paulo: "))
        sp2=int(input("\nAdicionar numero de população infectada em São Paulo: "))
    elif infec==2:
        rj1=int(input("\nAdicionar número de profissionais de saúde infectados no Rio de Janeiro: "))
        rj2=int(input("\nAdicionar número da população infectada no Rio de Janeiro: "))
    elif infec==3:
        es1=int(input("\nAdicionar número de profissionais de saúde infectados no Espirito Santo: "))
        es2=int(input("\nAdicionar número da população infectada no Espirito Santo: "))
    elif infec==4:
        mg1=int(input("\nAdicionar número de profissionais de saúde infectados em Minas Gerais: "))
        mg2=int(input("\nAdicionar numero de população infectada em Minas Gerais: "))
    elif infec==5:
        sudeste=sp1+sp2+rj1+rj2+es1+es2+mg1+mg2
        print("-"*60)
        print("                    Situação atual no Sudeste")
        print("-"*60)
        print("                    Prof. de Saúde   População")
        print("-"*60)
        print("São Paulo                ",sp1,"          ",sp2)
        print("Rio de Janeiro           ",rj1,"          ",rj2)
        print("Espírito Santo           ",es1,"          ",es2)
        print("Minas Gerais             ",mg1,"          ",mg2)
        print("-"*60)
        print("\nTotal de Prof. de Saúde      -->",sp1+rj1+es1+mg1)
        print("\nTotal da população em geral  -->",sp2+rj2+es2+mg2)
    elif infec==6:
        print("\nPrograma encerrado pelo usuário")
        break
        
        