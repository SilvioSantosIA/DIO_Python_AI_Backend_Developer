def gerar_holerith(nome_funcionario, salario_bruto, salario_liquido, total_acrescimos, total_abatimentos, horas_extras, desconto_inss, plano_saude, imposto_renda, vem_trabalhador):

    ## Dicionário para armazenar as informações do contracheque:
    holerith = {
        "Nome do Funcionário": nome_funcionario,
        "Salário Bruto": salario_bruto,
        "Horas-extras:": horas_extras,
        "Acréscimos:": total_acrescimos,
        "Imposto de Renda": imposto_renda,
        "INSS": desconto_inss,
        "Plano de Saúde": plano_saude,
        "VEM Trabalhador:": vem_trabalhador,
        "Abatimentos": total_abatimentos,
        "Salário Líquido:": salario_liquido      
    }
   
   ## Calcule as despesas e acréscimos:    
    holerith["Salário Bruto"] = salario_bruto
    holerith["Horas extras"] = horas_extras
    holerith["Acréscimos"] = calcular_acrescimos(horas_extras)
    holerith["Imposto de Renda"] = calcular_irrf(salario_bruto, holerith["INSS"], imposto_renda)
    holerith["INSS"] = desconto_inss
    holerith["Plano de Saúde"] = plano_saude
    holerith["Vem Trabalhador:"] = vem_trabalhador
    holerith["Abatimentos:"] = calcular_abatimentos(desconto_inss, plano_saude, vem_trabalhador, imposto_renda)       
    holerith["Salário Líquido"] = calcular_salario_liquido(salario_bruto, total_acrescimos, total_abatimentos)

    ## Calcule as horas extras (se houver):
    if horas_extras > 0
        valor_hora_extra = salario_bruto / jornada_mensal
        remuneracao_hora_extra = valor_hora_extra * horas_extras * percentual_hora_extra
        holerith["Horas extras"] = horas_extras
        holerith["Remuneração Hora Extra"] = remuneracao_hora_extra
        holerith["Salário Líquido com Hora Extra"] = holerith["Salário Líquido"] + remuneracao_hora_extra

    ## Retorne o dicionário com as informações do contracheque:
    return holerith

def calcular_INSS(salario_bruto, aliquota_inss):
    ## Calcule o desconto do INSS com base na aliquota:
    return salario_bruto * aliquota_inss / 100

def calcular_irrf(salario_bruto, desconto_inss, aliquota_irrf):
    ## Calcule o desconto do Imposto de Renda com base ma alíquota e na base de cálculo:
    base_calculo_irrf = salario_bruto - desconto_inss
    ## Aplique a tabela progressiva do IRRF:
    return calcular_irrf_tabela(base_calculo_irrf, aliquota_irrf):

def calcular_abatimentos(desconto_inss, plano_saude, vem_trabalhador, imposto_renda):
    total_abatimentos = desconto_inss + plano_saude + vem_trabalhador + imposto_renda
    return total_abatimentos

def calcular_acrescimos(horas_extras):
    return horas_extras

def calcular_salario_liquido(salario_bruto, total_acrescimos, total_abatimentos):
    salario_liquido = salario_bruto + total_acrescimos - total_abatimentos
    return salario_liquido

holerith_completo = gerar_holerith(

    nome_funcionario= "Zenildo Zoroastro."
    salario_bruto=5000.00,
    horas_extras=10,
    desconto_inss=8
    plano_saude=120.00,
    imposto_renda=15
    jornada_mensal=2
)

print(gerar_holerith)

## Surgiram vários erros na execução do código, então é melhor tentar algo mais simples e curto,
## para entender como funciona cada coisa, para depois investir em algo maior. Mesmo assim,
## foi um ótimo exercício.