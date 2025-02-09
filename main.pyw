#!/usr/bin/env python


import tkinter as tk
from PIL import Image, ImageTk
from math import floor
debug = False

class Morris:
    '''
        Morris - A Simple Morse Code Library
        
        
        Alphabet: A B C D E F G H I J K L M
                  N O P Q R S T U V W X Y Z
                  0 1 2 3 4 5 6 7 8 9
        
        Notes:
            - The formatting is strict and requires:
                - every word be seperated by a space block ' '
                - no word will start with a space block
                - last word must have a space block
                
                
        Colorize Functionality:
            Morris.colorize(True)
            Morris.set_color("red", "green")
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
        '---..' : '8', '----.' : '9'
    }
    morse_dict = {
        'A' : '.-',     'B' : '-...',   'C' : '-.-.',   'D' : '-..',
        'E' : '.',      'F' : '..-.',   'G' : '--.',    'H' : '....',
        'I' : '..',     'J' : '.---',   'K' : '-.-',    'L' : '.-..',
        'M' : '--',     'N' : '-.',     'O' : '---',    'P' : '.--.',
        'Q' : '--.-',   'R' : '.-.',    'S' : '...',    'T' : '-',
        'U' : '..-',    'V' : '...-',   'W' : '.--',    'X' : '-..-',
        'Y' : '-.--',   'Z' : '--..',
        '0' : '-----',  '1' : '.----',  '2' : '..---',  '3' : '...--',
        '4' : '....-',  '5' : '.....',  '6' : '-....',  '7' : '--...',
        '8' : '---..',  '9' : '----.'
    }
    
    
    dot = 3
    dash = 7
    char_space = 1
    word_space = 3
    space_char = '/'
    space_chars = ['/', ':', ';', '?']

    # 'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', and 'magenta'
    colorize = False
    first_color = "black"
    second_color = "blue"
    """ 
        Text/Morse data structures for code processing and manipulation.
        
        TODO: Incorporate data structure into m2t()
        
        text = [[h, e, l, l, o], [w, o, r, l, d]]
        morse = [['....', '.', '.-..', '.-..', '---'], 
                 ['.--', '---', '.-.', '.-..', '-..']]
    """
    text = []
    morse = []


    def __init__(self):
            None
            
    def set_space(self, char):
        """ set_space(char) - Assign the internal word space character
        """
        if char not in self.space_chars:
            if debug: print("WARNING: set_space(): Provided character is not valid. Default: '/'")
            self.space_char = '/'
        else:
            self.space_char = char
        
        return True
    
    def toggle_color(self, bool=False):
        """ Toggle the colorize boolean and return the values
        """
        if self.colorize:
            self.colorize = False
        else:
            self.colorize = True
            
        return self.colorize
        
    def set_color(self, first=None, second=None):
        """ Set the first and second colors for string hilight alternation
        
            TODO: set_color("first=red", "second=blue")
        """
        colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
        
        if first in colors:
            self.first_color = first
        else:
            if debug: print("ERROR: Morris::set_color(): invalid first color value")
            
        if second in colors:
            self.second_color = second
        else:
            if debug: print("ERROR: Morris::set_color(): invalid second color value")
            
        return True
            
    def get_colors(self):
        """ Return the current colors for colorization in the format of:
            - [colorize, color_1, color_2] - [True, 'red', 'green']
        """
        return [self.colorize, self.first_color, self.second_color]
         
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
        """
        if not append:
            self.text = []
        self.m_word = []
        # Pad a space to add a trailing processing loop TODO: Fix Hack
        code = code + " "
        code_len = len(code)
        word_bool = False


        for i in range(code_len):
            # BUG: A single character with no trailing space won't trigger 
            #      word_bool-isalnum() condition
            
            #if debug: print("t2m():", code[i], ":", ord(code[i]))
            #if debug: print(f"{i} : {code[i]}")
                
            # Leave word and assign word to struct
            if word_bool and not code[i].isalnum():
                word_bool = False
                self.text.append(self.m_word)
                self.m_word = []
                
            # Last alphanumeric character - EOF
            elif word_bool and code[i].isalnum() and i == (code_len - 1):
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
                
        if debug: print(self.morse)
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
            #if debug: print("m2t():", code[i], ":", ord(code[i]))

            # Store character of word
            if code[i] in ('.', '-'):
                word_bool = True
                morse_word = morse_word + code[i]
                
            # Store word (Character)
            elif word_bool and not code[i] in ('.', '-'):
                word_bool = False
                t_code = t_code + self.text_dict[morse_word]
                morse_word = ''
                
                # Word space character
                try:
                    if code[i+1] == self.space_char:
                        t_code = t_code + ' '
                    
                    # Deal with extra space before space_char
                    else:
                        n = i
                        while code[n] not in ('.', '-'):
                            if code[n] == self.space_char:
                                t_code = t_code + ' '
                            n += 1
                            
                except IndexError:
                    continue
                
            # EOF
            elif word_bool and code[i] in ('.', '-') and i == code_len - 1:
                morse_word = morse_word + code[i]
                t_code = t_code + self.text_dict[code[i]]
                    
            # Ignore all else
            else:
                continue
                

        return t_code.strip(" ")
        
    def morse_string(self):
        """ morse_string() - Return the Morse Struct as a blob string
        """
        morse = ""
        
        # Iter data structure and cast to string
        for word in range(len(self.morse)):
            for char in range(len(self.morse[word])):
                morse = morse + self.morse[word][char]
                morse = morse + ' '
                
            morse = morse + self.space_char + ' '
    
        # Strip last space character from tail
        morse = morse[0:-3]
        
        
        return morse


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("777x575")
        self.root.minsize(200, 200)
        
        self.morris = Morris()
        
        # TODO: Morse Display Color Alternation
        self.colorize = True
        self.even_color = "green"
        self.odd_color = "blue"
        
        ### GUI Layout ###
        # File Menu
        self.menu = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.root.destroy)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.__about_me__)
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
        
    def __about_me__(self):
        """ Display toplevel About Me window.
        """
        about_x = 250
        about_y = 300
        
        about = tk.Toplevel(takefocus="true")
        # Hide first spawn point
        about.withdraw()
        about.update()
        about.resizable("false", "false")
        about.attributes("-toolwindow", True)
        about.attributes("-topmost", True)

        ### Center the about me on parent window
        t = self.root.geometry().split("+")
        parent_x = int(t[0].split("x")[0])
        parent_y = int(t[0].split("x")[1])
        
        x_offset = int(t[1])
        y_offset = int(t[2])
        
        x_geom = x_offset + ((parent_x / 2) - (about_x / 2))
        y_geom = y_offset + ((parent_y / 2) - (about_y / 2))
        about.geometry(f"{about_x}x{about_y}+{floor(x_geom)}+{floor(y_geom)}")
        
        # Show About
        about.deiconify()
        
        # Naval Sailors Morse Image
        # Double click - Open: https://www.military.com/history/the-tuskegee-airmen.html
        image = Image.open("tuskegee-code-training.jpg")
        # W x H
        image.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(image)
        
        img = tk.Label(about, image=photo)
        img.image = photo
        img.pack()
        
        # Line Break
        lb2 = tk.Label(about)
        lb2.pack()
        
        # Version Information
        self.ver_lbl = tk.Label(about, text="Morris")
        self.ver_lbl.pack()
        
        desc_lbl = tk.Label(about, text="A simple Morse Code translator")
        desc_lbl.pack()
        
        subver_lbl = tk.Label(about, text="1.0.0")
        subver_lbl.pack()
        
        # Line Break
        lb3 = tk.Label(about)
        lb3.pack()
        
        # Author Information
        author_lbl = tk.Label(about, text="Tom Smith", justify="left")
        author_lbl.pack()
        
        email_lbl = tk.Label(about, text="Thomas.Briggs.Smith@gmail.com", 
            justify="left")
        email_lbl.pack()
        
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

    def __whitespace_select_change__(self, char):
        self.morris.set_space(char)
        self.__morse_btn_clicked__()

    def __whitespace_postcommand__(self):
        # TODO: Incorporate more character spacing functionality
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