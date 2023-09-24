""" Function to return the descriptive statistics of a Polars Dataframe"""
import polars as pl
import matplotlib.pyplot as plt
from lib import select_col, summary_stats
from datetime import datetime
import os


def descriptive_stats(fname, col=None):
    df = pl.read_csv(fname)

    col_name = select_col(df, col)

    # check if error code(-1) is received, if no error code-proceed further
    if col_name == -1:
        return "Please select valid column number"

    # calculate the summary statistics and store in a list
    result = summary_stats(df, col_name)

    # Clear the exiting output.png and summary.md files if they exist
    if os.path.isfile("./outputs/output.png"):
        os.remove("./outputs/output.png")
    if os.path.isfile("./outputs/summary.md"):
        os.remove("./outputs/summary.md")

    # crete timestamp to add in files
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M") + " (UTC)"

    # create Histogram and save as output.png in output folder
    plt.hist(df.select(col_name))
    plt.ylabel("Count of " + col_name)
    plt.xlabel(col_name)
    plt.title("Data Loaded from : " + fname + "\n" + "Created at: " + dt_string)
    plt.savefig("./outputs/output.png")  # change the filepath here in case reequired
    plt.clf()

    # Write the summary statistics to a summary.md in output folder
    with open("./outputs/summary.md", "w", encoding="utf-8") as f:
        f.write("# Summary Statistics" + " file Generated at " + dt_string + "\n")
        f.write("## Data Loaded from : " + fname + "\n")
        f.write("## Selected Column : " + col_name + "\n")
        f.write("\n")
        f.write("Mean: " + str(result[0]) + "\n")
        f.write("\n")
        f.write("Median: " + str(result[1]) + "\n")
        f.write("\n")
        f.write("Standard Deviation: " + str(result[2]))

    return result
