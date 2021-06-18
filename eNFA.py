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

def getEClosure():
    temp =[]
    for key in trans:
        if 'e' in trans[key]:
            eclosure[key].append(trans[key]['e'])
            if 'e' in trans[trans[key]['e']]:
                eclosure[key].append(trans[trans[key]['e']]['e'])               
    print(eclosure)
        
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
    if len(sequence) == 0:
        while len(currentState) > 0:
            current = currentState.pop(0)
            print("Current State ", current)
            nextState = getNextState(current)
            print("Next State",nextState)
            currentState.append(nextState['e'])
            print("Next upcoming state ",currentState)
            if currentState[0] == finalState[0]:
                print("String is accepted with Epsilon Transitions")
                currentState.clear()
                return
            else:
                continue
    else:
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
                        if 'e' not in nextState.keys():
                            sequence.pop(0)
                            if len(sequence)==0:
                                print("String is Invalid as per the NFA")
                                return
                            else:
                                currentState.append(current)
                        else:    
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
        print("string is valid as per the NFA")
        print("Epsilon closures :" ,eclosure)
        currentState.clear()
        print(currentState)
    else:
        print("String is not valid as per the NFA")
    
def enfaRun():
    option = int(input ("Select the option : 1.Test String in eNFA 2. Exit 3.getEClosure : "))
    if option == 1:
        inputString = str(input("Enter the pattern in a,b,c : "))
        initializationNFA(inputString)
        enfaRun()
    elif option == 2:
        return "Thanks"
    elif option == 3:
        getEClosure()
    else:
        print("Please enter a valid input")
        enfaRun()
enfaRun()


    
    


            
