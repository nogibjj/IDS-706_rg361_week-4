"""This library file contains the common functions used in the project."""


def select_col(df, col_num=None):
    """This function takes in a DataFrame and user selected column number and returns:
    - the corresponding column name if it is a valid numeric column,
    - the last column if no input is selected and last column is numeric
    - else it returns an error code
    """

    # Check if user has selectd a valid column number, else assign it to last column.
    if col_num is None:
        col = len(df.columns) - 1
    else:
        if (col_num > len(df.columns)) or (col_num < 1):
            return -1
        col = col_num - 1

    # get the column name
    col_name = df.columns[col]

    # validate if this column has numeric data before returning
    if df[col_name].is_numeric():
        return col_name
    else:
        return -1


def summary_stats(df, col_name):
    return [df[col_name].mean(), df[col_name].median(), df[col_name].std()]
