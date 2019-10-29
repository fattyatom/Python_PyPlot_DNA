import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    """Reads the XML.gz file and finds the protein records"""
    records = []
    count = 0

    handle = gzip.open(file_location)
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append({})

        records[count]["taxonomy"] = record.annotations["taxonomy"]
        records[count]["sequence_length"] = record.annotations["sequence_length"]

        count += 1

    return records
