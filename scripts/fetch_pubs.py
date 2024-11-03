from metapub import PubMedFetcher
import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import os
from subprocess import Popen, PIPE

git_dir, err = Popen(['git', 'rev-parse', '--show-toplevel'], stdout=PIPE).communicate()
git_dir = git_dir.strip().decode("utf8")
pubs_yaml = os.path.join(git_dir, "_data/pubs_data.yaml")
pubs_list = os.path.join(git_dir, "publications/publications_list.txt")

# Add new PMIDS to publications.txt then run this script
q = PubMedFetcher()

# open the things to be updated from the publications.txt file
pub_list = map(str, open(pubs_list, 'r').read().splitlines()[1:])


def fetch_pub(pmid):
    pub = q.article_by_pmid(pmid)
    # only grab relevant information
    dpub = {'Title': pub.title.strip("."), 'Authors': pub.authors, 'DOI': pub.doi, 'Date_Published': pub.year, 'Journal': pub.journal, 'PMC': pub.pmc, 'PMID': str(pub.pmid)}
    return dpub

doc_list = []

#  load current file
with open(pubs_yaml, 'r') as f:
    yaml_db = yaml.load(f, Loader=Loader)

existing_pmids = [str(x["PMID"]) for x in yaml_db if 'PMID' in x]

for i in pub_list:
    if i not in existing_pmids:
        doc_list.append(fetch_pub(i))

for entry in yaml_db:
    doc_list.append(entry)
    
with open(pubs_yaml, 'w') as f:
        f.write(yaml.safe_dump(doc_list))
