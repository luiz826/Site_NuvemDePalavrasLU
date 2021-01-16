# Importanto algumas bibliotecas e pacotes necessários
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 

# carregando o dataset das letras
df = pd.read_excel('https://github.com/luiz826/Site_NuvemDePalavrasLU/blob/main/lu2.xlsx?raw=true')

#definindo essa função para facilitar    
def wc_por_mcs(name):
    wordcloud1 = WordCloud(width = 1000, height = 500, random_state=2, background_color= 'white',collocations=False, stopwords = STOPWORDS).generate(name)
    fig, ax = plt.subplots(figsize=(20, 15))
    ax.imshow(wordcloud1, interpolation='bilinear')
    ax.axis("off")
    return fig

df["letra"] = df["letra"] + " "
escolha = pd.DataFrame(df["musica"].unique())
msc_wc = df.groupby("musica").sum()['letra']

#Streamlit

st.title('Nuvem de Palavras - Legião Urbana')

option = st.selectbox(
    'Escolha a música que deseja plotar a nuvem de palavras:', 
    escolha[0])

st.write("Nuvem de Palavras de "+option)
fug = wc_por_mcs(msc_wc[option])
st.pyplot(fug)
st.write("* Se quiser baixar a imagem, clique com o botão direito do mouse e vá em salvar imagem")
