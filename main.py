# %%
from matplotlib.pyplot import title
from sklearn import metrics

import csv_parser
import pandas as pd
import student_dataset as sd
import clustering
import matplotlib.pyplot as plt
import os

from dataset_utils import add_score_g3_classes_columns


def get_grade_class(grade):
    if grade < 10:
        return 'F'
    elif grade < 12:
        return 'D'
    elif grade < 14:
        return 'C'
    elif grade < 16:
        return 'B'
    return 'A'


def add_discret_columns(dataframe):
    dataframe['score_G3_classes'] = dataframe.apply(lambda row: get_grade_class(row["G3"]), axis=1)
    return dataframe


def create_plots(dataset):
    if os.path.exists("plots"):
        for file in os.listdir("plots"):
            os.remove(f'plots/{file}')
    if os.path.exists("plots.md"):
        os.remove("plots.md")

    if not os.path.exists("plots"):
        os.mkdir("plots")

    plots = []
    plot_count = 0

    piechart_length = len(sd.string_fields)

    fig, subplots = plt.subplots()

    for category_type in sd.string_fields:
        plot_count += 1
        dataset.groupby(category_type).size().plot(kind='pie', title=category_type)
        plt_name = f'plots/plot_{plot_count}_{category_type}.svg'
        plots.append(plt_name)
        plt.savefig(plt_name)
        plt.clf()

    with open('plots.md', 'w') as f:
        for plot in plots:
            f.write(f'![Plot {plot}](./{plot})\n')


if __name__ == '__main__':
    # Load DataFrame
    dataset = csv_parser.parse_student_csv("student-por.csv", separator=";", cast_types=sd.dataset_types)
    add_score_g3_classes_columns(dataset)


    # Create G2 + G3 column
    create_plots(dataset)



    # Cluster


