"""
Naftali Panitz
Final Project GUI

0aa 1bb 2cc
3dd 4ee 5ff
6gg 7hh 8ii
"""

from tkinter import *
from tkinter import messagebox
from game import TicTacToeGame

class GameGUI:
    def __init__(self):

        # Constants
        self.__USERNAME_PROMPT = ('Please enter a username:  ')
        self.__X_O = ['X', 'O']

        # create a model
        self.__model = TicTacToeGame()

        # Create GUI main window
        self.__main_window = Tk()
        self.__main_window.title('Tic-Tac-Toe, 3 in a Row')
        self.__main_window.geometry('395x500')
        self.__main_window['bg'] = 'light blue'

         #Variables
#-----------------------------------------------------------------------------
        # Create Username Variables
        user_name1 = StringVar()
        self.__user_name1 = user_name1
        
        user_name2 = StringVar()
        self.__user_name2 = user_name2

        # Initiate score Text Variable
        p1_score_text = StringVar()
        self.__p1_score_text = p1_score_text
        
        p2_score_text = StringVar()
        self.__p2_score_text = p2_score_text

        # Button text variables
        button_text_a = StringVar()
        self.__button_text_a = button_text_a

        button_text_b = StringVar()
        self.__button_text_b = button_text_b

        button_text_c = StringVar()
        self.__button_text_c = button_text_c

        button_text_d = StringVar()
        self.__button_text_d = button_text_d

        button_text_e = StringVar()
        self.__button_text_e = button_text_e

        button_text_f = StringVar()
        self.__button_text_f = button_text_f

        button_text_g = StringVar()
        self.__button_text_g = button_text_g

        button_text_h = StringVar()
        self.__button_text_h = button_text_h

        button_text_i = StringVar()
        self.__button_text_i = button_text_i

        # Labels
#-----------------------------------------------------------------------------
        # Create heading label
        self.__heading = Label(self.__main_window, text = 'Tic Tac Toe')
        self.__heading.grid(row = 1, column = 1, sticky = W)
        self.__heading['bg'] = 'light blue'
        self.__heading.config(font = ('Comic Sans', 10, 'bold'))

        # Create Player labels 
        self.__user1_label = Label(self.__main_window, text = "Player 1: ")
        self.__user1_label.grid(row = 7, column = 0,  sticky = W)
        self.__user1_label['bg'] = 'light blue'

        self.__user2_label = Label(self.__main_window, text = "Player 2: ")
        self.__user2_label.grid(row = 8, column = 0, sticky = W)
        self.__user2_label['bg'] = 'light blue'

        
        # Create user name Labels
        self.__user1 = Label(self.__main_window, \
                             textvariable = self.__user_name1)
        self.__user1.grid(row = 7, column = 1, sticky = W)
        self.__user1['bg'] = 'light blue'

        self.__user2 = Label(self.__main_window, \
                             textvariable = self.__user_name2)
        self.__user2.grid(row = 8, column = 1, sticky = W)
        self.__user2['bg'] = 'light blue'
        
            
        # Create score labels
        self.__user1_score_label = Label(self.__main_window, \
                                         text = ('Score:  '))
        self.__user1_score_label.grid(row = 7, column = 2, sticky = W)
        self.__user1_score_label['bg'] = 'light blue'
    

        self.__user2_score_label = Label(self.__main_window, \
                                         text = ('Score:  '))
        self.__user2_score_label.grid(row = 8, column = 2, sticky = W)
        self.__user2_score_label['bg'] = 'light blue'

        # Entry prompt Labels
        self.__user1_prompt = Label(self.__main_window, \
                                    text = self.__USERNAME_PROMPT)
        self.__user1_prompt.grid(row = 3, column = 13, sticky = E)
        self.__user1_prompt['bg'] = 'light blue'

        self.__user2_prompt = Label(self.__main_window, \
                                    text = self.__USERNAME_PROMPT)
        self.__user2_prompt.grid(row = 4, column = 13, sticky = E)
        self.__user2_prompt['bg'] = 'light blue'

        # Create Player Score Labels
        self.__player_one_score = Label(self.__main_window, \
                                        textvariable = self.__p1_score_text)
        self.__player_one_score.grid(row = 7, column = 2, sticky = E)
        self.__player_one_score['bg'] = 'light blue'

        self.__player_two_score = Label(self.__main_window, \
                                        textvariable = self.__p2_score_text)
        self.__player_two_score.grid(row = 8, column = 2, sticky = E)
        self.__player_two_score['bg'] = 'light blue'

        #Entry
