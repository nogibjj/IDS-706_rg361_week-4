"""This file tests the lib.py file."""

import polars as pl

# import sys and add location of project files to path
import sys

sys.path.insert(0, "./codes/project_codes")
from lib import select_col, summary_stats  # noqa: E402


def test_select_col():
    """Test the select_col funtion from lib file"""

    # Create the polars DataFrame from the sample file
    fname = "./resources/blood_pressure.csv"
    df = pl.read_csv(fname)

    # Test case 1: col number is specified
    assert "bp_before" == select_col(df, 4)

    # Test case 2: col number is not specified, should return name of last column
    assert "bp_after" == select_col(df)

    # Test case 3: wrong column number gives, should return error code -1
    assert -1 == select_col(df, 10)

    # Test case 4: non numeric column selected, should return error code -1
    assert -1 == select_col(df, 3)


def test_summary_stats():
    """Test the summary_stats function from lib file"""

    # Create the polars DataFrame from the sample file
    fname = "./resources/blood_pressure.csv"
    df = pl.read_csv(fname)
    col_name = "bp_before"
    assert [
        df[col_name].mean(),
        df[col_name].median(),
        df[col_name].std(),
    ] == summary_stats(df, col_name)


test_select_col()
test_summary_stats()
