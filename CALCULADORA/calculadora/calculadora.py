from sympy import symbols, diff, integrate, sympify
from tkinter import *
from PIL import Image, ImageTk

def calcular_derivada(expresion, variable):
    x = symbols(variable)
    derivada = diff(expresion, x)
    return derivada

def calcular_integral(expresion, variable, limite_inferior=None, limite_superior=None):
    x = symbols(variable)
    funcion = sympify(expresion)
    integral_indefinida = integrate(funcion, x)
    
    if limite_inferior is not None and limite_superior is not None:
        integral_definida = integrate(funcion, (x, limite_inferior, limite_superior))
        return integral_definida
    else:
        return integral_indefinida

def derivada():
    expresion = funcion.get()
    variable = variable_entry.get()
    try:
        derivada_resultado = calcular_derivada(expresion, variable)
        resultado_label.configure(text="Resultado: " + str(derivada_resultado))
    except:
        resultado_label.configure(text="Error: Ingresa la expresión y variable correctamente")

def integral():
    expresion = funcion.get()
    variable = variable_entry.get()
    limite_inferior = limite_inferior_entry.get()
    limite_superior = limite_superior_entry.get()
    try:
        if limite_inferior and limite_superior:
            resultado = calcular_integral(expresion, variable, float(limite_inferior), float(limite_superior))
        else:
            resultado = calcular_integral(expresion, variable)
        resultado_label.configure(text="Resultado: " + str(resultado) + " + C")
    except:
        resultado_label.configure(text="Error: Ingresa la expresión, variable y límites correctamente")

ventana = Tk()
ventana.geometry('700x650')  # Se ajustó el tamaño de la ventana
ventana.title("Cálculo Diferencial e Integral")

# Configuración del fondo de la ventana
fondo_color = 'lightgreen'  # Se cambió el color del fondo a verde
ventana.configure(bg=fondo_color)

# Texto "CALCULADORA"
texto_calculadora = Label(ventana, text="CALCULADORA", font=("Verdana", 20, "bold"), bg=fondo_color)
texto_calculadora.grid(row=0, column=0, columnspan=2, pady=10)

# Configuración de la imagen
fondo_img = Image.open("fet.jpg")
fondo_img = fondo_img.resize((200, 200), Image.ANTIALIAS)  # Se ajustó el tamaño de la imagen
fondo_img = ImageTk.PhotoImage(fondo_img)
fondo_label = Label(ventana, image=fondo_img, bg=fondo_color)
fondo_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Sección de entrada y botones
anuncio = Label(ventana, text="Expresión:", font=("Verdana", 14), bg=fondo_color)
anuncio.grid(row=2, column=0, padx=10, pady=5, sticky=E)

funcion = Entry(ventana, font=("Verdana", 14), width=30)  # Se ajustó el tamaño del campo de entrada
funcion.grid(row=2, column=1, padx=10, pady=5, sticky=W)

anuncio_variable = Label(ventana, text="Variable:", font=("Verdana", 14), bg=fondo_color)
anuncio_variable.grid(row=3, column=0, padx=10, pady=5, sticky=E)

variable_entry = Entry(ventana, font=("Verdana", 14), width=30)  # Se ajustó el tamaño del campo de entrada
variable_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

limite_inferior_label = Label(ventana, text="Límite inferior (opcional):", font=("Verdana", 14), bg=fondo_color)
limite_inferior_label.grid(row=4, column=0, padx=10, pady=5, sticky=E)

limite_inferior_entry = Entry(ventana, font=("Verdana", 14), width=30)  # Se ajustó el tamaño del campo de entrada
limite_inferior_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

limite_superior_label = Label(ventana, text="Límite superior (opcional):", font=("Verdana", 14), bg=fondo_color)
limite_superior_label.grid(row=5, column=0, padx=10, pady=5, sticky=E)

limite_superior_entry = Entry(ventana, font=("Verdana", 14), width=30)  # Se ajustó el tamaño del campo de entrada
limite_superior_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

boton_derivar = Button(ventana, text="Calcular Derivada", font=("Verdana", 14), command=derivada, bg='sky blue', fg='black')
boton_derivar.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

boton_integral = Button(ventana, text="Calcular Integral", font=("Verdana", 14), command=integral, bg='sky blue', fg='black')
boton_integral.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

resultado_label = Label(ventana, text="Resultado:", font=("Verdana", 14), bg=fondo_color)
resultado_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

ventana.mainloop()
