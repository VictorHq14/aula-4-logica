notas_total = 0
for média in range(5):
    notas = int(input("Digite suas notas desse ano: "))
    notas_total += notas
media_notas = notas_total / 5
if media_notas >= 6:
    print(f"Sua média foi {media_notas} e você está Aprovado(a)!")
else:
    print(f"Reprovado! Pois sua media foi de {media_notas}")

