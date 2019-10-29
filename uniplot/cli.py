import argparse
from . import parse
from . import analysis
from . import plot


def dump(args):
    """Prints the records in the uniprot_seqrecords in the parse.py file."""
    for record in parse.uniprot_seqrecords(args.customfile):
        print(record)

def names(args):
    """Prints the names in the records in the dump of uniprot_seqrecords."""
    for record in parse.uniprot_seqrecords(args.customfile):
        print(record.name)

def average(args):
    """Prints the average length of proteins."""
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(args.customfile))))

def plot_average_by_taxa(args):
    """Generates a table of various types of average protein lengths."""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(args.customfile))
    plot.plot_bar_show(av)

def cli():
    """Handles all the argument parsers required in the table."""
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot", description="A python program of discovering DNA sequences")

    parser.add_argument('--customfile',  default='uniprot_receptor.xml.gz', action='store', help='Type custom protein DB file path at prompt for custom UniProt file')

    subparsers = parser.add_subparsers(help="Sub Commands Help")

    ## Add subparsers
    subparsers.add_parser("dump", help='Print all values in the database').set_defaults(func=dump)
    subparsers.add_parser("list", help='Print a name list of the records').set_defaults(func=names)
    subparsers.add_parser("average", help='Finding the average values of the name strings').set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa", help='Show bar chart of various types').set_defaults(func=plot_average_by_taxa)

    ## Parse the command line
    args = parser.parse_args()


    ## Take the func argument, which points to our function and call it.
    args.func(args)

# H:/PyCharmProjects/practical-2/resources/uniprot_sprot_small.xml.gz
