from tkinter import *
from tkinter.filedialog import *
import fileinput,csv,sys,codecs
from tkinter import messagebox as tkMessageBox
from PIL import ImageTk, Image

root = Tk()
root.title("G2P")
root.geometry("500x600-400+50")

inputfile=""
textfile=""


mydict=dict()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def loadLex():
    # try:
        filenames = askopenfilenames()
        global file
        for file in filenames:
            with open(file, mode='r') as infile:
                reader = csv.reader(infile)
                global mydict
                mydict = {rows[0]: rows[1] for rows in reader}
                mydict = {key: val for key, val in mydict.items() if val != "N/A"}
                Llexiconv.set("Lexicon: "+str(file))
                if (not ((Lfilev.get().__eq__("Missing text file")) or (
                Llexiconv.get().__eq__("Missing lexicon file")))):
                    LReadyv.set("Ready")
                    saveButton.pack(side=LEFT)
                else:
                    LReadyv.set("Pending proccess...")
                    saveButton.pack_forget()
    # except:
    #     Llexiconv.set("Missing lexicon file")
    #     saveButton.pack_forget()
    #     LReadyv.set("Pending proccess...")
    #     pass

def importFiles():
    try:
        filenames = askopenfilenames()
        global file
        for file in filenames:
            global textfile
            textfile=str(file)
            Lfilev.set("Text file: "+str(file))
        if (not ((Lfilev.get().__eq__("Missing text file")) or (Llexiconv.get().__eq__("Missing lexicon file")))):
            LReadyv.set("Ready")
            saveButton.pack(side=LEFT)
        else:
            LReadyv.set("ending proccess...")
            saveButton.pack_forget()

    except:
        Lfilev.set("Missing text file")
        saveButton.pack_forget()
        LReadyv.set("Pending proccess...")
        pass



def saveFile():
    # try:
        global textfile
        global mydict
        for w in (saveButton,lexButton,textButton):
            w.config(state=DISABLED)

        f = asksaveasfile(mode='w',title="Choose transcription file", defaultextension=".txt")
        #f2=f= open("log.txt","w+")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return

        #textfile = codecs.open(textfile, "w", "utf-8")
        with fileinput.FileInput(textfile, backup='.bak', openhook=fileinput.hook_encoded("utf-8"), ) as file:
            for line in file:
                print(type(line))
                words = line.split()
                transcriptions = [mydict[word] for word in words if word in mydict]
                line_transcription = ' '.join(transcriptions)
                print(line_transcription)
         #       f2.write(line.encode("UTF-8"))

                f.write(line_transcription)
                f.write('\n')
        f.close()


        for w in (saveButton,lexButton,textButton):
            w.config(state=NORMAL)
        tkMessageBox.showinfo("Notification", "G2P Completed")
    # except:
    #     pass

# listFrame = Frame(root)
# listFrame.pack()
#
# sby = Scrollbar(listFrame, orient='vertical')
# sby.pack(side=RIGHT, fill=Y)

# fileList = Listbox(listFrame, width=100, height=5, yscrollcommand=sby.set)
# fileList.pack()

# sby.config(command=fileList.yview)

Title = Label(root, text="Grapheme to phoneme converter \nG2P\nממיר ייצוגים בשפה"+"\n\n")
Title.pack()

lexButton = Button(root, text="Load Lexicon", command=loadLex)
lexButton.pack()

textButton = Button(root, text="Load Text File", command=importFiles)
textButton.pack()


Llexiconv=StringVar()
Llexiconv.set("Missing lexicon file")
Llexicon = Label(root, textvariable=Llexiconv)
Llexicon.pack()
Lfilev=StringVar()
Lfilev.set("Missing text file")
Lfile = Label(root, textvariable=Lfilev)
Lfile.pack()
LReadyv=StringVar()
LReadyv.set("Pending proccess...")
LReady = Label(root, textvariable=LReadyv)
LReady.pack()

buttonFrame = Frame(root)
buttonFrame.pack()




saveButton = Button(buttonFrame, text="Save", command=saveFile)
saveButton.pack(side=LEFT)
saveButton.pack_forget()

img = ImageTk.PhotoImage(Image.open(resource_path("../img/Logo.png")))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

img2 = ImageTk.PhotoImage(Image.open(resource_path("../img/ganan.png")))
panel2 = Label(root, image = img2)
panel2.pack(side = "bottom", fill = "both", expand = "yes")

# text = Text(root)
# text.pack()

root.mainloop()
