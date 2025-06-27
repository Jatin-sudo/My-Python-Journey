Pesos = int(input("How much you have left in Pesos ? " ))
Soles = int(input("How much you have left in Soles ? " ))
Reais = int(input("How much you have left in Reais ? " ))

C_Pesos = Pesos*0.00024
C_Soles = Soles*0.28
C_Reais = Reais*0.18

Amount_left_in_usd = C_Pesos + C_Soles + C_Reais

print ("The total amount you are left in usd is:" ,Amount_left_in_usd )