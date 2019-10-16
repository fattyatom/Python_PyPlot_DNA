def average_len(records):
    """Returns the average len for records."""
    total_length = 0
    for record in records:
        total_length += len(record)
    return total_length / len(records)
