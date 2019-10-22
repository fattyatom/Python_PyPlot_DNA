import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """Reads the XML.gz file and finds the protein records"""
    records = []

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)

    return records
