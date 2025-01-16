#!/usr/bin/env python


import tkinter as tk
import winsound
from time import sleep




class Morris:
    '''
        Morris - A Simple Morse Code Library
        
        
        Alphabet: A B C D E F G H I J K L M
                  N O P Q R S T U V W X Y Z
                  0 1 2 3 4 5 6 7 8 9
                  . / : ;
        
        Notes:
            - The formatting is strict and requires:
                - every word be seperated by a space block ' '
                - no word willd start with a space block
                - last word must have a space block
                
               
        
        BUGS:
            - t2m() doesn't handle newlines properly
    '''
    text_dict = {
        '.-'    : 'A', '-...'  : 'B', '-.-.'  : 'C', '-..'   : 'D',
        '.'     : 'E', '..-.'  : 'F', '--.'   : 'G', '....'  : 'H',
        '..'    : 'I', '.---'  : 'J', '-.-'   : 'K', '.-..'  : 'L',
        '--'    : 'M', '-.'    : 'N', '---'   : 'O', '.--.'  : 'P',
        '--.-'  : 'Q', '.-.'   : 'R', '...'   : 'S', '-'     : 'T',
        '..-'   : 'U', '...-'  : 'V', '.--'   : 'W', '-..-'  : 'X',
        '-.--'  : 'Y', '--..'  : 'Z',
        '-----' : '0', '.----' : '1', '..---' : '2', '...--' : '3',
        '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7',
        '---..' : '8', '----.' : '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?'
    }
    morse_dict = {
        'A' : '.-',     'B' : '-...',   'C' : '-.-.',   'D' : '-..',
        'E' : '.',      'F' : '..-.',   'G' : '--.',    'H' : '....',
        'I' : '..',     'J' : '.---',   'K' : '-.-',    'L' : '.-..',
        'M' : '--',     'N' : '-.',     'O' : '---',    'P' : '.--.',
        'Q' : '--.-',   'R' : '.-.',    'S' : '...',    'T' : '-',
        'U' : '..-',    'V' : '...-',   'W' : '.--',    'X' : '-..-',
        'Y' : '-.--',   'Z' : '--..',
        '0' : '.----',  '1' : '..---',  '2' : '...--',  '3' : '....-',
        '4' : '.....',  '5' : '-....',  '6' : '--...',  '7' : '---..',
        '8' : '----.',  '9' : '-----',
        '.' : '.-.-.-', ',' : '--..--', ":" : '−−−...', '?' : '..--..',
        "'" : '.----.', '-' : '-....-'
    }
    
    
    dot = 3
    dash = 7
    char_space = 1
    word_space = 3
    space_char = '/'
    space_chars = ['/', ':', ';', '?']

    text = []
    morse = []


    def __init__(self):
            None
            
    def set_space(self, char):
        """ set_space(char) - Assign the internal word space character
        """
        if char not in self.space_chars:
            print("WARNING: set_space(): Provided character is not valid. Default: '/'")
            self.space_char = '/'
        else:
            self.space_char = char
        
        return True
        
    def isMorse(self, char):
        try:
            self.text[char]
        except KeyError:
            return False
        else:
            return True
        
    def set_text(self, text, append=False):
        None
        
    def set_morse(self, text, append=False):
        None
        
    def t2m(self, code, append=False, morse_string=True):
        """ t2m() - Text 2 Morse 
                Returns: Morse code as a list object with code separated by
                         by whitespace(s)
        
            code - The text to be tranlated into Morse
            string - True: returns the Morse in a formatted string format
                     False: Returns the Morse data structure with characters
                            and words separated respectively.
                            EG. [[h, e, l, l, o], [w, o, r, l, d]]
                            
            NOTES:
                - internally updates both self.text and self.morse as it encodes
                  respectively
            TODO:
                - Ignore characters that are not Morse accepted and print
                - Ignore newline characters
        
        """
        if not append:
            self.text = []
        self.m_word = []
        code_len = len(code)
        word_bool = False

        for i in range(code_len):
            print(code[i], ":", ord(code[i]))
                
            # Leave word and assign word to struct
            if word_bool and not code[i].isalnum():
                word_bool = False
                self.text.append(self.m_word)
                self.m_word = []
                
            # Last alphanumeric character - EOF
            elif word_bool and code[i].isalnum() and i == code_len - 1:
                word_bool = False
                self.m_word.append(code[i])
                self.text.append(self.m_word)
                
            # Beginning of word
            elif code[i].isalnum():
                word_bool = True
                self.m_word.append(code[i])

            # Ignore all else
            else:
                continue
            
        # Mirror data structure and assign
        self.morse = self.text
        for word in range(len(self.text)):
            for char in range(len(self.text[word])):

                    
                morse = self.morse_dict[self.text[word][char].upper()]
                self.morse[word][char] = morse
                
        if morse_string:
            return self.morse_string()
        else:
            return self.text
        
    def m2t(self, code):
        """ m2t() - Morse 2 Text"""
        code_len = len(code)
        t_code = ""
        morse_word = ''
        word_bool = False

        for i in range(code_len):
            print(f"for i: {i} code[{i}]: {code[i]}")
            print(f"\tmorse_word: {morse_word}")
            # Deal with Morse code

            # Deal with space character
            if word_bool and code[i] == ' ':
                try:
                    # Deal with word space character
                    # TODO: What if Morris space_char is different than the 
                    #       provided text?
                    if code[i+1] in self.space_chars:
                        word_bool = False
                        t_code = t_code + self.text_dict[morse_word] + ' '
                        morse_word = ''
                    
                    # Otherwise store character
                    else:
                        # Ensure valid morse character
                        try:
                            word_bool = False
                            t_code = t_code + self.text_dict[morse_word]
                            morse_word = ''
                        except KeyError:
                            print("WARNING: m2t(): Invalid Morse character")
                        
                except IndexError:
                    print(f"m2t() exception: index out of range")
                
            # EOF
            elif i == code_len:
                if code[i] in ('.', '-'):
                    morse_word = morse_word + code[i]
                    t_code = t_code + self.text_dict[morse_word]
                
            # Finish word
            elif word_bool and code[i] not in ('.', '-'):
                word_bool = False
                print(morse_word)
                try:
                    t_code = t_code + self.text_dict[morse_word] + ' '
                except KeyError:
                    print("WARNING: m2t(): Invalid Morse character")
                morse_word = ''
                
            # Store character
            elif code[i] in ('.', '-'):
                word_bool = True
                morse_word = morse_word + code[i]
                
            else:
                continue
                

        return t_code.strip(" ")
        
    def morse_string(self):
        """ morse_string() - Return the Morse Struct as a blob string
        """
        morse = ""
        space = '/ '
        
        if self.space_char == ' ':
            self.space_char = ' '
        elif self.space_char == '   ':
            self.space_char = '   '
        elif self.space_char == '       ':
            self.space_char == '       '
        elif self.space_char == '/':
            self.space_char = '/ '
        elif self.space_char == ':':
            self.space_char = ': '
        elif self.space_char == ';':
            self.space_char = '; '
        elif self.space_char == '?':
            self.space_char = '? '
        else:
            self.space_char = '/'
        
        for word in range(len(self.morse)):
            for char in range(len(self.morse[word])):
                morse = morse + self.morse[word][char]
                morse = morse + ' '
                
            morse = morse + self.space_char
    
        # Strip last space character from tail
        morse = morse[0:-3]
        
        
        return morse
        
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
        
        # Morse Display Color Alternation
        self.colorize = True
        self.even_color = "green"
        self.odd_color = "blue"
        
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
        self.actionmenu.add_command(label="Play Morse", 
            command=self.__action_play_morse_clicked__)
        self.menu.add_cascade(label="Action", menu=self.actionmenu)
        
        # Whitespace character selection
        self.actionsubmenu1 = tk.Menu(self.actionmenu, tearoff=0, 
            postcommand=self.__whitespace_postcommand__)
        self.actionmenu.add_cascade(label="White Space Char", 
            menu=self.actionsubmenu1)
        # NOTE: Text sensitive with __action_space_postcommand__
        self.actionsubmenu1.add_command(label="1 Space", 
            command=lambda: self.__whitespace_select_change__(' '))
        self.actionsubmenu1.add_command(label="3 Space", 
            command=lambda: self.__whitespace_select_change__('   '))
        self.actionsubmenu1.add_command(label="7 Space", 
            command=lambda: self.__whitespace_select_change__('       '))
        self.actionsubmenu1.add_command(label="/", 
            command=lambda: self.__whitespace_select_change__('/'))
        self.actionsubmenu1.add_command(label=":", 
            command=lambda: self.__whitespace_select_change__(':'))
        self.actionsubmenu1.add_command(label=";", 
            command=lambda: self.__whitespace_select_change__(';'))
        self.actionsubmenu1.add_command(label="?", 
            command=lambda: self.__whitespace_select_change__('?'))
        
        # Colorize the Morse output
        
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
        self.morse_btn = tk.Button(self.nav_btn_frame, text="Morse", 
            command=self.__morse_btn_clicked__)
        self.morse_btn.pack(side="right", expand="False", fill="none")
        # Text
        self.text_btn = tk.Button(self.nav_btn_frame, text="Text", 
            command=self.__text_btn_clicked__)
        self.text_btn.pack(side="right", expand="False", fill="none")
        # Clear
        self.clear_btn = tk.Button(self.nav_btn_frame, text="Clear", 
            command=self.__clear_btn_clicked__)
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
        
        # TODO: Deal with exception of no entered text (empty Text() field)
        print("__morse_btn_clicked__(): ", ord(text[-1]))
        
        if text != '\n':
            self.morse_code.delete("0.0", "end")
            self.morse_code.insert("0.0", self.morris.t2m(text))
            
        #self.__colorize__(self.colorize)
        
    def __action_play_morse_clicked__(self):
        morse_code = self.morse_code.get("0.0", "end")
        self.morris.play(morse_code)

    def __whitespace_select_change__(self, char):
        self.morris.set_space(char)
        self.__morse_btn_clicked__()

    def __whitespace_postcommand__(self):
        ## Show active indicator in Whitespace Selection Dropdown
        # Whitespace
        if self.morris.space_char == ' ':
            self.actionsubmenu1.entryconfig(0, label='* - 1 Space')
        else:
            self.actionsubmenu1.entryconfig(0, label='    1 Space')

        # 3 Whitespace
        if self.morris.space_char == '   ':
            self.actionsubmenu1.entryconfig(1, label='* - 3 Space')
        else:
            self.actionsubmenu1.entryconfig(1, label='    3 Space')

        # Forward Slash
        if self.morris.space_char == '/':
            self.actionsubmenu1.entryconfig(2, label='* - /')
        else:
            self.actionsubmenu1.entryconfig(2, label='    /')

        # Colon
        if self.morris.space_char == ':':
            self.actionsubmenu1.entryconfig(3, label='* - :')
        else:
            self.actionsubmenu1.entryconfig(3, label='    :')

        # Semicolon
        if self.morris.space_char == ';':
            self.actionsubmenu1.entryconfig(4, label='* - ;')
        else:
            self.actionsubmenu1.entryconfig(4, label='    ;')

        # Question Mark
        if self.morris.space_char == '?':
            self.actionsubmenu1.entryconfig(5, label='* - ?')
        else:
            self.actionsubmenu1.entryconfig(5, label='    ?')

    def __colorize__(self, state=True):
        e_color = "green"
        o_color = "blue"
        
        even = False
        
        # Remove color
        if not state:
            self.morse_code.tag_config("even", foreground="black")
            self.morse_code.tag_config("odd", foreground="black")




if __name__ == "__main__":
    morris = GUI()
    tk.mainloop()
    
