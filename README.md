

**Taller 3 - Vistas**

**Por:**

Santiago Triana 201923265

Gabriela García 201912531

Para probar los requerimientos se crearán 5 medidas de prueba como se muestra a

continuación

***Imagen 1.** Captura de pantalla añadiendo valores de prueba.*

***Imagen 2.** Lista con todos los valores de prueba que se van a probar.*





\1. Consultar la lista de medidas (*measurements*) en formato JSON

***Imagen 3.** Resultado al acceder a [http://localhost:8000/measurements/list/*](http://localhost:8000/measurements/list/)[ ](http://localhost:8000/measurements/list/)desplegando la*

*lista de measurements*

*2. Consultar una medida en formato JSON dado su identificador*

***Imagen 4.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/4*](http://localhost:8000/measurements/get_by_id/4)[ ](http://localhost:8000/measurements/get_by_id/4),*

*desplegando el measurement con id 4.*





***Imagen 5.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/7*](http://localhost:8000/measurements/get_by_id/7)[ ](http://localhost:8000/measurements/get_by_id/7),*

*desplegando el measurement con id 7.*

\3. Borrar una medida dado su identificador

***Imagen 6.** Resultado al acceder a*

[*http://localhost:8000/measurements/delete_by_id/7*](http://localhost:8000/measurements/delete_by_id/7)[ ](http://localhost:8000/measurements/delete_by_id/7)*, desplegando un mensaje de*

*confirmación de la eliminación.*





***Imagen 7.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/7*](http://localhost:8000/measurements/get_by_id/7)*

*, error DoesNotExist un measurement con id 7, confirmando que ya no se encuentra*

*en la base de datos.*

\4. Cambiar una medida dado su identificador

***Imagen 8.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/6*](http://localhost:8000/measurements/get_by_id/6)[,*](http://localhost:8000/measurements/get_by_id/6)[ ](http://localhost:8000/measurements/get_by_id/6)donde*

*se evidencia que el measurement con id 6 tiene valor 300*





***Imagen 9.** Resultado al acceder a*

[*http://localhost:8000/measurements/update_by_id/6/250*](http://localhost:8000/measurements/update_by_id/6/250)[ ](http://localhost:8000/measurements/update_by_id/6/250)*, donde se actualiza el valor del*

*measurement con id 6 a 250.*

***Imagen 10.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/6*](http://localhost:8000/measurements/get_by_id/6)[,*](http://localhost:8000/measurements/get_by_id/6)*

*donde se evidencia que el measurement con id 6 tiene valor 250 y se confirma una correcta*

*actualización.*