#-----------------------------------------------------------------------------
        # Entry Box
        self.__entry1 = Entry(self.__main_window, width = 23)
        self.__entry1.bind('<Return>', self.set_user_name1)
        self.__entry1.grid(row = 3, column = 13, sticky = SE)

        self.__entry2 = Entry(self.__main_window, width = 23)
        self.__entry2.bind('<Return>', self.set_user_name2)
        self.__entry2.grid(row = 4, column = 13, sticky = SE)
    
        # Buttons
#-----------------------------------------------------------------------------
        # Create and pack aa Button
        self.__button_aa = Button(self.__main_window ,\
                                  textvariable = self.__button_text_a , \
                                  height = '5', width = '10', \
                                  command = self.update_a)
        self.__button_aa.grid(row = 3, column = 0)

        # Create and pack bb Button
        self.__button_bb = Button(self.__main_window, \
                                  textvariable = self.__button_text_b, \
                                  height = '5' , width = '10', \
                                  command = self.update_b)
        self.__button_bb.grid(row = 3, column = 1)

        # Create and pack cc Button
        self.__button_cc = Button(self.__main_window,\
                                  textvariable = self.__button_text_c, \
                                  height = '5', width = '10', \
                                  command = self.update_c)
        self.__button_cc.grid(row = 3, column = 2)

        # Create and pack dd Button
        self.__button_dd = Button(self.__main_window, \
                                  textvariable = self.__button_text_d, \
                                  height = '5' , width = '10', \
                                  command = self.update_d)
        self.__button_dd.grid(row = 4, column = 0)

        # Create and pack ee Button
        self.__button_ee = Button(self.__main_window, \
                                  textvariable = self.__button_text_e, \
                                  height = '5' , width = '10', \
                                  command = self.update_e)
        self.__button_ee.grid(row = 4, column = 1)

        # Create and pack ff Button
        self.__button_ff = Button(self.__main_window , \
                                  textvariable = self.__button_text_f, \
                                  height = '5' , width = '10', \
                                  command = self.update_f)
        self.__button_ff.grid(row = 4, column = 2)

        # Create and pack gg Button
        self.__button_gg = Button(self.__main_window , \
                                  textvariable = self.__button_text_g, \
                                  height = '5' , width = '10', \
                                  command = self.update_g)
        self.__button_gg.grid(row = 5, column = 0)

        # Create and pack hh Button
        self.__button_hh = Button(self.__main_window , \
                                  textvariable = self.__button_text_h, \
                                  height = '5' , width = '10', \
                                  command = self.update_h)
        self.__button_hh.grid(row = 5, column = 1)

        # Create and pack ii Button
        self.__button_ii = Button(self.__main_window , \
                                  textvariable = self.__button_text_i, \
                                  height = '5' , width = '10', \
                                  command = self.update_i)
        self.__button_ii.grid(row = 5, column = 2)

        # Create and pack reset button
        self.__reset_button = Button(self.__main_window , \
                                     text = 'Reset', height = 3 , \
                                     width = 10, command = self.reset)
        self.__reset_button.grid(row = 6 ,  column = 1)

        # Iterable Lists
#-----------------------------------------------------------------------------        
        # List of Buttons/Button Texts so indexing is easy
        self.__LIST_OF_BUTTONS = [self.__button_aa, self.__button_bb, \
                                  self.__button_cc, self.__button_dd, \
                                  self.__button_ee, self.__button_ff, \
                                  self.__button_gg, self.__button_hh, \
                                  self.__button_ii]

        # Iterable List of Button text variables
        self.__LIST_OF_BUTTON_TEXTS = [self.__button_text_a, \
                                       self.__button_text_b, \
                                       self.__button_text_c, \
                                       self.__button_text_d, \
                                       self.__button_text_e, \
                                       self.__button_text_f, \
                                       self.__button_text_g, \
                                       self.__button_text_h, \
                                       self.__button_text_i]
        # Image
#-----------------------------------------------------------------------------
        # Canvas for image
        image_canvas = Canvas(self.__main_window, width = 135, height = 135)
        image_canvas.grid(row = 9, column = 13)
        image_canvas['bg'] = 'light blue'

        # Image insert
        image_file = PhotoImage(file = 'bu_bearcat.png')
        image_canvas.create_image(0,0, anchor = NW, image = image_file)

        # Start listener
