#!/usr/bin/env python


import tkinter as tk




class Morris:
    def __init__(self):
        self.root = tk.Tk()
        #self.root.geometry("777x575")
        #self.root.minsize(777, 575)
        #self.root.columnconfigure(0, weight=1)
        #self.root.columnconfigure(1, weight=200)
        #self.root.rowconfigure(0, weight=1)
        
        
        # Text Code
        self.text_code_lbl = tk.Label(self.root, text="Text Code:")
        self.text_code_lbl.pack()
        
        self.text_code = tk.Text(self.root, height=1, width=1)
        self.text_code.pack(fill="both", expand=True)
        
        # Morse Code
        self.morse_code_lbl = tk.Label(self.root, text="Morse Code:")
        self.morse_code_lbl.pack()
        
        self.morse_code = tk.Text(self.root, height=1, width=1)
        self.morse_code.pack(fill="both", expand=True)
        
        # Navigation
        self.nav_btn_frame = tk.Frame(self.root)
        self.nav_btn_frame.pack(side="right", expand="False", fill="none")
        
        # Generate
        self.morse_btn = tk.Button(self.nav_btn_frame, text="Generate", command=self.__morse_btn_clicked__)
        self.morse_btn.pack(side="right", expand="False", fill="none")
        # Clear
        self.clear_btn = tk.Button(self.nav_btn_frame, text="Clear", command=self.__clear_btn_clicked__)
        self.clear_btn.pack(side="right", expand="False", fill="none")

    def __menubar__(self):
        self.menu = tk.Menu(self.root)
        
        self.filebar = tk.Menu(self.root)
        self.filebar.add_command(label="Exit", command="")
        self.filebar.add_cascade(label="File", menu=filebar)
        
        self.helpbar = tk.Menu(root)
        self.helpbar.add_command("About", command="")
        self.helpbar.add_cascade(label="Help", menu=helpbar)
        
        root.config(menu=self.menu)
        
    def __clear_btn_clicked__(self):
        None
        
    def __morse_btn_clicked__(self):
        None
        
    def __text_code__(self):
        None
        
    def __morse_code__(self):
        None
        
    def __buttons__(self):
        None
        




if __name__ == "__main__":
    morris = Morris()
    tk.mainloop() 