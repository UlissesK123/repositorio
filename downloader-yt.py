import os
from tkinter import *
from pytube import YouTube
from tkinter import filedialog

#a funçao pack do tk serve para desenhar o objeto na tela
#o frame serve para criar o espaço para colocar as coisas na janela
#o label serve para escrever textos
#bd é a borda

def downloadAudio(url_):
    pasta = filedialog.askdirectory()
    audio = YouTube(url_).streams.get_audio_only().download(pasta)
    base, ext = os.path.splitext(audio)

    arquivo_novo = base + ".mp3"
    os.rename(audio, arquivo_novo)

    avisoFinal()

def avisoFinal():
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.geometry("200x200")
    Label(janela_msg, text="Download finalizado", font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()

janela = Tk()
janela.title("Downloader de música")

quadro = Frame(janela, pady=10, padx=10)
quadro.pack()

Label(quadro, text="Inserir url do video", font="arial 14").pack()
url = Entry(quadro, font="arial 12", width=75)
url.pack()
Button(quadro, text="Download", font="arial 13", width=10, height=1,background="#800000", bd=4, fg="white", command= lambda: downloadAudio(url.get())).pack(side="right")


janela.mainloop()