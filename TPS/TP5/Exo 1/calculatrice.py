import tkinter as tk

def append_to_expression(value):
    expression.set(expression.get() + str(value))

def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Erreur")

def clear():
    expression.set("")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice Basique")

expression = tk.StringVar()

# Champ d'entrée pour afficher l'expression
entry = tk.Entry(root, textvariable=expression, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Boutons de la calculatrice
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=20, pady=20, command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=20, pady=20, command=clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: append_to_expression(b))
    
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()