#aqui o sistema pede o nome do usuario
nome = input("digite seu  nome; ")
#aqui o sistema pede a idade do usuario
idade = int (input("Qual sua idade?"))
#aqui mostra o nome e a idade que o usuario informou
print(f"Bem vindo{nome}, voce tem {idade} anos. ")
#aqui e uma funçao que serve como menu
def menu():
print ("Como posso te ajudar hoje?")
print("1- bebidas")
print("2- Salgados")
print("3- Doces")
#aqui grava a opçao que o usuario digitou
opc_user = int(input("Digite o número da opção desejada:"))
#aqui começa a lógica do SE
opc_user == 1:
print(Temos coca, fanta e guaraná")
      
opc_user == 2:
print("Temos coxinha, risole e empadão")

opc_user == 3:
print("Temos brigadeiro")

print("Opção incorreta! Digite um número de 1 a 3")