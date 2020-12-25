import math
Bandera=True
Lista=""
Total=0
while Bandera:
    datos=(input())
    datos_1=datos.split("&") #La función split vuelve elementos de una lista los datos dados en el input
    if datos_1[0]=="1":
        articulo,Q,P=(datos_1[1],int(datos_1[2]),int(datos_1[3]))
        Total+=Q*P
        Total1=Q*P
        while "&" in datos_1:
            datos_1.remove("&")
        #datos_u=" ".join(datos_1)
        Lista+="\n"+str(articulo)+" x"+str(Q)+" $"+str(Total1)
    if datos_1[0]=="2":
        cc=datos_1[1]
        def descuento(Total):
            if Total>700000:
                return Total*0.2
            elif Total>300000:
                return Total*0.15
            elif Total>150000:
                return Total*0.1
            else:
                return 0
        def Total_con_descuento(Total):
            if Total>700000:
                return Total-(Total*0.2)
            elif Total>300000:
                return Total-(Total*0.15)
            elif Total>150000:
                return Total-(Total*0.1)
            else:
                return Total
        print("Centro Comercial Unaleño\nCompra más y Gasta Menos"+
        "\nNIT: 899.999.063")
        print("Cliente: ",cc,"\nArt Cant Precio",Lista)
        print("Total: $"+ str(math.ceil(Total_con_descuento(Total))) +"\nEn esta compra tu descuento fue $"+ str(math.floor(descuento(Total))))
        print("Gracias por tu compra"+"\n---")
        while Lista!="":
            Lista=""
        while Total!=0:
            Total=0
    if datos_1[0]=="3":
        Bandera=False
        



