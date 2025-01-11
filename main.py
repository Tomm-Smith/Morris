#!/usr/bin/env python


import tkinter as tk
import winsound
from time import sleep




class Morris:
    '''
        Morris - A Simple Morse Code Library
        
        
        Notes:
            - The formatting is strict and requires:
                - every word be seperated by a space block ' '
                - no word willd start with a space block
                - last word must have a space block
    '''
    dot = 3
    dash = 7
    char_space = 1
    word_space = 3
    space_char = '/'
    text = {
            '.-'    : 'A',
            '-...'  : 'B',
            '-.-.'  : 'C',
            '-..'   : 'D',
            '.'     : 'E',
            '..-.'  : 'F',
            '--.'   : 'G',
            '....'  : 'H',
            '..'    : 'I',
            '.---'  : 'J',
            '-.-'   : 'K',
            '.-..'  : 'L',
            '--'    : 'M',
            '-.'    : 'N',
            '---'   : 'O',
            '.--.'  : 'P',
            '--.-'  : 'Q',
            '.-.'   : 'R',
            '...'   : 'S',
            '-'     : 'T',
            '..-'   : 'U',
            '...-'  : 'V',
            '.--'   : 'W',
            '-..-'  : 'X',
            '-.--'  : 'Y',
            '--..'  : 'Z',
            '-----' : '0',
            '.----' : '1',
            '..---' : '2',
            '...--' : '3',
            '....-' : '4',
            '.....' : '5',
            '-....' : '6',
            '--...' : '7',
            '---..' : '8',
            '----.' : '9'
            }
    morse = {
            'A' : '.-',
            'B' : '-...',
            'C' : '-.-.',
            'D' : '-..',
            'E' : '.',
            'F' : '..-.',
            'G' : '--.',
            'H' : '....',
            'I' : '..',
            'J' : '.---',
            'K' : '-.-',
            'L' : '.-..',
            'M' : '--',
            'N' : '-.',
            'O' : '---',
            'P' : '.--.',
            'Q' : '--.-',
            'R' : '.-.',
            'S' : '...',
            'T' : '-',
            'U' : '..-',
            'V' : '...-',
            'W' : '.--',
            'X' : '-..-',
            'Y' : '-.--',
            'Z' : '--..',
            '0' : '.----',
            '1' : '..---',
            '2' : '...--',
            '3' : '....-',
            '4' : '.....',
            '5' : '-....',
            '6' : '--...',
            '7' : '---..',
            '8' : '----.',
            '9' : '-----'
            }

    def __init__(self):
            None
            
    def isMorse(self, char):
        try:
            self.text[char]
        except KeyError:
            return False
        else:
            return True
        
    def t2m(self, code):
        """ t2m() - Text 2 Morse 
        
            - Why does this insert a space and newline character?
        """
        code_len = len(code)
        m_code = ''
        word_space = ' / '
        word_bool = False

        for i in range(code_len):
            if code[i] != ' ':
                word_bool = True
                m_code = m_code + self.morse[code[i].upper()] + " "
                
            elif word_bool and code[i] == ' ':
                word_bool = False
                m_code = m_code + word_space
                
            elif code[i] == ' ':
                continue
                
            else:
                print("t2m(): if-elif-else statement: else exception")
                
                
        # Remove trailing space and word seperator
        if m_code[-3:] == word_space:
            m_code = m_code[0:-3]
        if m_code[-1] == ' ':
            m_code = m_code[0:-1]
            
        return m_code
        
    def m2t(self, code):
        """ m2t() - Morse 2 Text"""
        t_code = ""
        m_word = ""
        ws_bool = False
        
        
    
    def play(self, code):
        for char in code:
            if char == '.':
                winsound.Beep(700, 60 * self.dot)
                sleep(60 * self.char_space / 1000)
            elif char == '-':
                winsound.Beep(700, 60 * self.dash)
                sleep(60 * self.char_space / 1000)
            elif char == ' ':
                sleep(60 * self.word_space / 1000)


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("777x575")
        #self.root.minsize(777, 575)
        
        self.morris = Morris()
        
        
        ### GUI Layout ###
        # File Menu
        self.menu = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Open", command="")
        self.filemenu.add_command(label="Save", command="")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.destroy)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        
        self.actionmenu = tk.Menu(self.menu, tearoff=0)
        self.actionmenu.add_command(label="Play Morse", command=self.__action_play_morse_clicked__)
        self.menu.add_cascade(label="Action", menu=self.actionmenu)
        
        self.actionsubmenu1 = tk.Menu(self.actionmenu)
        self.actionmenu.add_cascade(label="White Space Char", menu=self.actionsubmenu1)
        self.actionsubmenu1.add_command(label="/")
        self.actionsubmenu1.add_command(label=":")
        self.actionsubmenu1.add_command(label=";")
        
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label="About", command="")
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        
        self.root.config(menu=self.menu)
        
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
        
        
        # UI Buttons
        self.nav_btn_frame = tk.Frame(self.root)
        self.nav_btn_frame.pack(side="right", expand="False", fill="none")
        
        # Morse
        self.morse_btn = tk.Button(self.nav_btn_frame, text="Morse", command=self.__morse_btn_clicked__)
        self.morse_btn.pack(side="right", expand="False", fill="none")
        # Text
        self.text_btn = tk.Button(self.nav_btn_frame, text="Text", command=self.__text_btn_clicked__)
        self.text_btn.pack(side="right", expand="False", fill="none")
        # Clear
        self.clear_btn = tk.Button(self.nav_btn_frame, text="Clear", command=self.__clear_btn_clicked__)
        self.clear_btn.pack(side="right", expand="False", fill="none")
        
    def __clear_btn_clicked__(self):
        self.text_code.delete("0.0", "end")
        self.morse_code.delete("0.0", "end")
        
    def __text_btn_clicked__(self):
        morse = self.morse_code.get("0.0", "end")
        
        if morse != '\n':
            self.text_code.delete("0.0", "end")
            self.text_code.insert("0.0", self.morris.m2t(morse))
            
    def __morse_btn_clicked__(self):
        text = self.text_code.get("0.0", "end-1c")
        
        if text != '\n':
            self.morse_code.delete("0.0", "end")
            self.morse_code.insert("0.0", self.morris.t2m(text))
        
    def __action_play_morse_clicked__(self):
        morse_code = self.morse_code.get("0.0", "end")
        self.morris.play(morse_code)




if __name__ == "__main__":
    morris = GUI()
    tk.mainloop()
    
    m = Morris()
    
    morse = m.t2m("hello")
    text = m.m2t(morse)
    
    print("Text: ###" + text +"###")
    print("Morse: ###" + morse + "###")
    
