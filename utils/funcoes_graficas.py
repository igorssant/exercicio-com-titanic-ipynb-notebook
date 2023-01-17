from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def grafico_pizza(x: pd.Series, label: pd.Series, selected_data: pd.DataFrame, title: str) -> None:
    figure = plt.figure(figsize = (12, 6))
    plt.pie(
        x = x,
        labels = label,
        autopct = "%1.2f%%",
        startangle = 90,
        data = selected_data
    )
    plt.title = (f"{title}")
    plt.show()

def grafico_barra(dataframe: pd.DataFrame, eixo_x: pd.Series, eixo_y: pd.Series, eixo_x_titulo: str, eixo_y_titulo: str, titulo: str, rotation: int = 0, cor: str = "#A03312") -> None:
    figure = plt.figure(figsize = (12, 6))
    plt.bar(x = eixo_x,
             height= eixo_y,
             data = dataframe,
             color = cor,
             width = 0.5
         )
    plt.xlabel(eixo_x_titulo, fontsize = 16)
    plt.ylabel(eixo_y_titulo, fontsize = 14)
    plt.xticks(rotation = rotation, size = 12)
    plt.yticks(size = 12)
    plt.title(titulo)
    plt.show()