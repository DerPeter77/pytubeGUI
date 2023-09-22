from pytube import YouTube
import customtkinter
import time

# Variabeln
turndark = 0
downloadurl = ''
choiceofstream = 0
streamID = ''
streams = ''
mp4 = 0
audio = 0
onlymp4187 = 0
onlyaudio187 = 0
# Variabeln

# Methoden
def darkAndLight():
    print("switch toggled, current value: " + turndark.get())
    turndark187187 = int(turndark.get())
    if turndark187187 == 0:
        customtkinter.set_appearance_mode('dark')
        print('DarkMode')
    else:
        customtkinter.set_appearance_mode('light')
        print('LightMode')

def downloadbutton():
    print('DOWNLOADBUTTON')
    streamID = streamentry.get()
    global stream
    stream = yt.streams.get_by_itag(int(streamID))
    stream.download()

def printStreamList():
    print('Du hast folgendes eingegeben: ' + urlentry.get())
    global yt
    yt = YouTube(str(urlentry.get()), on_complete_callback=downloadComplete)
    print('Dieses Video wurde gefunden: ' + yt.title)
    textbox.delete("0.0", "end")  # delete all text
    if onlymp4187 == 1: #mp4Only == 1:
        textbox.insert("0.0", 'Du hast folgendes eingegeben: ' + urlentry.get() + '\nDieses Video wurde gefunden: ' + yt.title + 'Hier sind alle streams aufgelistet: ' + str(yt.streams.filter(file_extension='mp4')))  # insert at line 0 character 0
        print('mp4')
    elif onlyaudio187 == 1: #audioOnly == 1:
        textbox.insert("0.0", 'Du hast folgendes eingegeben: ' + urlentry.get() + '\nDieses Video wurde gefunden: ' + yt.title + 'Hier sind alle streams aufgelistet: ' + str(yt.streams.filter(only_audio=True)))  # insert at line 0 character 0
        print('audio')
    else:
        textbox.insert("0.0", 'Du hast folgendes eingegeben: ' + urlentry.get() + '\nDieses Video wurde gefunden: ' + yt.title + 'Hier sind alle streams aufgelistet: ' + str(yt.streams))  # insert at line 0 character 0
        #print('nothing')

def selectStream():
    streamID = streamentry.get()
    global stream
    stream = yt.streams.get_by_itag(int(streamID))

def downloadComplete():
    label1 = customtkinter.CTkLabel(app, text='DOWNLOAD FERTIG', width=35, height=35, corner_radius=15, fg_color='#27699c', text_color='white', font=('roboto', 26))
    label1.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'we')

def onlyMp4():
    print('onlyMp4')
    global onlymp4187
    onlymp4187 = int(mp4.get())
    print(onlymp4187)

def onlyAudio():
    print('onlyAudio')
    global onlyaudio187
    onlyaudio187 = int(audio.get())
    print(onlyaudio187)


# Ende Methoden

##############################################################################################################################################################################################################################################################

# Customtkinter init
app = customtkinter.CTk()
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("system")
app.title('YouTube Downloader')
app.geometry('900x800')
app.columnconfigure(0, weight = 1)
app.columnconfigure(1, weight = 1)
app.columnconfigure(2, weight = 1)
app.rowconfigure(0, weight = 1)
app.rowconfigure(1, weight = 1)
app.rowconfigure(2, weight = 10)
app.rowconfigure(3, weight = 10)
app.rowconfigure(4, weight = 10)
app.rowconfigure(5, weight = 10)

## Widgets ##

# DARK / LIGHT MODE
turndark = customtkinter.StringVar(value="on")
switchdarklight = customtkinter.CTkSwitch(app, text="DarkMode / LightMode", command=darkAndLight, variable=turndark, onvalue=1, offvalue=0)
switchdarklight.grid(row = 0, column = 2, padx = 30, pady = 10, sticky = 'ne')

# MP4 STREAMS ONLY
mp4 = customtkinter.StringVar(value=0)
onlymp4 = customtkinter.CTkSwitch(app, text="MP4 Streams", command=onlyMp4, variable=mp4, onvalue=1, offvalue=0)
onlymp4.grid(row = 1, column = 2, padx = 30, pady = 10, sticky = 'ne')

# AUDIO STREAMS ONLY
audio = customtkinter.StringVar(value=0)
onlyaudio = customtkinter.CTkSwitch(app, text="Audio Streams", command=onlyAudio, variable=audio, onvalue=1, offvalue=0)
onlyaudio.grid(row = 2, column = 2, padx = 30, pady = 10, sticky = 'ne')

# Youtube Video Downloader LABEL
label1 = customtkinter.CTkLabel(app, text='Youtube Video Downloader', width=35, height=35, corner_radius=15, fg_color='#27699c', text_color='white', font=('roboto', 26))
label1.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'we')

# URL Entry Field
urlentry = customtkinter.CTkEntry(app, placeholder_text='YouTube-URL', width=150, height=20, font=('roboto', 20), textvariable=downloadurl)
urlentry.grid(row = 1, column = 1, sticky = 'we')

# TEXTBOX
textbox = customtkinter.CTkTextbox(app, width=750, height=550)
textbox.grid(row = 2, column = 1, sticky = 'ew', padx = 10, pady = 10)

# SEARCH VIDEO AND GET STREAMS
searchvideo = customtkinter.CTkButton(app, text='Search', width=20, height=20, font=('roboto', 20), command=printStreamList)
searchvideo.grid(row = 3, column = 1, padx = 10, pady = 10)

# Stream ID Entry Field
streamentry = customtkinter.CTkEntry(app, placeholder_text='STREAM-ID', width=150, height=20, font=('roboto', 20), textvariable=streamID)
streamentry.grid(row = 4, column = 1, sticky = 'we')

# DOWNLOADBUTTON
download = customtkinter.CTkButton(app, text='Download', width=20, height=20, font=('roboto', 20), command=downloadbutton)
download.grid(row = 5, column = 1, padx = 10, pady = 10)

## Widgets ##


app.mainloop()
