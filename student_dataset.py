dataset_types = [
    str,
    str,
    int,
    str,
    str,
    str,
    int,
    int,
    str,
    str,
    str,
    str,
    str,
    str,
    int,
    bool,
    bool,
    bool,
    bool,
    bool,
    bool,
    bool,
    bool,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    float,
    float,
    float
]

string_fields = ['school',
                 'address',
                 'famsize',
                 'Pstatus',
                 'Mjob',
                 'Fjob',
                 'reason',
                 'guardian',
                 'traveltime',
                 'studytime',
                 'sex',
                 'score_G3_classes'
                 ]
boolean_fields = [
    'schoolsup',
    'famsup',
    'paid',
    'activities',
    'nursery',
    'internet',
    'romantic',
    'higher'
]

target_columns = [
    'G1',
    'G2',
    'G3',
    'G1+G2'
]

__all__ = ('boolean_fields', 'string_fields', 'dataset_types')
