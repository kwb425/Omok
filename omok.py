# -*- coding: utf-8 -*-
##############################################################################
# Omok
#
#                                                      Written by Kim, Wiback.
#                                                          2016.04.02 Ver 1.1.
#                                                          2016.04.04 Ver 1.2.
#                                                          2016.04.05 Ver 1.3.
############################################################################## 
import random





#%% Board %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#



###################
# Size of the board
###################
def ask_board_size():
    five_or_nineteen = raw_input("Press 5 for 5 X 5. \nPress 19 for 19 X 19: ")
    if five_or_nineteen == "5":
        num_of_stones = 5 * 5
    elif five_or_nineteen == "19":
        num_of_stones = 19 * 19
    else:
        # Break out when user types wrong input.
        print "Wrong number. \n5 for 5 X 5 \n19 for 19 X 19"
        return
    return (int(five_or_nineteen), num_of_stones)



##########
# Displays
##########
def display_board_5(stones):
    print """              COM = X, YOU = O
   |   A  |   B  |   C  |   D  |   E  | 
   ------------------------------------
1  |  %s   |  %s   |  %s   |  %s   |  %s   |
   ------------------------------------
2  |  %s   |  %s   |  %s   |  %s   |  %s   |
   ------------------------------------
3  |  %s   |  %s   |  %s   |  %s   |  %s   |
   ------------------------------------
4  |  %s   |  %s   |  %s   |  %s   |  %s   |
   ------------------------------------
5  |  %s   |  %s   |  %s   |  %s   |  %s   |
   ------------------------------------
""" %(tuple(stones))
def display_board_19(stones):
    print """                                                               COM = X, YOU = O            
   |   A  |   B  |   C  |   D  |   E  |   F  |   G  |   H  |   I  |   J  |   K  |   L  |   M  |   N  |   O  |   P  |   Q  |   R  |   S  |
   --------------------------------------------------------------------------------------------------------------------------------------
1  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
2  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
3  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
4  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
5  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
6  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
7  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
8  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
9  |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
10 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
11 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
12 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
13 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
14 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
15 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
16 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
17 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
18 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
19 |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |  %s   |
   --------------------------------------------------------------------------------------------------------------------------------------
""" %(tuple(stones))



#################
# Basic variables
#################
# The computer's stone is X
computer = "X"
# The human's stone is O
human = "O"
# Asking the user the board size
(five_or_nineteen, num_of_stones) = ask_board_size()
# Latest board status will be saved here.
stones = [" "] * num_of_stones
# Corresponding weights will be stored here.
stones_weights = [0] * num_of_stones
# Optimal box indices for the computer's defence
optimal_choice = [0] * num_of_stones
# Column names
columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",\
"M", "N", "O", "P", "Q", "R", "S"]
# Row names
rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",\
"14", "15", "16", "17", "18", "19"]



