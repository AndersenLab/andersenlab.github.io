from metapub import PubMedFetcher
import yaml


# Add new PMIDS to publications.txt then run this script

q = PubMedFetcher()

# open the things to be updated from the publications.txt file
pub_list = map(int, open("../publications/publications_list.txt", 'r').read().splitlines()[1:])


def fetch_pub(pmid):
    pub = q.article_by_pmid(pmid)
    # only grab relevant information
    dpub = {'Title': pub.title, 'Authors': pub.authors, 'DOI': pub.doi, 'Date_Published': pub.year, 'Journal': pub.journal, 'PMC': pub.pmc, 'PMID': pub.pmid}
    return dpub

doc_list = []

#  load current file
with open('../_data/pubs_data.yaml', 'r') as f:
    yaml_db = yaml.load(f)

existing_pmids = [int(x["PMID"]) for x in yaml_db if 'PMID' in x]

for i in pub_list:
    print(i)
    if i not in existing_pmids:
        doc_list.append(fetch_pub(i))

for entry in yaml_db:
    doc_list.append(entry)
    
print(doc_list)

with open("../_data/pubs_data2.yaml", 'w') as f:
        f.write(yaml.safe_dump(doc_list))
