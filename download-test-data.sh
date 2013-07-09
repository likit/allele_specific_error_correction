wget http://allim.googlecode.com/files/parent1_RNAseq_fastq.tar.gz
wget http://allim.googlecode.com/files/parent2_RNAseq_fastq.tar.gz
wget http://allim.googlecode.com/files/F1_RNAseq_fastq.tar.gz
wget http://allim.googlecode.com/files/parent1_genome.fa
wget http://allim.googlecode.com/files/parent2_genome.fa
wget http://allim.googlecode.com/files/reference.fa
wget http://allim.googlecode.com/files/reference.gtf
# wget http://allim.googlecode.com/files/AllimOptions_2Pexpr
# wget http://allim.googlecode.com/files/AllimOptions_2Pgenomes

###### untar files ##########
ls *.tar.gz | xargs -n1 tar xvfz
mv parent1_RNAseq_fastq/*.fastq .
mv parent2_RNAseq_fastq/*.fastq .
mv F1_RNAseq_fastq/*.fastq .
