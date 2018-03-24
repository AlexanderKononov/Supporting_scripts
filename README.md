# File preparator for PyClone
Here I store different templates
and some parts of unfinished code.
So, below I try to add some annotation to few useful scripts from this "project"

*TransToTSV.py*

The script is used to prepare input data to PyClone alalysis. The script use SNV file with data of single somatic mutations and CNA file with segmentation datata of ploidy and creates TSV file which is needed to PyClone analyze 

*CNABAFSNVviewer.py*

This script can draw DNA profile for three level of WGS data.CNA, BAF and SNV sample profiles are drawn in pdf file from raw data. The input is similar to CloneHD input. This programme can be used to visualization of raw input data to CloneHD. Programme takes 3 input file with read depth data (CNA), read depth of alternative alleles as example for snp position (BAF), and  read depth of alternative somatic mutations as example from MuTect2 GATK (SNV). 

*CnaBafViewer.py*

This script can draw CNA and BAF profiles of tumor subclones. It visualize the data using output files for CloneHD. As input you should  note wey to the output file like `sampleA.cna.subclone-1.txt` .

*MergerCNA.py* and *overlupForAll.py*

This scripts can be used to preparing CloneHD input. It merges two file from 2 samples (MergerCNA.py) or a lot of file (overlupForAll.py) in one file to complex analysis.

*SNV_extract.py*

This programme take file with SNVs data of every samples of patient (by this format the variant data are stored in HERCULES project) and split on separate files by samples.
