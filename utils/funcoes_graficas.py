from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def grafico_pizza(x: str, label: str, selected_data: pd.DataFrame, title: str = "Sem título") -> None:
    figure = plt.figure(figsize = (12, 6))
    plt.pie(
        x = x,
        labels = label,
        autopct = "%1.2f%%",
        startangle = 90,
        data = selected_data
    )
    plt.title(f"{title}")
    plt.show()

def grafico_barra(dataframe: pd.DataFrame, eixo_x: pd.Series, eixo_y: pd.Series, eixo_x_titulo: str, eixo_y_titulo: str, titulo: str, rotation: int = 0, cor: str = "#A03312") -> None:
    figure = plt.figure(figsize = (12, 6))
    plt.bar(
        x = eixo_x,
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

def grafico_boxplot(dataframe: pd.DataFrame, x_arg: str, y_arg: str, title: str = "Sem título", rotate: int = 90) -> None:
    figure, axis = plt.subplots(figsize = (12, 6))
    sns.boxplot(
        data = dataframe,
        x = x_arg,
        y = y_arg,
        ax = axis
    )
    plt.title(title)
    plt.xticks(rotation = rotate)
    plt.show()

def grafico_heatmap(data: pd.DataFrame, rotation: int = 90) -> None:
    figure = plt.figure(figsize = (12, 6))
    sns.heatmap(data = data)
    plt.xticks(rotation = rotation)
    plt.show()
    
def grafico_scatterplot(dataframe: pd.DataFrame, nome_coluna_1: str, nome_coluna_2: str, cor: str = "blue", alfa: float = 0.75):
    figure, axis = plt.subplots(figsize = (12, 6))
    sns.scatterplot(
        data = dataframe,
        x = nome_coluna_1,
        y = nome_coluna_2,
        color = cor,
        alpha = alfa
    )
    plt.show()