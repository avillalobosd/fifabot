#AGREGAR EN EL SISTEMA PATH LA RUTA DE CHROME

# CORRE ESTO PRIMERO EN EL CMD
# chrome.exe --remote-debugging-port=9250 --user-data-dir="C:/chromedriver2"
#INICIAR SESION EN LA WEBAPP EN LA PANTALLA QUE SE ABRIO
from tkinter import *
from tkinter import ttk
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import threading  
from io import BytesIO
import win32clipboard
from PIL import Image
switch = True  
os.system('clear')
import pyrebase

config = {
  "apiKey": "AIzaSyCO09JciLlqV3N4K7hV90qK_8XBvGBaCLI",
  "authDomain": "fifabot-e4c0b.firebaseapp.com",
  "databaseURL": "https://fifabot-e4c0b.firebaseio.com",
  "storageBucket": "fifabot-e4c0b.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()







#### CONGIRUACION PANTALLA DE WEB APP
opts = Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9250')
driver = webdriver.Chrome(options=opts)
seguir = True
cuantos=0

#### CONGIRUACION PANTALLA DE WEB APP
optsWhats = Options()
optsWhats.add_experimental_option('debuggerAddress', 'localhost:9222')
driverWhatsapp = webdriver.Chrome(options=optsWhats)


iteraciones=0

#######################################################################
####################################################################### 
############ PANTALLA 1 DE BUSQUEDA ###################################
#######################################################################
#######################################################################


#CLICK EN EL BOTON BUSCAR DEL MERCADO DE TRANSFERENCIAS
def clickBuscar():
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()

# TOMA EL PRECIO MAXIMO DE INFERFAZ Y LO PONE EN LA WEBAPP
def precioMaximoBusqueda():
    precioMax= driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")
    precioMax.click()
    time.sleep(1)
    precioMax.send_keys(maximo.get())

#CLICK EN AUMENTAR EL PRECIO MINIMO
def aumentaMinimoCompraYa():
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/button[2]").click()

#CLICK EN DISMINUIR EL PRECIO MINIMO
def disminuyeMinimoCompraYa():
    for x in range(0, 3):
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/button[1]").click()
def Mas1ClickMaximo():
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/button[2]").click()
    time.sleep(2)

def Menos1ClickMaximo():
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/button[1]").click()
    time.sleep(2)
aumento=0

def buscarRango():
    print("BUSCANCO RANGO")
    global aumento
    aumento=0
    switchoff()
    irMercadoTransferencias()
    Mas1ClickMaximo()
    Mas1ClickMaximo()
    clickBuscar()
    time.sleep(3)
    global count
    count = len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li"))
    print(count)
    while aumento!=1000:
        count = len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li"))
        if count ==0:
            aumento=aumento+1
            irMercadoTransferencias()
            Mas1ClickMaximo()
            clickBuscar()
            time.sleep(3)
            # count = len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li"))
            print("+1 COUNT=0")
        elif driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[1]/div/div[1]/span[2]").text[:1]=="<":
            print(count)
            # print()
            aumento=aumento-1
            irMercadoTransferencias()
            Menos1ClickMaximo()
            clickBuscar()
            time.sleep(3)

        elif count<=10 and int(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[1]/div/div[1]/span[2]").text[:2])>=50 :
            print("<8 TIEMPO MAYOR A 50")
            break
        else:
            print(count)
            # print()
            aumento=aumento-1
            irMercadoTransferencias()
            Menos1ClickMaximo()
            clickBuscar()
            time.sleep(3)
            # count = len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li"))
            print("-1 NO SE CUMPLE")
    print(aumento)
    actualMaximo=int(maximo.get())
    actualFinal=int(final.get())
    if actualMaximo+int(aumento)*100>2600:
        final.delete(0,END)
        final.insert(0,actualFinal+int(aumento)*100)
        maximo.delete(0,END)
        maximo.insert(0,int(final.get())-300)
        enviarWhatsapp("Nuevo Rango Compra: "+str(maximo.get())+" Venta: "+final.get())
        irMercadoTransferencias()
        time.sleep(3)
        precioMaximoBusqueda()
        clickBuscar()
        switchoff()
        time.sleep(5)
        iniciar()
    else:
        if actualMaximo+int(aumento)*100<=int(numeroDetener.get()):
            switchoff()
        else:
            final.delete(0,END)
            final.insert(0,actualFinal+int(aumento)*100)
            maximo.delete(0,END)
            maximo.insert(0,int(final.get())-200)
            enviarWhatsapp("Nuevo Rango Compra: "+str(maximo.get())+" Venta: "+final.get())
            irMercadoTransferencias()
            time.sleep(3)
            precioMaximoBusqueda()
            clickBuscar()
            switchoff()
            time.sleep(5)
            iniciar()

def buscarRango2():
    print(int(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[1]/div/div[1]/span[2]").text[:2]))


#######################################################################
####################################################################### 
############ PANTALLA 2 DE BUSQUEDA ###################################
#######################################################################
#######################################################################
MmWhats=""
#CLICK PRIMER ELEMENTO ENCONTRADO SOLO SI LO ENCUENTRA
def clickEncontrado():
    if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div")) > 0:
        # driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div").click()
        # print(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div/div[2]/div[3]/span[2]").text)
        pe=driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div/div[2]/div[3]/span[2]").text
        global mWhats
        mWhats=pe
        # enviarWhatsapp("POR: "+pe)
        # tablaLog.insert(parent="",index="end",text="parent",values=("Encontrado: "+pe))
        comprar()
     

#CLICK REGRESAR A BUSQUEDA DE MERCADO DE TRANSFERENCIA
def clickRegresar():
    # print(inicial.get())
    driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]").click()



#CLICK EN PONER ARTICULO COMPRADO
def ponerMercado():
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button").click()

#DEFINIR PRECIO INICIAL DE ARTICULO COMPRADO
def definirPrecio():
    #DEFINIR MINIMO
    if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")) > 0:
        minimo= driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
        minimo.click()
        time.sleep(2)
        minimo.send_keys(inicial.get())
        #DEFINIR MAXIMO
        maximo = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
        maximo.click()
        time.sleep(2)
        maximo.send_keys(final.get())
        #CLICK EN PONER EN EL MERCADO
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button").click()
    else:
        print("FALSA ALARMA")



## COMPRA EL ARTICULO Y LO PONER EN EL MERCADO
def comprar():
    try:
        nueva=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
        saldoInicial=nueva.replace(",",".")
        print("ESTE ES EL SALDO INICIAL")
        print(saldoInicial)
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]").click()
        if len(driver.find_elements_by_xpath("/html/body/div[4]/section/div/div/button[1]")) > 0:
            driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]").click()
            # print("PUES LO COMPRE")
            time.sleep(5)
            nueva2=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
            saldoF=nueva2.replace(",",".")
            if float(saldoF) != float(saldoInicial):
                saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
                print(saldo)
                enviarWhatsapp("SE COMPRO "+mWhats+" Iteracion: " + str(iteraciones))
                time.sleep(5)
                if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")) > 0:
                    ponerMercado()
                    time.sleep(2)
                    definirPrecio()
                else:
                    enviarWhatsapp("FALSA ALARMA")
                    print("FALSA ALARMA")
            else:
                print("NO SE COMPRO "+str(mWhats))
                enviarWhatsapp("NO SE COMPRO "+str(mWhats) + " Iteracion: " + str(iteraciones))
            time.sleep(2)
        else:
            enviarWhatsapp("FALSA ALARMA")
            print("FALSA ALARMA")
    except:
        print("ERROR EN COMPRAR")

def limpiarvendidos():
    ##CLICK MENU TRASPASOS
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]/span").click()
    time.sleep(5)
    ## CLICK MENU ELEMENTOS 
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[3]/div[2]").click()
    time.sleep(5)
    if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button")) > 0:
        enviarScreenshot()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button").click()
        time.sleep(3)
    else:
        print("NO HAY VENDIDOS")
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]/span").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]/div[2]").click()
    saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
    enviarWhatsapp(saldo)
    
    
    
