import fileinput
import os
import sys
os.system('tail -n +2 copy.tsv > copy1.tsv')

li = []

def update_tsv_file(fname, master):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        length = i + 1
        for i in range(length):
                li.append('WGS')

        for fl, line in zip(li, fileinput.input([fname], inplace=True)):
                with open(master, "a") as myfile:
                        myfile.write('\n' + (line.strip() + '\t' + str(fl)))

update_tsv_file('copy1.tsv', 'gt_hmm.tsv')
os.system('rm copy.tsv')
os.system('rm copy1.tsv')

