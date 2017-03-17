import os, sys, yaml, subprocess

stream = open("../_data/pubs_data.yaml", "r")
pubs = yaml.load(stream)

for pub in pubs:
	title = pub["Title"].replace('<em>', '').replace('</em>', '')
	proc = subprocess.Popen(['python','scholar.py', '-c', '1', '--phrase', '%s' %title],stdout=subprocess.PIPE)
	while True:
	  line = proc.stdout.readline()
	  print line
	  if "Citations" in line:
	    number_of_citations = int(line.strip().split(' ')[1])
	    pub["Citations"] = number_of_citations
	    break
	  elif line == "":
	  	break

with open("../_data/pubs_data.yaml", 'w') as f:
	f.write(yaml.dump(pubs, default_flow_style=False))