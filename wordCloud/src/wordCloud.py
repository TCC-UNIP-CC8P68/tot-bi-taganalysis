# importar os pacotes necessários
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from . import databaseOperations as dbOperations
from .databaseConnection import open, close
import wordcloud

def wordCloud(cur, conn):
  userIds = dbOperations.getDistinctUserIds(cur)
  for userId in userIds:
    tags = dbOperations.getCapturedTags(cur, userId)
    print(tags)
    # eliminar as colunas com valores ausentes
    summary = tags.dropna(subset=['summary'], axis=0)['summary']

    # concatenar as palavras
    all_summary = " ".join(s for s in summary)

    # lista de stopword
    stopwords = set(STOPWORDS)
    stopwords.update(["da", "meu", "em", "você", "de", "ao", "os", "br", "o", "a", "para", "e"])

    # gerar uma wordcloud
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color="black",
                          width=1600, height=800).generate(all_summary)

    # mostrar a imagem final
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()

    plt.imshow(wordcloud)
    wordcloud.to_file("teste.png")
