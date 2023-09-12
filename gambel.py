import random  # to get the random values


MAX_LINES=3    #constant values so caps
MAX_BET = 100  # to set max amount on a line
MIN_BET=1    

ROWS=3  # number of rows and cols in a slot machine cols for reel
COLS=3

symbol_count={     # dictionary to set the values for the items in the reel ex A is most valuable 
                   # i.e EVERY SINGLE REEL HAS 2A's 4B's   ... 
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={     # dictionary to set the values for the items in the reel ex A is most valuable 
                   # i.e EVERY SINGLE REEL HAS 2A's 4B's   ... 
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


# to check 3 in a row and the winnings
def check_winnings(columns,lines,bet,value):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line] #the symbol we need to check is the 1st symbol of the line zero and all the symbols must be same for a win
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+= value[symbol]*bet
            winnings_lines.append(line+1)  # the winning line 
    return winnings,winnings_lines







# inorder to gnerate the slot machine using these values
def get_slot_machine_spin(rows,cols,symbols):
    # what symbols in each cols(3) 
    all_symbols=[]
    for symbol,symbol_count in symbols.items():  # fill the list all_symbols to the number of values for each item in symbol 
        for i in range(symbol_count):               # ex A gets added to the list two times 
            all_symbols.append(symbol)

    columns=[]
    for col in range(cols): # for every column we need to generate rows number of symbols
        column=[]
        current_symbols=all_symbols[:] #slice operator so we does a copy
        
        for row in range(rows):        
            value=random.choice(current_symbols)
            current_symbols.remove(value) # after selecteing 1 random value that should be removed from the current list
            column.append(value)          # ex if 1 A is selected as the value then for that column there can be one more A atmost
                                          # or for that row we can get only one A's so we need to remove the second value
        columns.append(column)    
            
    return columns        
            
def print_solt_machine(columns):
    # flip the rows to represent in the columns (reels) so flipping opearation 
    # TRANSPOSING OPERATION
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns)-1:  # last column should not have seperation so 
                print(column[row],"|",end=" | ") # to seperate using pipe operator            
            else:
                print(column[row],end="")
        
        print()        
            
# to get the inital amount to gambel
def deposit():
    while True: # deposit until get a valid amount
        amount=input("What would you like to deposit? 💲")
        if amount.isdigit(): # check if amount is positive and should be a digit 
            amount = int(amount) # string to int
            if amount>0:
                break
            else:
                print("Amount must be Greater then 0!!!")
        else:
            print("Please Enter a Number.")        
     
    return amount        

# to get the number of lines from the user to bet
def get_number_of_lines():
    while True: # deposit until get a valid number of lines
        lines=input("Enter the Number of Lines to bet on(1-"+str(MAX_LINES)+")?")  # max number of lines is ued to dynamic
        if lines.isdigit(): # check if lines is positive and should be a digit 
            lines = int(lines) # string to int
            if 1<=lines<=MAX_LINES: # should lie between 1 and maxlines
                break
            else:
                print("Enter a valid number of lines!!")
        else:
            print("Please Enter a Number.")        
     
    return lines 

def get_bet():
    while True: # deposit until get a valid amount
        amount=input("What would you like to Bet on Each line? 💲")
        if amount.isdigit(): # check if bet amount is positive and should be a digit 
            amount = int(amount) # string to int
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be.{MIN_BET}-{MAX_BET}")
        else:
            print("Please Enter a Number.")        
     
    return amount   


def spin(balance):
    lines= get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        
        if total_bet>balance:
            print(f"You do not have enough to bet that amount!!! Your current balance is :{balance}") # to check if bet is < balance
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
   
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    
    print_solt_machine(slots)
    
    winnings,winning_lines= check_winnings(slots,lines,bet,symbol_value)
    
    
    print(f"YOU WON {winnings}!!")
    
    print(f"YOU WON ON LINES:",*winning_lines)
    
    return winnings-total_bet
    

def main():
    balance = deposit()
    while True:
        print(f"CURRENT BALANCE IS ${balance}")
        ans=input("Press enter to play (q to quit):")
        
        if ans=='q':
            break
        balance+=spin(balance)
        
    print(f"YOU LEFT WITH ${balance}")    
        
main()     