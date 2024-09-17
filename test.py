import streamlit as st
import MeCab
import random
import time
import unidic

# st.title("今日もきっといい日")
st.title("ポケットやる気チャージ")
st.text("テキストボックスに今日心に残った言葉を記入してください")

text_input = st.text_area("心に残った一言を記入してください", "")
mecab = MeCab.Tagger('-d "{}"'.format(unidic.DICDIR))
tmp = mecab.parse(text_input)
rel = tmp.split("\n")
s_list = [s.split(",")[0].split("\t") for s in rel[:-2]]
noun = []#noun
adje = []#adjective
inte = []#interjection
other = []
for s_word in s_list:
    if s_word[1] == "名詞":
        noun.append(s_word[0])
    elif s_word[1] == "形容詞":
        adje.append(s_word[0])
    elif s_word[1] == "感動詞":
        inte.append(s_word[0])
    else:
        other.append(s_word[0])

a = len(inte)*random.randint(75, 100)
b = len(adje)*random.randint(50, 75)
c = len(noun)*random.randint(25, 50)
d = len(other)*random.randint(0, 25)
ans = a+b+c+d

now = 2556
if st.button("Check"):
    with st.spinner("計測中"):
        time.sleep(3)
    st.write(f"あなたは今日、{ans} ポイント感謝されました🎉")
    now += ans
    st.write("👏👏👏","\n\n")
st.write(f"今日までの累積ポイントは　{now} ポイント　です😃")

