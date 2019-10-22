import pytest
import uniplot.analysis
import uniplot.parse


TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_hello_world():
    """Returns hello world if runs."""
    assert True

def test_average():
    """Checks whether the average value equals to the value in the small uniprot table."""
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222223
