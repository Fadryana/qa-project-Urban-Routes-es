"""Vas a escribir varias pruebas para comprobar la funcionalidad de Urban Routes. Escribe tus pruebas en el archivo main.py."""

import data

from utilitarios import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


"""Define los localizadores y métodos necesarios en la clase UrbanRoutesPage"""
class UrbanRoutesPage:
    from_field = (By.ID, 'from')        #campo texto From
    to_field = (By.ID, 'to')                # campo texto To
    boton_pedir_taxi = (By.CSS_SELECTOR, ".button.round")  # boton pedir un taxi
    icono_tarifa_confort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]') # icono carrito celeste tarifa Comfort
    campo_fono = (By.CLASS_NAME, "np-text")      # campo Numero de telefono
    campo_fono2 = (By.ID, "phone")         # Introduce numero de telefono en ventana emergente
    boton_siguiente = (By.XPATH, "//button[@type='submit'][@class = 'button full']")     # boton Siguiente
    campo_codigo = (By.XPATH, "//*[@id='code']")         # ventana emergente -Introduce el codigo SMS-
    boton_confirmar = (By.XPATH, "//button[text()='Confirmar']")    # boton confirmar
    metodo_de_pago = (By.CSS_SELECTOR, ".pp-button")    # metodo de pago
    agregar_tj = (By.CSS_SELECTOR, ".pp-plus-container")   # agregar tarjeta de credito
    numero_de_tarjeta = (By.ID, "number")       # numero de tarjeta de credito
    codigo_tj = (By.NAME, "code")       # codigo de seguridad de tarjeta de credito
    boton_agregar_tj = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")    #boton agregar
    tj_check = (By.XPATH, "//div[contains(@class, 'pp-title') and text()='Tarjeta']")   #metodo de pago escogido -tarjeta- con check o visto azul
    click_icono_x = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')  # icono "X" para cerrar ventana
    msj_chofer = (By.XPATH, "//label[@for='comment']")      #mensaje para conductor o chofer
    msj_chofer_a_digitar = (By.XPATH, "//input[contains(@placeholder, 'aperitivo')]")   #escribir el texto -traiga un postre-
    pedir_una_mantayp_switch = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/parent::*/descendant::span[contains(@class, 'slider')]") #pedir una manta y panuelos
    pedir_una_mantayp_switchinput = (By.XPATH, "(//input[@class='switch-input'])[1]")   #switch input - deslizador-pedir una manta y panuelos-.pedir_una_mantayp_switchinput
    pedir_helado = (By.CLASS_NAME, 'counter-plus')     #seleccidonar helado
    cuenta_helados = (By.XPATH, "(//div[@class='counter-value'])[1]")   #contar helados
    modal_taxi = (By.CLASS_NAME, 'smart-button-main')   # modal o ventana emergente del taxi

    def __init__(self, driver):         #constructor
        self.driver = driver


#metodo - 1 - configurar la direccion#
    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

#boton azul pedir un taxi
    def get_boton_pedir_taxi(self):         # localizador
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.boton_pedir_taxi))

    def click_on_boton_pedir_taxi(self):        # hacer click en el boton pedir un taxi
        self.get_boton_pedir_taxi().click()

#metodo - 2 - seleccionar la tarifa confort#
    def get_obtener_icono_de_la_tarifa_comfort(self):       #obtener el localizador de la tarifa comfort
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.icono_tarifa_confort))

    def click_on_hacer_clicen_tarifa_comfort(self):     #hacer click en el icono de la tarifa comfort
        self.get_obtener_icono_de_la_tarifa_comfort().click()

    def get_desplazar_masabajo0(self):      #hacer scroll o desplazarse mas abajo en el formulario
        desp0 = self.driver.find_element(By.CLASS_NAME, "np-text")   #ir al siguiente campo - numero de telefono
        self.driver.execute_script("arguments[0].scrollIntoView();", desp0)    # usando scroll

