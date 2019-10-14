import gzip
from Bio import SeqIO

def cli():
    handle = gzip.open("uniprot_receptor.xml.gz")
    for record in SeqIO.parse(handle, "uniprot-xml"):
        print(record)