def irMercadoTransferencias():
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]/span").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]/div[2]").click()



#######################################################################
####################################################################### 
#######################  WHATSAPP #####################################
#######################################################################
#######################################################################  

## ENVIAR WHATSAPP
def enviarWhatsapp(mensaje):
    if eW.get()== 1:
        posicionar=driverWhatsapp.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        posicionar.click()
        time.sleep(2)
        posicionar.send_keys(mensaje)
        botonEnviar=driverWhatsapp.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
        botonEnviar.click()
        print("WHATSAPP ENVIADO")



def enviarImagenWhatsapp():
    if eSS.get() ==1:
        posicionar=driverWhatsapp.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        posicionar.click()
        posicionar.send_keys(Keys.CONTROL, 'v') #paste
        time.sleep(3)
        botonEnviar=driverWhatsapp.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div")
        botonEnviar.click()
        print("IMAGEN ENVIADA")

##TOMA UN SCREENSHOT DE LA PANTALLA Y GUARDARLA EN EL CLIPBOARD
def enviarScreenshot():
    # if SSVar.get()==1:
    driver.save_screenshot("screenshot.png");
    filepath = 'screenshot.png'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    enviarImagenWhatsapp()


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

 
def detener():
    if len(driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[23]/div/div/div/div[1]/div/span[1]/span")) > 0:
        global y
        y=True
        enviarWhatsapp("PROCESO DETENIDO")
        time.sleep(2)
        while y:
            if len(driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[23]/div/div/div/div[1]/div/span[1]/span")) > 0:
                y=False
            else:
                time.sleep(5)






#######################################################################
####################################################################### 
#######################################################################
#######################################################################
####################################################################### 

## IMPRIME LAS MONEDAS ACTUALES
saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
print(saldo)
# tablaLog.insert(parent="",index="end",text="parent",values=("SaldoActual:"+saldo))

root = Tk()
root.title('FIFA BOT')
root.geometry("800x600")
##DETENER PROCESO
def stop():
    print("STOP")
    global seguir
    seguir = False

## INICIAR A BUSCAR Y COMPRAR
def iniciar():
    print("INICIO")
    # tablaLog.insert(parent="",index="end",text="parent",values=("Iniciado" ))
    saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
    print(saldo)
    # tablaLog.insert(parent="",index="end",text="parent",values=("SaldoActual:"+saldo))
    #TOMA PRECIO FINAL DE CAMPO 
    # precioFinal=int(final.get()) 
    # maximo.delete(0,END)
    # maximo.insert(0,int(precioFinal/1.07))
    # inicial.delete(0,END)
    # inicial.insert(0,precioFinal-1000)

    # print("GANANCIA MINIMA")
    # print(float(precioFinal)*.95-int(maximo.get()))
    # print(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input").text)
    # tablaLog.insert(parent="",index="end",text="parent",values=("Jugador:"+driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input").text.replace(" ", "")))
    
    # gananciaMinima = "GananciaMinima:"+str(float(precioFinal)*.95-int(maximo.get()))
    # print(gananciaMinima)
    # tablaLog.insert(parent="",index="end",text="parent",values=(gananciaMinima))

    # tablaLog.insert(parent="",index="end",text="parent",values=(gananciaMinima ))
    global switch  
    switch = True


    #DEFINE EL PRECIO MAXIMO DE BUSQUEDA
    precioMaximoBusqueda()
    def run():
        try:
            global espera
            espera=3
            while seguir:
                # detener()
                global iteraciones
                iteraciones=iteraciones+1
                global cuantos
                cuantos=cuantos+1
                if int(eR.get())==1:
                    if int(cuantos) % int(numeroRango.get())==0: 
                        enviarWhatsapp("Van "+str(cuantos))
                        enviarWhatsapp("Calculando Rango")
                        buscarRango()    
                        saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
                        enviarWhatsapp(saldo)
                if cuantos==10000:
                    break

                print(iteraciones)
                if iteraciones>=int(itera.get()):
                    # print("Limpiando vendidos")
                    # enviarWhatsapp("Limpiando vendidos")
                    if r.get() ==1:
                        enviarWhatsapp("Limpiando vendidos")
                        limpiarvendidos()
                        saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
                        enviarWhatsapp(saldo)                        
                    if r.get() ==2:
                        print("ESPERANDO S SEGUNDOS")
                        enviarWhatsapp("ESPERANDO "+str(segundos.get())+" SEGUNDOS")
                        time.sleep(int(segundos.get()))
                        enviarWhatsapp("REINICIADO")
                        print("REINICIANDO")
                    iteraciones=0
                if espera==3:
                    aumentaMinimoCompraYa()
                    espera=espera+1
                else: 
                    disminuyeMinimoCompraYa()
                    espera=espera-1
                time.sleep(int(espera))
                if switch == False:  
                    break  
                clickBuscar()
                time.sleep(1)
                if switch == False:  
                    break  
                clickEncontrado()
                time.sleep(2)
                if switch == False:  
                    break  
                clickRegresar()
                if switch == False:  
                    break
                # detener()
        except Exception:
            try:
                if r.get() ==1:
                    time.sleep(5)
                    irMercadoTransferencias()
                    iteraciones=0
                    run()
                else:
                    print("ALGO OCURRIO") 
                    enviarWhatsapp("ALGO OCURRIO 1")
                    enviarScreenshot() 

            except Exception:
                print("ALGO OCURRIO") 
                enviarWhatsapp("ALGO OCURRIO 2")
                enviarScreenshot() 
    thread = threading.Thread(target=run)
    thread.start()  





def switchon():    
    global switch  
    switch = True  
    print ("switch on") 
    # iniciar()

def switchoff():    
    print ("switch off")
    global switch  
    switch = False  
    # tablaLog.insert(parent="",index="end",text="parent",values=("Apagado") )


############### CONTROL REMOTO #####################


# def stream_handler(message):
#     command=message['data']['comando']
#     if command=='STOP':
#         switchoff()

#     print(message['data']['comando']) # put

# my_stream = db.child("comando").stream(stream_handler)





#######################################################################
####################################################################### 
############ INTERFAZ DE USUARIO ######################################
#######################################################################
#######################################################################




#### FRAMES PRINCIPALES ####
    ### IZQUIERDA
frame1 = LabelFrame(root, pady=10)
frame1.place(x=0, y=0, anchor="nw", width=450)
    ### DERECHA
frame2 = LabelFrame(root)
frame2.place(x=460, y=0, anchor="nw")

#### FRAMES SECUNDARIOS
    ### EN FRAME 1
frameControles = LabelFrame(frame1, text="CONTROLES", padx=150, pady=5)
frameControles.grid(row=0,column=0)
frameCompraVenta= LabelFrame(frame1, text="COMPRAVENTA", padx=10)
frameCompraVenta.grid(row=1,column=0)
    ## EN FRAME 2
frameOpciones = LabelFrame(frame2, text="Cada N búsquedas")
frameOpciones.grid(row=0,column=0)
frameAcciones = LabelFrame(frame2, text="Acciones")
frameAcciones.grid(row=2,column=0)
frameRango = LabelFrame(frame2, text="Buscar Cambio de Precios")
frameRango.grid(row=4,column=0)

#### FRAME ACCIONES
    ## ENVIAR WHATSAPP
eW=IntVar()
eW.set("2")
eWradio=Radiobutton(frameAcciones, text="Enviar Whatsapp eW=1", variable=eW, value=1)
eWradio2=Radiobutton(frameAcciones, text="NO Enviar Whatsapp eW=2", variable=eW, value=2)
eWradio.grid(sticky=W,row=0,column=0)
eWradio2.grid(sticky=W, row=1,column=0)

    ## ENVIAR IMAGEN WHATSAPP
eSS=IntVar()
eSS.set("2")
eSSradio=Radiobutton(frameAcciones, text="Enviar ScreenShot eSS=1", variable=eSS, value=1)
eSSradio2=Radiobutton(frameAcciones, text="NO Enviar ScreenShot eSS=2", variable=eSS, value=2)
eSSradio.grid(sticky=W,row=2,column=0)
eSSradio2.grid(sticky=W, row=3,column=0)

#### FRAME RANGO
eR=IntVar()
eR.set("1")
eRango=Radiobutton(frameRango, text="Buscar Rango eR=1", variable=eR, value=1)
eRango2=Radiobutton(frameRango, text="NO Buscar Rango eR=2", variable=eR, value=2)
eRango.grid(sticky=W,row=1,column=0)
eRango2.grid(sticky=W, row=2,column=0)

rangoLabel=Label(frameRango,text="Cada __ busquedas")
rangoLabel.grid(row=3,column=0)
numeroRango = Entry(frameRango)
numeroRango.grid(row=4,column=0)
numeroRango.delete(0,END)
numeroRango.insert(0,31)

detenerLabel=Label(frameRango,text="Detener cuando el precio sea")
detenerLabel.grid(row=5,column=0)
numeroDetener = Entry(frameRango)
numeroDetener.grid(row=6,column=0)
numeroDetener.delete(0,END)
numeroDetener.insert(0,1000)



######FRAME CONTROLES########
    ## BOTON INICIAR
iniciar2 = Button(frameControles, text="Iniciar", command=iniciar, width=7, height=3)
iniciar2.grid(row=0,column=0)
    ##BOTON DETENER
finalizar = Button(frameControles, text="Detener", command=switchoff, width=7, height=3)
finalizar.grid(row=0,column=2)
    ##BUSCAR RANGO
# buscarRango2 = Button(frameControles, text="Buscar Rango", command=buscarRango, width=7, height=3)
# buscarRango2.grid(row=0,column=3)

##### FRAME OPCIONES #######
    ## CHECKBOX
        ## LIMPIAR COMPRADOS
r=IntVar()
r.set("1")
radio=Radiobutton(frameOpciones, text="Limpiar Comprados", variable=r, value=1)
        ## ESPERAR SEGUNDOS
radio2=Radiobutton(frameOpciones, text="Esperar 'S' segundos", variable=r, value=2)
radio.grid(row=0,column=0)
radio2.grid(row=1,column=0)
    ## NUMERO DE INTERVALOS
labelInvervalo=Label(frameOpciones,text="N")
labelInvervalo.grid(row=0,column=1)
itera = Entry(frameOpciones)
itera.grid(row=0,column=2)
itera.delete(0,END)
itera.insert(0,10)
    ## NUMERO DE INTERVALOS
labelSegundos=Label(frameOpciones,text="S")
labelSegundos.grid(row=1,column=1)
segundos = Entry(frameOpciones)
segundos.grid(row=1,column=2)
segundos.delete(0,END)
segundos.insert(0,45)


##### FRAME COMPRAVENTA  #####
    #### COMPRA
Compra=Label(frameCompraVenta,text="COMPRAS")
Compra.grid(row=1,column=2)
    #### PRECIO COMPRA
labelMaximo=Label(frameCompraVenta,text="Precio Compra")
labelMaximo.grid(row=2,column=0)
maximo = Entry(frameCompraVenta)
maximo.grid(row=2,column=2)
    #### VENTA
Venta=Label(frameCompraVenta,text="VENTA")
Venta.grid(row=3,column=2)
    ### PRECIO INICIAL
labelMinimo=Label(frameCompraVenta,text="Precio Inicial")
labelMinimo.grid(row=4,column=0)
inicial = Entry(frameCompraVenta)
inicial.grid(row=4,column=2)
    ### PRECIO FINAL
labelMaximo=Label(frameCompraVenta,text="Precio Final")
labelMaximo.grid(row=4,column=3)
final = Entry(frameCompraVenta)
final.grid(row=4,column=4)



root.mainloop()