#metodo - 3 - rellenar el numero de telefono#
    def get_textbox1_num_fono(self):        #obtener el localizador en el formulario donde dice numero de telefono#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.campo_fono))

    def click_on_textbox(self):
        self.get_textbox1_num_fono().click()    #hacer click en el formulario donde dice numero de telefono#

    def get_textbox2_num_fono(self):        #obtener el localizador, de la ventana emergente, segundo campo de texto numero de telefono#
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.campo_fono2))

    def set_escribir_textbox2(self):    #escribir numeros, del archivo data, phone_number +1 123 123 12 12#
        self.get_textbox2_num_fono().send_keys(data.phone_number)

    def get_boton_azul_siguiente(self):     # localizador de boton color azul siguiente#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.boton_siguiente))

    def click_on_boton_sig(self):       #hacer click en el boton siguiente#
        self.get_boton_azul_siguiente().click()

    def get_textbox3(self):         #obtener el localizador del tercer campo de texto, donde va el codigo sms#
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.campo_codigo))

    def traer_codigo_sms(self):     # traer el codigo sms, del programa retrieve phone code#
        codigo = retrieve_phone_code(self.driver)
        self.get_textbox3().send_keys(codigo)

    def get_boton_azul_confirmar(self):     # localizador del boton azul confirmar#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.boton_confirmar))

    def click_on_confirmar(self):       #hacer click en boton azul confirmar#
        self.get_boton_azul_confirmar().click()

    def get_desplazar_masabajo1(self):    #hacer scroll o desplazarse mas abajo en el formulario#
        desp1 = self.driver.find_element(By.CSS_SELECTOR, ".pp-button")   # moverse hasta el siguiente elemento#
        self.driver.execute_script("arguments[0].scrollIntoView();", desp1)

#metodo - 4 - seleccionar metodo de pago#
    def get_campo_metod_pago(self):     # localizador del campo metodo de pago#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.metodo_de_pago))

    def click_metod_pago(self):         # hacer click en metodo de pago#
        self.get_campo_metod_pago().click()

    def get_campo2_metod_pago_agrtjcr(self):        # localizador del segundo campo, agregar tarjeta#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.agregar_tj))

    def click_campo2_agrtjcr(self):         ## hacer click en ventana emergente-metodo de pago, donde dice agregar tarjeta#
        self.get_campo2_metod_pago_agrtjcr().click()

    def get_campo3_numtjcr(self):           # localizador del tercer campo, numero de tarjeta#
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.numero_de_tarjeta))

    def set_campo3_digitar_numtjcr(self):
        self.get_campo3_numtjcr().send_keys(data.card_number)  # digitar del archivo data, el card_number: '1234 5678 9100'#
        self.get_campo3_numtjcr().send_keys(Keys.TAB) ## presionar la tecla TAB#

    def get_campo3_codseg(self):            # localizador del codigo de seguridad de la tarjeta#
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.codigo_tj))

    def set_campo3_digitar_codseg(self):
        self.get_campo3_codseg().send_keys(data.card_code)  # digitar numero del codigo de seguridad, del archivo data, card_code 111#
        self.get_campo3_codseg().send_keys(Keys.TAB) # presionar la tecla TAB para activar el botón agregar#

    def get_campo3_boton_agregar(self):         # localizador del boton agregar#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.boton_agregar_tj))

    def click_campo3_boton_azul_agregar(self):     # hacer click en boton agregar tarjeta de credito como metodo de pago#
        self.get_campo3_boton_agregar().click()

    def get_campo4_check_tjcr(self):        # localizador de tarjeta de credito seleccionada#
            return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.tj_check))

    def get_campo4_icono_x(self):           # localizador del icono x para cerrar ventana#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.click_icono_x))

    def click_campo4_en_la_x(self):         # hacer click en icono x para cerrar ventana#
        self.get_campo4_icono_x().click()

    def get_desplazar_masabajo2(self):    #hacer scroll o desplazarse mas abajo en el formulario#
        desp2 = self.driver.find_element(By.XPATH, "//label[@for='comment']")   # moverse hasta el siguiente elemento#
        self.driver.execute_script("arguments[0].scrollIntoView();", desp2)

