lines = open("words.txt").readlines()
# rev_lines = []
# for i in lines :
#     rev_lines.append(i[::-1])

rev_lines = [i[::-1] for i in lines]
open("reversed_words.txt","w").writelines(rev_lines)
