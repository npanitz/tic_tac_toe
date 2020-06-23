"""
0aa 1bb 2cc
3dd 4ee 5ff
6gg 7hh 8ii
"""

class TicTacToeGame:
    

    def __init__(self):
        # Initialize winner to None
        self.__winner = None
        # Initialize turn (responsible for which player is clicking)
        self.__turn = 0
        # Initialize player scores to 0 
        self.__p1_score = 0
        self.__p2_score = 0
        # Create indexable list of player marks
        self.__X_O = ['X', 'O']
        # Create associate dict of button colors
        self.__button_colors = {'X':'magenta', 'O':'yellow'}
        # Initialize user names
        self.__user1 = ''
        self.__user2 = ''
        # Initialize turn marker
        self.__turn_marker = ''
        # Initialize button color
        self.__button_color = ''
        # Initialize winning string
        self.__winning_string = ''
        
        # Create indexible list of spots
        # Each spot can be accessed using an int or str
        self.__NUM_2_SPOT = ['aa',  'bb', 'cc', 'dd', 'ee', 'ff', \
                             'gg', 'hh', 'ii']
        """
        Inititialize all spots to an empty string, use 
        dictionary for accessing
        """
        self.__spots = {'aa' : ' ', \
            'bb' : ' ', \
            'cc' : ' ', \
            'dd' : ' ',\
            'ee' : ' ', \
            'ff' : ' ', \
            'gg' : ' ', \
            'hh' : ' ', \
            'ii' : ' ', }


        # Predicates
 #---------------------------------------------------------------------------
    # Show the board, only used for debugging
    def print_board(self):
        print("%s %s %s" % (self.__spots['aa'] ,self.__spots['bb'],\
                            self.__spots['cc'] )) 
        print("%s %s %s" % (self.__spots['dd'] ,self.__spots['ee'],\
                            self.__spots['ff'] ))
        print("%s %s %s" % (self.__spots['gg'] ,self.__spots['hh'],\
                            self.__spots['ii'] ))
        
    # test to see if space is open
    # returns true if open
    # returns false if not open
    def space_open(self, spot):
        return self.__spots[spot] == ' '
    
    # Determine if there is a winner
    # True if there is a winner
    # False otherwise
    def is_game_over(self):        
        if (self.__spots['aa'] == self.__spots['bb'] == self.__spots['cc']) \
           and self.__spots['aa'] != ' ':
            win = True
            user = self.__spots['aa']
            #reason = 1
        elif (self.__spots['dd'] == self.__spots['ee'] == self.__spots['ff'])\
             and self.__spots['dd'] != ' ':
            win = True
            user = self.__spots['dd']
            #reason = 2
        elif (self.__spots['gg'] == self.__spots['hh'] == self.__spots['ii'])\
             and self.__spots['gg'] != ' ':
            win = True
            user = self.__spots['gg']
            #reason = 3
        elif (self.__spots['aa'] == self.__spots['ee'] == self.__spots['ii'])\
             and self.__spots['aa'] != ' ':
            win = True
            user = self.__spots['aa']
            #reason = 4
        elif (self.__spots['cc'] == self.__spots['ee'] == self.__spots['gg'])\
             and self.__spots['cc'] != ' ':
            win = True
            user = self.__spots['cc']
            #reason = 5
        elif (self.__spots['aa'] == self.__spots['dd'] == self.__spots['gg'])\
             and self.__spots['aa'] != ' ':
            win = True
            user = self.__spots['aa']
            #reason = 6
        elif (self.__spots['bb'] == self.__spots['ee'] == self.__spots['hh'])\
             and self.__spots['bb'] != ' ':
            win = True
            user = self.__spots['bb']
            #reason = 7
        elif (self.__spots['cc'] == self.__spots['ff'] == self.__spots['ii'])\
             and self.__spots['cc'] != ' ':
            win = True
            user = self.__spots['cc']
            #reason = 8
        # Tie Game - Every spot is taken
        elif not (self.__spots['aa'] == ' ' or self.__spots['bb'] == ' ' \
                  or self.__spots['cc'] == ' ' or self.__spots['dd'] == ' ' \
                  or self.__spots['ee'] == ' ' or self.__spots['ff'] == ' ' \
                  or self.__spots['gg'] == ' ' or self.__spots['hh'] == ' ' \
                  or self.__spots['ii'] ==' '):
            win = True #Just ends game, same way a win would for consistency 
            user = "It's a tie"
            reason = "Tie"
        else:
            win = False
            user = "No winner"
            reason = 9
        if win:
            self.set_winner(user)
        return (win)

        # Accessors
