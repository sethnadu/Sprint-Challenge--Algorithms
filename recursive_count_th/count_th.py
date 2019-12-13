'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # start total/count at 0
    total = 0

    def search_word(word):
        # all function to be able to use the total
        nonlocal total
        # break case
        if len(word) < 2:
            return total
        # look for two letters at a time
        if word[0:2] == 'th':
            # if found add 1 to total
            total +=1
        # Remove the two letter combination you found so it doesn't repeat
        word = word[1:]
        # Re run function as long as it dosen't hit break case
        search_word(word)
    # Call the function to start
    search_word(word)
    print("Total Count :", total)
    return total
