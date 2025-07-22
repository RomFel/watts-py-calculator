from tkinter import *

class WattPyCalculator:
    def __init__(self):
        self.jan = Tk()
        self.config()
        self.widgets(self.calcular)
         
        self.jan.mainloop()

    def config(self):
        self.jan.title('WattPy Calculator')
        self.jan.geometry('300x300')
        self.jan.config(bg='black')
    
    def widgets(self, calcular):
        # Título > linha 0
        lb_titulo = Label(self.jan, text='⚡️WattPy Calculator⚡️', fg='yellow', bg='black', font=('Arial', 20))
        lb_titulo.grid(row=0, column=0, columnspan=2, pady=20)
        # Aparelho  > linha 1
        lb_aparelho = Label(self.jan, text='Aparelho:', fg='yellow', bg='black')
        lb_aparelho.grid(row=1, column=0)
        self.et_aparelho = Entry(self.jan)
        self.et_aparelho.grid(row=1, column=1)
        # Unidades > linha 2
        lb_unidades = Label(self.jan, text='unidades:', fg='yellow', bg='black')
        lb_unidades.grid(row=2, column=0)
        self.et_unidades = Entry(self.jan)
        self.et_unidades.grid(row=2, column=1)
        # Watts > linha 3
        lb_watts = Label(self.jan, text='Watts:', fg='yellow', bg='black')
        lb_watts.grid(row=3, column=0)
        self.et_watts = Entry(self.jan)
        self.et_watts.grid(row=3, column=1)
        # horas > linha 4
        lb_horas = Label(self.jan, text='horas:', fg='yellow', bg='black')
        lb_horas.grid(row=4, column=0)
        self.et_horas = Entry(self.jan)
        self.et_horas.grid(row=4, column=1)
        # dias > linha 5
        lb_dias = Label(self.jan, text='dias:', fg='yellow', bg='black')
        lb_dias.grid(row=5, column=0)
        self.et_dias = Entry(self.jan)
        self.et_dias.grid(row=5, column=1)
        # botão > linha 6
        bt_calcular = Button(self.jan, text='calcular', bg='red', fg='white', command=calcular)
        bt_calcular.grid(row=6, column=0, columnspan=2, pady=20)
        # resultado
        self.lb_resultado = Label(self.jan, text=f'Consumo mensal\n0000 kWh')
        self.lb_resultado.grid(row=7, column=0, columnspan=2)

    def calcular(self):
        aparelho = self.et_aparelho.get()
        unidades = self.et_unidades.get()
        watts = self.et_watts.get()
        horas = self.et_horas.get()
        dias = self.et_dias.get()
        consumo_mensal = int(unidades)*int(watts)*int(horas)*int(dias)
        self.lb_resultado.config(text=f'Consumo mensal\n{consumo_mensal/1000} kWh')
        


if __name__ == "__main__":
    WattPyCalculator()