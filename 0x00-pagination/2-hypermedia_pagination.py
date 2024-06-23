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

    def get_hyper(self, page: int, page_size: int):
        """Get page details"""

        result = self.get_page(page, page_size)
        ret_dict = {}
        ret_dict["page_size"] = len(result)
        ret_dict["page"] = page
        ret_dict["data"] = result
        if len(self.get_page(page + 1, page_size)) == 0:
            ret_dict["next_page"] = None
        else:
            ret_dict["next_page"] = page + 1
        if page == 1:
            ret_dict["prev_page"] = None
        else:
            ret_dict["prev_page"] = page - 1
        ret_dict["total_pages"] = (len(self.dataset()) // page_size) + 1
        return (ret_dict)
