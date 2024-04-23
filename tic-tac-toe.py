import random as rand;

#Function that prints out table
def printTable(table):
    ct = 0;
    for row in table:
        print(str(row[0])+"|"+str(row[1])+"|"+str(row[2])); #print elements from table row
        ct = ct+1;
        if(ct!=3): #we don't need line after third row
            print("_____"); #print line between rows
    print("_____________________");
    
#Function that starts at the beginning as explanation
def intro():
    print("Here is the representation of table. Each number corresponds to field where it's placed.");
    print("Keep this representation in mind, in order to place letter on field, you need to insert corresponding number");
    print("");
    print("1|2|3");
    print("_____");
    print("4|5|6");
    print("_____");
    print("7|8|9");
    print("");


#Function that determines if the game is over
def currentState(table):
    if(table[0][0]==table[0][1]==table[0][2] and table[0][0]!=" "): #if character at field 1,2,3 is same and it's not equal to ' ' (space) then we have winner
        return table[0][0]; #we return winner's letter, which we use in order to identify winner
    elif(table[0][0]==table[1][0]==table[2][0] and table[0][0]!=" "): #same as above
        return table[0][0];
    elif(table[0][0]==table[1][1]==table[2][2] and table[0][0]!=" "): #same as above
        return table[0][0];
    elif(table[0][1]==table[1][1]==table[2][1] and table[0][1]!=" "): #same as above
        return table[0][1];
    elif(table[0][2]==table[1][2]==table[2][2] and table[0][2]!=" "): #same as above
        return table[0][2];
    elif(table[0][2]==table[1][1]==table[2][0] and table[0][2]!=" "): #same as above
        return table[0][2];
    elif(table[1][0]==table[1][1]==table[1][2] and table[1][0]!=" "): #same as above
        return table[1][0];
    elif(table[2][0]==table[2][1]==table[2][2] and table[2][0]!=" "): #same as above
        return table[2][0];
    elif(table[0][0]!=' ' and table[0][1]!=' ' and table[0][2]!=' ' and table[1][0]!=' ' and table[1][1]!=' ' and table[1][2]!=' ' and table[2][0]!=' ' and table[2][1]!=' ' and table[2][2]!=' '):
        return 'D'; #if all fields are filled and there is no winner, we return 'D', which stands for DRAW
    else:
        return 'C'; #in all other cases, game continues 
    
    
#Function to check if field is empty
def isEmpty(table,i,j):
    return(table[i][j]==' '); #if field is equal to ' ' (space), then returns True, otherwise returns False 


#Function that simulates player's turn
def playerTurn(table,letter):
    correctInput = False; #we are going to repeat input until player inserts number of empty field
    while(not correctInput):
        temp = False;
        print("Where do you want to place '"+letter+"'");
        try:
            field = int(input()); #try reading input and converting it to integer
        except ValueError:
            print("Insert integer!"); #if the input is not number, notify player to insert integer
            continue; #go to the start of while loop
        print("_____________________");
        if(field<1 or field>9): #if the input is number but not a number in range [1,9]
            continue; #go to the start of while loop
        if(field<4): #calculate indexes of field in table
            i=0; 
        elif(field>6):
            i=2;
        else:
            i=1;
        if(field%3 == 1):
            j = 0;
        elif(field%3 == 2):
            j = 1;
        else:
            j = 2;
        if(isEmpty(table,i,j)): #if the field is empty
            correctInput = True; #we can end turn
            table[i][j]=letter; #and add letter to table
            

#Function that simulates computer's turn    
def computerTurn(table,letter): 
    print("Computer plays:");
    i,j = rand.randint(0,2),rand.randint(0,2); #we pick a random field
    while(not isEmpty(table,i,j)): #try picking random field until we find one that is empty
        i,j = rand.randint(0,2),rand.randint(0,2);
    table[i][j]=letter; #add letter to table in field that was randomly picked
    

#choose number of players:
print("Do you want to play with another player(y/n):");
noOfPlayers = str(input()).upper(); 
while(noOfPlayers != 'Y' and noOfPlayers != 'N'): #reading number of players until we get correct input, 'Y' or 'N'; Y is for two players
    print("Wrong input, please insert 'Y' or 'N'")
    noOfPlayers = str(input()).upper();
    
    
#player decides what letter he wants to use
print("Do you want to be X or O?")
myLetter = str(input()).upper(); 
while(myLetter != 'X' and myLetter != 'O'): #letting first player pick his letter until he picks correct
    print("Wrong input, please insert 'X' or 'O'")
    myLetter = str(input()).upper();
    
    
#the computer/second player gets the other letter
if myLetter == 'X':
    compLetter = 'O';
else:
    compLetter = 'X';


#choose if you want to start first (only if playing against the computer):
if(noOfPlayers == 'N'):
    print("Do you want to play first(y/n):"); 
    playFirst = str(input()).upper();
    while(playFirst != 'Y' and playFirst != 'N'): 
        print("Wrong input, please insert 'Y' or 'N'")
        playFirst = str(input()).upper();
else:
    playFirst = 'Y';

    
#initializing table
table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]; #table is empty at the beginning


#game against computer
def onePlayerMode(table,myLetter,playFirst):
    print("Starting game against computer.");
    state = currentState(table); #getting current state of table
    while(state=='C'): #if we get 'C', that means that the game is still on
        if(playFirst=='Y'): #player and computer change their turns
            playerTurn(table,myLetter);
            playFirst = 'N';
            state = currentState(table);
            printTable(table);
        else:
            computerTurn(table,compLetter);
            playFirst = 'Y';
            state = currentState(table);
            printTable(table);
    if(state=='D'): #if we get 'D', that means table is full, but there is no winner
        print("It's a draw...");
    elif(state == myLetter): #if the letter we got is player's, he's the winner
        print("You win!");
    else:	#otherwise, computer wins
        print("You lose.");
    
    
#game against another player
def twoPlayerMode(table,myLetter,playFirst):
    print("Starting game against another player.");
    state = currentState(table);#getting current state of table
    while(state=='C'): #if we get 'C', that means that the game is still on
        if(playFirst=='Y'): #if it's first players turn
            playerTurn(table,myLetter); #start his turn
            playFirst = 'N'; #change to second player's turn
            state = currentState(table); #get current state of table
            printTable(table); #print table
        else: #same but for second player
            playerTurn(table,compLetter); 
            playFirst = 'Y';
            state = currentState(table);
            printTable(table);
    if(state=='D'):
        print("It's a draw...");
    elif(state == myLetter):
        print("Player one wins!");
    else:
        print("Player two wins!");


#Function that starts game
def startGame(table,letter,playf,noOfPlayers):
    intro();
    if(noOfPlayers == 'N'):
        onePlayerMode(table,letter,playf);
    else:
        twoPlayerMode(table,letter,playf);

        
#startGame        
startGame(table,myLetter,playFirst,noOfPlayers);