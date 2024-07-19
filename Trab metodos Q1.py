# Dados
deb = 10235 # débito mensal
n_anos = 30 # tempo em anos
n_meses = n_anos*12 # tempo em meses
r = 0.0089 #juros simples
s_inicial = 11100 # saldo inicial
s_final = 1000000 #saldo final

#Q1a---------------------------------
#Cálculo para resgatar uma taxa fixa mensalmente sem mexer no $$
def din_acumulado(deb,r):
    din_acu = deb/r #1.150.000
    return din_acu 

# Q1b -------------------------------
#Cálculo de valor presente para uma série de retiradas
def saldo_presente(deb, n_meses, r):
    s_presente = 0
    for i in range (n_meses):
        s_presente += deb / (1 + i*r) # aproximadamente 1.143.726 
    return s_presente

# Q1c-------------------------------
#Calculo investimento mensal
def investimento_mensal(s_inicial, s_final, n_meses, r):
    va_inicial = 0; va_mensal = 0; inv_mensal = 0 #setando os valores para 0
    va_inicial = s_inicial*(1+ (n_meses*r)) # valor acumulado da parcela inicial
    for i in range (n_meses-1):
        va_mensal += (1 + (r*i)) # valor acumulado mensal
    #va_mensal = (n_meses + ((r*n_meses*(n_meses-1))/2)) # valor acumulado mensal
    inv_mensal = (s_final - va_inicial)/va_mensal # aproximadamente 1.024
    return inv_mensal

#Q1d--------------------------------
def investimento_inicial(s_inicial, s_final, n_meses, r):
    va_inicial = 0; va_mult = 0; inv_mes_um = 0 #setando os valores para 0
    va_inicial = s_inicial*(1+ (n_meses*r)) # valor acumulado da parcela inicial
    va_mult = (1 +((n_meses-1)*r)) # valor a ser multiplicado pelo investimento inicial
    inv_mes_um = (s_final-va_inicial)/va_mult # aproximadamente 227.250
    return inv_mes_um

#Calculando
din_necessario = din_acumulado(deb,r)
#print(din_necessario) #Q1a
s_necessário = saldo_presente(deb, n_meses, r)
#print(s_necessário) #Q1b
i_mes = investimento_mensal(s_inicial, s_final, n_meses, r)
#print(i_mes) # Q1c
i_inicial = investimento_inicial(s_inicial, s_final, n_meses, r)
#print(i_inicial) #Q1d
print("oi")
