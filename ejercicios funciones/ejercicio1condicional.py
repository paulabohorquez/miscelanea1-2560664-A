def nota (num):
    if num > 11:
        print("valor erroneo")
    elif num <= 2:
        print("mal")
    elif num <= 4:
        print("insuficiente")
    elif num <= 7:
        print("suficiente")
    elif num <= 9:
        print("muy bien")
    elif num == 10:
        print("excelente")

nota(5)