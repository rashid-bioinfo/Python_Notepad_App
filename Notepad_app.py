from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    # delete(1.0, END) means to erase from first line, 0th character till end
    textArea.delete(1.0, END) 
     
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", 
                           filetypes=[("All Files", "*.*"), 
                           ("Text Documents", "*.txt")
                           ])
    if (file == ""):
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

 
def saveFile():
    global file
    if (file == None):
        file = asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt", 
                           filetypes=[("All Files", "*.*"), 
                           ("Text Documents", "*.txt")
                           ])
        if (file == ""):
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy() 

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Rashid Hussain")

if __name__ == '__main__':
    # Basic tkinter setup

    root= Tk()
    root.title("Untitled - Notepad")
    root.geometry("544x688")


    textArea = Text(root, font="lucida 13")
    file = None
    textArea.pack(fill=BOTH, expand=True)





    # Lets creat a menubar
    menuBar = Menu(root)

    ### ------------------------  ###
    ##          File Menu          ##
    ### ------------------------- ###

    fileMenu=Menu(menuBar, tearoff=0)
    # To open new file
    fileMenu.add_command(label="New", command=newFile)

    # To open already exisiting file
    fileMenu.add_command(label="Open", command=openFile)

    # To save the current file
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)

    # It will associate the above menu with the file menu
    menuBar.add_cascade(label="File", menu=fileMenu)

    ## ------------------------  ###
    #          Edit Menu          ##
    ## ------------------------- ###

    editMenu = Menu(menuBar, tearoff=0)
    
    # To give a feature of cut, copy and paste
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    # It will associate the above menu with the edit menu
    menuBar.add_cascade(label="Edit", menu=editMenu)

    ### ------------------------  ###
    ##          Help Menu          ##
    ### ------------------------- ###
 
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

    ### ------------------------  ###
    ##          Scroll Bar         ##
    ### ------------------------- ###

    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)


root.mainloop()