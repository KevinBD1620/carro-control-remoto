from tkinter import *
import serial #Se comunica con el Arduino 
import pygame #Leera el teclado cuando se pulse


ser = serial.Serial('COM12', 9600) #Comunicacion con el puerto COM8, debes cambiarlo por el tuyo.
def game():
    pygame.init() #Inicia pygame
    screen = pygame.display.set_mode((940, 540)) #Paremtros para dibujar una ventana
    fondo = pygame.image.load("principal.png").convert()
    tux = pygame.image.load("principal.png").convert_alpha()

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(tux, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()
    pygame.display.set_caption('Controlador')
    pygame.mouse.set_visible(1)
 
    val = '-'
 
    while val != 'stop':
        #Si se presiona alguna flecha se enviara un caracter por el puerto al que se conecte el Arduino 
        events = pygame.event.get()
        for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                            ser.write (str.encode("F"))
                    elif event.key == pygame.K_LEFT:
                            ser.write (str.encode("L"))
                    elif event.key == pygame.K_RIGHT:
                            ser.write(str.encode("R"))
                    elif event.key == pygame.K_DOWN:
                            ser.write(str.encode("B"))
                    elif event.key == pygame.K_ESCAPE:
                            val = 'stop'
                if event.type == pygame.KEYUP: #Si se deja de presionar una tecla envia la instrucción de parada por Serial.
                    ser.write(str.encode("S"))

def homescreen() :
    home=Frame(root,width=940,height=540)
    home.place(x=0,y=0)
    widget=Label(home,image=screenimage).place(x=0,y=0) #fondo
    back = Button(home,image=backbtn, bd=0, activebackground = "white",command = home.destroy ,bg="black"). place (x=230,y=100)
    front = Button(home,image=frontbtn, bd=0, activebackground = "white",command = home.destroy ,bg="black"). place (x=320,y=107)
    izq = Button(home,image=izqbtn, bd=0, activebackground = "white",command = home.destroy ,bg="black"). place (x=500,y=110)
    der = Button(home,image=derbtn, bd=0, activebackground = "white",command = home.destroy ,bg="black"). place (x=600,y=110)


root = Tk()
root.title=("GAME")
root.geometry("940x540+100+50")
root.configure(bg="black")
fondo=PhotoImage(file="fondo.png")
widget=Label(root,image=fondo).place(x=0,y=0) #fondo
PBoton=PhotoImage(file="botonplay.png")
Power=Button(root,image=PBoton, bd=0,command=game, activebackground = "black"). place (x=800,y=75)
screenimage=PhotoImage(file="principal.png")
backbtn=PhotoImage(file="stop.png")
frontbtn=PhotoImage(file="delanteras.png")
izqbtn=PhotoImage(file="izq.png")
derbtn=PhotoImage(file="der.png")
root.mainloop()
