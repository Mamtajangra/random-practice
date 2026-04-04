# firstly we will load a file and replace some words according to user 
# "with " is using ,so that file is closing automatically there is no need to close file 
with open("d:\\python_practice\\alien.txt","r") as f:
    # open file in reading mode and store it in a variable story  
    story = f.read()
    # print(story)
    
    
    
    # store the words into set, it is helpful to remove duplicate
    words = set()
    # suppose starting word is not in story so we set -1 by default 
    start_word = -1
    # []  is using in placeholder and suppose [ is starting point of target and ] is ending point of target 
    target_start = "["
    target_end = "]"
    # now we are using a loop enumeration on story where we are checking the element with target if target found then store it in index i 
    for i ,char in enumerate(story):
        if char == target_start:
            start_word = i
            # another case, if target reaches to end point so that starting  point is not -1 at this  stage 
        if char== target_end and start_word!=-1:
            # now slicing ,because we want to extract ([]) word from story and add it to the set 
            word = story[start_word:i+1] 
            words.add(word)
            # for further checking  we use start word is -1 again for clear and easy checking 
            start_word = -1
            # display the found placeholder 
    print(words) 
    
    
    
    # suppose there is a dict named answers and user input are stored in this dict 
    answers = {}  
    # loop over the eliminating words and ask the user for input     
    for word in words:
        # input by users 
       answer = input(f"Enter replacement for {word}: ") 
        # add there input in dict with specific indices
       answers[word] = answer
#
# 
# 
#  again loop in words because our main motto is to replace all words with the user's input 
    for word in words:
        # replace all words with new one in story 
        story = story.replace(word,answers[word])
        # now  print the final version with user inputs
    print(story)        





