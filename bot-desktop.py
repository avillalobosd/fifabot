from tkinter import *
from tkinter import ttk
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import threading  
switch = True  

os.system('clear')


opts = Options()
opts.add_experimental_option('debuggerAddress', 'localhost:9250')
driver = webdriver.Chrome(options=opts)
seguir = True
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
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/button[1]").click()


#######################################################################
#######################################################################
#######################################################################    
#######################################################################    


#######################################################################
####################################################################### 
############ PANTALLA 2 DE BUSQUEDA ###################################
#######################################################################
#######################################################################

#CLICK PRIMER ELEMENTO ENCONTRADO SOLO SI LO ENCUENTRA
def clickEncontrado():
    if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div")) > 0:
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div").click()
        print(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div/div[2]/div[3]/span[2]").text)
        pe=driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li/div/div[2]/div[3]/span[2]").text
        tablaLog.insert(parent="",index="end",text="parent",values=("Encontrado: "+pe))
        comprar()
    # else:
    #     print("NO SE ENCONTRO")
        

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
    saldoInicial=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]").click()
    if len(driver.find_elements_by_xpath("/html/body/div[4]/section/div/div/button[1]")) > 0:
        driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]").click()
        time.sleep(5)
        if float(driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text) != float(saldoInicial):
            print("SE COMPRO")
            # saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
            time.sleep(3)
            if len(driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")) > 0:
                ponerMercado()
                time.sleep(2)
                definirPrecio()
            else:
                print("ALGO SALIO MAL")
        else:
            print("NO SE COMPRO")
        time.sleep(5)
    else:
        print("FALSA ALARMA")


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
    tablaLog.insert(parent="",index="end",text="parent",values=("Iniciado" ))
    saldo=driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
    print(saldo)
    tablaLog.insert(parent="",index="end",text="parent",values=("SaldoActual:"+saldo))
    #TOMA PRECIO FINAL DE CAMPO 
    precioFinal=int(final.get()) 
    maximo.delete(0,END)
    maximo.insert(0,int(precioFinal/1.07))
    inicial.delete(0,END)
    inicial.insert(0,precioFinal-1000)
    print("GANANCIA MINIMA")
    print(float(precioFinal)*.95-int(maximo.get()))
    print(driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input").text)
    tablaLog.insert(parent="",index="end",text="parent",values=("Jugador:"+driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input").text.replace(" ", "")))
    
    gananciaMinima = "GananciaMinima:"+str(float(precioFinal)*.95-int(maximo.get()))
    # print(gananciaMinima)
    tablaLog.insert(parent="",index="end",text="parent",values=(gananciaMinima))

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
                global iteraciones
                iteraciones=iteraciones+1
                # print(iteraciones)
                if iteraciones==30:
                    print("ESPERANDO 45 SEGUNDOS")
                    time.sleep(45)
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
        except Exception:
            print("ALGO OCURRIO")  
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
    tablaLog.insert(parent="",index="end",text="parent",values=("Apagado") )

#######################################################################
####################################################################### 
############ INTERFAZ DE USUARIO ######################################
#######################################################################
#######################################################################

# root.geometry("400x600")
frame1 = LabelFrame(root, pady=10)
frame1.place(x=0, y=0, anchor="nw", width=450)
# frame1.grid(row=0,column=0)
frame2 = LabelFrame(root)
frame2.place(x=460, y=0, anchor="nw")

frameControles = LabelFrame(frame1, text="CONTROLES", padx=150, pady=5)
frameControles.grid(row=0,column=0)
frameCompraVenta= LabelFrame(frame1, text="COMPRAVENTA", padx=10)
frameCompraVenta.grid(row=1,column=0)
frameLog = LabelFrame(frame2)
frameLog.grid(row=0,column=0)
frameJugadores = LabelFrame(root)


## BOTON INICIAR
iniciar = Button(frameControles, text="Iniciar", command=iniciar, width=7, height=3)
iniciar.grid(row=0,column=0)
## BOTON FINALIZAR
finalizar = Button(frameControles, text="Detener", command=switchoff, width=7, height=3)
finalizar.grid(row=0,column=1)


###################### COMPRA
Compra=Label(frameCompraVenta,text="COMPRAS")
Compra.grid(row=1,column=2)

labelMaximo=Label(frameCompraVenta,text="Precio Compra")
labelMaximo.grid(row=2,column=0)

maximo = Entry(frameCompraVenta)
maximo.grid(row=2,column=2)

##################### VENTA
Venta=Label(frameCompraVenta,text="VENTA")
Venta.grid(row=3,column=2)

labelMinimo=Label(frameCompraVenta,text="Precio Inicial")
labelMinimo.grid(row=4,column=0)

inicial = Entry(frameCompraVenta)
inicial.grid(row=4,column=2)

labelMaximo=Label(frameCompraVenta,text="Precio Final")
labelMaximo.grid(row=4,column=3)

final = Entry(frameCompraVenta)
final.grid(row=4,column=4)

## LOG
tablaLog = ttk.Treeview(frameLog)
tablaLog['columns'] = ("Evento")
tablaLog.column("#0", width=0)
tablaLog.column("Evento", anchor=W, width=300)
# tablaLog.heading("#0", text="Label", anchor=W)
tablaLog.heading("Evento", text="Evento")

tablaLog.pack()

# tablaLog.insert(parent="",index='end',iid=0,text="parent",values=("OK") )


root.mainloop()