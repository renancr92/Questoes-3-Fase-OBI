def min(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def normal(x, m=1440):
    return ((x % m) + m) % m

def main():
    print("Digite os horários no formato 00:00")
    pA1 = input(" Horário de partida de A para B (hora local de A): ")
    cB2 = input(" Horário de chegada em B (hora local de B): ")
    pB1 = input(" Horário de partida de B para A (hora local de B): ")
    cA2 = input(" Horário de chegada em A (hora local de A): ")

    pA = min(pA1)
    cB = min(cB2)
    pB = min(pB1)
    cA = min(cA2)

    print("\n Convertendo horários para minutos:")
    print(f"pA = {pA1} → {pA} minutos")
    print(f"cB = {cB2} → {cB} minutos")
    print(f"pB = {pB1} → {pB} minutos")
    print(f"cA = {cA2} → {cA} minutos")

    for fuso in range(-11, 13):
        base = cB - pA - fuso * 60
        D = normal(base, 1440)

        if D >= 720:
            continue
        
        if normal(pB + D - fuso * 60 - cA, 1440) == 0:
            print("\n Resultado encontrado!")
            print(f"Tempo real de voo (D): {D} minutos ({D//60}h {D%60}min)")
            print(f" Diferença de fuso horário : {fuso} horas")
            
            if fuso < 0:
                print(f" A cidade B está {-fuso} hora(s) ATRÁS da cidade A.")
            elif fuso > 0:
                print(f" A cidade B está {fuso} hora(s) À FRENTE da cidade A.")
            else:
                print(" As cidades A e B têm o MESMO fuso horário.")
            
            return

    print("\n Nenhuma combinação válida encontrada.")

if __name__ == "__main__":
    main()
