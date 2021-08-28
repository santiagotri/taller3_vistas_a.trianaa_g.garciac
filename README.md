
 
 --- EL CONTENIDO DE ESTE README SE PUEDE EVIDENCIAR MEJOR EN 'Taller 3 - g.garciac_a.trianaa.pdf' ---
 
 
**Taller 3 - Vistas**

**Por:**

Santiago Triana 201923265

Gabriela García 201912531

Para probar los requerimientos se crearán 5 medidas de prueba como se muestra a

continuación


![image](https://user-images.githubusercontent.com/69616930/131229397-8a4234c1-039d-4de2-820b-ade57d3e68da.png)


***Imagen 1.** Captura de pantalla añadiendo valores de prueba.*

![image](https://user-images.githubusercontent.com/69616930/131229412-7326928d-05fa-4b82-93cb-0314eba0880d.png)



***Imagen 2.** Lista con todos los valores de prueba que se van a probar.*





\1. Consultar la lista de medidas (*measurements*) en formato JSON

![image](https://user-images.githubusercontent.com/69616930/131229423-4908e51b-39f7-47da-8cfe-14be21b0d874.png)



***Imagen 3.** Resultado al acceder a [http://localhost:8000/measurements/list/*](http://localhost:8000/measurements/list/)[ ](http://localhost:8000/measurements/list/)desplegando la*

*lista de measurements*



*2. Consultar una medida en formato JSON dado su identificador*

![image](https://user-images.githubusercontent.com/69616930/131229436-a28ae6ab-c7e1-4fd7-bbde-dba5906b07fe.png)



***Imagen 4.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/4*](http://localhost:8000/measurements/get_by_id/4)[ ](http://localhost:8000/measurements/get_by_id/4),*

*desplegando el measurement con id 4.*



![image](https://user-images.githubusercontent.com/69616930/131229438-f1a4c4ab-2270-461b-9929-21fae2bb5bf6.png)




***Imagen 5.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/7*](http://localhost:8000/measurements/get_by_id/7)[ ](http://localhost:8000/measurements/get_by_id/7),*

*desplegando el measurement con id 7.*

\3. Borrar una medida dado su identificador


![image](https://user-images.githubusercontent.com/69616930/131229442-954be084-bf34-4aa3-b923-3fca6f7c14ac.png)



***Imagen 6.** Resultado al acceder a*

[*http://localhost:8000/measurements/delete_by_id/7*](http://localhost:8000/measurements/delete_by_id/7)[ ](http://localhost:8000/measurements/delete_by_id/7)*, desplegando un mensaje de*

*confirmación de la eliminación.*



![image](https://user-images.githubusercontent.com/69616930/131229451-4ea54b1c-40b7-4c05-a50b-510d7f66db92.png)



***Imagen 7.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/7*](http://localhost:8000/measurements/get_by_id/7)*

*, error DoesNotExist un measurement con id 7, confirmando que ya no se encuentra*

*en la base de datos.*

\4. Cambiar una medida dado su identificador



![image](https://user-images.githubusercontent.com/69616930/131229456-5a0043c8-27b9-4a36-aa00-037be36ef6c3.png)



***Imagen 8.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/6*](http://localhost:8000/measurements/get_by_id/6)[,*](http://localhost:8000/measurements/get_by_id/6)[ ](http://localhost:8000/measurements/get_by_id/6)donde*

*se evidencia que el measurement con id 6 tiene valor 300*



![image](https://user-images.githubusercontent.com/69616930/131229458-872b680e-cc09-49f9-8d64-097e47a8d62b.png)




***Imagen 9.** Resultado al acceder a*

[*http://localhost:8000/measurements/update_by_id/6/250*](http://localhost:8000/measurements/update_by_id/6/250)[ ](http://localhost:8000/measurements/update_by_id/6/250)*, donde se actualiza el valor del*

*measurement con id 6 a 250.*


![image](https://user-images.githubusercontent.com/69616930/131229464-257bd6b0-ac8e-4c1c-8c48-ec25d9f9ae22.png)



***Imagen 10.** Resultado al acceder a [http://localhost:8000/measurements/get_by_id/6*](http://localhost:8000/measurements/get_by_id/6)[,*](http://localhost:8000/measurements/get_by_id/6)*

*donde se evidencia que el measurement con id 6 tiene valor 250 y se confirma una correcta*

*actualización.*

