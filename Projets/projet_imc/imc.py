poids = int(input("votre poids en kg: "))
taille = float(input("votre taille en mètre: "))

imc = poids / (taille ** 2)
print(f"votre imc est de {imc}")

if imc<18.5:
    print("Attention, maigreur")
elif 18.5<imc<25:
    print("Corpulence normale")
elif 25<imc<30:
    print("Attention surpoids")
elif 30<imc<40:
    print("Attention obésité modéré")
elif imc>40:
    print("Danger obésité sévère")