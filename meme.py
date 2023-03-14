
import streamlit as st
import requests
import json

if st.button("Generar meme"):
	url= "http://meme-api.com/gimme/wholesomememes"
	respuesta = requests.get(url)
	data = json.loads(respuesta.text)
	meme = data["url"]
	st.title(data["title"])
	
	st.markdown("![Una imagen graciosa]("+meme+")")
