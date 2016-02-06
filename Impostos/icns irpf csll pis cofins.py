while 0 < 1:
    mec = input("Valor da Medardoria: ")
    icns = float(mec) * 17/100
    irpf = float(mec) * 15/100
    csll = float(mec) * 7.6/100
    cofins = float(mec) * 3/100    
    pis = float(mec) * 1.65/100
    me = float(mec) - (icns + irpf + cofins + pis + csll)
    
    print("<<<<<<<<<<<RESLTADO>>>>>>>>>>")
    print("Anicota    Imposto    Valor")
    print("17%         ICMS      " + str(icns))
    print("15%         IRPF      " + str(irpf))
    print("7.6%        CSLL      " + str(csll))
    print("3%         COFINS     " + str(cofins))
    print("1.65%        PIS      " + str(pis))
    print("Valor real da Mercadoria: " + str(me))
    print("<<<<<<<<<<<RESULTADO>>>>>>>>>>")
