import tkinter as tk

class JogoChapeuSeletor:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo do Chapéu Seletor")

        self.perguntas = [
            "Pergunta 1: Qual é a sua cor favorita?",
            "Pergunta 2: Qual é o seu animal favorito?",
            "Pergunta 3: Qual é o seu hobby preferido?",
            "Pergunta 4: Qual é a sua matéria favorita?",
            "Pergunta 5: Qual é o seu objetivo na vida?"
        ]

        self.respostas = [
            ["Vermelho", "Azul", "Amarelo", "Verde"],
            ["Leão", "Águia", "Texugo", "Serpente"],
            ["Jogar esportes", "Ler livros", "Cozinhar", "Assistir filmes"],
            ["Transfiguração", "Defesa Contra as Artes das Trevas", "Herbologia", "Poções"],
            ["Aventura", "Sabedoria", "Paz", "Poder"]
        ]

        self.respostas_corretas = ['a', 'b', 'c', 'd', 'a']
        self.pontuacao = 0
        self.pergunta_atual = 0

        self.label_pergunta = tk.Label(self.janela, text=self.perguntas[self.pergunta_atual])
        self.label_pergunta.pack()

        self.var_resposta = tk.StringVar()

        for i, resposta in enumerate(self.respostas[self.pergunta_atual]):
            radio_button = tk.Radiobutton(self.janela, text=resposta, variable=self.var_resposta, value=chr(ord('a') + i))
            radio_button.pack()

        self.botao_responder = tk.Button(self.janela, text="Responder", command=self.verificar_resposta)
        self.botao_responder.pack()

        self.janela.mainloop()

    def verificar_resposta(self):
        resposta = self.var_resposta.get().lower()

        if resposta == self.respostas_corretas[self.pergunta_atual]:
            self.pontuacao += 1

        self.pergunta_atual += 1

        if self.pergunta_atual < len(self.perguntas):
            self.atualizar_pergunta()
        else:
            self.mostrar_resultado()

    def atualizar_pergunta(self):
        self.label_pergunta.config(text=self.perguntas[self.pergunta_atual])
        self.var_resposta.set("")

        for widget in self.janela.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        for i, resposta in enumerate(self.respostas[self.pergunta_atual]):
            radio_button = tk.Radiobutton(self.janela, text=resposta, variable=self.var_resposta, value=chr(ord('a') + i))
            radio_button.pack()

    def mostrar_resultado(self):
        self.label_pergunta.config(text="Parabéns! Você foi selecionado para a casa de Hogwarts.")
        self.var_resposta.set("")

        for widget in self.janela.winfo_children():
            widget.destroy()

        imagem_path = ""

        if self.pontuacao == 0:
            imagem_path = "D:\PYCHARM\PyCharm Community Edition 2022.2.1\jbr\bin\d\chapeuseletorgame\sonserina.gif"
        elif self.pontuacao == 1:
            imagem_path = "D:\PYCHARM\PyCharm Community Edition 2022.2.1\jbr\bin\d\chapeuseletorgame\grifinoria.gif"
        elif self.pontuacao == 2:
            imagem_path = "D:\PYCHARM\PyCharm Community Edition 2022.2.1\jbr\bin\d\chapeuseletorgame\lufa.gif"
        elif self.pontuacao == 3:
            imagem_path = "D:\PYCHARM\PyCharm Community Edition 2022.2.1\jbr\bin\d\chapeuseletorgame\corvinal.gif"
        elif self.pontuacao == 4:
            imagem_path = "D:\PYCHARM\PyCharm Community Edition 2022.2.1\jbr\bin\d\chapeuseletorgame\lufa.gif"

        imagem = tk.PhotoImage(file=imagem_path)
        label_imagem = tk.Label(self.janela, image=imagem)
        label_imagem.pack()

jogo = JogoChapeuSeletor()
