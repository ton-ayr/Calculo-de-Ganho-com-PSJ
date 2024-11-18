def calcular_ganhos(valor_base, parcelas):
    
    taxa_venda = 0.049
    taxa_parcelamento_mensal = 0.0329
    produtor_percentual = 0.72
    parceiro_percentual = 0.18 

    valor_venda_com_juros = valor_base * (1 + taxa_parcelamento_mensal) ** parcelas
    taxa_parcelamento_total = valor_venda_com_juros - valor_base

    valor_taxa_venda = valor_base * taxa_venda
    taxa_da_venda_total = valor_taxa_venda + 1.00

    ganho_total = valor_base - taxa_da_venda_total
    ganho_produtor = ganho_total * produtor_percentual
    ganho_parceiro = ganho_total * parceiro_percentual

    taxa_parcelamento_produtor = taxa_parcelamento_total * produtor_percentual
    taxa_parcelamento_parceiro = taxa_parcelamento_total * parceiro_percentual

    ganho_final_produtor = ganho_produtor - taxa_parcelamento_produtor
    ganho_final_parceiro = ganho_parceiro - taxa_parcelamento_parceiro

    return {
        "Valor da venda": valor_base,
        "Valor da venda com juros": round(valor_venda_com_juros, 2),
        "Taxa de parcelamento": round(taxa_parcelamento_total, 2),
        "Taxa da venda": round(taxa_da_venda_total, 2),
        "Ganho final do Produtor": round(ganho_final_produtor, 2),
        "Ganho do Parceiro": round(ganho_final_parceiro, 2),
    }


valor_venda = 20.00  # Valor inicial da venda
parcelas = 4  # Número de parcelas
resultado = calcular_ganhos(valor_venda, parcelas)

print("Resultado do cálculo:")
for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor}")
