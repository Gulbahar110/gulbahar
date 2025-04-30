import streamlit as st
import random

# Har shair ka andaaz represent karta hua lafz
iqbal_words =  ["khudi", "shaheen", "junoon", "taqdeer", "khwab"]
mir_words =  ["dil", "gham", "aah", "ishq", "mehfil"]
ghalib_words =  ["naqsh", "sitam", "falsafa", "husn", "khaak"]
hafiz_words =  ["saaqi", "jam", "mast", "bahaar", "raaz"]
alahbadi_words =  ["taang", "nakaam", "biryani", "sheher", "afsos"]

# Randomly select one word from each poet
word1 = st.text_input.choice(iqbal_words)
word2 = st.text_.choice(mir_words)
word3 = input.choice(ghalib_words)
word4 = input.choice(hafiz_words)
word5 = input.choice(alahbadi_words)

# Generate a short abstract-style poem
shayari = st.write( f"""1. {word1} se roshan hai meri zindagi
2. {word2} ka silsila hai har gali
3. {word3} mein chhupi hai meri bandagi
4. {word4} ki talaash mein hai dil ki lagi
5. aur {word5} pe khatam hoti hai meri kahani"""
)
st.write("Random Shayari (Ek-Lafzi Andaaz):")
st.write(shayari)