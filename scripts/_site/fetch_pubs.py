from metapub import PubMedFetcher
import yaml


# Add new PMIDS to publications.txt then run this script

#  load current file
with open('../_data/pubs_data.yaml', 'r') as q:
	current_file = yaml.load(q)

q = PubMedFetcher()

# open the things to be updated from the publications.txt file
pub_list = open("../pub/publications_list.txt", 'r').read().splitlines()[1:]

def fetch_pub(pmid):
    pub = q.article_by_pmid(pmid)
    # only grab relevant information
    dpub = {'Title': pub.title, 'Authors': pub.authors, 'DOI': pub.doi, 'Date_Published': pub.year, 'Journal': pub.journal, 'PMC': pub.pmc, 'PMID': pub.pmid}

    return dpub

# first entry isn't in correct format and doesnt have a PMID
# del current_file[0]
PMID_list = []
doc_list = []

# grab all PMIDs
for i, entry in enumerate(current_file):
	if 'PMID' not in entry:
		doc_list.append(entry)
	if 'PMID' in entry:
		if 'DOI' in entry:
			doc_list.append(entry)
		else:
			doc_list.append(fetch_pub(str(entry['PMID']))) 


with open("../_data/pubs_data2.yaml", 'w') as f:
		f.write(yaml.safe_dump(doc_list))
