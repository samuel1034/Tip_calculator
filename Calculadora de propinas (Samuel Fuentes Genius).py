print ("Bienvenidos a la calculadora de propinas");
factura = float(input ("¿Cual es el importe de tu factura?"))
propina = int (input ("¿Cual es el porcentaje de propina que quieras dejar?"))
personas = int (input ("¿Entre cuantas personas hay que repartir la factura?"))

importe_propina = (factura * propina) /100
factura_total = factura + importe_propina

importe_por_persona = factura_total /personas

print ("El importe a pagar por persona es de " + str(importe_propina));



