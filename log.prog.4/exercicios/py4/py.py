texto = "Eu, sou muito lindo, é isso to certo e acabou tudo KAKAKAKA"
contador_vogais = 0
for caractere in texto:
    if caractere.lower() in "aeiou":
        contador_vogais +=1
print(f"numero de vogais é : {contador_vogais}")        