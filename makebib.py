#!/usr/bin/env python3

import yaml
import os

#get .bib for files with arXiv identifier
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)

    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='arxiv'):
                print('working on ArXiv file ' + url)
                os.system("./scripts/arxiv2bib.py " + str(v) + " > publications/" + url +".txt")

#get .bib for files with DOI 
with open(r'_data/publist.yml') as file:
    pubs = yaml.load(file, Loader=yaml.FullLoader)
    for pub in pubs:
        for k,v in pub.items():
            if (k=='url'):
                url=v
            if (k=='doi'):
                print('working on DOI file ' + url)
                os.system("./scripts/doi2bib.py " + str(v) + " > publications/" + url +".txt")
                #remove empty lines that doi2bib gives
                open("publications/tmp.bib",'w').write(
                    ''.join(
                        l for l in open("publications/" + url + ".txt") if l.strip()))
                os.system("mv publications/tmp.bib publications/" + url + ".txt")
