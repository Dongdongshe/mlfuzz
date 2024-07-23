import glob
import sys
import subprocess

seed_corpus=glob.glob(sys.argv[1]+'/*')
vari_corpus=glob.glob(sys.argv[2]+'/*')
splice_corpus=glob.glob(sys.argv[3]+'/*')

cov = set()

for f in seed_corpus+vari_corpus+splice_corpus:
    out = subprocess.check_output("/aflpp/afl-showmap -q -e -o /dev/stdout -m none -- " + sys.argv[4] + " <" + f, shell=True)
    for edge in out.splitlines():
        cov.add(edge)
    print("cov " + str(len(cov)))

    