#---------------------------------------------------------------------------
    # Access to current state of players usernames
    def get_user1_name(self):
        return self.__user1
    
    def get_user2_name(self):
        return self.__user2
    
    
    # Access to current button color
    def get_button_color(self):
        return self.__button_color
    
    # Access to the the winner, returns 'X' or 'O'
    def get_winner(self):
        return self.__winner
    
    # Access player one score
    # Return Score as string
    def get_p1_score(self):
        return str(self.__p1_score)
    
    # Access player two score
    # return score as string
    def get_p2_score(self):
        return str(self.__p2_score)

    # Access to value of turn marker
    def get_turn_marker(self):
        return self.__turn_marker
    
    # Reset the game board to empty spaces again
    # Score stays the same
    # Reset turn value so player one is up again 
    def get_reset_button(self):
        return ' '
    
    # Param: winner, str, 'X' or 'O' or "It's a tie"
    # Create a string to display for winning message
    def get_win_string(self):
        return self.__winning_string
    
    def get_winner(self):
        return self.__winner
    
        
            
        
        # Mutators
#----------------------------------------------------------------------------    
    # Param: user names (string)
    def set_user1_name(self, user_name):
        self.__user1 = user_name
    def set_user2_name(self, user_name):
        self.__user2 = user_name

    # Sets the turn marker as either 'X' or 'O'
    def set_turn_marker_and_color(self, spot):
        if self.space_open(spot):
            if self.__turn % 2 == 0:
                self.__spots[spot] = self.__X_O[0]
                self.__button_color = self.__button_colors[self.__X_O[0]]
            elif self.__turn % 2 == 1:
                self.__spots[spot] = self.__X_O[1]
                self.__button_color = self.__button_colors[self.__X_O[1]]
            self.set_increment_player_turn()
            self.__turn_marker = self.__spots[spot]
        else:
            self.__turn_marker = self.__spots[spot]
            self.__button_color = \
                self.__button_colors[self.__spots[spot]]
            
            
        
    # Param: user that won the game, 'X' or 'O'
    # set the value of self.__winner to the username of that player
    def set_winner(self, user):
        if user == self.__X_O[0]:
            self.__winner = self.__user1
        elif user == self.__X_O[1]:
            self.__winner = self.__user2
        else:
            self.__winner = user

    # Param: value -string
    # used to set a variable as the value parmater
    def set(self, value):
        old_val = value
        
    # Set reset conditions
    def set_reset_button(self):
        self.__turn = 0
        for i in self.__NUM_2_SPOT:
            self.__spots[i] = ' '

    # Updates the player turn number
    # Used to keep track of which players turn it is
    def set_increment_player_turn(self):
        self.__turn += 1
        

    # Param: winner ,str, 'X' or 'O' or "It's a tie"
    # update the value of individual scores for each player based on winner
    def set_increment_score(self, winner):
        if winner == self.__user1:
            self.__p1_score += 1
        elif winner == self.__user2:
            self.__p2_score += 1

    def set_win_string(self, winner):
        if winner == "It's a tie":
            self.__winning_string = winner
        else:
            self.__winning_string = 'Congratulations %s, you win!' % \
                             (self.get_winner())
        
"""
TESTING
board_obj = TicTacToeGame()
                        
def refresh_board():
    board_obj.print_board()

print(board_obj.determine_winner())
while not ((board_obj.determine_winner())[0]) :

    user_one_pick = int(input("Input num between 0-8: "))
    board_obj.user_one_turn(user_one_pick)
    refresh_board()
    board_obj.determine_winner()
    print(board_obj.determine_winner())

    user_two_pick = int(input('Input num between 0 8: ' ))
    board_obj.user_two_turn(user_two_pick)
    refresh_board()
    board_obj.determine_winner()
    print(board_obj.determine_winner())
"""
    
                        

                        













        
        
    
