#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

    #Compara duas strings
    #String 1: Brasil Hexa 2006
    #String 2: Brasil! Hexa 2006!
    #Tamanho de "Brasil Hexa 2006": 16 caracteres
    #Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    #As duas strings são de tamanhos diferentes.
    #As duas strings possuem conteúdo diferente.

string1 = str(input("Digite a primeira frase: "))
string2 = str(input("Digite a segunda frase: "))

print("Tamanho de", string1, ":", len(string1), "caracteres")
print("O tamanho de", string2, ":", len(string2), "caracteres")

if len(string1) == len(string2): #len calcula o comprimento
    print("As duas frases são de tamanhos iguais.")
else:
    print("As duas frases tem tamanhos diferentes.")