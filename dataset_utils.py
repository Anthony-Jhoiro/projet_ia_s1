

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


def add_score_g3_classes_columns(dataframe):
    dataframe['score_G3_classes'] = dataframe.apply(lambda row: get_grade_class(row["G3"]), axis=1)
    return dataframe


def add_ratio_g1pg2_column(dataframe):
    dataframe['ratio_G1+G2'] = dataframe.apply(lambda row: row["G1"] + row["G2"], axis=1)


