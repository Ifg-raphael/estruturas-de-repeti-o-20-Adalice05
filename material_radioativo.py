# Exercício 3

m= float(input("Insira o valor da massa em gramas: ")) #Entrada do valor inicial da massa

tempo = 0

#O while faz com que a divisão se repita enquanto o valor da massa é maior ou igual a 0.5

while m >= 0.5:
    m = m/2  #divide o valor da massa pela metade até que a condição de parada seja atendida
    tempo = tempo + 50  #calcula o tempo em segundos considerando que o material perde metade de sua massa a cada 50 segundos
    horas = tempo//3600  #converte em horas,pegando apenas a parte inteira da divisão
    minutos = (tempo % 3600) // 60 #Converte em minutos,pegando o resto das horas e dividindo por 60 
    segundos = tempo % 60 #Converte em segundos
    
print(f"Levou {horas:02d} horas, {minutos:02d} minutos e {segundos:02d} segundos!")
