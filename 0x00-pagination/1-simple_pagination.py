#!/usr/bin/env python3
"""Class server"""
import csv
import math
from typing import List
from typing import Sequence


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page function"""

        def index_range(page: int, page_size: int) -> Sequence:
            """Function to get index range"""

            return ((page - 1) * page_size, page * page_size)

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        tup = index_range(page, page_size)
        if tup[1] > len(self.dataset()) and tup[0] < len(self.dataset()):
            return (self.dataset()[tup[0]:])
        elif tup[1] <= len(self.dataset()):
            return (self.dataset()[tup[0]: tup[1]])
        else:
            return ([])
