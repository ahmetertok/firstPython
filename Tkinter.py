import tkinter as tk


class Test():
    def __init__(self):



        self.root = tk.Tk()
        self.root.geometry('250x250')


        self.label = tk.Label(self.root, text="Merhaba grafik arayüz")
        self.label.place(x=60, y=40)


        self.button = tk.Button(self.root, text='Çik', command=self.quit)
        self.button.pack()
        self.button.place(x=80, y=70)

        self.root.mainloop()


    def quit(self):



         self.label.config(text="Hoşçakal grafik arayüz ...")
         self.button.config(text="Lütfen bekleyin...")
         self.root.after(2000, lambda: self.root.destroy())


app = Test()

