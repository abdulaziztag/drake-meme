from tkinter import *
from time import sleep

tk = Tk()
tk.title('Akbarbek Umurzakov')
tk.geometry("750x750")

canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()


def DrawElipse(xc, yc, rx, ry):
    xk = 0
    yk = ry
    pk = ry ** 2 - rx ** 2 * ry + 1 / 4 * rx ** 2

    while ry ** 2 * xk < rx ** 2 * yk:
        if pk > 0:
            xk = xk + 1
            yk = yk - 1
            pk = pk + 2 * ry ** 2 * xk + ry ** 2 - 2 * rx ** 2 * yk

        else:
            xk = xk + 1
            pk = pk + 2 * ry ** 2 * xk + ry ** 2

        canvas.create_oval(xc + xk, yc + yk, xc + xk, yc + yk, fill="red")
        canvas.create_oval(xc + xk, yc - yk, xc + xk, yc - yk, fill="red")
        canvas.create_oval(xc - xk, yc + yk, xc - xk, yc + yk, fill="red")
        canvas.create_oval(xc - xk, yc - yk, xc - xk, yc - yk, fill="red")
    if ry ** 2 * xk >= rx ** 2 * yk:
        pk = ry ** 2 * (xk + 0.5) ** 2 + rx ** 2 * (yk - 1) ** 2 - rx ** 2 * ry ** 2
        while yk > 0:
            if pk > 0:
                yk = yk - 1
                pk = pk - 2 * rx ** 2 * yk + rx ** 2
            else:
                xk = xk + 1
                yk = yk - 1
                pk = pk - 2 * rx ** 2 * yk + rx ** 2 + 2 * ry ** 2 * xk

            canvas.create_oval(xc + xk, yc + yk, xc + xk, yc + yk, fill="red")
            canvas.create_oval(xc + xk, yc - yk, xc + xk, yc - yk, fill="red")
            canvas.create_oval(xc - xk, yc + yk, xc - xk, yc + yk, fill="red")
            canvas.create_oval(xc - xk, yc - yk, xc - xk, yc - yk, fill="red")


DrawElipse(50, 50, 50, 50)

"""ball = canvas.create_oval(0,0,50,50, fill="red")
xspeed = 1
yspeed = 0

while True:
    canvas.move(ball, xspeed, yspeed)
    tk.update()
    sleep(0.1)"""

tk.mainloop()