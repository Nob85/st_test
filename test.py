import streamlit as st
import MeCab
import random
import time

st.title(":red[ポケット]")
st.title(":red[やる気チャージ]💪")

text_input = st.text_area("テキストボックスに  \n今日心に残った言葉を記入してください", "")
mecab = MeCab.Tagger()
tmp = mecab.parse(text_input)
rel = tmp.split("\n")
s_list = [s.split(",")[0].split("\t") for s in rel[:-2]]
noun = []#noun
adje = []#adjective
inte = []#interjection
other = []
tmp = []
ans = 0
parents = ["父", "母", "パパ", "ママ", "ぱぱ", "まま"] 
for s_word in s_list:
    if s_word[1] == "名詞":
        noun.append(s_word[0])
    elif s_word[1] == "形容詞":
        adje.append(s_word[0])
    elif s_word[1] == "感動詞":
        inte.append(s_word[0])
    else:
        other.append(s_word[0])

    if s_word[0] == "さん" and s_word[1] == "接尾辞":
        if tmp[1] == "名詞":
            ans += 500
            
    if s_word[0] in parents:
        ans += 500
    tmp = s_word

a = len(inte)*random.randint(75, 100)
b = len(adje)*random.randint(50, 75)
c = len(noun)*random.randint(25, 50)
d = len(other)*random.randint(0, 25)
ans += a+b+c+d

now = 2556
if st.button("Check"):
    with st.spinner("計測中"):
        time.sleep(2)
    st.write(f"**あなたは今日、  \n{ans:,} ポイント 感謝されました**🎉")
    now += ans
    st.write("👏👏👏")
st.write(f"**今日までの累積ポイントは  \n{now:,} ポイント です**😃")