########################################
# Row and column indices for later process
########################################
def row_col_indices(five_or_nineteen):
    dummy_numbers = range(0, five_or_nineteen * five_or_nineteen)
    
    ## The board's size 5
    if five_or_nineteen == 5:
        # Rows
        r_1 = [dummy_numbers[n] for n in range(0 * five_or_nineteen, 1 * five_or_nineteen)]
        r_2 = [dummy_numbers[n] for n in range(1 * five_or_nineteen, 2 * five_or_nineteen)]
        r_3 = [dummy_numbers[n] for n in range(2 * five_or_nineteen, 3 * five_or_nineteen)]
        r_4 = [dummy_numbers[n] for n in range(3 * five_or_nineteen, 4 * five_or_nineteen)]
        r_5 = [dummy_numbers[n] for n in range(4 * five_or_nineteen, 5 * five_or_nineteen)]
        # Columns
        c_1 = [dummy_numbers[n] for n in range(0, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_2 = [dummy_numbers[n] for n in range(1, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_3 = [dummy_numbers[n] for n in range(2, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_4 = [dummy_numbers[n] for n in range(3, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_5 = [dummy_numbers[n] for n in range(4, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        # Left diagonals / (beginning at top left corner)
        ld_1 = [dummy_numbers[n] for n in range(0, 0 * five_or_nineteen + 1, 1)]
        ld_2 = [dummy_numbers[n] for n in range(1, 1 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_3 = [dummy_numbers[n] for n in range(2, 2 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_4 = [dummy_numbers[n] for n in range(3, 3 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_5 = [dummy_numbers[n] for n in range(4, 4 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_6 = [dummy_numbers[n] for n in range(4 + 1 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_7 = [dummy_numbers[n] for n in range(4 + 2 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_8 = [dummy_numbers[n] for n in range(4 + 3 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_9 = [dummy_numbers[n] for n in range(4 + 4 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        # Right diagonals \ (beginning at top right corner)
        rd_1 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 1, 1 * five_or_nineteen, 1)]
        rd_2 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 2, 2 * five_or_nineteen, five_or_nineteen + 1)]
        rd_3 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 3, 3 * five_or_nineteen, five_or_nineteen + 1)]
        rd_4 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 4, 4 * five_or_nineteen, five_or_nineteen + 1)]
        rd_5 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 5, 5 * five_or_nineteen, five_or_nineteen + 1)] 
        rd_6 = [dummy_numbers[n] for n in range(1 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_7 = [dummy_numbers[n] for n in range(2 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_8 = [dummy_numbers[n] for n in range(3 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_9 = [dummy_numbers[n] for n in range(4 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        # Returning
        return (r_1, r_2, r_3, r_4, r_5, c_1, c_2, c_3, c_4, c_5, ld_1, ld_2, ld_3, ld_4, ld_5, ld_6, ld_7, ld_8, ld_9, rd_1, rd_2, rd_3, rd_4, rd_5, rd_6, rd_7, rd_8, rd_9)
        
    ## The board's size 19 
    elif five_or_nineteen == 19:
        # Rows        
        r_1 = [dummy_numbers[n] for n in range(0 * five_or_nineteen, 1 * five_or_nineteen)]
        r_2 = [dummy_numbers[n] for n in range(1 * five_or_nineteen, 2 * five_or_nineteen)]
        r_3 = [dummy_numbers[n] for n in range(2 * five_or_nineteen, 3 * five_or_nineteen)]
        r_4 = [dummy_numbers[n] for n in range(3 * five_or_nineteen, 4 * five_or_nineteen)]
        r_5 = [dummy_numbers[n] for n in range(4 * five_or_nineteen, 5 * five_or_nineteen)]
        r_6 = [dummy_numbers[n] for n in range(5 * five_or_nineteen, 6 * five_or_nineteen)]
        r_7 = [dummy_numbers[n] for n in range(6 * five_or_nineteen, 7 * five_or_nineteen)]
        r_8 = [dummy_numbers[n] for n in range(7 * five_or_nineteen, 8 * five_or_nineteen)]
        r_9 = [dummy_numbers[n] for n in range(8 * five_or_nineteen, 9 * five_or_nineteen)]
        r_10 = [dummy_numbers[n] for n in range(9 * five_or_nineteen, 10 * five_or_nineteen)] 
        r_11 = [dummy_numbers[n] for n in range(10 * five_or_nineteen, 11 * five_or_nineteen)]
        r_12 = [dummy_numbers[n] for n in range(11 * five_or_nineteen, 12 * five_or_nineteen)]
        r_13 = [dummy_numbers[n] for n in range(12 * five_or_nineteen, 13 * five_or_nineteen)]
        r_14 = [dummy_numbers[n] for n in range(13 * five_or_nineteen, 14 * five_or_nineteen)]
        r_15 = [dummy_numbers[n] for n in range(14 * five_or_nineteen, 15 * five_or_nineteen)]
        r_16 = [dummy_numbers[n] for n in range(15 * five_or_nineteen, 16 * five_or_nineteen)]
        r_17 = [dummy_numbers[n] for n in range(16 * five_or_nineteen, 17 * five_or_nineteen)] 
        r_18 = [dummy_numbers[n] for n in range(17 * five_or_nineteen, 18 * five_or_nineteen)]
        r_19 = [dummy_numbers[n] for n in range(18 * five_or_nineteen, 19 * five_or_nineteen)]
        # Columns        
        c_1 = [dummy_numbers[n] for n in range(0, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_2 = [dummy_numbers[n] for n in range(1, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_3 = [dummy_numbers[n] for n in range(2, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_4 = [dummy_numbers[n] for n in range(3, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_5 = [dummy_numbers[n] for n in range(4, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_6 = [dummy_numbers[n] for n in range(5, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_7 = [dummy_numbers[n] for n in range(6, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_8 = [dummy_numbers[n] for n in range(7, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_9 = [dummy_numbers[n] for n in range(8, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_10 = [dummy_numbers[n] for n in range(9, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_11 = [dummy_numbers[n] for n in range(10, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_12 = [dummy_numbers[n] for n in range(11, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_13 = [dummy_numbers[n] for n in range(12, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_14 = [dummy_numbers[n] for n in range(13, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_15 = [dummy_numbers[n] for n in range(14, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_16 = [dummy_numbers[n] for n in range(15, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_17 = [dummy_numbers[n] for n in range(16, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_18 = [dummy_numbers[n] for n in range(17, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        c_19 = [dummy_numbers[n] for n in range(18, five_or_nineteen * five_or_nineteen, five_or_nineteen)]
        # Left diagonals / (beginning at top left corner)
        ld_1 = [dummy_numbers[n] for n in range(0, 0 * five_or_nineteen + 1, 1)]
        ld_2 = [dummy_numbers[n] for n in range(1, 1 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_3 = [dummy_numbers[n] for n in range(2, 2 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_4 = [dummy_numbers[n] for n in range(3, 3 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_5 = [dummy_numbers[n] for n in range(4, 4 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_6 = [dummy_numbers[n] for n in range(5, 5 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_7 = [dummy_numbers[n] for n in range(6, 6 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_8 = [dummy_numbers[n] for n in range(7, 7 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_9 = [dummy_numbers[n] for n in range(8, 8 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_10 = [dummy_numbers[n] for n in range(9, 9 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_11 = [dummy_numbers[n] for n in range(10, 10 * five_or_nineteen + 1, five_or_nineteen - 1)]        
        ld_12 = [dummy_numbers[n] for n in range(11, 11 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_13 = [dummy_numbers[n] for n in range(12, 12 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_14 = [dummy_numbers[n] for n in range(13, 13 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_15 = [dummy_numbers[n] for n in range(14, 14 * five_or_nineteen + 1, five_or_nineteen - 1)]        
        ld_16 = [dummy_numbers[n] for n in range(15, 15 * five_or_nineteen + 1, five_or_nineteen - 1)]        
        ld_17 = [dummy_numbers[n] for n in range(16, 16 * five_or_nineteen + 1, five_or_nineteen - 1)]        
        ld_18 = [dummy_numbers[n] for n in range(17, 17 * five_or_nineteen + 1, five_or_nineteen - 1)]        
        ld_19 = [dummy_numbers[n] for n in range(18, 18 * five_or_nineteen + 1, five_or_nineteen - 1)]
        ld_20 = [dummy_numbers[n] for n in range(18 + 1 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_21 = [dummy_numbers[n] for n in range(18 + 2 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_22 = [dummy_numbers[n] for n in range(18 + 3 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_23 = [dummy_numbers[n] for n in range(18 + 4 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_24 = [dummy_numbers[n] for n in range(18 + 5 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_25 = [dummy_numbers[n] for n in range(18 + 6 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_26 = [dummy_numbers[n] for n in range(18 + 7 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_27 = [dummy_numbers[n] for n in range(18 + 8 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_28 = [dummy_numbers[n] for n in range(18 + 9 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_29 = [dummy_numbers[n] for n in range(18 + 10 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_30 = [dummy_numbers[n] for n in range(18 + 11 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_31 = [dummy_numbers[n] for n in range(18 + 12 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_32 = [dummy_numbers[n] for n in range(18 + 13 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_33 = [dummy_numbers[n] for n in range(18 + 14 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_34 = [dummy_numbers[n] for n in range(18 + 15 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]
        ld_35 = [dummy_numbers[n] for n in range(18 + 16 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]        
        ld_36 = [dummy_numbers[n] for n in range(18 + 17 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]        
        ld_37 = [dummy_numbers[n] for n in range(18 + 18 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen - 1)]                
        # Right diagonals \ (beginning at top right corner)
        rd_1 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 1, 1 * five_or_nineteen, 1)]
        rd_2 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 2, 2 * five_or_nineteen, five_or_nineteen + 1)]
        rd_3 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 3, 3 * five_or_nineteen, five_or_nineteen + 1)]
        rd_4 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 4, 4 * five_or_nineteen, five_or_nineteen + 1)]
        rd_5 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 5, 5 * five_or_nineteen, five_or_nineteen + 1)]
        rd_6 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 6, 6 * five_or_nineteen, five_or_nineteen + 1)]
        rd_7 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 7, 7 * five_or_nineteen, five_or_nineteen + 1)]
        rd_8 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 8, 8 * five_or_nineteen, five_or_nineteen + 1)]
        rd_9 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 9, 9 * five_or_nineteen, five_or_nineteen + 1)]
        rd_10 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 10, 10 * five_or_nineteen, five_or_nineteen + 1)]
        rd_11 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 11, 11 * five_or_nineteen, five_or_nineteen + 1)]
        rd_12 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 12, 12 * five_or_nineteen, five_or_nineteen + 1)]
        rd_13 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 13, 13 * five_or_nineteen, five_or_nineteen + 1)]
        rd_14 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 14, 14 * five_or_nineteen, five_or_nineteen + 1)]
        rd_15 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 15, 15 * five_or_nineteen, five_or_nineteen + 1)]
        rd_16 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 16, 16 * five_or_nineteen, five_or_nineteen + 1)]
        rd_17 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 17, 17 * five_or_nineteen, five_or_nineteen + 1)]
        rd_18 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 18, 18 * five_or_nineteen, five_or_nineteen + 1)]        
        rd_19 = [dummy_numbers[n] for n in range(1 * five_or_nineteen - 19, 19 * five_or_nineteen, five_or_nineteen + 1)]        
        rd_20 = [dummy_numbers[n] for n in range(1 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_21 = [dummy_numbers[n] for n in range(2 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_22 = [dummy_numbers[n] for n in range(3 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_23 = [dummy_numbers[n] for n in range(4 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]        
        rd_24 = [dummy_numbers[n] for n in range(5 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_25 = [dummy_numbers[n] for n in range(6 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_26 = [dummy_numbers[n] for n in range(7 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_27 = [dummy_numbers[n] for n in range(8 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]        
        rd_28 = [dummy_numbers[n] for n in range(9 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_29 = [dummy_numbers[n] for n in range(10 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_30 = [dummy_numbers[n] for n in range(11 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_31 = [dummy_numbers[n] for n in range(12 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]        
        rd_32 = [dummy_numbers[n] for n in range(13 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_33 = [dummy_numbers[n] for n in range(14 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_34 = [dummy_numbers[n] for n in range(15 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]
        rd_35 = [dummy_numbers[n] for n in range(16 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]        
        rd_36 = [dummy_numbers[n] for n in range(17 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]                
        rd_37 = [dummy_numbers[n] for n in range(18 * five_or_nineteen, five_or_nineteen * five_or_nineteen, five_or_nineteen + 1)]                
        # Returning
        return (r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17, r_18, r_19, \
        c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17, c_18, c_19, \
        ld_1, ld_2, ld_3, ld_4, ld_5, ld_6, ld_7, ld_8, ld_9, ld_10, ld_11, ld_12, ld_13, ld_14, ld_15, ld_16, ld_17, ld_18, ld_19, ld_20, ld_21, ld_22, ld_23, ld_24, ld_25, ld_26, ld_27, ld_28, ld_29, ld_30, ld_31, ld_32, ld_33, ld_34, ld_35, ld_36, ld_37, \
        rd_1, rd_2, rd_3, rd_4, rd_5, rd_6, rd_7, rd_8, rd_9, rd_10, rd_11, rd_12, rd_13, rd_14, rd_15, rd_16, rd_17, rd_18, rd_19, rd_20, rd_21, rd_22, rd_23, rd_24, rd_25, rd_26, rd_27, rd_28, rd_29, rd_30, rd_31, rd_32, rd_33, rd_34, rd_35, rd_36, rd_37)



#####################
# Surrounding indices
#####################
def surrounding(computational_coordinates):
    # Dummies
    surrounding_boxes_vertexes = [0] * 3
    surrounding_boxes_edges = [0] * 5
    surrounding_boxes_others = [0] * 8
    # Dummies which have double the size 
    surrounding_boxes_vertexes_double = [0] * 5
    surrounding_boxes_edges_double = [0] * 9
    surrounding_boxes_others_double = [0] * 16
    # Indices to be stored in accordance with different locations of the stones: single fence
    box_up = computational_coordinates - five_or_nineteen
    box_down = computational_coordinates + five_or_nineteen
    box_left = computational_coordinates - 1
    box_right = computational_coordinates + 1
    box_up_left = computational_coordinates - five_or_nineteen - 1
    box_up_right = computational_coordinates - five_or_nineteen + 1
    box_down_left = computational_coordinates + five_or_nineteen - 1
    box_down_right = computational_coordinates + five_or_nineteen + 1
    # Indices to be stored in accordance with different locations of the stones: double fence
    box_up_up = box_up - five_or_nineteen
    box_up_up_left = box_up_up - 1
    box_up_up_left_left = box_up_up_left - 1
    box_up_up_right = box_up_up + 1
    box_up_up_right_right = box_up_up_right + 1
    box_down_down = box_down + five_or_nineteen
    box_down_down_left = box_down_down - 1
    box_down_down_left_left = box_down_down_left - 1
    box_down_down_right = box_down_down + 1
    box_down_down_right_right = box_down_down_right + 1
    box_left_left = box_left - 1
    box_left_left_up = box_left_left - five_or_nineteen
    box_left_left_down = box_left_left + five_or_nineteen
    box_right_right = box_right + 1
    box_right_right_up = box_right_right - five_or_nineteen
    box_right_right_down = box_right_right + five_or_nineteen
    
    
    ## Vertexes
    # Top left vertex
    if computational_coordinates == 0:
        surrounding_boxes_vertexes[0] = box_down
        surrounding_boxes_vertexes[1] = box_right
        surrounding_boxes_vertexes[2] = box_down_right
        surrounding_boxes_vertexes_double[0] = box_down_down
        surrounding_boxes_vertexes_double[1] = box_down_down_right
        surrounding_boxes_vertexes_double[2] = box_down_down_right_right
        surrounding_boxes_vertexes_double[3] = box_right_right
        surrounding_boxes_vertexes_double[4] = box_right_right_down
    # Top right vertex
    elif computational_coordinates == five_or_nineteen - 1:
        surrounding_boxes_vertexes[0] = box_down
        surrounding_boxes_vertexes[1] = box_left
        surrounding_boxes_vertexes[2] = box_down_left
        surrounding_boxes_vertexes_double[0] = box_down_down
        surrounding_boxes_vertexes_double[1] = box_down_down_left
        surrounding_boxes_vertexes_double[2] = box_down_down_left_left
        surrounding_boxes_vertexes_double[3] = box_left_left
        surrounding_boxes_vertexes_double[4] = box_left_left_down
    # Bottom left vertex
    elif computational_coordinates == five_or_nineteen * (five_or_nineteen - 1):
        surrounding_boxes_vertexes[0] = box_up
        surrounding_boxes_vertexes[1] = box_right
        surrounding_boxes_vertexes[2] = box_up_right
        surrounding_boxes_vertexes_double[0] = box_up_up
        surrounding_boxes_vertexes_double[1] = box_up_up_right
        surrounding_boxes_vertexes_double[2] = box_up_up_right_right
        surrounding_boxes_vertexes_double[3] = box_right_right
        surrounding_boxes_vertexes_double[4] = box_right_right_up
    # Bottom right vertex
    elif computational_coordinates == five_or_nineteen * five_or_nineteen - 1:
        surrounding_boxes_vertexes[0] = box_up
        surrounding_boxes_vertexes[1] = box_left
        surrounding_boxes_vertexes[2] = box_up_left
        surrounding_boxes_vertexes_double[0] = box_up_up
        surrounding_boxes_vertexes_double[1] = box_up_up_left
        surrounding_boxes_vertexes_double[2] = box_up_up_left_left
        surrounding_boxes_vertexes_double[3] = box_left_left
        surrounding_boxes_vertexes_double[4] = box_left_left_up      
    
    ## Edges    
    # Top edge
    elif computational_coordinates in range(1, five_or_nineteen - 1):
        surrounding_boxes_edges[0] = box_down
        surrounding_boxes_edges[1] = box_left
        surrounding_boxes_edges[2] = box_right
        surrounding_boxes_edges[3] = box_down_left
        surrounding_boxes_edges[4] = box_down_right
        if computational_coordinates in range(2, five_or_nineteen - 2):        
            surrounding_boxes_edges_double[0] = box_down_down
            surrounding_boxes_edges_double[1] = box_down_down_left
            surrounding_boxes_edges_double[2] = box_down_down_left_left
            surrounding_boxes_edges_double[3] = box_down_down_right
            surrounding_boxes_edges_double[4] = box_down_down_right_right
            surrounding_boxes_edges_double[5] = box_left_left
            surrounding_boxes_edges_double[6] = box_left_left_down
            surrounding_boxes_edges_double[7] = box_right_right
            surrounding_boxes_edges_double[8] = box_right_right_down        
    # Bottom edge
    elif computational_coordinates in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):    
        surrounding_boxes_edges[0] = box_up
        surrounding_boxes_edges[1] = box_left
        surrounding_boxes_edges[2] = box_right
        surrounding_boxes_edges[3] = box_up_left
        surrounding_boxes_edges[4] = box_up_right    
        if computational_coordinates in range(five_or_nineteen * (five_or_nineteen - 1) + 2, five_or_nineteen * five_or_nineteen - 2):    
            surrounding_boxes_edges_double[0] = box_up_up
            surrounding_boxes_edges_double[1] = box_up_up_left
            surrounding_boxes_edges_double[2] = box_up_up_left_left
            surrounding_boxes_edges_double[3] = box_up_up_right
            surrounding_boxes_edges_double[4] = box_up_up_right_right
            surrounding_boxes_edges_double[5] = box_left_left
            surrounding_boxes_edges_double[6] = box_left_left_up
            surrounding_boxes_edges_double[7] = box_right_right
            surrounding_boxes_edges_double[8] = box_right_right_up
    # Left edge
    elif computational_coordinates in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
        surrounding_boxes_edges[0] = box_up
        surrounding_boxes_edges[1] = box_down
        surrounding_boxes_edges[2] = box_right
        surrounding_boxes_edges[3] = box_up_right
        surrounding_boxes_edges[4] = box_down_right  
        if computational_coordinates in range(2 * five_or_nineteen, five_or_nineteen * (five_or_nineteen - 2), five_or_nineteen):    
            surrounding_boxes_edges_double[0] = box_up_up
            surrounding_boxes_edges_double[1] = box_up_up_right
            surrounding_boxes_edges_double[2] = box_up_up_right_right
            surrounding_boxes_edges_double[3] = box_down_down
            surrounding_boxes_edges_double[4] = box_down_down_right
            surrounding_boxes_edges_double[5] = box_down_down_right_right
            surrounding_boxes_edges_double[6] = box_right_right
            surrounding_boxes_edges_double[7] = box_right_right_up
            surrounding_boxes_edges_double[8] = box_right_right_down
    # Right edge
    elif computational_coordinates in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
        surrounding_boxes_edges[0] = box_up
        surrounding_boxes_edges[1] = box_down
        surrounding_boxes_edges[2] = box_left
        surrounding_boxes_edges[3] = box_up_left
        surrounding_boxes_edges[4] = box_down_left
        if computational_coordinates in range(3 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 2), five_or_nineteen):    
            surrounding_boxes_edges_double[0] = box_up_up
            surrounding_boxes_edges_double[1] = box_up_up_left
            surrounding_boxes_edges_double[2] = box_up_up_left_left
            surrounding_boxes_edges_double[3] = box_down_down
            surrounding_boxes_edges_double[4] = box_down_down_left
            surrounding_boxes_edges_double[5] = box_down_down_left_left
            surrounding_boxes_edges_double[6] = box_left_left
            surrounding_boxes_edges_double[7] = box_left_left_up
            surrounding_boxes_edges_double[8] = box_left_left_down        

    ## Others
    else:
        surrounding_boxes_others[0] = box_up
        surrounding_boxes_others[1] = box_down
        surrounding_boxes_others[2] = box_left
        surrounding_boxes_others[3] = box_right
        surrounding_boxes_others[4] = box_up_left
        surrounding_boxes_others[5] = box_up_right
        surrounding_boxes_others[6] = box_down_left       
        surrounding_boxes_others[7] = box_down_right
        surrounding_boxes_others_double[0] = box_up_up - five_or_nineteen
        surrounding_boxes_others_double[1] = box_up_up_left - five_or_nineteen
        surrounding_boxes_others_double[2] = box_up_up_left_left - five_or_nineteen
        surrounding_boxes_others_double[3] = box_up_up_right - five_or_nineteen
        surrounding_boxes_others_double[4] = box_up_up_right_right - five_or_nineteen
        surrounding_boxes_others_double[5] = box_down_down - five_or_nineteen
        surrounding_boxes_others_double[6] = box_down_down_left - five_or_nineteen
        surrounding_boxes_others_double[7] = box_down_down_left_left - five_or_nineteen
        surrounding_boxes_others_double[8] = box_down_down_right - five_or_nineteen
        surrounding_boxes_others_double[9] = box_down_down_right_right - five_or_nineteen
        surrounding_boxes_others_double[10] = box_left_left - five_or_nineteen
        surrounding_boxes_others_double[11] = box_left_left_up - five_or_nineteen
        surrounding_boxes_others_double[12] = box_left_left_down - five_or_nineteen
        surrounding_boxes_others_double[13] = box_right_right - five_or_nineteen
        surrounding_boxes_others_double[14] = box_right_right_up - five_or_nineteen
        surrounding_boxes_others_double[15] = box_right_right_down - five_or_nineteen
        if box_up in range(1, five_or_nineteen - 1):
            # Pushing down right 
            if box_left in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
                surrounding_boxes_others_double[0] = box_up_up + 1 + five_or_nineteen
                surrounding_boxes_others_double[1] = box_up_up_left + 1 + five_or_nineteen
                surrounding_boxes_others_double[2] = box_up_up_left_left + 1 + five_or_nineteen            
                surrounding_boxes_others_double[3] = box_up_up_right + 1 + five_or_nineteen
                surrounding_boxes_others_double[4] = box_up_up_right_right + 1 + five_or_nineteen
                surrounding_boxes_others_double[5] = box_down_down + 1 + five_or_nineteen
                surrounding_boxes_others_double[6] = box_down_down_left + 1 + five_or_nineteen
                surrounding_boxes_others_double[7] = box_down_down_left_left + 1 + five_or_nineteen
                surrounding_boxes_others_double[8] = box_down_down_right + 1 + five_or_nineteen
                surrounding_boxes_others_double[9] = box_down_down_right_right + 1 + five_or_nineteen
                surrounding_boxes_others_double[10] = box_left_left + 1 + five_or_nineteen
                surrounding_boxes_others_double[11] = box_left_left_up + 1 + five_or_nineteen
                surrounding_boxes_others_double[12] = box_left_left_down + 1 + five_or_nineteen
                surrounding_boxes_others_double[13] = box_right_right + 1 + five_or_nineteen
                surrounding_boxes_others_double[14] = box_right_right_up + 1 + five_or_nineteen
                surrounding_boxes_others_double[15] = box_right_right_down + 1 + five_or_nineteen                                
            # Pushing down left
            elif box_right in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
                surrounding_boxes_others_double[0] = box_up_up - 1 + five_or_nineteen
                surrounding_boxes_others_double[1] = box_up_up_left - 1 + five_or_nineteen
                surrounding_boxes_others_double[2] = box_up_up_left_left - 1 + five_or_nineteen            
                surrounding_boxes_others_double[3] = box_up_up_right - 1 + five_or_nineteen
                surrounding_boxes_others_double[4] = box_up_up_right_right - 1 + five_or_nineteen
                surrounding_boxes_others_double[5] = box_down_down - 1 + five_or_nineteen
                surrounding_boxes_others_double[6] = box_down_down_left - 1 + five_or_nineteen
                surrounding_boxes_others_double[7] = box_down_down_left_left - 1 + five_or_nineteen
                surrounding_boxes_others_double[8] = box_down_down_right - 1 + five_or_nineteen
                surrounding_boxes_others_double[9] = box_down_down_right_right - 1 + five_or_nineteen
                surrounding_boxes_others_double[10] = box_left_left - 1 + five_or_nineteen
                surrounding_boxes_others_double[11] = box_left_left_up - 1 + five_or_nineteen
                surrounding_boxes_others_double[12] = box_left_left_down - 1 + five_or_nineteen
                surrounding_boxes_others_double[13] = box_right_right - 1 + five_or_nineteen
                surrounding_boxes_others_double[14] = box_right_right_up - 1 + five_or_nineteen
                surrounding_boxes_others_double[15] = box_right_right_down - 1 + five_or_nineteen
            # Pushing down
            else:
                surrounding_boxes_others_double[0] = box_up_up + five_or_nineteen
                surrounding_boxes_others_double[1] = box_up_up_left + five_or_nineteen
                surrounding_boxes_others_double[2] = box_up_up_left_left + five_or_nineteen            
                surrounding_boxes_others_double[3] = box_up_up_right + five_or_nineteen
                surrounding_boxes_others_double[4] = box_up_up_right_right + five_or_nineteen
                surrounding_boxes_others_double[5] = box_down_down + five_or_nineteen
                surrounding_boxes_others_double[6] = box_down_down_left + five_or_nineteen
                surrounding_boxes_others_double[7] = box_down_down_left_left + five_or_nineteen
                surrounding_boxes_others_double[8] = box_down_down_right + five_or_nineteen
                surrounding_boxes_others_double[9] = box_down_down_right_right + five_or_nineteen
                surrounding_boxes_others_double[10] = box_left_left + five_or_nineteen
                surrounding_boxes_others_double[11] = box_left_left_up + five_or_nineteen
                surrounding_boxes_others_double[12] = box_left_left_down + five_or_nineteen
                surrounding_boxes_others_double[13] = box_right_right + five_or_nineteen
                surrounding_boxes_others_double[14] = box_right_right_up + five_or_nineteen
                surrounding_boxes_others_double[15] = box_right_right_down + five_or_nineteen
        if box_down in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):    
            # Pushing up right
            if box_left in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
                surrounding_boxes_others_double[0] = box_up_up - five_or_nineteen + 1
                surrounding_boxes_others_double[1] = box_up_up_left - five_or_nineteen + 1
                surrounding_boxes_others_double[2] = box_up_up_left_left - five_or_nineteen + 1
                surrounding_boxes_others_double[3] = box_up_up_right - five_or_nineteen + 1
                surrounding_boxes_others_double[4] = box_up_up_right_right - five_or_nineteen + 1
                surrounding_boxes_others_double[5] = box_down_down - five_or_nineteen + 1
                surrounding_boxes_others_double[6] = box_down_down_left - five_or_nineteen + 1
                surrounding_boxes_others_double[7] = box_down_down_left_left - five_or_nineteen + 1
                surrounding_boxes_others_double[8] = box_down_down_right - five_or_nineteen + 1
                surrounding_boxes_others_double[9] = box_down_down_right_right - five_or_nineteen + 1
                surrounding_boxes_others_double[10] = box_left_left - five_or_nineteen + 1
                surrounding_boxes_others_double[11] = box_left_left_up - five_or_nineteen + 1
                surrounding_boxes_others_double[12] = box_left_left_down - five_or_nineteen + 1
                surrounding_boxes_others_double[13] = box_right_right - five_or_nineteen + 1
                surrounding_boxes_others_double[14] = box_right_right_up - five_or_nineteen + 1
                surrounding_boxes_others_double[15] = box_right_right_down - five_or_nineteen + 1      
            # Pushing up left    
            elif box_right in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
                surrounding_boxes_others_double[0] = box_up_up - five_or_nineteen - 1
                surrounding_boxes_others_double[1] = box_up_up_left - five_or_nineteen - 1
                surrounding_boxes_others_double[2] = box_up_up_left_left - five_or_nineteen - 1
                surrounding_boxes_others_double[3] = box_up_up_right - five_or_nineteen - 1
                surrounding_boxes_others_double[4] = box_up_up_right_right - five_or_nineteen - 1
                surrounding_boxes_others_double[5] = box_down_down - five_or_nineteen - 1
                surrounding_boxes_others_double[6] = box_down_down_left - five_or_nineteen - 1
                surrounding_boxes_others_double[7] = box_down_down_left_left - five_or_nineteen - 1
                surrounding_boxes_others_double[8] = box_down_down_right - five_or_nineteen - 1
                surrounding_boxes_others_double[9] = box_down_down_right_right - five_or_nineteen - 1
                surrounding_boxes_others_double[10] = box_left_left - five_or_nineteen - 1
                surrounding_boxes_others_double[11] = box_left_left_up - five_or_nineteen - 1
                surrounding_boxes_others_double[12] = box_left_left_down - five_or_nineteen - 1
                surrounding_boxes_others_double[13] = box_right_right - five_or_nineteen - 1
                surrounding_boxes_others_double[14] = box_right_right_up - five_or_nineteen - 1
                surrounding_boxes_others_double[15] = box_right_right_down - five_or_nineteen - 1
            # Pushing up 
            else:
                surrounding_boxes_others_double[0] = box_up_up - five_or_nineteen
                surrounding_boxes_others_double[1] = box_up_up_left - five_or_nineteen
                surrounding_boxes_others_double[2] = box_up_up_left_left - five_or_nineteen            
                surrounding_boxes_others_double[3] = box_up_up_right - five_or_nineteen
                surrounding_boxes_others_double[4] = box_up_up_right_right - five_or_nineteen
                surrounding_boxes_others_double[5] = box_down_down - five_or_nineteen
                surrounding_boxes_others_double[6] = box_down_down_left - five_or_nineteen
                surrounding_boxes_others_double[7] = box_down_down_left_left - five_or_nineteen
                surrounding_boxes_others_double[8] = box_down_down_right - five_or_nineteen
                surrounding_boxes_others_double[9] = box_down_down_right_right - five_or_nineteen
                surrounding_boxes_others_double[10] = box_left_left - five_or_nineteen
                surrounding_boxes_others_double[11] = box_left_left_up - five_or_nineteen
                surrounding_boxes_others_double[12] = box_left_left_down - five_or_nineteen
                surrounding_boxes_others_double[13] = box_right_right - five_or_nineteen
                surrounding_boxes_others_double[14] = box_right_right_up - five_or_nineteen
                surrounding_boxes_others_double[15] = box_right_right_down - five_or_nineteen
        if box_left in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
            # Pushing down right
            if box_up in range(1, five_or_nineteen - 1):
                pass
            # Pushing up right
            elif box_down in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):
                pass
            # Pusing right
            else:
                surrounding_boxes_others_double[0] = box_up_up + 1
                surrounding_boxes_others_double[1] = box_up_up_left + 1
                surrounding_boxes_others_double[2] = box_up_up_left_left + 1
                surrounding_boxes_others_double[3] = box_up_up_right + 1
                surrounding_boxes_others_double[4] = box_up_up_right_right + 1
                surrounding_boxes_others_double[5] = box_down_down + 1
                surrounding_boxes_others_double[6] = box_down_down_left + 1
                surrounding_boxes_others_double[7] = box_down_down_left_left + 1
                surrounding_boxes_others_double[8] = box_down_down_right + 1
                surrounding_boxes_others_double[9] = box_down_down_right_right + 1
                surrounding_boxes_others_double[10] = box_left_left + 1
                surrounding_boxes_others_double[11] = box_left_left_up + 1
                surrounding_boxes_others_double[12] = box_left_left_down + 1
                surrounding_boxes_others_double[13] = box_right_right + 1
                surrounding_boxes_others_double[14] = box_right_right_up + 1
                surrounding_boxes_others_double[15] = box_right_right_down + 1
        if box_right in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):    
            # Pushing down left
            if box_up in range(1, five_or_nineteen - 1):
                pass
            # Pushing up left
            elif box_down in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):
                pass
            # Pusing left
            else:
                surrounding_boxes_others_double[0] = box_up_up - 1
                surrounding_boxes_others_double[1] = box_up_up_left - 1
                surrounding_boxes_others_double[2] = box_up_up_left_left - 1
                surrounding_boxes_others_double[3] = box_up_up_right - 1
                surrounding_boxes_others_double[4] = box_up_up_right_right - 1
                surrounding_boxes_others_double[5] = box_down_down - 1
                surrounding_boxes_others_double[6] = box_down_down_left - 1
                surrounding_boxes_others_double[7] = box_down_down_left_left - 1
                surrounding_boxes_others_double[8] = box_down_down_right - 1
                surrounding_boxes_others_double[9] = box_down_down_right_right - 1
                surrounding_boxes_others_double[10] = box_left_left - 1
                surrounding_boxes_others_double[11] = box_left_left_up - 1
                surrounding_boxes_others_double[12] = box_left_left_down - 1
                surrounding_boxes_others_double[13] = box_right_right - 1
                surrounding_boxes_others_double[14] = box_right_right_up - 1
                surrounding_boxes_others_double[15] = box_right_right_down - 1            

    ## Returning    
    return (surrounding_boxes_vertexes, surrounding_boxes_edges, surrounding_boxes_others, surrounding_boxes_vertexes_double, surrounding_boxes_edges_double, surrounding_boxes_others_double)
    



        
#%% Movement %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#



#####################
# Coordinates control
#####################
# From user friendly (A1, E11, ...) to computational coordinates (1, 2, ...)
def coordination_transition(user_friendly, five_or_nineteen):
    
    ## Break out with any improper inputs.
    if user_friendly[0] not in columns:
        print "Wrong coordinate, check your board again."
        return
    elif user_friendly[1:] not in rows:
        print "Wrong coordinate, check your board again."
        return
    
    ## Finding out the column index
    for n in range(0, five_or_nineteen):
        if user_friendly[0] == columns[n]:
            column_index = n
            
            ## Finding out the row index
            for m in range(0, five_or_nineteen):
                # When the both row and column indices are found, proceed.                    
                if user_friendly[1:] == rows[m]:
                    row_index = m                    
                    computational_coordinates = five_or_nineteen * \
                    row_index + column_index
                    
    ## Returning (computational_coordinates; 1 2 3 ->
    ##                                       4 5 6 ->    
    ##                                       7 8 9 -> ...)           
    return computational_coordinates



###############
# One turn each
###############
def one_turn_each(stones, stones_weights, five_or_nineteen, optimal_choice):   
        
    ## Human's turn
    human_coordinates = raw_input("Your next move (e.g, A1 / E11 / C7)? ")
    # Calling coordination_transition
    computational_coordinates = \
    coordination_transition(human_coordinates, five_or_nineteen)
    # Avoiding any positional overlaps: the human's version
    while stones[computational_coordinates] != " ":
        print "That spot is already taken."
        # Receiving the user's input
        human_coordinates = raw_input("Your next move (e.g, A1 / E11 / C7)? ")
        # Calling coordination_transition
        computational_coordinates = \
        coordination_transition(human_coordinates, five_or_nineteen)
    # Drawing 'O' stone on the coordinate that the user has verified.
    stones[computational_coordinates] = human
    
    ## Computer's turn    
    # Calculating the weights for the computer to move 
    stones_weights = weighting(computational_coordinates)
    # The computer picking the optimal position (stalking defence)
    (surrounding_boxes_vertexes, surrounding_boxes_edges, surrounding_boxes_others, surrounding_boxes_vertexes_double, surrounding_boxes_edges_double, surrounding_boxes_others_double) = surrounding(computational_coordinates)
    # When the user places his or her stone on any vertex, follow him (her).
    if any(surrounding_boxes_vertexes) != 0:
        for n in surrounding_boxes_vertexes:
            optimal_choice[n] = stones_weights[n]            
        # If there is no place to put the stone in the single fence range, go double.
        if max(optimal_choice) == 0:
            optimal_choice = [0] * num_of_stones
            for n in surrounding_boxes_vertexes_double:
                optimal_choice[n] = stones_weights[n]            
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
        # If there is place to put the stone in the single fence range, stay.
        else:
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
    # When the user places his or her stone on any edge, follow him (her).           
    elif any(surrounding_boxes_edges) != 0:
        for n in surrounding_boxes_edges:
            optimal_choice[n] = stones_weights[n]            
        # If there is no place to put the stone in the single fence range, go double.
        if max(optimal_choice) == 0:
            optimal_choice = [0] * num_of_stones
            for n in surrounding_boxes_edges_double:
                optimal_choice[n] = stones_weights[n]            
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
        # If there is place to put the stone in the single fence range, stay.
        else:
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
    # When the user places his or her stone on others, follow him (her).                    
    elif any(surrounding_boxes_others) != 0:
        for n in surrounding_boxes_others:
            optimal_choice[n] = stones_weights[n]            
        # If there is no place to put the stone in the single fence range, go double.
        if max(optimal_choice) == 0:
            optimal_choice = [0] * num_of_stones
            for n in surrounding_boxes_others_double:
                optimal_choice[n] = stones_weights[n]            
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
        # If there is place to put the stone in the single fence range, stay.
        else:
            # Random maximal choosing process
            maxes = [n for n, m in enumerate(optimal_choice) if m == max(optimal_choice)] 
            optimal_position = random.choice(maxes)
            stones[optimal_position] = computer
            
    ## Preventing the computer from the overlapping
    stones_weights[computational_coordinates] = -100
    stones_weights[optimal_position] = -100
    ## Returning
    return (stones, stones_weights)



###############
# The weighting
###############
def weighting(computational_coordinates):

    ## For the board size 5
    if five_or_nineteen == 5:
        (r_1, r_2, r_3, r_4, r_5, c_1, c_2, c_3, c_4, c_5, ld_1, ld_2, ld_3, ld_4, ld_5, ld_6, ld_7, ld_8, ld_9, rd_1, rd_2, rd_3, rd_4, rd_5, rd_6, rd_7, rd_8, rd_9) = row_col_indices(five_or_nineteen)
        
        ## A stone with three directions around: top left vertex
        if computational_coordinates == 0:
            # Adding the weights to adjacent spaces (vertical-line)
            for n in c_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)        
            for n in rd_5:
                stones_weights[n] = stones_weights[n] + 1
            
        ## A stone with three directions around: top right vertex
        elif computational_coordinates == five_or_nineteen - 1: 
            # Adding the weights to adjacent spaces (vertical-line)                
            for n in c_5:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)        
            for n in r_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /)                
            for n in ld_5:
                stones_weights[n] = stones_weights[n] + 1
            
        ## A stone with three directions around: bottom left vertex
        elif computational_coordinates == five_or_nineteen * (five_or_nineteen - 1):
            # Adding the weights to adjacent spaces (vertical-line)        
            for n in c_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_5:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /)                
            for n in ld_5:
                stones_weights[n] = stones_weights[n] + 1
                
        ## A stone with three directions around: bottom right vertex
        elif computational_coordinates == five_or_nineteen * five_or_nineteen - 1:
            # Adding the weights to adjacent spaces (vertical-line)        
            for n in c_5:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_5:
                stones_weights[n] = stones_weights[n] + 1                 
            # Adding the weights to adjacent spaces (right diagonal \)                
            for n in rd_5:
                stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: top edge
        elif computational_coordinates in range(1, five_or_nineteen - 1):
            if computational_coordinates == 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 2:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_3:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 3:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_2:
                    stones_weights[n] = stones_weights[n] + 1
            
        ## A stone with five directions around: left edge
        elif computational_coordinates in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):
            if computational_coordinates == five_or_nineteen:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)    
                for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 2 * five_or_nineteen: 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)    
                for n in rd_7:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 3 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)    
                for n in rd_8:
                    stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: right edge
        elif computational_coordinates in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):
            if computational_coordinates == 2 * five_or_nineteen - 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_2:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 3 * five_or_nineteen - 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_3:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
                    
        ## A stone with five directions around: bottom edge
        elif computational_coordinates in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):
            if computational_coordinates == 4 * five_or_nineteen + 1:
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_8:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4 * five_or_nineteen + 2:
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_7:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4 * five_or_nineteen + 3:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
                                              
        ## A stone with eight directions around (on others)    
        elif computational_coordinates == 1 * five_or_nineteen + 1:
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_5:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 1 * five_or_nineteen + 2:    
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 1 * five_or_nineteen + 3:        
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_5:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_3:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 2 * five_or_nineteen + 1:    
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 2 * five_or_nineteen + 2:        
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_5:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_5:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 2 * five_or_nineteen + 3:    
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 3 * five_or_nineteen + 1:    
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_5:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_7:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 3 * five_or_nineteen + 2:        
            # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
        elif computational_coordinates == 3 * five_or_nineteen + 3:    
            # Adding the weights to adjacent spaces (vertical-line)      
                  for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)    
                  for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /) 
                  for n in ld_7:
                    stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)
                  for n in rd_5:
                    stones_weights[n] = stones_weights[n] + 1
    
    ## For the board size 19
    if five_or_nineteen == 19:
        (r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17, r_18, r_19, \
        c_1, c_2, c_3, c_4, c_5, c_6, c_7, c_8, c_9, c_10, c_11, c_12, c_13, c_14, c_15, c_16, c_17, c_18, c_19, \
        ld_1, ld_2, ld_3, ld_4, ld_5, ld_6, ld_7, ld_8, ld_9, ld_10, ld_11, ld_12, ld_13, ld_14, ld_15, ld_16, ld_17, ld_18, ld_19, ld_20, ld_21, ld_22, ld_23, ld_24, ld_25, ld_26, ld_27, ld_28, ld_29, ld_30, ld_31, ld_32, ld_33, ld_34, ld_35, ld_36, ld_37, \
        rd_1, rd_2, rd_3, rd_4, rd_5, rd_6, rd_7, rd_8, rd_9, rd_10, rd_11, rd_12, rd_13, rd_14, rd_15, rd_16, rd_17, rd_18, rd_19, rd_20, rd_21, rd_22, rd_23, rd_24, rd_25, rd_26, rd_27, rd_28, rd_29, rd_30, rd_31, rd_32, rd_33, rd_34, rd_35, rd_36, rd_37) = row_col_indices(five_or_nineteen)

        ## A stone with three directions around: top left vertex
        if computational_coordinates == 0:
            # Adding the weights to adjacent spaces (vertical-line)
            for n in c_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)        
            for n in rd_19:
                stones_weights[n] = stones_weights[n] + 1
        
        ## A stone with three directions around: top right vertex
        elif computational_coordinates == five_or_nineteen - 1: 
            # Adding the weights to adjacent spaces (vertical-line)                
            for n in c_19:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)        
            for n in r_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /)                
            for n in ld_19:
                stones_weights[n] = stones_weights[n] + 1
            
        ## A stone with three directions around: bottom left vertex
        elif computational_coordinates == five_or_nineteen * (five_or_nineteen - 1):
            # Adding the weights to adjacent spaces (vertical-line)        
            for n in c_1:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_19:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (left diagonal /)                
            for n in ld_19:
                stones_weights[n] = stones_weights[n] + 1
                
        ## A stone with three directions around: bottom right vertex
        elif computational_coordinates == five_or_nineteen * five_or_nineteen - 1:
            # Adding the weights to adjacent spaces (vertical-line)        
            for n in c_19:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (horizontal-line)
            for n in r_19:
                stones_weights[n] = stones_weights[n] + 1
            # Adding the weights to adjacent spaces (right diagonal \)                
            for n in rd_19:
                stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: top edge
        elif computational_coordinates in range(1, five_or_nineteen - 1):
            if computational_coordinates == 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_18:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 2:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_17:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 3:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_16:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_15:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 5:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_14:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 6:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_13:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 7:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_12:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 8:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_11:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 9:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_10:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 10:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_9:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 11:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                for n in rd_8:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 12:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_7:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 13:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 14:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_5:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 15:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 16:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_3:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 17:
                # Adding the weights to adjacent spaces (vertical-line)
                 for n in c_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                 for n in r_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                 for n in ld_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                    
                 for n in rd_2:
                    stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: left edge
        elif computational_coordinates in range(five_or_nineteen, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):
            if computational_coordinates == 1 * five_or_nineteen:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_2:
                    stones_weights[n] = stones_weights[n] + 1                                    
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_20:
                    stones_weights[n] = stones_weights[n] + 1                                
            elif computational_coordinates == 2 * five_or_nineteen: 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1            
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_3:
                    stones_weights[n] = stones_weights[n] + 1                
                # Adding the weights to adjacent spaces (right diagonal \)   
                for n in rd_21:
                    stones_weights[n] = stones_weights[n] + 1      
            elif computational_coordinates == 3 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_22:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_23:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 5 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_24:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 6 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_25:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 7 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_26:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 8 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_27:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 9 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)   
                for n in rd_28:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 10 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_29:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 11 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_30:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 12 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_31:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 13 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)   
                for n in rd_32:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 14 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_33:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 15 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)   
                for n in rd_34:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 16 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)   
                for n in rd_35:
                    stones_weights[n] = stones_weights[n] + 1                
            elif computational_coordinates == 17 * five_or_nineteen:                 
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_1:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)  
                for n in rd_36:
                    stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: right edge
        elif computational_coordinates in range(2 * five_or_nineteen - 1, five_or_nineteen * (five_or_nineteen - 1), five_or_nineteen):
            if computational_coordinates == 2 * five_or_nineteen - 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_2:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /) 
                for n in ld_20:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)
                for n in rd_2:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 3 * five_or_nineteen - 1:
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)
                for n in ld_21:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_3:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 4 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_22:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_4:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 5 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_23:
                    stones_weights[n] = stones_weights[n] + 1                                            
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_5:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 6 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_24:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_6:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 7 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_25:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_7:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 8 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_26:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_8:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 9 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_27:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_9:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 10 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_28:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \) 
                for n in rd_10:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 11 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_29:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_11:
                    stones_weights[n] = stones_weights[n] + 1 
            elif computational_coordinates == 12 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_30:
                    stones_weights[n] = stones_weights[n] + 1                                            
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_12:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 13 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_31:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_13:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 14 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_32:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_14:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 15 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_33:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_15:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 16 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_34:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_16:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 17 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_35:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_17:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen - 1:               
                # Adding the weights to adjacent spaces (vertical-line)
                for n in c_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                    
                for n in ld_36:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_18:
                    stones_weights[n] = stones_weights[n] + 1

        ## A stone with five directions around: bottom edge
        elif computational_coordinates in range(five_or_nineteen * (five_or_nineteen - 1) + 1, five_or_nineteen * five_or_nineteen - 1):
            if computational_coordinates == 18 * five_or_nineteen + 1:
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_2 :
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_20:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_36:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 2:
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_3:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_21:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_35:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 3:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_4:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_22:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_34:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 4:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_5:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_23:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_33:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 5:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_6:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_24:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_32:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 6:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_7:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_25:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_31:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 7:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_8:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_26:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_30:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 8:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_9:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_27:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_29:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 9:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_10:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_28:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_28:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 10:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_11:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_29:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_27:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 11:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_12:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_30:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_26:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 12:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_13:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_31:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_25:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 13:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_14:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_32:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_24:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 14:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_15:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_33:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_23:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 15:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_16:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_34:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_22:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 16:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_17:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_35:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_21:
                    stones_weights[n] = stones_weights[n] + 1
            elif computational_coordinates == 18 * five_or_nineteen + 17:                
                # Adding the weights to adjacent spaces (vertical-line)      
                for n in c_18:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (horizontal-line)    
                for n in r_19:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (left diagonal /)                
                for n in ld_36:
                    stones_weights[n] = stones_weights[n] + 1
                # Adding the weights to adjacent spaces (right diagonal \)                
                for n in rd_20:
                    stones_weights[n] = stones_weights[n] + 1
        ## A stone with eight directions around (on others)    
        # Too many instances, so giving up visibility.    
        else:                      
            for n in range(1, 18): 
                for m in range(1, 18):
                    # From 2nd to 18th row (each row is consisted of 17 columns.)
                    if computational_coordinates == eval("%d * five_or_nineteen + %d" %(n, m)):
                        # Adding the weights to adjacent spaces (vertical-line)
                        exec("for p in c_%d: stones_weights[p] = stones_weights[p] + 1" %(m + 1))
                        # Adding the weights to adjacent spaces (horizontal-line)    
                        exec("for p in r_%d: stones_weights[p] = stones_weights[p] + 1" %(n + 1))
                        # Adding the weights to adjacent spaces (left diagonal /)
                        exec("for p in ld_%d: stones_weights[p] = stones_weights[p] + 1" %(n + m + 1))
                        # Adding the weights to adjacent spaces (right diagonal \)                
                        exec("for p in rd_%d: stones_weights[p] = stones_weights[p] + 1" %(n + 19 - m))
                    
    ## Returning current board status
    return stones_weights



    
    
#%% Play control %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#



###################
# Win and Lose and Draw
###################
def win_lose_draw(stones, stones_weights):
            
    ## Row, column-wise inspections
    for n in range(five_or_nineteen):
        for m in range(five_or_nineteen - 4):
            if (stones[n * five_or_nineteen + m] == stones[n * five_or_nineteen + m + 1] ==  stones[n * five_or_nineteen + m + 2] ==  stones[n * five_or_nineteen + m + 3] == stones[n * five_or_nineteen + m + 4] == human) \
            or (stones[m * five_or_nineteen + n] == stones[(m + 1) * five_or_nineteen + n ] == stones[(m + 2) * five_or_nineteen + n ] == stones[(m + 3) * five_or_nineteen + n ] ==  stones[(m + 4) * five_or_nineteen + n ] == human):
                ## Display the current status
                if five_or_nineteen == 5:
                    display_board_5(stones)
                elif five_or_nineteen == 19:
                    display_board_19(stones)
                print "You win!"
                return
            elif (stones[n * five_or_nineteen + m] ==  stones[n * five_or_nineteen + m + 1] == stones[n * five_or_nineteen + m + 2] ==  stones[n * five_or_nineteen + m + 3] == stones[n * five_or_nineteen + m + 4] == computer) \
            or (stones[m * five_or_nineteen + n] ==  stones[(m + 1) * five_or_nineteen + n ] == stones[(m + 2) * five_or_nineteen + n ] == stones[(m + 3) * five_or_nineteen + n ] ==  stones[(m + 4) * five_or_nineteen + n ] == computer):
                ## Display the current status
                if five_or_nineteen == 5:
                    display_board_5(stones)
                elif five_or_nineteen == 19:
                    display_board_19(stones)                
                print "You lose!"                    
                return
                
    ## Diagonal inspections
    for n in range(five_or_nineteen - 4):
        for m in range(4, five_or_nineteen):
            if (stones[n * five_or_nineteen + m + 0 * (five_or_nineteen - 1)] == human and stones[n * five_or_nineteen + m + 1 * (five_or_nineteen - 1)] == human and stones[n * five_or_nineteen + m + 2 * (five_or_nineteen - 1)] == human and stones[n * five_or_nineteen + m + 3 * (five_or_nineteen - 1)] == human and stones[n * five_or_nineteen + m + 4 * (five_or_nineteen - 1)] == human) \
            or (stones[n * five_or_nineteen + (m - 4) + 0 * (five_or_nineteen + 1)] == human and stones[n * five_or_nineteen + (m - 4) + 1 * (five_or_nineteen + 1)] == human and stones[n * five_or_nineteen + (m - 4) + 2 * (five_or_nineteen + 1)] == human and stones[n * five_or_nineteen + (m - 4) + 3 * (five_or_nineteen + 1)] == human and stones[n * five_or_nineteen + (m - 4) + 4 * (five_or_nineteen + 1)] == human):
                ## Display the current status
                if five_or_nineteen == 5:
                    display_board_5(stones)
                elif five_or_nineteen == 19:
                    display_board_19(stones)                
                print "You win!"
                return 
            elif (stones[n * five_or_nineteen + m + 0 * (five_or_nineteen - 1)] == computer and stones[n * five_or_nineteen + m + 1 * (five_or_nineteen - 1)] == computer and stones[n * five_or_nineteen + m + 2 * (five_or_nineteen - 1)] == computer and stones[n * five_or_nineteen + m + 3 * (five_or_nineteen - 1)] == computer and stones[n * five_or_nineteen + m + 4 * (five_or_nineteen - 1)] == computer) \
            or (stones[n * five_or_nineteen + (m - 4) + 0 * (five_or_nineteen + 1)] == computer and stones[n * five_or_nineteen + (m - 4) + 1 * (five_or_nineteen + 1)] == computer and stones[n * five_or_nineteen + (m - 4) + 2 * (five_or_nineteen + 1)] == computer and stones[n * five_or_nineteen + (m - 4) + 3 * (five_or_nineteen + 1)] == computer and stones[n * five_or_nineteen + (m - 4) + 4 * (five_or_nineteen + 1)] == computer):
                ## Display the current status
                if five_or_nineteen == 5:
                    display_board_5(stones)
                elif five_or_nineteen == 19:
                    display_board_19(stones)                
                print "You lose!"
                return     
        
    ## Draw
    if " " not in stones:
        ## Display the current status
        if five_or_nineteen == 5:
            display_board_5(stones)
        elif five_or_nineteen == 19:
            display_board_19(stones)                
        print "Draw!"
        return
    
    ## Do not escape until the show is somehow over.         
    else:
        main(stones, stones_weights)



######
# Main
######
def main(stones, stones_weights):
    
    ## Starting with a the computer's turn
    if five_or_nineteen == 5:
        stones[12] = computer
        stones_weights[12] = -100        
        display_board_5(stones)
    elif five_or_nineteen == 19:
        stones[180] = computer
        stones_weights[180] = -100        
        display_board_19(stones)

    ## Turn taking (renewing optimal_choice for next stone's location to be setted properly)
    optimal_choice = [0] * num_of_stones    
    (latest_stones, latest_stones_weights) = one_turn_each(stones, stones_weights, five_or_nineteen, optimal_choice)
    win_lose_draw(latest_stones, latest_stones_weights)





#%% Module Importation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

## Run when objects' namespaces are located in main 
## (when imported, objects' are not given any namespaces.).
if __name__ == "__main__":
    main(stones, stones_weights)