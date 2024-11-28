import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

def mark_complete():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, task + " (complète)")
    except IndexError:
        pass

# Création de la fenêtre principale
root = tk.Tk()
root.title("ToDo List")

# Champ d'entrée pour ajouter une tâche
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Bouton pour ajouter une tâche
add_button = tk.Button(root, text="Ajouter une tâche", command=add_task)
add_button.pack()

# Liste des tâches
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Bouton pour supprimer une tâche
delete_button = tk.Button(root, text="Supprimer la tâche sélectionnée", command=delete_task)
delete_button.pack()

# Bouton pour marquer une tâche comme complète
complete_button = tk.Button(root, text="Marquer comme complète", command=mark_complete)
complete_button.pack()

root.mainloop()