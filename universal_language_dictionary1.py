Languages = 'Tiv = "a"\nIgbo = "b"\nJenjo = "c"\nEfik = d"\nYoruba = "e"'              #  PLEASE PUT YOUR LANGUAGE DIRECTLY BESIDE THE "\n" (no spacing) in the order you see (i.e \nYoruba = "c") the fifth person should not include the "\n" after their language
Tiv_dictionary = {'come': 'vah', 'take': 'ngohol', 'see': 'nenge', 'go': 'yem', 'eat': 'ya', 'house': 'yah',
                                'sleep': 'yav', 'walk': 'zande', 'work': 'tom', 'play': 'numbe', 'ask': 'pine', 'food': 'kwaghyan',
                                'water': 'ngeren', 'please': 'nzamber', 'eyes': 'ashe', 'make': 'er', 'name': 'ti', 'like': 'sow',
                                'love': 'dooshima', 'good': 'doo'}

jenjo_dictionary ={
              "Water": "Mirit","Air": "Fɔli","Fire": "Fayol","Earth": "Kana","Tree": "Gasorund",'Cat':"Nak",
              "Moon":"kili","Red": "Rudu","Purple": "Puruli", "Brother": "Bumia","Sister": "Sissma", "Father": "Banito",
              "Sand": "Sanda", "Dog":"Mush", "Man":"Gorio","Phone": "Telenouy", "Hammer": "Garia",
              "Story": "Kima","Bed": "Lakm","Tall":"Talero"}

Efik_dictionary = {"hello": "mfo", "goodbye": "ka do", "thank you": "sosongo", "yes": "iyo", "no": "mba",
                   "water": "mmong",
                   "food": "udon", "house": "ufok", "man": "eka", "woman": "edi", "child": "eyen", "friend": "eka inam",
                   "love": "ima",
                   "school": "ufok mme", "book": "mbuk", "sun": "utong", "moon": "onen", "money": "owo",
                   "work": "utomo", "name": "enyin"}
Tiv_dict_words = 'come\ntake\nsee\ngo\neat\nhouse\nsleep\nwalk\nwork\nplay\nask\nfood\nwater\nplease\neyes\nmake\nname\nlike\nlove\ngood'
Jenjo_dict_words = 'Water\nAir\nFire\nEarth\nTree\nCat\nMoon\nRed\nPurple\nBrother\nSister\nFather\nSand\nDog\nMan\nPhone\nHammer\nStory\nBed\nTall'
Igbo_dict_words = 'Hello\nPlease\nThank you \nNo\nYes\nChair\nCup\nMother\nFather\nChild\nWater\nRoad\nHouse\nBook\nEye\nHead\nGround\nBody\nDay\nMoney'
Efik_dict_words = 'hello\ngoodbye\nthank you\nyes\nno\nwater\nfood\nhouse\nman\nwoman\nchild\nfriend\nlove\nschool\nbook\nsun\nmoon\nmoney\nwork\nname'
print('Welcome to the universal dictionary you may choose from the following languages')
print(Languages)
while True:
        language_choice = input('Which language do you want to use?')
        if language_choice == 'a':
                print('you have chosen "Tiv" language, you may now choose from the following words to translate:')
                print(Tiv_dict_words)

                Tiv_word = input('what word would you like to translate?')
                if Tiv_word in Tiv_dictionary:
                    print(Tiv_word, 'means', Tiv_dictionary[Tiv_word], 'in Tiv')
                else:
                     print("please choose from the list of words")


        if language_choice == 'b':
            print('you have chosen "Igbo" language, you may now choose from the following words to translate:') #this is for Treasure
            print(Igbo_dict_words)
            Igbo_word = input('what word would you like to translate')
            print("welcome to Treasure igbo dictionary")
            print("feel free to search for a word of your choice")
            print("Dictionary for igbo languages" , "please enter a word")
            my_dictionary ={'Hello' : 'Ndewo' , 'Please' : 'Biko' , 'Thank you' : 'Daalu' , 'No' : 'Mba' , 'Yes' : 'Ee' , 'Chair' : 'Oche' , 'Cup' : ''Iko' , 'Mother' : 'Nne' , 'Father' : 'Nna' , 'Child' : 'Nwa' , 'Water' : 'Mmiri' , 'Road' : 'Uzo', 'House' : 'Ulo' , 'Book' : 'Akwukwo' , 'Eye' : 'Anya' , 'Head' : 'Isi' , 'Ground' : 'Ala' , 'Body' : 'Ahu' , 'Day' : 'Ubochi' , 'Money' : 'Ego'}             
            print(my_dictionary)
            language = my_dictionary['Hello']
            print(language)
            while true:
                 word = input("Enter word")
                 if word in my_dictionary:
                     print(my_dictionary[word])
        if language_choice == 'c':
            print('you have chosen "Jenjo" language, you may now choose from the following words to translate:') #this is for Pheeyamila
            print(Jenjo_dict_words)
            Jenjo_word = input('what word do you want to translate?')
            if  Jenjo_word in jenjo_dictionary:
              print(Jenjo_word,'means',jenjo_dictionary[Jenjo_word], 'in jenjo')
            else:
              print("apologies word not found ,select from available words")



        if language_choice == 'd':
            print('you have chosen "Efik" language, you may now choose from the following words to translate:')
            print(Efik_dict_words)
            Efik_word = input('what word do you wish to translate?')

            if Efik_word in Efik_dictionary :
                print(Efik_word,'means',Efik_dictionary[Efik_word], 'in Efik')
            else:
                    print("Sorry, that word is not in the dictionary.")


        if language_choice == 'e':
            print('you have chosen Yoruba language, you may now choose from the following words to translate:')  # this is for Uriel, please replace 'Your_language' with your language for the dictionary
            # ---> Print your list of english words on this line (you can delete this)
