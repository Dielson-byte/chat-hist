import tkinter as tk
import random
import time

def enviar_mensagem(event=None):
    mensagem = entrada.get()
    if mensagem.strip() != "":
        caixa_chat.config(state=tk.NORMAL)
        caixa_chat.insert(tk.END, "Você: " + mensagem + "\n", "eu")
        caixa_chat.config(state=tk.DISABLED)
        entrada.delete(0, tk.END)
        if mensagem.isdigit() and 1 <= int(mensagem) <= 10:
            tema_escolhido = int(mensagem)
            exibir_historia(tema_escolhido)

def exibir_historia(tema_escolhido):
    historia = obter_historia(tema_escolhido)
    exibir_letra_a_letra(historia)

def obter_historia(tema_escolhido):
    temas = {
        1: "A história da Internet remonta ao final da década de 1960, quando a ARPANET, a primeira rede de computadores, foi criada pelo Departamento de Defesa dos Estados Unidos. Desde então, a Internet evoluiu enormemente, tornando-se uma parte essencial da vida moderna. Ela conecta bilhões de dispositivos em todo o mundo, permitindo comunicação instantânea, acesso a informações e serviços online.",
        2: "A evolução dos computadores teve início no século XIX com máquinas mecânicas rudimentares, como a máquina analítica de Charles Babbage. No século XX, os computadores eletrônicos foram desenvolvidos, culminando no surgimento do computador pessoal na década de 1970. Desde então, os computadores se tornaram cada vez mais poderosos e onipresentes, desempenhando papéis fundamentais em quase todos os aspectos da sociedade moderna.",
        3: "A linguagem de programação Python foi criada por Guido van Rossum em 1991. Python é conhecido por sua sintaxe simples e legibilidade, tornando-o uma escolha popular para iniciantes em programação. Ao longo dos anos, Python se tornou uma das linguagens de programação mais populares do mundo, utilizada em uma variedade de campos, incluindo desenvolvimento web, análise de dados, inteligência artificial e muito mais.",
        4: "A história da Apple começou em 1976 com Steve Jobs, Steve Wozniak e Ronald Wayne, que fundaram a empresa na garagem de Jobs. A Apple lançou o Apple I em 1976, seguido pelo Apple II em 1977, que se tornou um dos primeiros computadores pessoais de sucesso. Desde então, a Apple lançou uma série de produtos inovadores, incluindo o Macintosh, iPod, iPhone e iPad, tornando-se uma das empresas mais valiosas do mundo.",
        5: "O Linux foi criado por Linus Torvalds em 1991 como um sistema operacional de código aberto baseado no Unix. Desde então, o Linux se tornou uma parte fundamental da infraestrutura de tecnologia em todo o mundo, alimentando servidores, dispositivos embarcados, supercomputadores e muito mais. Sua comunidade de desenvolvimento ativa e sua natureza de código aberto promovem a inovação contínua e a colaboração.",
        6: "A Microsoft foi fundada por Bill Gates e Paul Allen em 1975. A empresa lançou seu primeiro sistema operacional, o MS-DOS, em 1981, seguido pelo Windows em 1985. O Windows se tornou o sistema operacional dominante para computadores pessoais e é amplamente utilizado em todo o mundo. A Microsoft também desenvolveu uma ampla gama de produtos de software e serviços, incluindo o pacote Office, Azure e Xbox.",
        7: "A história do Facebook começou em 2004 em Harvard, quando Mark Zuckerberg e seus colegas de quarto lançaram uma plataforma de rede social chamada 'TheFacebook'. A plataforma rapidamente se expandiu para outras universidades e, eventualmente, para o público em geral. Hoje, o Facebook é a maior rede social do mundo, com bilhões de usuários ativos mensais.",
        8: "A história do Google começou em 1996 como um projeto de pesquisa de Larry Page e Sergey Brin na Universidade Stanford. Eles desenvolveram um algoritmo de pesquisa revolucionário, que se tornou a base do mecanismo de busca do Google. O Google foi fundado em 1998 e desde então expandiu-se para uma variedade de produtos e serviços, incluindo o Gmail, Google Maps, YouTube e Android.",
        9: "A evolução dos smartphones teve início na década de 1990 com dispositivos como o IBM Simon, que combinava funções de telefone celular com recursos de computador. O lançamento do iPhone pela Apple em 2007 marcou o início da era moderna dos smartphones, com dispositivos cada vez mais poderosos e recursos avançados. Hoje, os smartphones são uma parte essencial da vida cotidiana para bilhões de pessoas em todo o mundo.",
        10: "A história dos videogames remonta ao século XX, com os primeiros protótipos desenvolvidos em laboratórios de pesquisa. O boom dos videogames ocorreu na década de 1980, com o lançamento de consoles domésticos como o Atari 2600 e o Nintendo Entertainment System. Desde então, os videogames evoluíram rapidamente, passando de gráficos simples e jogabilidade básica para experiências complexas e imersivas em 3D."
    }
    return temas.get(tema_escolhido, "Desculpe, não consegui encontrar informações sobre esse tema.")

def exibir_letra_a_letra(texto):
    for letra in texto:
        caixa_chat.config(state=tk.NORMAL)
        caixa_chat.insert(tk.END, letra)
        caixa_chat.see(tk.END)
        caixa_chat.config(state=tk.DISABLED)
        caixa_chat.update()
        time.sleep(0.02)  # Ajuste o tempo de espera entre as letras aqui
        if letra == '\n':  # Adiciona uma pausa maior para quebra de linha
            time.sleep(0.5)

root = tk.Tk()
root.title("History Word")

# Definindo estilos
root.configure(bg="#000000")
root.iconphoto(False, tk.PhotoImage(file='PYTHON\img\icon.png'))  # Adicione um ícone personalizado

# Estilos de texto
caixa_chat = tk.Text(root, height=20, width=50, bg="#000000", fg="#00FF00", font=("Courier", 12), wrap="word")
caixa_chat.pack(pady=10)
caixa_chat.tag_configure("eu", foreground="#00FF00")
caixa_chat.tag_configure("bot", foreground="#FF0000")
caixa_chat.config(state=tk.DISABLED)

entrada = tk.Entry(root, width=50, bg="#000000", fg="#00FF00", font=("Courier", 12))
entrada.pack(pady=10)

enviar_button = tk.Button(root, text="Enviar", command=enviar_mensagem, bg="#000000", fg="#00FF00", font=("Courier", 12))
enviar_button.pack()

# Opções de tema
caixa_chat.config(state=tk.NORMAL)
caixa_chat.insert(tk.END, "Bot: Escolha um tema digitando um número de 1 a 10:\n1. História da Internet\n2. Evolução dos Computadores\n3. Python\n4. Apple\n5. Linux\n6. Microsoft\n7. Facebook\n8. Google\n9. Evolução dos Smartphones\n10. História dos Videogames\n", "bot")
caixa_chat.config(state=tk.DISABLED)

root.bind("<Return>", enviar_mensagem)
root.mainloop()
