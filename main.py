import os,math
largu = float(input("Largura: "))
compr = float(input("Comprimento: "))
altur = float(input("Altura: "))
qtdMao = int(input("Quantidade de demão: "))
rendim = float(input("Qual rendimento da lata por M²: "))
cusTin = float(input("Qual o custo da lata de tinta: R$"))
cusMao = float(input("Qual o custo da mão de obra do pintor: R$"))

os.system('clear')

#calculos das paredes
ms = (largu*altur*2)+(compr*altur*2)+(largu*compr)

#calculo do rendimento
#Qtd de Mão vezes o metro quadrado
totalQtdMao = qtdMao * ms

#calculo da demão com metro dividindo pelo rendimento da lata
cr = totalQtdMao/rendim

#Quantidade de latas de tintas nescessarias
qlt = totalQtdMao/cr

#Custo total gastos com tinta
ctt = qlt*cusTin

#Custo total com pintor
cmpt = totalQtdMao*cusMao

#Valor total que será gasto com tudo
cp = cmpt+ctt

print("Quantidade de lata de tintas: ",qlt)
print("Custo total gasto com tinta: R$",ctt)
print("Custo total gasto com mão de obra do pintor: R$",cmpt)
print("Custo total da obra: R$",cp)




