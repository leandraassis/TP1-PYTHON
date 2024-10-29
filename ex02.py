# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

minutos = int(input("Digite o tempo em MINUTOS: "))

def minutosEmHoras(minutos):
    horas = minutos // 60
    minutosRestantes = minutos % 60
    return [horas, minutosRestantes]

def horasEmMinutos(tempo): 
    horas = tempo[0]
    minutos = tempo[1]
    minutosTotais = (horas * 60) + minutos
    return minutosTotais

def mostrarResultado(minutos):
    listaResultado = minutosEmHoras(minutos)
    minutosTotais = horasEmMinutos(listaResultado)
    horas = listaResultado[0]
    minutosRestantes = listaResultado[1]
    if(minutosRestantes == 0):
        print(f"{minutos} minutos equivalem a {horas} horas.")
    else:
        print(f"{minutos} minutos equivale a {horas} hora(s) e {minutosRestantes} minutos.")
    print(f"{horas} hora(s) e {minutosRestantes} minutos equivalem a {minutosTotais} minutos.")

mostrarResultado(minutos)