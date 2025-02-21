
def converter_para_centimetros(metros):
    centimetros = metros * 100
    return centimetros

 
metros = float(input("Digite o valor em metros: "))


centimetros = converter_para_centimetros(metros)


print(f"{metros} metros é igual a {centimetros} centímetros.")