#metodo - 5 - escribir un mensaje para el conductor#
    def get_textbox_msj_conductor(self):            #obtener el localizador textbox mensaje para conductor o chofer#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.msj_chofer))

    def click_mensj_conductor(self):            #hacer click en ese campo de texto#
        self.get_textbox_msj_conductor().click()

    def get_msj(self):              #obtener localizador donde va a escribir el texto para el conductor o chofer#
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.msj_chofer_a_digitar))

    def set_digitar_msj(self):
        self.get_msj().send_keys(data.message_for_driver)     # digitar del archivo data, el message_for_driver ----> Traiga un postre#

    def get_desplazar_masabajo3(self):    #hacer scroll o desplazarse mas abajo en el formulario#
        desp3 = self.driver.find_element(By.CLASS_NAME, 'switch')   # moverse hasta el elemento pedir una manta y panuelos#
        self.driver.execute_script("arguments[0].scrollIntoView();", desp3)

#metodo - 6 - pedir una manta y panuelos#
    def get_area_mantayp(self):     ##obtener localizador manta y panuelos
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.pedir_una_mantayp_switch))

    def click_on_area_mantayp(self):        #hacer click
        self.get_area_mantayp().click()

    def get_desplazar_masabajo4(self):    #hacer scroll o desplazarse mas abajo en el formulario#
        desp4 = self.driver.find_element(By.XPATH, "(//input[@class='switch-input'])[1]")   #moverse hasta el siguiente elemento#
        self.driver.execute_script("arguments[0].scrollIntoView();", desp4)

    def get_pedir_una_mantaypanuelos(self):     #localizador de seleccionar el switch o deslizador
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.pedir_una_mantayp_switchinput))

    def click_on_deslizador_pedirmantayp(self):     #hacer click
        self.get_pedir_una_mantaypanuelos().click()

#metodo - 7 - pedir helados#
    def get_helado(self):       #obtener el localizador de helados#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.pedir_helado))

    def set_pedir_helad(self):  # Hacer click en la opción de helados#
        self.get_helado().click()  #hacer un click para seleccionar el primer helado#
        self.get_helado().click()  #hacer otro click para seleccionar el segundo helado#

    def get_dos_helados(self):       #obtener el localizador de dos helados#
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.cuenta_helados)).text

    def get_desplazar_masabajo5(self):   #hacer scroll o desplazarse mas abajo en el formulario#
        desp5 = self.driver.find_element(By.CLASS_NAME, 'smart-button-main')   # moverse hasta el elemento modal o ventana emergente taxi#
        self.driver.execute_script("arguments[0].scrollIntoView();", desp5)

#metodo - 8 - aparece modal o ventana emergente  buscar un taxi#
    def get_boton_modal(self):      #obtener el boton del modal o ventana del taxi#
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.modal_taxi))

    def click_boton_modal_taxi(self):       #hacer click en el boton del modal o ventana del taxi#
        self.get_boton_modal().click()


"""Vas a escribir varias pruebas para comprobar la funcionalidad de Urban Routes. Escribe tus pruebas en el archivo main.py."""
"""Define las pruebas en la clase TestUrbanRoutes"""
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)


#test -1- caso de prueba_ruta desde y hasta#
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

#test - 2 - caso de prueba_seleccionar la tarifa comfort#
    def test_selecciona_tarifa_confort(self):
        routes_page = UrbanRoutesPage(self.driver)  #self driver permite controlar navegador
        routes_page.click_on_boton_pedir_taxi()     #hace click en el boton pedir taxi
        assert routes_page.get_boton_pedir_taxi().is_enabled(), "El botón 'Pedir taxi' no se activó" #confirmar si el boton esta habilitado...
        routes_page.click_on_hacer_clicen_tarifa_comfort()  #hace click en el icono tarifa comfort
        assert routes_page.get_obtener_icono_de_la_tarifa_comfort().is_enabled(),  "el icono tarifa Comfort no se activo" #confirmar si comfort esta habilitado...

