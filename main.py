import tkinter as tk
from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
        self.brush_size = 10
        self.brush_color = "black"

    def setUI(self):
        self.parent.title('Графический редактор')
        self.pack(fill=BOTH, expand=1)  # заполнение самого редактора        # BOTH-можно растягивать и по горизонтали и вертикали, expand-виджет заполняет все пространство
        self.columnconfigure(6, weight=1)
        # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1)  # То же самое для третьего ряда
        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)
        # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок,        # задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        # создали метку Color
        color_lab = Label(self, text="Color:")
        color_lab.grid(row=0, column=0, padx=6)
        # создаем кнопку КРАСННУЮ КНОПКУ
        red_btn = Button(self, text="Red", command=lambda:self.set_color("red"))
        red_btn.grid(row=0, column=1)

        blue_btn = Button(self, text="Blue", command = lambda:self.set_color("blue"))
        blue_btn.grid(row=0, column=2)

        green_btn = Button(self, text="Green", command = lambda:self.set_color("green"))
        green_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", command = lambda:self.set_color("black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", command = lambda:self.set_color("white"))
        white_btn.grid(row=0, column=5)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)

        two_btn = Button(self, text="Two", command = lambda:self.set_size(2))
        two_btn.grid(row=1, column=1)

        five_btn = Button(self, text="Five", command = lambda:self.set_size(5))
        five_btn.grid(row=1, column=2)

        seven_btn = Button(self, text="Seven",command = lambda:self.set_size(7))
        seven_btn.grid(row=1, column=3)

        ten_btn = Button(self, text="Ten", command = lambda:self.set_size(11))
        ten_btn.grid(row=1, column=4)

        twenty_btn = Button(self, text="Twenty", command = lambda:self.set_size(12))
        twenty_btn.grid(row=1, column=5)

        clear_btn = Button(self, text="Clear all", command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)
    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill = self.brush_color, outline = self.brush_color)
    def set_color(self, new_color):
        self.brush_color=new_color

    def set_size(self, new_size):
        self.brush_size = new_size



def main():
    root=Tk()
    root.geometry("1920x1080+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()





