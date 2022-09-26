
from random import randint
from os import system
import time
from util import *
from tweet import *
import schedule

SIZE = 4006

class Var:
    word_len  = 0
    space_word = False
    letter_inside = ""
    position_of_letter = 0
    letter = "k"
    word = ""
    num_of_letter = 1

def letter_to_emoji(word):
    Eletter = ["🇦 ", "🇧 ", "🇨 ", "🇩 ", "🇪 ", "🇫 ", "🇬 ", "🇭 ", "🇮 ", "🇯 ", "🇰 ", "🇱 ", "🇲 ", "🇳 ", "🇴 ", "🇵 ", "🇶 ", "🇷 ", "🇸 ", "🇹 ", "🇺 ", "🇻 ", "🇼 ", "🇽 ", "🇾 ", "🇿 "]
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = ""
    color = ["🟥","🟧","🟩","🟨","⬛"]
    for i in range(len(word)):
        if word[i] in letter.upper():
            string = string + Eletter[letter.find(word[i])]
        else:
            string = string + word[i]
    return (string)

def main_game():
    all_word = print_file("list.txt")
    all_word = all_word.split("\n")
    rdm_word = random_line("list.txt",0,SIZE).replace("\n","").lower()
    NotFound = True
    Max_Attemp = 8
    nb = print_file("nb.txt")
    nbr = int(nb)
    output = []
    win = 0
    l_word = []
    final_list = []
    tweet_output = ""
    color = ["🟥","🟧","🟩","🟨","⬛"]
    make_tweet("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8")
    TIME = 5400
    time.sleep(TIME)
    to_tweet = ""
    current_date = time.strftime("%H:%M:%S")
    dhour = current_date[0:2]
    restart_at_8 = 32
    
    while NotFound:
        print("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8")
        #print(rdm_word)
        word = get_latest_tweet().upper()
        if len(word) == 5:
            result = check_pos(rdm_word.upper(),word.upper())
        else:
            result  = "X"
        if word.lower() == rdm_word.lower():
            NotFound = False
            win = 1
        else:
            print("Not Found")
            Max_Attemp = Max_Attemp - 1
        if Max_Attemp == 0:
            print("Tu as perdu le mot était " + rdm_word)
            NotFound = False
        if len(word) == 5:
            output.append(letter_to_emoji(word))
            output.append(''.join(result))
        if Max_Attemp != 0:
            to_tweet = '\n'.join(output)
        
        print(word,rdm_word)
        if win == 1:
            print("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n" + "Bravo tu as trouvé le mot" + "\n" + to_tweet)
            make_tweet("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n" + "Bravo tu as trouvé le mot" + "\n" + to_tweet)
            nbr = nbr + 1
            write_into_file("nb.txt",str(nbr))
            print((restart_at_8-int(dhour))*3600)
            time.sleep((restart_at_8-int(dhour))*3600)
            #time.sleep(20)
            main_game()

        elif NotFound == False:
            print("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n" + "Tu as perdu le mot était " + rdm_word + "\n" + to_tweet)
            make_tweet("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n" + "Tu as perdu le mot était " + rdm_word + "\n" + to_tweet)
            nbr = nbr + 1
            write_into_file("nb.txt",str(nbr))
            print((restart_at_8-int(dhour))*3600,restart_at_8-int(dhour))
            time.sleep((restart_at_8-int(dhour))*3600)
            #time.sleep(20)
            main_game()
        else:
            print("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n"+to_tweet)
            make_tweet("🤖#"+str(nb)+ " _LeMot_ " + str(Max_Attemp)+"/8" + "\n" + to_tweet)
            time.sleep(TIME)
            #time.sleep(20)


print("Launch")
current_date = time.strftime("%H:%M:%S")
dhour = current_date[0:2]
restart_at_8 = 32
time.sleep((restart_at_8-int(dhour))*3600)
main_game()