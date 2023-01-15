from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def grafico_pizza(x: pd.Series, label: pd.Series, selected_data: pd.DataFrame, title: str) -> None:
    figure = plt.figure(figsize=(12, 6))
    plt.pie(
        x = x,
        labels = label,
        autopct = "%1.2f%%",
        startangle = 90,
        data = selected_data
    )
    plt.title = (f"{title}")
    plt.show()

def grafico_barra() -> None:
    pass