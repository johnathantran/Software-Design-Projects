#  File: Friends.py
#  Description: simulates the 'friend' functionality of a Facebook-like
#  application using linked lists
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E
#  Unique Number: 54170
#
#  Date Created: 11/09/2017
#  Date Last Modified: 11/10/2917



# creates class Node to be used in linked list
class Node (object):

   def __init__(self,initdata):
      self.data = initdata
      self.next = None

   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER


# creates class for Ordered linked list
class UnorderedList():

   def __init__(self):
      self.head = None

   def isEmpty (self):
      return self.head == None

   def add (self,item):
      # add a new Node to the beginning of an existing list
      current = self.head
      if (current == None):
         self.head = Node(item)
      else:
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

   def length (self):
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   # goes through the unordered linked list for the name of the User object
   def searchName (self,item):
      
      current = self.head
      found = False

      while (current != None and not found):
         
         if (current.getData().name == item):

            found = True
         else:

            current = current.getNext()

      if (found == False):
         return False

      return current.getData()

   # goes through the unordered linked list for the User object
   def searchUser(self,item):
      
      current = self.head
      found = False

      while (current != None and not found):
         
         if (current.getData() == item):

            found = True
         else:

            current = current.getNext()

      if (found == False):
         return False
      
      return current.getData()

   
   def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )

   def __str__(self):
        current = self.head
        s = "[ "
        while current != None:
           s += str(current.getData().name) + " "
           current = current.getNext()
        s += "]"
        return s


# creates class User and variables for the user name and friends
class User:

    def __init__(self,name):
       
        self.name = name
        self.friends = UnorderedList()

    
    def addFriend(self,other):

       # checks to see if the friend already exists in the user's friend's list
       if (self.friends.searchUser(other) != False):

          print("    " + self.name + " and " + other.name + " are already friends.\n")
          return

       print("    " + self.name + " and " + other.name + " are now friends.\n")
       
       self.friends.add(other)
       other.friends.add(self)
       
    def unfriend(self,other):

       # checks to see if the friend exists in the user's friend's list or not
       if (self.friends.searchUser(other) == False):

         print("    " + self.name + " and " + other.name + " aren't friends, so you can't unfriend them.\n")
         return

       print("    " + self.name + " and " + other.name + " are no longer friends.\n")

       self.friends.remove(other)
       other.friends.remove(self)

    # prints the list of the user's friends
    def listFriends(self):

       if (self.friends.length() == 0):

          print("    " + self.name + " has no friends.\n")
       else:

          print("    " + str(self.friends) + "\n")

    # checks to see if the users are friends
    def queryFriend(self,other):
         
       if (self.friends.searchUser(other) == False):

         print("    " + self.name + " and " + other.name + " are not friends.\n")
       else:

         print("    " + self.name + " and " + other.name + " are friends.\n")  

# main program
def main():

    allUsers = UnorderedList()

    # opens the file for reading
    f = open("FriendData.txt","r")
    
    for line in f:

        print("--> " + line, end = "")
        line = line.split()

        if (line[0] == "Person"):
           
           username = line[1]

           # checks to see if the given name already exists
           if (allUsers.searchName(username)!= False):

              print("    A person with name " + username + " already exists.\n")
              continue
            
           # creates a new User object given the name
           newUser = User(username)
           print("    " + username + " now has an account.\n")

           # add the new user to list of users
           allUsers.add(newUser)

        # case if asked to list friends
        if (line[0] == "List"):

            person = line[1]

            targetUser = allUsers.searchName(person)
            targetUser.listFriends()

        # case if asked to add friends
        if (line[0] == "Friend"):

           person = line[1]
           friend = line[2]

           if (person == friend):

             print("    A person cannot friend him/herself.\n")
             continue
            
           # finds the user to add the friend to the user's friend list
           foundUser = allUsers.searchName(person)
           friendUser = allUsers.searchName(friend)

           if (foundUser == False):

              print("    A person with name " + person + " does not currently exist.\n")
           elif (friendUser == False):

              print("    A person with name " + friend + " does not currently exist.\n")
           else:

              foundUser.addFriend(friendUser)

        # case if asked to unfriend two people
        if (line[0] == "Unfriend"):

           person = line[1]
           friend = line[2]

           # case if asked two of the same names are given
           if (person == friend):

             print("    A person cannot unfriend him/herself.\n")
             continue

           # obtains the user objects given the names
           foundUser = allUsers.searchName(person)
           friendUser = allUsers.searchName(friend)

           # if the user is not found in the list of users
           if (foundUser == False):

              print("    A person with name " + person + " does not currently exist.\n")

           elif (friendUser == False):

              print("    A person with name " + friend + " does not currently exist.\n")
           else:

              foundUser.unfriend(friendUser)

        # case if asked to check if two people are friends
        if (line[0] == "Query"):

           person = line[1]
           friend = line[2]

           if (person == friend):

             print("    A person cannot query him/herself.\n")
             continue
 
           foundUser = allUsers.searchName(person)
           friendUser = allUsers.searchName(friend)

           # cases if either user does not exist
           if (foundUser == False):

              print("    A person with name " + person + " does not currently exist.\n")
           elif (friendUser == False):

              print("    A person with name " + friend + " does not currently exist.\n")
           else:

              foundUser.queryFriend(friendUser)

        if (line[0] == "Exit"):

           print("\n    Exiting...")
           return

main()
