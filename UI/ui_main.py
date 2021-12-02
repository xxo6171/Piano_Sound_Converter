from tkinter import *
from tkinter import filedialog

def browsefile() :
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/", title="choose your file", filetypes=(("wav", "*.wav"),))
    la_url["text"] = root.filename
    btn_convert['state'] = NORMAL

def convert() :
    from ui_convert import UI_PSC
    global note
    global pernote
    note, pernote = UI_PSC(la_url["text"])
    la_midi["text"] = "output.mid"
    btn_play['state'] = NORMAL
    btn_save['state'] = NORMAL
    return note, pernote

def play() :
    from ui_convert import return_score
    from output_midi import midi_play
    sc = return_score(note, pernote)
    midi_play(sc)

def save() :
    from ui_convert import return_score
    from output_midi import midi_save
    sc = return_score(note, pernote)
    midi_save(sc, 'C:/Users/kyung/Desktop/output.mid')

root = Tk()
root.title("Piano Sound Converter")
w = 300
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

btn_find = Button(root, text="browse file", width=15, command=browsefile)
btn_find.pack(padx=0,pady=10)

la_url = Label(root,text="")
la_url.pack(padx=0,pady=10)

btn_convert = Button(root, text="convert", width=15, command=convert, state=DISABLED)
btn_convert.pack(padx=0,pady=10)

la_midi = Label(root,text="")
la_midi.pack(padx=0,pady=10)

btn_play = Button(root, text="play", width=15, command=play, state=DISABLED)
btn_save = Button(root, text="save", width=15, command=save, state=DISABLED)
btn_play.pack(padx=0,pady=10)
btn_save.pack(padx=0,pady=10)

root.mainloop()