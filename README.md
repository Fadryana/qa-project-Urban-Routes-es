ARCHIVO :
README.md

---
# NOMBRE DEL PROYECTO :
qa-project-Urban-Routes-es Soft Skills

  
---

# NOMBRE USUARIO :
fadrimir

---
# COHORTE :
25

---
# DESCRIPCION DEL PROYECTO:

---
# 👫 Soft Skills

  -  ✔ Se está comprobando cómo la aplicación URBAN ROUTES funciona para pedir un taxi.
  -  ✔ Se han realizado varias pruebas para comprobar la funcionalidad de URBAN ROUTES.
  -  ✔ Se han definido los localizadores en la clase UrbanRoutesPage.
  -  ✔ Se han definido los métodos en la clase UrbanRoutesPage.
  -  ✔ Se han definido las pruebas en la clase TestUrbanRoutes.
  -  ✔ Se han escrito pruebas automatizadas del proceso completo de pedir un taxi. Las pruebas siguen estas acciones:
  -  -  * Configurar la dirección.
     -  * Seleccionar la tarifa Comfort.
     -  * Rellenar el número de teléfono.
     -  * Agregar una tarjeta de crédito.
     -  * Escribir un mensaje para el controlador.
     -  * Pedir una manta y pañuelos.
     -  * Pedir 2 helados
     -  * Aparece el modal para buscar un taxi.
---

### Se utilizo CINCO archivos en total:

  -  data
  -  main.py
  -  utilitarios.py
  -  readme.py
  -  .gitignore.

---

### Detalle de cada archivo:
data.py
-Se reemplaza la URL base con la URL de Urban Routes:
https://cnt-b1112777-ad5c-4e43-b438-d38ee15d86e6.containerhub.tripleten-services.com?lng=es
-Los datos que se van a usar en las pruebas son los siguiente:
address_from = ‘East 2nd Street, 601’
address_to = ‘1300 1st St’
phone_number = ‘+1 123 123 12 12’
card_number, card_code = ‘1234 5678 9100’, ‘111’
message_for_driver = ‘Traiga un postre’
cantidad_de_helados = ‘2’

main.py
-En este archivo se encuentran las pruebas para comprobar la funcionalidad de Urban Routes.
-Se definieron los localizadores en la clase UrbanRoutesPage - class UrbanRoutesPage
-Se definieron los métodos en la clase UrbanRoutesPage - class UrbanRoutesPage
-Se escribieron pruebas automatizadas que cubren el proceso completo de pedir un taxi. Las pruebas cubren estas acciones:
En el método - 1 - configurar la dirección.
En el método - 2 - seleccionar la tarifa confort
En el método - 3 - rellenar el numero de teléfono
En el método - 4 - seleccionar método de pago
En el método - 5 - escribir un mensaje para el conductor
En el método - 6 - pedir una manta y pañuelos
En el método - 7 - pedir helados
En el método - 8 - aparece modal o ventana emergente buscar un taxi.
-Se han definido las pruebas en la clase TestUrbanRoutes - class TestUrbanRoutes
La prueba o test - 1 - caso de prueba_ruta desde y hasta
La prueba o test - 2 - caso de prueba_seleccionar la tarifa comfort
La prueba o test - 3 - caso de prueba_rellenar el número de teléfono
La prueba o test - 4 - caso de prueba_agregar una tarjeta de crédito
La prueba o test - 5 - caso de prueba_escribir un mensaje para el conductor
La prueba o test - 6 - caso de prueba_pedir una manta y pañuelos
La prueba o test - 7 - caso de prueba_pedir dos helados
La prueba o test - 8 - caso de prueba_modal para buscar un taxi

utilitarios.py
-En este archivo utilitarios.py se encuentra el código que devuelve un número de confirmación de teléfono y lo devuelve como un string. Se utiliza cuando la aplicación espera el código de confirmación. Este código se usa para las pruebas. El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación. El repositorio tiene preparada la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta.

readme.py
-En readme.py se encuentra la descripción del proyecto.

FUENTE DE DOCUMENTACION UTILIZADA :
Servidor - Dirección del banco:
https://cnt-09bfdbca-8c1f-4bf1-bfe8-5ea5f4ac1edd.containerhub.tripleten-services.com?lng=es
(esta es la URL de servidor para que tu código pueda acceder al servidor.)

DESCRIPCION DE LAS TECNOLOGIAS Y TECNICAS UTILIZADAS :
-Se uso Python 3.13 el lenguaje de programación de los testers.
-Se uso PyCharm, se programo en dispositivo personal, proyecto en PyCharm
-Se han importado paquetes. Se uso Selenium WebDriver 4.30.0, es un controlador de navegador, que emula las acciones de usuario.
Para usar los comandos de Selenium, se tuvo que importar el paquete Selenium WebDriver:
from selenium import webdriver
Selenium es capaz de emular la mayoría de las acciones de usuario en el navegador:
Hacer clicks, rellenar campos de entrada, abrir URL, etc.
-Se importo la clase By, esta clase ayuda a especificar los criterios de búsqueda de los elementos. Para usar los métodos de la clase By, se usa: from selenium.webdriver.common.by import By
-Se importo la clase WebdriverWait, las esperas explícitas detienen la prueba durante un período de tiempo exacto: from selenium.webdriver.support.wait import WebDriverWait
-Para personalizar las esperas, se establece una condición utilizando la clase expected_conditions. Estas son las condiciones más utilizadas:
element_to_be_clickable : se puede hacer clic en el elemento.
presence_of_element_located : el elemento está presente en la página.
visibility_of_element_located : el elemento está presente en la página y es visible.
-Se instalo los paquetes Pytest 8.3.5 para ejecutar las pruebas.
-Se uso el Git, el sistema de control de versiones. El proyecto en GitHub.
-Se uso para el archivo README.md , el link: https://dillinger.io/ - README es un archivo de texto markdown con formato md. Markdown es similar a HTML: todos los encabezados, párrafos e hipervínculos tienen una forma de indicarse, solo que con símbolos especiales en lugar de etiquetas.
