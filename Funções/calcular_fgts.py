def calcular_fgts(salario_bruto, percentual_FGTS):
    percentual_FGTS_numerico = float(percentual_FGTS[:-1])
    fgts_recolhido = salario_bruto * (percentual_FGTS_numerico / 100)
    return fgts_recolhido  

salario_bruto = 1600.00
percentual_FGTS = "8%"

calculo_fgts = calcular_fgts(salario_bruto, percentual_FGTS)

print(f"O FGTS recolhido é: {calculo_fgts}")