
Languages = 'Tiv = "a"\nIgbo = "b"\nJenjo = "c"\nEfik = d\n'              #  PLEASE PUT YOUR LANGUAGE DIRECTLY BESIDE THE "\n" (no spacing) in the order you see (i.e \nYoruba = "c") the fifth person should not include the "\n" after their language
eng_words = 'come\ntake\nsee\ngo\neat\nhouse\nsleep\nwalk\nwork\nplay\nask\nfood\nwater\nplease\neyes\nmake\nname\nlike\nlove\ngood'
print('Welcome to the universal dictionary you may choose from the following languages')
print(Languages)

language_choice = input('Which language do you want to use?')
if language_choice == 'a':
        print('you have chosen "Tiv" language, you may now choose from the following words to translate:')
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
    print('you have chosen "Igbo" language, you may now choose from the following words to translate:') #this is for Treasure
#---> Print your list of english words on this line (you can delete this)
#then yea you can paste your code here->

if language_choice == 'c':
    print('you have chosen "Jenjo" language, you may now choose from the following words to translate:') #this is for Pheeyamila
 Print(eng_words) 
jenjo_dictionary ={
  "Water": "Mirit","Air": "Fɔli","Fire": "Fayol","Earth": "Kana","Tree": "Gasorund","How are you": "Foli wɛ?",
  "Moon":"kili","Red": "Rudu","Purple": "Puruli", "Brother": "Bumia","Sister": "Sissma", "Father": "Banito",
  "Sand": "Sanda", "How old are you": "Fo sɔ?", "Good day": "Nifa","Phone": "Telenouy", "Hammer": "Garia",
  "Story": "Kima","Bed": "Lakm","Tall":Talero"
}
   while 1==1:
     word= input(what word do you want to translate ?)      
if the word is in jenjo_dict:
print(word,'means',jenjo dict_dict[word], 'in jenjo')
else :
print("apologies word not found ,select from available words")
if language_choice == 'd':
    print('you have chosen "Efik" language, you may now choose from the following words to translate:')  
    print(eng_words)
        Efik_dict{"hello": "mfo", "goodbye": "ka do", "thank you": "sosongo", "yes": "iyo", "no": "mba", "water": "mmong",
    "food": "udon",  "house": "ufok","man": "eka", "woman": "edi", "child": "eyen",  "friend": "eka inam", "love": "ima",
    "school": "ufok mme",  "book": "mbuk", "sun": "utong", "moon": "onen", "money": "owo", "work": "utomo", "name": "enyin"}
print("Choose a language:")
for key, value in languages.items():
    print(key, "-", value[0])
choice = input("Enter the number of the language: ")
if choice in languages:
    language_name, dictionary = languages[choice]
    word = input("Enter an English word to translate: ").lower()
  if word in dictionary:
        print(f"The word in {language_name} is: {dictionary[word]}")
    else:
        print("Sorry, that word is not in the dictionary.")
else:
    print("Invalid language choice.")
if language_choice == 'e':
    print('you have chosen "Your_language" language, you may now choose from the following words to translate:')  # this is for Uriel, please replace 'Your_language' with your language for the dictionary
    # ---> Print your list of english words on this line (you can delete this)
