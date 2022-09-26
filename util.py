from random import randint
from os import system
import time

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_into_file(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def write_into_file_a(path,x):
    f = open(path, "a")
    f.write(str(x))
    f.close

def count_occurence(letter,word):
    idx = 0
    for i in range(len(word)):
        if letter == word[i]:
            idx = idx + 1
    return (idx)

def only_letter(word):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = 0
    for i in range(len(word)):
        if word[i] not in letter.upper():
            idx = idx + 1
    return(idx)

def check_pos(Word_To_Guess,My_word):
    color = ["🟥","🟧","🟩","🟨","⬛"]
    res = []
    letter = ""
    for i in range(len(Word_To_Guess)):
        if Word_To_Guess[i] == My_word[i]:
            res.append(color[2] + " ")
        elif Word_To_Guess[i] != My_word[i] and My_word[i] in Word_To_Guess:
            if count_occurence(My_word[i],Word_To_Guess) == 0 or count_occurence(My_word[i],My_word) != count_occurence(My_word[i],Word_To_Guess):
                if My_word[i] in Word_To_Guess and count_occurence(My_word[i],Word_To_Guess) == 1:
                    res.append(color[1] + " ")
                elif My_word[i] in Word_To_Guess and count_occurence(My_word[i],Word_To_Guess) > 1:
                    res.append(color[3] + " ")
                else:
                    res.append(color[0] + " ")
            else:
                res.append(color[1] + " ")
        elif Word_To_Guess[i] != My_word[i]:
            if count_occurence(My_word[i],Word_To_Guess) == 0 and My_word[i] in Word_To_Guess:
                res.append(color[0] + " ")
            elif count_occurence(My_word[i],Word_To_Guess) == 0 and My_word[i] not in Word_To_Guess:
                res.append(color[0] + " ")
            else:
                res.append(color[1] + " ")
    return (res)
        