##### Upgrade packages #####
apt-get update -y
apt-get upgrade -y

##### Install R 2.15.0 #####
cd
apt-get build-dep -y r-base
wget http://cran.mtu.edu/bin/linux/ubuntu/precise/r-base_2.15.0.orig.tar.gz
tar vxfz r-base_2.15.0.orig.tar.gz 
cd R-2.15.0/
./configure --enable-R-shlib
make
make install

##### Install required R packages and Rpy2 #####
cd
R CMD BATCH install-R-packages.R install.log
wget -O rpy2-2.2.0.tar.gz http://sourceforge.net/projects/rpy/files/rpy2/2.2.x/rpy2-2.2.0.tar.gz/download
tar xvfz rpy2-2.2.0.tar.gz
cd rpy2-2.2.0/
python setup.py build
python setup.py install

##### Install Samtools and Bedtools #####
cd
apt-get install -y samtools
wget -O picard-tools-1.75.zip http://sourceforge.net/projects/picard/files/picard-tools/1.75/picard-tools-1.75.zip
apt-get install -y unzip
unzip picard-tools-1.75.zip 
apt-get install -y bedtools

##### Install GSNAP #####
wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2012-07-20.tar.gz
tar xvfz gmap-gsnap-2012-07-20.tar.gz 
cd gmap-2012-07-20/
./configure
make
make install
ln -s /usr/local/bin/gsnap /usr/local/bin/GSNAP

##### Install Biopython and Numpy #####
cd
apt-get install -y python-biopython

cd /mnt/ebs
wget https://allim.googlecode.com/files/Allim_1.0.tar.gz
tar xvfz Allim_1.0.tar.gz
cd /mnt/ebs/Allim_1.0
mkdir test_data/
cd /mnt/ebs/Allim_1.0/test_data/
sh download-test-data.sh
