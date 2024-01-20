def solution1():
    f = open("words.txt").read()
    f = f.split("\n")
    open("reversed_words.txt", "w").writelines(f)


def solution2():
    f = open("words.txt").read()
    f = f.replace("\n", "")
    open("reversed_words.txt", "w").write(f)


def solution3():
    f = open("words.txt").read()
    f = f.split("\n")
    output = "".join(f)
    open("reversed_words.txt", "w").write(output)

solution3()
