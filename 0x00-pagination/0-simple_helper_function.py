#!/usr/bin/env python3
"""
Task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function that takes two integer arguments page and page_size, returns
    a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
