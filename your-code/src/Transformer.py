import pandas as pd
import os
import nltk
import re

nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

def remove_non_alfabetic_chars(text):
    #Quita todos los signos de puntuación y los números.
    text = re.sub('[^A-Za-zñÑáéíóúÁÉÍÓÚ]', ' ', text)
    return text

def get_word_root(word):
    #Extrae la raiz de una palabra.
    stemmer = SnowballStemmer("spanish")
    root_word = stemmer.stem(word)
    return root_word

def transform_leyes_año(df_leyes_año):
    #Función que agrega las funciones de limpieza y transformación a aplicar a cada una de las leyes
    titulos=''
    for ley in df_leyes_año:
        ley=remove_non_alfabetic_chars(ley)
        tokens=ley.split(' ')
        for token in tokens:
            if token not in stopwords.words('spanish'):
                token=get_word_root(token.lower())
                titulos=titulos + ' ' + token

    tokens=nltk.tokenize.word_tokenize(titulos.strip())
    freq=nltk.FreqDist(tokens)
    return freq

def get_max_freq(df_leyes,limite=10):
    #Obtiene una tabla de frecuencias globales para todas las leyes promulgadas.
    leyes_merge=''
    for ley in df_leyes.TITULO_LEY:
        ley=remove_non_alfabetic_chars(ley)
        leyes_merge=leyes_merge + " " + ley
    tokens=leyes_merge.split(" ")
    clean_tokens=' '
    for token in tokens:
        if token not in stopwords.words('spanish'):
            token = get_word_root(token.lower())
            clean_tokens = clean_tokens + ' ' + token

    tokens = nltk.tokenize.word_tokenize(clean_tokens.strip())
    freq = nltk.FreqDist(tokens)
    filter_words =freq.tabulate(limite)
    return filter_words

def Transform(df_leyes):
    #Función que genera un dataframe con los datos normalizados.
    df_titulos_leyes_agrupados = df_leyes.groupby('AÑO')['TITULO_LEY'].apply(list)
    df_titulos_leyes_agrupados = df_titulos_leyes_agrupados.apply(transform_leyes_año)
    return df_titulos_leyes_agrupados

#df_leyes=pd.read_csv(r'C:\Users\Miguel\IronHack\data-labs\module-1\web-project\your-code\data\leyes.txt', encoding='UTF-8',sep=";")

#a=get_max_freq(df_leyes)
#print(a)

