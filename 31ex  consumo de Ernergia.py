


#31. O valor da conta de energia elétrica deve ser calculado considerando o acréscimo dado pela
#quantidade consumida, conforme descrito na tabela abaixo:

#              Consumo (KWh)                         Crescimento
#            até 40 (inclusive)                         10%
#              acima de 40                              30%

Energia = int(input("Quantos (KWh) voce consumiu?: "))

Energia10 = (Energia*10/100+Energia)
Energia30 = (Energia*30/100+Energia)

if (Energia <= 40):
    print(f"\nVoce Consumiu ({Energia}KWh), Total com Acrescimo de 10% = ({Energia10}KWh)\n")
else:
    print(f"\nVoce Consumiu ({Energia}KWh), Total com Acrescimo de 30% = ({Energia30}KWh) \n")