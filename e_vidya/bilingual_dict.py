def translate(bilingual_dict,english_words_list):
    swedish_list=[]
    for x in english_words_list:
        swedish_list.append(bilingual_dict[x])
    return swedish_list
bilingual_dict= {"merry":"god","christmas":"jul", "and":"och", "happy":"gott",
                 "new":"nytt", "year":"ar"}
english_words_list=["happy","year"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_list=translate(bilingual_dict,english_words_list)
print('The swedish words are:',swedish_list)
