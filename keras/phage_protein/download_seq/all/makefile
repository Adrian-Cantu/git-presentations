all:
	cat makefile

list:
	ls *fasta | cut -f1 -d'.' | xargs -I{} -t sh -c 'grep ">" {}.fasta | cut -f1 -d'[' | cut -f1 --complement -d" " | sort | uniq -c | sort -n -r > {}.list'

fastas:
	ls *fasta | cut -f1 -d'.' | xargs -I{} -t sh -c './list2fasta.pl {}.list > clean/{}_clean.fasta'

cluster:
	ls *fasta | cut -f1 -d'.' | xargs -I{} -t sh -c 'cdhit -i clean/{}_clean.fasta -o clustered/{}_clustered.fasta -c 0.9 -M 0 -T 0'
