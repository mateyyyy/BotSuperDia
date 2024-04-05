DIA BOT
=======

DIA BOT es un bot de Twitter que proporciona informes diarios sobre la variacion en los precios de los productos del supermercado Día.
Realiza un scrapping sobre la url de cada producto Dia retirando el elemento que contiene el precio.

Características
---------------

*   Analiza aproximadamente 2050 productos diariamente.
*   Utiliza una base de datos local como respaldo.
*   Se integra con la API de Twitter para twittear.
*   Publica tweets sobre los 3 productos con la mayor variación de precio en el mes y los 3 con la menor variación.

Empezar
-------

1.  Clona el repositorio: `git clone https://github.com/your_username/DIA-BOT.git](https://github.com/mateyyyy/BotSuperDia.git`
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Configura las credenciales de la API de Twitter en `twitapi.py`.
4.  Configura las credenciales de la Base de datos en `dbconnect.py`.


EJEMPLO
-------
![image](https://github.com/mateyyyy/BotSuperDia/assets/65136286/972acba7-12f9-462c-9b1d-b1a51b34f401)
