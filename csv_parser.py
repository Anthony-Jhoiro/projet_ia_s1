from typing import List, Type
import pandas as pd


def parse_student_csv(filename: str, separator=",", with_headers=True, cast_types: List[Type] = None):
    headers = None
    data = []
    with open(filename, "r") as source:
        if with_headers:
            headers = [header.strip() for header in source.readline().split(separator)]

        for line in source:
            str_data = line.split(separator)
            if cast_types is not None:
                data.append(cast_line(str_data, cast_types))
            else:
                data.append(str_data)

    return pd.DataFrame(data, columns=headers)


def format_dataset(dataset, target_columns, category_columns, boolean_columns):
    _dataframe = dataset.copy()

    filtered_category_columns = [col for col in category_columns if col in _dataframe]
    _dataframe = pd.get_dummies(_dataframe, columns=filtered_category_columns)
    # Cast boolean values to integers
    filtered_boolean_columns = [col for col in boolean_columns if col in _dataframe]
    _dataframe[filtered_boolean_columns] = _dataframe[filtered_boolean_columns].astype(int)

    return _dataframe


def drop_columns(dataset, target_columns):
    _dataframe = dataset.copy()
    filtered_target_columns = [col for col in target_columns if col in _dataframe]
    _dataframe = _dataframe.drop(labels=filtered_target_columns, axis=1)
    return _dataframe


def cast_line(line: List[str], types: List[Type]):
    casted_line = []

    for i in range(len(line)):
        casted_line.append(cast_str(line[i], types[i]))

    return casted_line


def cast_str(source: str, dest_type: Type):
    clean_source = clean_data(source)
    if len(clean_source) == 0 and dest_type != str:
        return None
    if dest_type == int:
        return int(clean_source)
    elif dest_type == bool:
        return str_to_bool(clean_source)
    elif dest_type == float:
        return float(clean_source)
    return clean_source


def str_to_bool(source) -> bool:
    return source.lower() in ["y", "yes", "true", "t"]


def clean_data(source: str) -> str:
    return source.strip('" \n')