#test - 3 - caso de prueba_rellenar el número de teléfono#
    def test_rellenar_num_fono(self):
        routes_page = UrbanRoutesPage(self.driver)  #self driver permite controlar navegador
        routes_page.click_on_textbox()      #hacer click en el formulario donde dice numero de telefono
        routes_page.set_escribir_textbox2()    #escribe el numero de telefono, en el textbox
        numtelactual = routes_page.get_textbox2_num_fono().get_attribute("value")  #obtiene el numero de telefono que se escribio, en el textbox
        numteldefault = data.phone_number   #del archivo data py trae lo que contiene, phone number
        assert numtelactual == numteldefault, "El numero de telefono no corresponde"    #verifica que el numero ingresado sea el correcto
        routes_page.click_on_boton_sig()       #hace click en el boton siguiente
        routes_page.traer_codigo_sms()     #obtiene el codigo sms, del programa retrieve phone code
        routes_page.click_on_confirmar()   #hace click en el boton confirmar

#test - 4 - caso de prueba_agregar una tarjeta de crédito#
    def test_prueba_metodo_pago(self):
        routes_page = UrbanRoutesPage(self.driver)      #self driver permite controlar navegador
        routes_page.click_metod_pago()      #hacer click en metodo de pago primera parte
        routes_page.click_campo2_agrtjcr()      #hacer click en agregar tarjeta
        routes_page.set_campo3_digitar_numtjcr()    #digita el numero de tarjeta,  digitar del archivo data, el card_number: '1234 5678 9100'
        routes_page.get_campo3_numtjcr().send_keys(Keys.TAB)    #con send keys, dar un TAB por teclado
        routes_page.set_campo3_digitar_codseg()     ## digita numero del codigo de seguridad, del archivo data, card_code 111
        routes_page.get_campo3_codseg().send_keys(Keys.TAB)     #con send keys, dar un TAB por teclado
        routes_page.click_campo3_boton_azul_agregar()       #hacer click en boton agregar tarjeta
        routes_page.click_campo4_en_la_x()      #hacer click para cerrar la ventana

#test - 5 - caso de prueba_escribir un mensaje para el conductor#
    def test_mensaje_conductor(self):
        routes_page = UrbanRoutesPage(self.driver)      #self driver permite controlar navegador
        routes_page.click_mensj_conductor()        #hacer click en campo de texto mensaje al conductor o chofer
        routes_page.set_digitar_msj()      #digitar el mensaje para el conductor o chofer, del archivo data, message_for_driver ---->Traiga un postre
        msjchofactual = routes_page.get_msj().text     #obtener el mensaje actual
        msjchofdefault = data.message_for_driver    #obtener del archivo data, message_for_driver ---->Traiga un postre
        assert msjchofactual in msjchofdefault, "El mensaje de error no apareció correctamente"

#test - 6 - caso de prueba_pedir una manta y pañuelos#
    def test_seleccion_mantayp(self):
        routes_page = UrbanRoutesPage(self.driver)      #self driver permite controlar navegador
        routes_page.click_on_area_mantayp()         #hacer click en manta y panuelos
        routes_page.get_desplazar_masabajo4()       #hacer scroll o desplazarse mas abajo

#test - 7 - caso de prueba_pedir dos helados#
    def test_helado(self):
        routes_page = UrbanRoutesPage(self.driver)  # self driver permite controlar navegador#
        routes_page.set_pedir_helad()               #clicks para pedir helados#
        cantidad_real_helados = routes_page.get_dos_helados()   #obtener el localizador del 2 helados#
        assert cantidad_real_helados == data.cantidad_de_helados    #comparar el 2 con el archivo data, cantidad_de_helados = '2'#

#test - 8 - caso de prueba_modal para buscar un taxi#
    def test_prueba_modal_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)      #self driver permite controlar navegador#
        routes_page.click_boton_modal_taxi()            #hacer click en el boton del modal o ventana del taxi#


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()