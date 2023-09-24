"""This file tests the python script for descriptive statistics using Polars."""

# import sys and add location of project files to path
import sys
import polars as pl

sys.path.insert(0, "./codes/project_codes")
from main_script import descriptive_stats  # noqa: E402


def test_stat():
    """Test main code agaisnt conditions"""

    fname = "./resources/blood_pressure.csv"
    # Create the polars DataFrame
    df = pl.read_csv(fname)

    # Test case 1: col number specified
    col = 3
    col_name = df.columns[col]
    assert [
        df[col_name].mean(),
        df[col_name].median(),
        df[col_name].std(),
    ] == descriptive_stats(fname, 4)

    # Test case 2: col number not specified, should use last column
    col = 4
    col_name = df.columns[col]
    assert [
        df[col_name].mean(),
        df[col_name].median(),
        df[col_name].std(),
    ] == descriptive_stats(fname)

    # Test case 3: wrong column number given, should return error message
    assert "Please select valid column number" == descriptive_stats(fname, 10)

    # Test case 4: non numeric column selected, should return error code -1
    assert "Please select valid column number" == descriptive_stats(fname, 10)


test_stat()
