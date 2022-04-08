from itertools import product


class Product:
    codigo=None
    Nome=None
    Preco=None
    Qdemestoque=None

vectproduct=[]
while True:
    InfProduct=Product()
    InfProduct.codigo=int(input("Digite o código do seu produto:"))
    InfProduct.Nome=input("Digite o nome do seu produto:")
    InfProduct.Preco=float(input("Digite o preco do seu produto:"))
    InfProduct.Qdemestoque=int(input("Digite a quantidade de produto:"))
    vectproduct.append(InfProduct)
    while True:
        Question=str(input("deseja continuar? S/N")).upper()[0]
        if Question in "SN":
            break
        print("Erro!!! a sua resposta tem que ser S/N")
    if Question=="N":
        break   
for prod in vectproduct:
    print("\nRelatório dos produtos:") 
    print("Codigo:",prod.codigo)
    print("Nome:",prod.Nome)
    print("preco:",prod.Preco)
    print("Quantidade em estoque:",prod.Qdemestoque)

print("**********************************")
print("Atualização dos produtos")
while True:
    Cprod=int(input("digite o codigo do produto:")) 
    if Cprod==0:
        break
    for prod in vectproduct:
        if prod.codigo ==Cprod:
            achar=True
            InfProduct.Preco=int(input("digite o novo preco:"))
            InfProduct.Qdemestoque=int(input("digite a nova quantidade:"))
    if achar==False:        
            print("ouppsss erro! voce digitou um codigo diferente!!!")           
  
    #print("\nRelatório dos produtos:") 
    #print("Codigo:",prod.codigo)
    #print("Nome:",prod.Nome)
    #print("preco:",prod.Preco)
    #print("Quantidade em estoque:",prod.Qdemestoque)

print("***********************************")
#compra
listadosProdutosComprados=[]
while True:
    found = False
    codDoProduto=int(input("digite o codigo:"))
    if codDoProduto == -1:
        break
    
    for prod in vectproduct:
        if prod.codigo==codDoProduto:
            found = True
            QdAsercomprada=int(input("quantos produtos que deseja comprar?:"))
            if QdAsercomprada<=InfProduct.Qdemestoque:
                QdAsercomprada-=InfProduct.Qdemestoque
                listadosProdutosComprados.append(prod)
    if found == False:
        print("ouppss! ocorreu um erro na sua compra voce digitou uma quantidade superior ao estoque!!!")
print("coprovante dos produtos comprados")       
      
print("Impressão das compras") 
preco=0    
for prC in listadosProdutosComprados:    # prC lista dos produtos comprados
    print("Codigo:",prC.codigo)
    print("Nome:",prC.Nome)
    print("preco:",prC.Preco)
    print("***************************************")
    preco+=prC.Preco
print("Total=",preco)    
print("Fim da mpressão das compras") 

#procurando produtos via codigo
seachforProd=int(input("digite o codigo do produto:"))
verificacao=False
for prd in vectproduct:
    if vectproduct == seachforProd:
        verificacao=True
        print(prd.codigo)
if verificacao==False:
    print("o produto que voce digito nao foi cadastrado")

#impressão de todos os produtos 
for p in vectproduct:
    print("\nRelatório dos produtos:") 
    print("Codigo:",p.codigo)
    print("Nome:",p.Nome)
    print("preco:",p.Preco)
    print("Quantidade em estoque:",p.Qdemestoque)  