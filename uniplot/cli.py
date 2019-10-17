import argparse
from . import parse
from . import analysis
from . import plot

LOC="resources/uniprot_sprot_small.xml.gz"

def dump(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record)

def names(args):
    for record in parse.uniprot_seqrecords(LOC):
        print(record.name)

def average(args):
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords(LOC))))

def plot_average_by_taxa(args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(LOC))
    plot.plot_bar_show(av)

def cli():
    ## Create a new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    subparsers = parser.add_subparsers(help="Sub Command Help")

    ## Add subparsers
    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa").set_defaults(func=plot_average_by_taxa)

    ## Parse the command line
    args = parser.parse_args()

    ## Take the func argument, which points to our function and call it.
    args.func(args)
