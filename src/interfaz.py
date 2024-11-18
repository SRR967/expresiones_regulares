import tkinter as tk
from tkinter import messagebox
from core.analizador import AnalizadorLexico
from core.motor_validacion import MotorDeValidacion
from core.generador_automata import GeneradorDeAutomatas

class InterfazUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Expresiones Regulares")

        # Campo de entrada para la expresión regular
        tk.Label(root, text="Expresión Regular:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_expresion = tk.Entry(root, width=40)
        self.entry_expresion.grid(row=0, column=1, padx=10, pady=5)

        # Campo de entrada para las cadenas
        tk.Label(root, text="Cadenas a Validar (separadas por coma):").grid(row=1, column=0, padx=10, pady=5)
        self.entry_cadenas = tk.Entry(root, width=40)
        self.entry_cadenas.grid(row=1, column=1, padx=10, pady=5)

        # Botón para iniciar la validación
        self.btn_validar = tk.Button(root, text="Validar", command=self.validar_expresion)
        self.btn_validar.grid(row=2, column=0, columnspan=2, pady=10)

        # Área de texto para mostrar resultados
        self.text_resultado = tk.Text(root, width=60, height=15)
        self.text_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Boton para ver el automata
        self.btn_generar_automata = tk.Button(root, text="Generar Autómata", command=self.mostrar_automata)
        self.btn_generar_automata.grid(row=4, column=0, columnspan=2, pady=10)

    def validar_expresion(self):
        # Obtener la expresión y las cadenas
        expresion = self.entry_expresion.get()
        cadenas = self.entry_cadenas.get().split(',')

        # Verificar que la expresión no esté vacía o solo contenga espacios
        if not expresion.strip():
            messagebox.showerror("Error", "La expresión regular no puede estar vacía o solo contener espacios.")
            # Limpiar el área de resultados
            self.text_resultado.delete(1.0, tk.END)
            return

        # Verificar que cada cadena no esté vacía
        for cadena in cadenas:
            if cadena=="":
                messagebox.showerror("Error", "Las cadenas a validar no pueden estar vacías o solo contener espacios.")
                #Limpiar el área de resultados
                self.text_resultado.delete(1.0, tk.END)
                return


        # Limpiar el área de resultados
        self.text_resultado.delete(1.0, tk.END)

        # Crear y analizar la expresión con AnalizadorLexico
        analizador = AnalizadorLexico(expresion)
        analizador.analizar()

        # Verificar si hay errores en la expresión
        if analizador.obtener_errores():
            errores = "\n".join(analizador.obtener_errores())
            self.text_resultado.insert(tk.END, f"Errores en la expresión:\n{errores}\n")
            messagebox.showerror("Error", "Expresión regular inválida.")
            return

        # Mostrar los tokens generados
        tokens = analizador.obtener_tokens()
        self.text_resultado.insert(tk.END, "Tokens generados:\n")
        for tipo, valor in tokens:
            self.text_resultado.insert(tk.END, f"{tipo}: '{valor}'\n")

        # Validar cada cadena con MotorDeValidacion
        motor = MotorDeValidacion(expresion)
        resultados = motor.validar_multiples_cadenas(cadenas)

        # Mostrar los resultados de validación
        self.text_resultado.insert(tk.END, "\nResultados de Validación:\n")
        for cadena, es_valido in resultados.items():
            if es_valido:
                resultado = "válida"
            else: 
                resultado = "inválida"
            
            self.text_resultado.insert(tk.END, f"{cadena.strip()}: {resultado}\n")
        
        # Mostrar errores de validación si existen
        if motor.obtener_errores():
            errores = "\n".join(motor.obtener_errores())
            self.text_resultado.insert(tk.END, f"\nErrores durante la validación:\n{errores}\n")

    def mostrar_automata(self):
        # Obtener la expresión regular
        expresion = self.entry_expresion.get()
        #Eliminar los espacios
        expresion = expresion.replace(" ","")
        if not expresion.strip():
            messagebox.showerror("Error", "La expresión regular no puede estar vacía.")
            return

        # Analizar tokens
        analizador = AnalizadorLexico(expresion)
        analizador.analizar()
        if analizador.obtener_errores():
            messagebox.showerror("Error", "Expresión regular inválida.")
            return

        # Obtener tokens generados por el analizador
        tokens = analizador.obtener_tokens()

        # Crear el generador de autómatas
        generador = GeneradorDeAutomatas()

        # Generar el AFND y convertirlo a AFD
        try:
            afnd = generador.construir_grafo_desde_tokens(tokens)  # Generar el AFND
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al construir el autómata: {e}")
            return

        # Mostrar el AFD en una nueva ventana
        ventana_automata = tk.Toplevel(self.root)
        ventana_automata.title("Visualización del Autómata Determinista (AFD)")
        label = tk.Label(ventana_automata, text="Autómata Finito Determinista (AFD):")
        label.pack()
        canvas = tk.Canvas(ventana_automata, width=800, height=600)
        canvas.pack()

        # Generar y visualizar el AFD con Graphviz
        dot = afnd.visualizar()  # Visualizar el AFD
        dot.render("automata_determinista", format="png", cleanup=True)
        img = tk.PhotoImage(file="automata_determinista.png")
        canvas.create_image(400, 300, image=img)
        canvas.image = img


