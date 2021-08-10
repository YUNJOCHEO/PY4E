a ="""안녕하세요. 
반갑습니다. 파이썬 공부는 정말 재밌습니다.
"""



def count_word(text, word):
    text_save = open("text.txt", "w")
    text_save.write(text)
    text_save.close()
    file = open("text.txt").read().strip().count(word)
    print(file)

count_word(a, "습니다1")