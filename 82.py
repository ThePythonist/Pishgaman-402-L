lines = open("words.txt").readlines()
rev_lines = lines[::-1]
open("reversed_words.txt","w").writelines(rev_lines)
