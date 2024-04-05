import requests
from urllib.parse import urlparse
from datetime import datetime
import calendar
import dbconnect
import twitapi
import time
from bs4 import BeautifulSoup

def botscraptwit():
    date = datetime.now()
    month = date.month
    day = date.day
    month = calendar.month_name[month]
    productosDB = dbconnect.verTodoProd()
    # GUARDO LA URL DE LOS PRODUCTOS EN EL ARRELGO productos
    diaProd = open('diaProd.txt')
    productos = diaProd.readlines()

    # VARIABLE PARA SUMAR EL PRECIO DE TODOS LOS PRODUCTOS
    totalPrice = 0
    id = 0
    #Verifica si cambio el mes
    datos = dbconnect.verInflation()
    if (str(datos[0][3]) != month):
        dbconnect.editinflat(0, month)
        dbconnect.resetRate()
    else:
        print('same month')
    # RECORRO EL ARREGLO Y HAGO SCRAPPING DEL PRECIO
    for prod_url in productos:
        prod_url = prod_url.strip()
        try:
            html = requests.get(prod_url).text
            soup = BeautifulSoup(html, 'html.parser')
            precio = soup.find('span', {'class': 'vtex-product-price-1-x-currencyContainer'})
            if precio:
                precio = precio.text.replace('$', "")
                precio = precio.replace('.', '')
                precio = precio.replace(',', '.')
                precio = float(precio)
                print(precio)
                totalPrice = precio + totalPrice
                if(float(productosDB[id][1])!=precio):
                    rateChange = (precio/float(productosDB[id][1]))-1
                    rateChange *= 100
                    rateChange = round(rateChange, 2)
                    rateChange += float(productosDB[id][2])
                    dbconnect.editarDB(id+1, precio)
                    dbconnect.editarRate(id+1, rateChange)
            else:
                precioList = dbconnect.verDB(id)
                precio = int(precioList[0][0])
                print("No tiene precio")
                totalPrice = precio + totalPrice
        except:
            precioList = dbconnect.verDB(id)
            precio = int(precioList[0][0])
            print("Error con url")
            totalPrice = precio + totalPrice
        id += 1

    diaProd.close()

    daily = ((totalPrice/float(datos[0][0]))-1)*100
    total = totalPrice
    monthly = float(datos[0][2])+daily
    monthly = round(monthly, 2)

    dbconnect.editarDBinflation(total, daily, monthly, month)

    twit = 'La inflación acumulada en el día ' + str(day) + ' de ' + str(month) + ' es del : ' + str(monthly) + '%'
    twitapi.twitear(twit, monthly, month, day)

    ListRate = dbconnect.orderByRateDESC()

    msg = 'Los productos con mayor aumento al día ' + str(day) + ' de ' + month + ' son:\n' \
          '' + str(ListRate[0][2]) + '% ' + ListRate[0][3] + '\n' \
          '' + str(ListRate[1][2]) + '% ' + ListRate[1][3] + '\n' \
          '' + str(ListRate[2][2]) + '% ' + ListRate[2][3] + '\n'
    twitapi.twitearRateIndividual(msg)

    ListRate = dbconnect.orderByRateASC()
    msg = 'Los productos con mayor descuento al día ' + str(day) + ' de ' + month + ' son:\n' \
          '' + str(ListRate[0][2]) + '% ' + ListRate[0][3] + '\n' \
          '' + str(ListRate[1][2]) + '% ' + ListRate[1][3] + '\n' \
          '' + str(ListRate[2][2]) + '% ' + ListRate[2][3] + '\n'
    twitapi.twitearRateIndividual(msg)


    dbconnect.cerrarConex()



horaInicio = datetime.now()
botscraptwit()
horaFinal = datetime.now()
print('Tiempo de ejecucion : ' + str(horaFinal-horaInicio))
