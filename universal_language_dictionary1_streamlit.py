import streamlit as st

# ================== DICTIONARIES ==================

Tiv_dictionary = {
    'come': 'vah', 'take': 'ngohol', 'see': 'nenge', 'go': 'yem', 'eat': 'ya',
    'house': 'yah', 'sleep': 'yav', 'walk': 'zande', 'work': 'tom',
    'play': 'numbe', 'ask': 'pine', 'food': 'kwaghyan', 'water': 'ngeren',
    'please': 'nzamber', 'eyes': 'ashe', 'make': 'er', 'name': 'ti',
    'like': 'sow', 'love': 'dooshima', 'good': 'doo'
}

Igbo_dictionary = {
    'hello': 'Ndewo', 'please': 'Biko', 'thank you': 'Daalu', 'no': 'Mba',
    'yes': 'Ee', 'chair': 'Oche', 'cup': 'Iko', 'mother': 'Nne',
    'father': 'Nna', 'child': 'Nwa', 'water': 'Mmiri', 'road': 'Uzo',
    'house': 'Ulo', 'book': 'Akwukwo', 'eye': 'Anya', 'head': 'Isi',
    'ground': 'Ala', 'body': 'Ahu', 'day': 'Ubochi', 'money': 'Ego'
}

Jenjo_dictionary = {
    'water': 'Mirit', 'air': 'Fɔli', 'fire': 'Fayol', 'earth': 'Kana',
    'tree': 'Gasorund', 'cat': 'Nak', 'moon': 'kili', 'red': 'Rudu',
    'purple': 'Puruli', 'brother': 'Bumia', 'sister': 'Sissma',
    'father': 'Banito', 'sand': 'Sanda', 'dog': 'Mush', 'man': 'Gorio',
    'phone': 'Telenouy', 'hammer': 'Garia', 'story': 'Kima',
    'bed': 'Lakm', 'tall': 'Talero'
}

Efik_dictionary = {
    'hello': 'mfo', 'goodbye': 'ka do', 'thank you': 'sosongo', 'yes': 'iyo',
    'no': 'mba', 'water': 'mmong', 'food': 'udon', 'house': 'ufok',
    'man': 'eka', 'woman': 'edi', 'child': 'eyen', 'friend': 'eka inam',
    'love': 'ima', 'school': 'ufok mme', 'book': 'mbuk',
    'sun': 'utong', 'moon': 'onen', 'money': 'owo', 'work': 'utomo',
    'name': 'enyin'
}

Yoruba_dictionary = {
    'chair': 'alaga', 'towel': 'aso inura', 'friend': 'ore',
    'food': 'onuje', 'leg': 'ese', 'come': 'wa', 'sit': 'joko',
    'read': 'ka', 'laugh': 'rerin', 'smoke': 'efin', 'boy': 'omokunrin',
    'drink': 'mimu', 'sing': 'korin', 'running': 'nsise',
    'black': 'dudu', 'white': 'funfun', 'rice': 'iresi',
    'lamp': 'atupa', 'car': 'oko ayokele', 'dance': 'ijo'
}

languages = {
    "Tiv": Tiv_dictionary,
    "Igbo": Igbo_dictionary,
    "Jenjo": Jenjo_dictionary,
    "Efik": Efik_dictionary,
    "Yoruba": Yoruba_dictionary
}

# ================== STREAMLIT UI ==================

st.title("Universal Language Dictionary")

language = st.selectbox("Choose a language", languages.keys())

dictionary = languages[language]

st.write("### Available words")
st.write(", ".join(dictionary.keys()))

word = st.text_input("Enter a word to translate").lower()

if st.button("Translate"):
    if word in dictionary:
        st.success(f'"{word}" means **{dictionary[word]}** in {language}')
    else:
        st.error("Word not found. Please choose from the list.")
st.feedback()

