def average_len(records):
    """Returns the average len for records."""

    total_length = 0
    for record in records:
        total_length += record["sequence_length"]
        total_length += len(record)
    return total_length / len(records)

def average_len_taxa(records, depth):
    """Returns the average length for the top level taxa"""
    record_by_taxa = {}
    for r in records:
        try:
            taxa = r["taxonomy"][depth]
            record_by_taxa.setdefault(taxa, []).append(r)
        except IndexError:
            pass

    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
