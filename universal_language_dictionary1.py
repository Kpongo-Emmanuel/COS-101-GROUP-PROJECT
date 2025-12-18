
Languages = 'Tiv = "a"\nIgbo = "b"\nJenjo = "c"\n'               #  PLEASE PUT YOUR LANGUAGE DIRECTLY BESIDE THE "\n" (no spacing) in the order you see (i.e \nYoruba = "c") the fifth person should not include the "\n" after their language
eng_words = 'come\ntake\nsee\ngo\neat\nhouse\nsleep\nwalk\nwork\nplay\nask\nfood\nwater\nplease\neyes\nmake\nname\nlike\nlove\ngood'
print('Welcome to the universal dictionary you may choose from the following languages')
print(Languages)

language_choice = input('Which language do you want to use?')
if language_choice == 'a':
        print('you have chosen "Tiv" language, you may now choose from the following words to translate')
        print(eng_words)
        Tiv_dict = {'come': 'vah', 'take': 'ngohol', 'see': 'nenge', 'go': 'yem', 'eat': 'ya', 'house': 'yah',
                    'sleep': 'yav', 'walk': 'zande', 'work': 'tom', 'play': 'numbe', 'ask': 'pine', 'food': 'kwaghyan',
                    'water': 'ngeren', 'please': 'nzamber', 'eyes': 'ashe', 'make': 'er', 'name': 'ti', 'like': 'sow',
                    'love': 'dooshima', 'good': 'doo'}
        while 1 == 1:
            word = input('what word would you like to translate?')
            if word in Tiv_dict:
                print(word, 'means', Tiv_dict[word], 'in Tiv')
            else:
                 print("please choose from the list of words")
if language_choice == 'b':
    print('you have chosen "Igbo" language, you may now choose from the following words to translate.') #this is for Treasure
#---> Print your list of english words on this line (you can delete this)
#then yea you can paste your code here->

if language_choice == 'c':
    print('you have chosen "Jenjo" language, you may now choose from the following words to translate') #this is for Pheeyamila
#---> Print your list of english words on this line (you can delete this)
#then yea you can paste your code here->

if language_choice == 'd':
    print('you have chosen "Your_language" language, you may now choose from the following words to translate')  # this is for Uriel, please replace 'Your_language' with your language for the dictionary
    # ---> Print your list of english words on this line (you can delete this)
    # then yea you can paste your code here->

if language_choice == 'e':
    print('you have chosen "Your_language" language, you may now choose from the following words to translate')  # this is for Alero, please replace 'Your_language' with your language for the dictionary
    # ---> Print your list of english words on this line (you can delete this)