#!/usr/bin/env python3
"""Return indices"""
from typing import Sequence


def index_range(page: int, page_size: int) -> Sequence:
    """Function to get index range"""

    return ((page - 1) * page_size, page * page_size)
