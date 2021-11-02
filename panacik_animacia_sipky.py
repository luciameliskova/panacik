import tkinter

okno = tkinter.Tk()
platno = tkinter.Canvas(okno, width = 600, height = 600)
platno.pack()


#definujeme zaciatocne suradnice nasej kacky
#x je vzdialenost od lava
#y je vzdialenost od hora
x = 300
y = 300


#nacitame frames naseho gifu
kacka1 = tkinter.PhotoImage (file = "duck.gif", format="gif -index 0")
kacka2 = tkinter.PhotoImage (file = "duck.gif", format="gif -index 1")
kacka3 = tkinter.PhotoImage (file = "duck.gif", format="gif -index 2")


#image_id nam vytvori kacku1 na platne na pozicii 300, 300
image_id = platno.create_image(300, 300, image = kacka1)
current_image1 = kacka1
current_image2 = kacka2


#definujeme funkciu, ktora vymeni frames
def swap_frames1():
    global image_id, current_image1, current_image2
    x, y = platno.coords(image_id)
    platno.delete(image_id)
    image_id = platno.create_image(x, y, image = current_image2)
    current_image1, current_image2 = current_image2, current_image1


#definujeme funkciu, ktora pocunie obrazok pri stlaceni sipky ny klavensnici
#pridame tam aj funkciu swap_frames
def sipka (event):
    if event.keysym == "Right":
        platno.move(image_id, 20, 0)
        swap_frames1()
    elif event.keysym == "Left":
        platno.move(image_id, -20, 0)
        swap_frames1()
    elif event.keysym == "Down":
        platno.move(image_id, 0, 20)
        swap_frames1()
    elif event.keysym == "Up":
        platno.move(image_id, 0, -20)
        swap_frames1()



#zavolame funkciu sipka ktora bude posuvat obrazok image_id po platne
#pri stlaceni sipky na klavesnici
platno.bind_all("<KeyPress-Up>", sipka)
platno.bind_all("<KeyPress-Down>", sipka)
platno.bind_all("<KeyPress-Left>", sipka)
platno.bind_all("<KeyPress-Right>", sipka)





platno.mainloop()
