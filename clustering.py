from typing import List
import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import InterclusterDistance


ColumnList = List[str]


def clean_dataframe_for_clustering(dataframe: pd.DataFrame, category_columns: List[str], boolean_columns: List[str]):
    # Split category colmns into multiple columns (is_cat1, is_cat2, ...)
    filtered_category_columns = [col for col in category_columns if col in dataframe]
    print(filtered_category_columns)
    _dataframe = pd.get_dummies(dataframe, columns=filtered_category_columns)
    # Cast boolean values to integers
    filtered_boolean_columns = [col for col in boolean_columns if col in dataframe]
    _dataframe[filtered_boolean_columns] = _dataframe[filtered_boolean_columns].astype(int)
    # Normalize all values so they will be between 0 and 1
    # return (_dataframe - _dataframe.min()) / (_dataframe.max() - _dataframe.min())
    return _dataframe


def apply_clustering(dataframe: pd.DataFrame, cluster_count: int, string_fields: ColumnList, boolean_fields: ColumnList,
                     exclude_columns: ColumnList):
    dataset_norm = dataframe.copy()
    dataset_norm = dataset_norm.drop(labels=exclude_columns, axis=1)
    dataset_norm = clean_dataframe_for_clustering(dataset_norm, string_fields, boolean_fields)
    predictions = KMeans(n_clusters=cluster_count, random_state=1)
    predictions.fit(dataset_norm)
    # visualizer.fit(dataset_norm)
    return predictions


# __all__ = ('apply_clustering', 'show_cluster')
