import random
import string
import tkinter as tk
from tkinter import messagebox

# Função para gerar senha
def gerar_senha():
    tam = int(entry_tam.get())    # Pega o tamanho da senha da entrada
    usar_maius = var_maius.get()  # Verifica se usa maiúsculas
    usar_minus = var_minus.get()  # Verifica se usa minúsculas
    usar_num = var_num.get()      # Verifica se usa números
    usar_simb = var_simb.get()    # Verifica se usa símbolos

    # Junta os tipos de caracteres escolhidos
    chars = ""
    if usar_maius:
        chars += string.ascii_uppercase
    if usar_minus:
        chars += string.ascii_lowercase
    if usar_num:
        chars += string.digits
    if usar_simb:
        chars += string.punctuation

    # Verifica se ao menos um tipo foi selecionado
    if not chars:
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere!")
        return

    # Gera a senha
    senha = ''.join(random.choice(chars) for _ in range(tam))
    entry_senha.delete(0, tk.END)   # Limpa a entrada de senha
    entry_senha.insert(0, senha)    # Exibe a senha gerada

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("300x300")

# Tamanho da senha
tk.Label(janela, text="Tamanho da senha:").pack()
entry_tam = tk.Entry(janela)
entry_tam.insert(0, "12")  # Valor padrão
entry_tam.pack()

# Tipos de caracteres
var_maius = tk.BooleanVar(value=True)
tk.Checkbutton(janela, text="Incluir maiúsculas", variable=var_maius).pack()

var_minus = tk.BooleanVar(value=True)
tk.Checkbutton(janela, text="Incluir minúsculas", variable=var_minus).pack()

var_num = tk.BooleanVar(value=True)
tk.Checkbutton(janela, text="Incluir números", variable=var_num).pack()

var_simb = tk.BooleanVar(value=True)
tk.Checkbutton(janela, text="Incluir símbolos", variable=var_simb).pack()

# Botão de gerar senha
tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

# Campo para exibir a senha gerada
tk.Label(janela, text="Senha gerada:").pack()
entry_senha = tk.Entry(janela, font=("Arial", 12))
entry_senha.pack()

# Inicia o programa
janela.mainloop()