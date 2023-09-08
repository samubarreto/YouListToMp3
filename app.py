from pytube import Playlist, YouTube
from unidecode import unidecode
import customtkinter
import os
  
class videoDownloader:
  def renameMp3(file):
    os.rename(file, f'{os.path.splitext(file)[0]}.mp3')
  
  def updateLabels(texto1:str, texto2:str, tamanho1:int, tamanho2:int, cor:str):
  
    global feedbackLabel1, feedbackLabel2, root
    
    feedbackLabel1.destroy()
    feedbackLabel2.destroy()
    
    feedbackLabel1 = customtkinter.CTkLabel(mainFrame, text = texto1, font=('Roboto', tamanho1, 'bold'), text_color = cor)
    feedbackLabel1.grid(columnspan=2, row=2)
    
    feedbackLabel2 = customtkinter.CTkLabel(mainFrame, text= texto2, font=('Roboto', tamanho2, 'bold'), text_color = cor)
    feedbackLabel2.grid(columnspan=2, row=3, pady=5)
    
    root.update()
  
  def downloader(link):

    try:
      playlist = Playlist(link)
      progress = 0; successes = 0; fails = 0

      for video in playlist.video_urls:
        progress += 1
        try:
          yt = YouTube(video)
          fileNameUnidecoded = unidecode(yt.title).replace('/','')
          stream = yt.streams.filter(only_audio=True).first()
          stream.download(output_path = f'{playlist.title}', filename = fileNameUnidecoded)
          
          videoDownloader.renameMp3(f'{playlist.title}\\{fileNameUnidecoded}')
          videoDownloader.updateLabels(f'Baixado: {yt.title}, por {yt.author}. {yt.views} views · ({progress}/{playlist.length}) ✅', '😎', 12, 50, 'green')

          successes += 1
          continue
          
        except Exception as erro:

          videoDownloader.updateLabels(f'Erro ao tentar baixar {yt.title} · ({progress}/{playlist.length}) ❌', str(erro), 12, 12, 'red')
          fails += 1

      videoDownloader.updateLabels(f'Downloads finalizados. Sucessos: {successes} · Erros: {fails}','😎', 12, 50, 'green')
            
    except Exception as erro:
      videoDownloader.updateLabels('Erro: Link inválido. Escolha um link de uma playlist pública do Youtube. ❌', '😭', 12, 50, cor = 'red')

if __name__ == '__main__':
  root = customtkinter.CTk()
  root.wm_title('YouList to mp3')

  customtkinter.set_appearance_mode('dark')
  customtkinter.set_default_color_theme('green')

  mainFrame = customtkinter.CTkFrame(root, corner_radius=20, border_width=2)
  mainFrame.place(relx=0.5, rely=0.5, anchor='center')

  h1 = customtkinter.CTkLabel(mainFrame, text='YouList to Mp3', text_color='white', font=('Roboto', 45, 'bold'))
  h1.grid(columnspan=2, row=0, pady=20)

  linkEntry = customtkinter.CTkEntry(mainFrame, placeholder_text='Cole o link da playlist aqui', font=('Roboto', 16), width=600, height=35)
  linkEntry.grid(column=0, row=1, padx=5)

  downloadButton = customtkinter.CTkButton(mainFrame, text='Baixar playlist', width=100, height=35, cursor='hand2', border_width=1, border_color='white', font=('Roboto', 20, 'bold'), command=lambda: videoDownloader.downloader(str(linkEntry.get())), fg_color=("black"))
  downloadButton.grid(column=1, row=1, padx=15)

  feedbackLabel1 = customtkinter.CTkLabel(mainFrame, text='Escolha um link de uma playlist pública do Youtube', font=('Roboto', 12, 'bold'), text_color='white')
  feedbackLabel1.grid(columnspan=2, row=2)

  feedbackLabel2 = customtkinter.CTkLabel(mainFrame, text='😎', font=('Roboto', 50, 'bold'), text_color='white')
  feedbackLabel2.grid(columnspan=2, row=3, pady=5)

  root.wm_minsize(1000, 450)
  root.mainloop()
