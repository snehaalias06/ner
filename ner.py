
import streamlit as st
import spacy
from spacy import displacy
from newspaper import Article
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities")


text1 = st.text_area("Enter URL:")
text2 = st.text_area("Enter a paragraph:")


if(st.button("Submit")):
  if text1:
    article = Article(text1)
    article.download()
    article.parse()
    doc = nlp(article.text)
    ent_html = displacy.render(doc, jupyter=False, style='ent')
    st.markdown(ent_html, unsafe_allow_html=True)    
  
  elif text2:  
    doc = nlp(text2)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)