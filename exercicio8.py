nume1 = "Gabinete_Cooler_master"
nume2 = "Geforce_RTX_2080TI"
nume3 = (input("Digite uma peça"))
nume4 = (input("Digite uma peça"))
Carrinho = [nume1,nume2,nume3,nume4]
print(Carrinho)
Remove = int(input("Oh não! os preços estão altos demais!, deseja remover o gabinete e a placa de video? 1- sim 2-não"))
if Remove is 1:
    del Carrinho[0,1]
    print(Carrinho)
if Remove is 2 :
    print("Você é rico!")
    print(Carrinho)

