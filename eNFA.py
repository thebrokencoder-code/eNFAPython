trans = {
          0 :{'e': 1,'a': 0},
          1 :{'e': 2,'b': 1},
          2 :{'c':2}
        }

initialState = [0]
finalState = [2]
eclosure = {0:[0],1:[1],2:[2]}

inputSymbols = ['a','b','c']
currentState = []

def initializationNFA(inputString):
    inputString = inputString.replace(" ","")    
    validSequence = True
    for char in inputString :
        if char not in inputSymbols:
            validSequence = False
    if validSequence == False:
        print("The input sequence is not valid")
    else:
        currentState.append(initialState[0])
        inputString = list(inputString)
        enfa(inputString)

def getNextState(current):
    stateList =[]
    for state in trans:
        if state == current:
            return trans[state]    
    
def enfa(sequence):
    while len(sequence) > 0 :
        if len(currentState) == 1 :
            current = currentState.pop(0)
            print("Current State is => " ,current)
            print("Current input symbol =>",sequence[0])
            nextState = getNextState(current)
            print("next available states = ",nextState)
            for value in nextState:
                if value == sequence[0]:
                    print("Next State =>" ,nextState[value])
                    currentState.append(nextState[value])
            else:
                if sequence[0] not in nextState.keys():
                    currentState.append(nextState['e'])
                    print("Epsilon Transition Occuring here..")
                    eclosure[current].append(nextState['e']) 
                    if len(currentState) == 0:
                        sequence.pop(0)
                        print(sequence)
                else:
                    sequence.pop(0)
                    print(sequence)
                    
    if currentState[0] == finalState[0]:
        print("string is valid as per the DFA")
        print("Epsilon closures :" ,eclosure)
    else:
        print("String is not valid as per the DFA")
    
def enfaRun():
    option = int(input ("Select the option : 1.Test String in eNFA 2. Exit : "))
    if option == 1:
        inputString = str(input("Enter the pattern in a,b,c : "))
        initializationNFA(inputString)
        enfaRun()
    elif option == 2:
        return "Thanks"
    else:
        print("Please enter a valid input")
        enfaRun()
enfaRun()


            
