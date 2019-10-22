import argparse
from . import parse
from . import analysis
from . import plot
from pathlib import Path

LOC="uniprot_receptor.xml.gz"

def custom_db(args):
    LOC=  Path('')

def dump(args):
    """Prints the records in the uniprot_seqrecords in the parse.py file."""
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    """Prints the names in the records in the dump of uniprot_seqrecords."""
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def average(args):
    """Prints the average length of proteins."""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))))

def plot_average_by_taxa(args):
    """Generates a table of various types of average protein lengths."""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)


def cli():
    """Handles all the argument parsers required in the table."""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot", description="A python program of discovering DNA sequences")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump", help='Print all values in the database').set_defaults(func=dump)
    subparsers.add_parser("list", help='Print a name list of the records').set_defaults(func=names)
    subparsers.add_parser("average", help='Finding the average values of the name strings').set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa", help='Show bar chart of various types').set_defaults(func=plot_average_by_taxa)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args)
