import gzip

for l in gzip.open("uniprot_receptor.xml.gz"):
    print(l.decode().strip())
