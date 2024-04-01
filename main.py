from pytube import YouTube
import os
import customtkinter


def SucessNote():
    texto2= customtkinter.CTkLabel(janela, text="Successfully Downloaded!!!", font=("Consolas", 15))
    texto2.pack()
    
def FailNote():
    texto2= customtkinter.CTkLabel(janela, text="Something Went Wrong Please Try Again....", font=("Consolas", 15))
    texto2.pack(padx=10, pady=10)

def Dowload(URL):
    yt = YouTube(URL) 
    try:
        print("\nDownloading....")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        SucessNote()
        print("\nSuccessfully Downloaded!!!\n")
    except:
        FailNote()
        print("\nSomething Went Wrong Please Try Again....\n")
        

janela = customtkinter.CTk()
janela.title("Music Downloader")
janela.geometry("500x300")
janela.minsize(500,300)


texto= customtkinter.CTkLabel(janela, font=("Consolas", 20),text="Music Download")
texto.pack(padx=20, pady=20)

URL = customtkinter.CTkEntry(janela,width=400, placeholder_text="Insert Link")
URL.pack(padx=50,pady=50)

botao = customtkinter.CTkButton(janela, text="Download", command=lambda: Dowload(URL.get()))
botao.pack(padx=10,pady=10)

janela.mainloop()
