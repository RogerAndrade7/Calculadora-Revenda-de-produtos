#Este programa calcula valores de revenda de produtos usando a fórmula definida em def revenda_calculo()

import customtkinter as ctk
import locale

#Defini as configurações de aparência do Programa.
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def revenda_calculo(): # Função para calcular o preço de revenda.
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') #Configurar a localização para o formato que utiliza vírgula como separador decimal
    valor_produto = locale.atof(valor_produto_caixa.get())
    valor_imposto = locale.atof(valor_imposto_caixa.get())
    valor_taxa = locale.atof(valor_taxa_caixa.get())    
    valor_imposto2 = valor_produto * (1+ valor_imposto/100)
    valor_revenda = (valor_imposto2 * (1+ valor_taxa/100))*1.5
    resultado.configure(text=f"O valor para revenda é: R$ {valor_revenda:.2f}") #Configura o command para executar o programa.

#Configurações para abrir a Janela.
janela = ctk.CTk()
janela.geometry("500x300")
janela.title("Calculadora Revenda")

texto = ctk.CTkLabel(janela, text="Calcule o valor de revenda") # Exibe o texto na tela.
#Recebe os valores para o cálculo.
valor_produto_caixa = ctk.CTkEntry(janela, placeholder_text="Valor do produto")
valor_imposto_caixa = ctk.CTkEntry(janela, placeholder_text="Valor do imposto")
valor_taxa_caixa = ctk.CTkEntry(janela, placeholder_text="Valor da taxa")
botao = ctk.CTkButton(janela, text="Calcular", command=revenda_calculo)# Define o botão.
resultado = ctk.CTkLabel(janela)# Exibe o valor do resultado.

# Configuração do tamanho das label e entry; botão e o resultado.
texto.pack(padx=10, pady=10)
valor_produto_caixa.pack(padx=10, pady=10)
valor_imposto_caixa.pack(padx=10, pady=10)
valor_taxa_caixa.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
resultado.pack(padx=10, pady=10)

janela.mainloop()# Faz com que responda aos comandos do usuário.