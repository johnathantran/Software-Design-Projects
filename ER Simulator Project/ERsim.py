#  File: ERsim.py
#  Description: simulates the queues of an emergency room
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E 
#  Unique Number: 54170
#
#  Date Created: 10/16/2017
#  Date Last Modified: 10/19/2017

# creates class Queue
class Queue():
    
    def __init__(self,name):
        self.patients = []
        self.name = name

    def isEmpty(self):
        return self.patients == []

    # modified version of dequeue, removes patient from front of the queue
    def treatNext(self):       
        print("   Treating ", self.patients[0], "from", self.name, "queue")      
        return self.patients.pop(0)     

    # modified version of enqueue, places a patient at the back of the queue
    def add(self,patient):
        self.patients.append(patient)
        print("Command: Add patient", patient, "to", self.name, "queue\n")
         
    
def main():
    
    # opens the file for reading
    f = open('ERsim.txt','r')
   
    # creates three queues for three different conditions
    Critical = Queue('Critical')
    Serious = Queue('Serious')
    Fair = Queue('Fair')
    
    # reads the lines in the file and splits them
    for line in f:
        line = line.split()
        
        # designates the command as the first item in the list
        command = line[0]

        # designates the condition and the patient name
        if len(line) == 3:
            cond = line[1]
            name = line[2]
            
        if len(line) == 2:
            who = line[1]

        # adds patients to appropriate queues
        if command == 'add':
            if cond == 'Critical':
                Critical.add(name)
            if cond == 'Serious':
                Serious.add(name)
            if cond == 'Fair':
                Fair.add(name)
        
            print("   Queues are:")
            print("   Fair:     ", Fair.patients)
            print("   Serious:  ", Serious.patients)
            print("   Critical: ", Critical.patients, "\n")

        # removes patients from appropriate queues upon treatment
        if command == 'treat':
            if (who == 'next'):
                print("Command: Treat next patient\n")

                if Critical.isEmpty() and Serious.isEmpty() and Fair.isEmpty():
                    print("   No patients in queue\n")
                    
                else:
                    # treats patients in order of priority
                    if Critical.isEmpty():
                        
                        if Serious.isEmpty():
                                Fair.treatNext()
                        else:
                            Serious.treatNext()
                    else:
                        Critical.treatNext()

                    print("   Queues are:")
                    print("   Fair:     ", Fair.patients)
                    print("   Serious:  ", Serious.patients)
                    print("   Critical: ", Critical.patients, "\n")
                
                
            # if the command designates to treat from a specified queue
            if (who == 'Critical') or (who == 'Serious') or (who == 'Fair'):
                print("Command: Treat next patient on", who, "queue\n")
                
                if Critical.isEmpty() and Serious.isEmpty() and Fair.isEmpty():
                    print("   No patients in queue")
                    
                else:
                    if who == 'Critical':
                        Critical.treatNext()
                    if who == 'Serious':
                        Serious.treatNext()
                    if who == 'Fair':
                        Fair.treatNext()
                  
                    print("   Queues are:")
                    print("   Fair:     ", Fair.patients)
                    print("   Serious:  ", Serious.patients)
                    print("   Critical: ", Critical.patients, "\n")

                
            # if the command designates to treat everyone  
            if who == 'all':
                print("Command: Treat all patients")

                # goes through all patients until all queues are empty
                notEmpty = True
                while notEmpty:

                    i = 0
                    if Critical.isEmpty():

                        j = 0
                        if Serious.isEmpty():
                            
                            k = 0
                            if Fair.isEmpty():
                                print("   No patients in queues\n")
                                notEmpty = False
                                break
                                
                            else:
                                while k < len(Fair.patients):
                                    Fair.treatNext()
                                    k += 1
                        else:
                            while j < len(Serious.patients):
                                Serious.treatNext()
                                j += 1
                    else:
                        while i < len(Critical.patients):
                            Critical.treatNext()
                            i += 1
                                              
                    print("   Queues are:")
                    print("   Fair:     ", Fair.patients)
                    print("   Serious:  ", Serious.patients)
                    print("   Critical: ", Critical.patients, "\n")

        # exits the program    
        if command == 'exit':
            print("Command: Exit")
            return

main()
