#  File: htmlChecker.py
#  Description: Checks an HTML file for valid tags
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E 
#  Unique Number: 54170
#
#  Date Created: 10/11/2017
#  Date Last Modified: 10/13/2017


# getTag function:
# read file by character
# when it gets to a '<', push it on a stack
# append everything after the '<' onto a string
# when it reaches a '>' or ' ' stop appending
# return the string as a tag

# creates the stack that will check for tags
class Stack (object):
    
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items[-1]

   def size (self):
      return len(self.items)
    
   def __str__(self):
      return str(self.items)


# this function returns a list of all tags in a given string
def getTag(string):
   
   tagList = []

   # 'check' is the bracket checker, and 'tag' is the content inside the brackets
   check = ''
   tag = ''
   
   i = 0  
   while i < len(string):

      char = string[i]

      # start saving the tag when a left angle bracket is found
      if char == '<':

         # 'check' indicates whether a left angle bracket has been used yet
         if check == '':        
            check += '<'
    
         else:
            print('error')
         
      # if right bracket found, tag is added to the tag list  
      if char == '>' or char == ' ':
         tag = tag[1:]
         if tag != '':
            tagList.append(tag)

         # reset 'tag' and 'check'
         tag = ''
         check = ''

      # builds the tag by each character after the left angle bracket 
      else:
         if check == '<':
            tag += char
         
      i += 1
      
   # returns a list of all the tags 
   return tagList
   

# this function checks for matching tags in the tag list         
def tagChecker(tagList):

   s = Stack()
   balanced = True
   exceptions = ["br", "meta", "hr"]
   VALIDTAGS = []
   i = 0
   while i < len(tagList) and balanced:

      firstTag = tagList[i]     
      if firstTag[0] != '/':

         # checks if the tag is in the exceptions list
         if (firstTag in exceptions):
            print("Tag", firstTag, "does not need to match:  stack is still ", str(s))
            if firstTag not in VALIDTAGS:
                  VALIDTAGS.append(firstTag)
                  print("New tag", firstTag, "found and added to list of valid tags")
            print()

         # if the tag is a start tag, push it onto the stack
         else:
            s.push(firstTag)
            if firstTag not in VALIDTAGS:
                  VALIDTAGS.append(firstTag)
                  print("New tag", firstTag, "found and added to list of valid tags")
            print("Tag", firstTag, "pushed: stack is now ", str(s))
            print()

      # if the tag is an end tag and matches the top of the stack,
      # pop the top of the stack to indicate a match
      top = s.peek()   
      if firstTag[0] == '/' and firstTag[1:] == top:
         s.pop()
         print("Tag", firstTag, "matches top of stack: stack is now", str(s))
         print()

      # if the tag is an end tag and doesn't match, indicate an error
      if firstTag[0] == '/' and firstTag[1:] != top:
         print("Error:  tag is ", firstTag, " but top of stack is ", top)
         print()
         balanced = False
         return
      
      i += 1

   # prints messages after process complete depending on stack contents
   if s.isEmpty():
      print("Processing complete. No mismatches found.")      
   else:      
      print("Processing complete. Unmatached tags remain on stack: ", str(s))

   print("\nThese are valid tags: \n", VALIDTAGS)
   print("\nThese are exceptions: \n", exceptions)
   return str(s)

   
def main():
   
   # opens the file for reading
   f = open('htmlfile.txt','r')
   line = f.readline()
   text = ''

   # adds each line to a string
   while line:
      text += str(line)
      line = f.readline()

   # retrieves a list of tags from the string
   listOfTags = getTag(text)
   print("This is the list of tags: ")
   print(listOfTags)
   print()

   # checks the tags for any mismatches
   tagChecker(listOfTags)

main()

