"#Python-projects" 
import tkinter as tk
import json
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        lista_task.insert(tk.END, f"->{task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warging', "Você deve digitar uma tarefa!")

def delete_task():
    try:
        selecionar_index_task = lista_task.curselection()[0]
        lista_task.delete(selecionar_index_task)
    except IndexError:
        messagebox.showwarning("Warning", "Você deve selecionar uma tarefa")

def mark_task_completed():
    try:
        selecionar_index_task = lista_task.curselection()[0]
        task = lista_task.get(selecionar_index_task)
        lista_task.delete(selecionar_index_task)
        lista_task.insert(tk.END, f'✔{task}')
    except:
        messagebox.showwarning('Warning', 'Você deve selecionar uma tarefa')

def save_tasks():
    tasks = lista_task.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                lista_task.insert(tk.END, task)
    except FileNotFoundError:
        pass    
    
def on_closing():
    save_tasks()
    tela.destroy()        
    
# Modelo gráfico
tela = tk.Tk()
tela.title("Lista de Tarefas")
tela.geometry("400x400")

task_entry = tk.Entry(tela, width=30)
task_entry.pack(pady=10)

adicionar_task_botao = tk.Button(tela, text='Adicionar Tarefa', command=add_task)
adicionar_task_botao.pack(pady=5)

lista_task = tk.Listbox(tela, width=40, height=15)
lista_task.pack(pady=5)

deletar_task = tk.Button(tela, text='Deletar Tarefa',command=delete_task)
deletar_task.pack(pady=5)

marcar_task_cumprida = tk.Button(tela, text='Marcar tarefa como concluída',command=mark_task_completed)
marcar_task_cumprida.pack(pady=5)

load_tasks()

tela.protocol('WM_DELETE_WINDOW', on_closing)

# define o loop da aplicação
tela.mainloop()