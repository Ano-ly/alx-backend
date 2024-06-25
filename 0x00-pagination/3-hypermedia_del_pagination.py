#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index in self.__indexed_dataset().keys()
        ret_dict = {}
        ret_dict["index"] = index
        ret_dict["next_index"] = index + page_size
        ret_dict["page_size"] = page_size
        data = []
        choice = 0
        for j in (index, max(self.__indexed_dataset().keys())+1):
            if self.__indexed_dataset().get(j) is not None:
                choice = j

        for i in range(j, j + page_size):
            r = self.__indexed_dataset().get(i)
            if r is None:
                ret_dict["next_index"] = None
                break
            data_append(r)
        ret_dict["data"] = data
        return (ret_dict)