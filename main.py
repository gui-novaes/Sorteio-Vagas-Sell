import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def embaralhar():
    unidades_text = unidades_entry.get("1.0", tk.END).strip().splitlines()
    vagas_text = vagas_entry.get("1.0", tk.END).strip().splitlines()

    if len(unidades_text) != len(vagas_text):
        messagebox.showerror("Erro", "O número de unidades e vagas deve ser o mesmo.")
        return

    vagas_embaralhadas = vagas_text.copy()
    random.shuffle(vagas_embaralhadas)

    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "🍀 Resultado do Sorteio:\n\n")
    for unidade, vaga in zip(unidades_text, vagas_embaralhadas):
        resultado_text.insert(tk.END, f"Unidade: {unidade} -> Vaga: {vaga}\n")

# Paleta de cores
COR_PRINCIPAL = "#152C40"
COR_DESTAQUE = "#368ABF"
COR_VERDE = "#7DBF5E"
COR_TEXTO = "#FFFFFF"


# Interface
janela = tk.Tk()
janela.title("Sorteio de Vagas - Sell Adm")
janela.configure(bg=COR_PRINCIPAL)
janela.minsize(750, 550)
janela.geometry("900x600")

# Logo
try:
    logo_img = Image.open("logo-sell-bg.png")
    logo_img = logo_img.resize((120, 120))
    logo_tk = ImageTk.PhotoImage(logo_img)
    tk.Label(janela, image=logo_tk, bg=COR_PRINCIPAL).pack(pady=10)
except Exception as e:
    print("Erro ao carregar a logo:", e)

# Frame de inputs
frame_inputs = tk.Frame(janela, bg=COR_PRINCIPAL)
frame_inputs.pack(padx=20, pady=10, fill="both", expand=True)

# Coluna unidades
frame_unidades = tk.Frame(frame_inputs, bg=COR_PRINCIPAL)
frame_unidades.pack(side="left", padx=20, fill="both", expand=True)
tk.Label(frame_unidades, text="Unidades (uma por linha):", fg=COR_TEXTO, bg=COR_PRINCIPAL).pack()
unidades_entry = tk.Text(frame_unidades, height=15, width=30)
unidades_entry.pack()

# Coluna vagas
frame_vagas = tk.Frame(frame_inputs, bg=COR_PRINCIPAL)
frame_vagas.pack(side="right", padx=20, fill="both", expand=True)
tk.Label(frame_vagas, text="Vagas (uma por linha):", fg=COR_TEXTO, bg=COR_PRINCIPAL).pack()
vagas_entry = tk.Text(frame_vagas, height=15, width=30)
vagas_entry.pack()

# Botão
botao_frame = tk.Frame(janela, bg=COR_PRINCIPAL)
botao_frame.pack(pady=10)
btn = tk.Button(botao_frame, text="Embaralhar", command=embaralhar, width=25, bg=COR_VERDE, fg="white", font=("Arial", 12, "bold"))
btn.pack()

# Resultado
resultado_frame = tk.Frame(janela, bg=COR_PRINCIPAL)
resultado_frame.pack(padx=20, pady=10, fill="both", expand=True)
tk.Label(resultado_frame, text="🍀 Resultado do Sorteio:", fg=COR_TEXTO, bg=COR_PRINCIPAL, font=("Arial", 14, "bold")).pack()
resultado_text = tk.Text(resultado_frame, height=10, width=100)
resultado_text.pack()

janela.mainloop()