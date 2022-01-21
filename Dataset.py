from dataclasses import dataclass
from typing import List, Any

DISPLAY_TABLE_COL_WIDTH = 12
DISPLAY_TABLE_CELL_SEPARATOR = " |"


@dataclass
class Dataset:
    headers: List[str]
    data: List[List[Any]]

    def display(self, *fields: int):
        if len(fields) == 0:
            fields = list(range(5))

        for header in self.headers:
            print(('\033[1;34m{0:>' + str(DISPLAY_TABLE_COL_WIDTH) + '}\033[0m').format(header), end=DISPLAY_TABLE_CELL_SEPARATOR)
        print("")

        print("-" * (len(DISPLAY_TABLE_CELL_SEPARATOR) + DISPLAY_TABLE_COL_WIDTH) * len(self.headers))

        for field in fields:
            for value in self.data[field]:
                print(('{0:>' + str(DISPLAY_TABLE_COL_WIDTH) + '}').format(value), end=DISPLAY_TABLE_CELL_SEPARATOR)
            print("")
