import tkinter as tk
from tkinter import W, filedialog , Text
import os


root = tk.Tk()
apps = []

def clearframe():
    for widget in frame.winfo_children():
        widget.destroy()

def addApp():

    clearframe()

    filename = filedialog.askopenfilename(initialdir = "/" , title="Select File" , filetypes=(("Executables" , ".exe"),("all files", "*.*")))
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame , text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def clearApps():
    with open("save.txt" , 'w') as f:
        clearframe()
        apps.clear()
        f.write('')

if __name__ == "__main__":

    if os.path.isfile("save.txt"):
        with open("save.txt" , 'r') as f:
            tempApps = f.read()
            tempApps = tempApps.split(',')
            apps = [x for x in tempApps if x.strip()]
    
    root.geometry("400x535")

    root.update()

    root.title('App Launcher')

    canvas = tk.Canvas(root , height= root.winfo_height() - 125 , width=root.winfo_width(), bg="#4A6572")
    canvas.pack()

    frame = tk.Frame(canvas , bg="white")
    frame.place(relwidth = 0.8 , relheight= 0.8 , relx = 0.1 , rely=0.1)

    openFile = tk.Button(root,text="Open File" , padx=10 , pady=5 , fg="white" , bg="#344955" , command=addApp)
    openFile.pack()

    runApps = tk.Button(root, text="Run Apps" , padx=10,pady=5,fg= "white" , bg= "#344955" , command=runApps)
    runApps.pack()

    tk.Label(root, text="" , height = 1).pack()

    clearApps = tk.Button(root , text="Delete Saved" , padx = 1 , pady = 1 , fg = "white", bg= "#232F34" , command=clearApps)
    clearApps.pack()

    for app in apps:
        label = tk.Label(frame , text=app)
        label.pack()

    root.mainloop()

    with open("save.txt" , 'w') as f:
        for app in apps:
            f.write(app + ',')
