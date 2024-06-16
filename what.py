from PyDictionary import PyDictionary

dictionary = PyDictionary()

word_list = []

with open("word_list.txt", "r") as words:
    word_list = { w:dictionary.meaning( w.removesuffix("\n") ) for w in words.readlines() }

with open("nigger.txt", "w") as word:
    word.writelines(word_list)

