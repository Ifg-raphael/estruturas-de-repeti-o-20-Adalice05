# Exercício 3

m= float(input("Insira o valor da massa em gramas: ")) #Entada do valor inicial da massa

tempo = 0

#O while faz com que a divisão se repita enquanto o valor da massa é maior ou igual a 0.5

while m >= 0.5:
    m = m/2
    tempo = tempo + 50
    horas = tempo//3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60
    
print(f"Levou {horas:02d} horas, {minutos:02d} minutos e {segundos:02d} segundos!")