#-----------------------------------------------------------------------------       
        # Continue window
        self.__main_window.mainloop()


        # Event Handlers
#-----------------------------------------------------------------------------
        
    # Updaters(setters + actions)
    
    # Determines and sets turn marker and color by calling the game class
    # Then check whether the game has been won or not
    def update_a(self):
        self.__model.set_turn_marker_and_color('aa')
        self.__button_text_a.set(self.__model.get_turn_marker())
        self.__button_aa['bg'] = self.get_button_color()
        self.__check_game_status()
        
    def update_b(self):
        self.__model.set_turn_marker_and_color('bb')
        self.__button_text_b.set(self.__model.get_turn_marker())
        self.__button_bb['bg'] = self.get_button_color()
        self.__check_game_status()
            
    def update_c(self):
        self.__model.set_turn_marker_and_color('cc')
        self.__button_text_c.set(self.__model.get_turn_marker())
        self.__button_cc['bg'] = self.get_button_color()
        self.__check_game_status()
        
    def update_d(self):
        self.__model.set_turn_marker_and_color('dd')
        self.__button_text_d.set(self.__model.get_turn_marker())
        self.__button_dd['bg'] = self.get_button_color()
        self.__check_game_status()
                                 
    def update_e(self):
        self.__model.set_turn_marker_and_color('ee')
        self.__button_text_e.set(self.__model.get_turn_marker())
        self.__button_ee['bg'] = self.get_button_color()
        self.__check_game_status()
                                 
    def update_f(self):
        self.__model.set_turn_marker_and_color('ff')
        self.__button_text_f.set(self.__model.get_turn_marker())
        self.__button_ff['bg'] = self.get_button_color()
        self.__check_game_status()
                                 
    def update_g(self):
        self.__model.set_turn_marker_and_color('gg')
        self.__button_text_g.set(self.__model.get_turn_marker())
        self.__button_gg['bg'] = self.get_button_color()
        self.__check_game_status()
                                 
    def update_h(self):
        self.__model.set_turn_marker_and_color('hh')
        self.__button_text_h.set(self.__model.get_turn_marker())
        self.__button_hh['bg'] = self.get_button_color()
        self.__check_game_status()
                                 
    def update_i(self):
        self.__model.set_turn_marker_and_color('ii')
        self.__button_text_i.set(self.__model.get_turn_marker())
        self.__button_ii['bg'] = self.get_button_color()
        self.__check_game_status()

    # Setters
    
    # General setter that references game class to set new values
    def set(self, value):
        self.__model.set(value)
        
    # Gets user name string entered in entry box and sets the game's usernames
    # Then set the display username in the GUI to the username stored in
    # The game class.
    def set_user_name1(self,user_name):
        self.__model.set_user1_name(self.__entry1.get())
        self.__user_name1.set(self.__model.get_user1_name())

    def set_user_name2(self, user_name):
        self.__model.set_user2_name(self.__entry2.get())
        self.__user_name2.set(self.__model.get_user2_name())
        
    # Sets player score to the current score stored in the game class    
    def set_player_one_score(self):
        self.__p1_score_text.set(self.__model.get_p1_score())
        
    def set_player_two_score(self):
        self.__p2_score_text.set(self.__model.get_p2_score())
        
    # Simple getter that returns a string of a color by accessing game class
    def get_button_color(self):
        return (self.__model.get_button_color())
        

    # Terminator
    
    # Resets game when game is over
    # Calls game classes reset button
    # Sets all values in dictionary of board to empty strings
    # Sets all the button colors back to light grey
    def reset(self):
        self.__model.set_reset_button()
        for button_text in self.__LIST_OF_BUTTON_TEXTS:
            button_text.set(self.__model.get_reset_button())
        for button in self.__LIST_OF_BUTTONS:
            button['bg'] = 'light grey'

    # Checks whether the game is over by calling game class's
    # is_game_over function
    def __check_game_status(self):
        if self.__model.is_game_over():
            self.game_terminator(self.__model.get_winner())
            
    # Terminates game, calls string generator from the game class
    # Generates message box and accesses the win string from the game class
    # Sets players' scores
    # Calls the reset handler
    def game_terminator(self, user):
        self.__model.set_win_string(user)
        messagebox.showinfo('Game Over', (self.__model.get_win_string()))
        self.__model.set_increment_score(user)
        self.set_player_one_score()
        self.set_player_two_score()
        self.reset()
    
        
        

GameGUI()
