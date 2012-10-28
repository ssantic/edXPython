from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all possible
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList) == True:


            # Find out how much making that word is worth
            score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if score > maxScore:

                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word

    # return the best word you found.
    return bestWord




#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    """
    totalScore = 0
    origHandlen = calculateHandlen(hand)
    while calculateHandlen(hand) > 0:
        print "Current Hand:",
        displayHand(hand)
        word = compChooseWord(hand, wordList)
        if word == None:
            break
        else:
            totalScore = totalScore + getWordScore(word, origHandlen)
            print '"%s" earned %d points. Total: %d points' % (word, getWordScore(word, origHandlen), totalScore)
            hand = updateHand(hand, word)
    print 'Total score: ' + str(totalScore) + ' points.'



#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    iter = 0

    while True:
        command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        if command == 'n':
            hand = dealHand(n)
            iter = 1
            while True:
                playCommand = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                if playCommand == 'u':
                        playHand(hand.copy(), wordList, n)
                        break
                elif playCommand == 'c':
                        compPlayHand(hand.copy(), wordList)
                        break
                else:
                        print "Invalid command."

        elif command == 'r':
            if iter == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                while True:
                       playCommand = raw_input('Enter u for the user to play the hand, or c for the computer to play the hand: ')
                       if playCommand == 'u':
                           playHand(hand.copy(), wordList, n)
                           break
                       elif playCommand == 'c':
                           compPlayHand(hand.copy(), wordList)
                           break
                       else:
                           print "Invalid command."

        elif command == 'e':
            return
            break
        else:
            print "Invalid command."


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    n = HAND_SIZE
    playGame(wordList)

    print "Goodbye!"
