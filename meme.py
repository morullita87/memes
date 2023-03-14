
import streamlit as st
import requests
import json

sub = st.text_input("subreddit")
if st.button("Generar meme"):
	url= "http://meme-api.com/gimme/cats"+sub
	respuesta = requests.get(url)
	data = json.loads(respuesta.text)
	meme = data["url"]
	st.title(data["title"])
	
	st.markdown("![Una imagen graciosa]("+meme+")")
