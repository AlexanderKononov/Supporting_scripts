# Toolbox for NGS data processing
Here I store different templates and scripts to process WGS data and scripts to format files as input to other WGS analyzing tools.

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

*fromPyCloneToSCHICM.py*

The script present a bridge between PyClone output data format and SCHISM input data format. It take 2+ argument: first is file of clonality PyClone output table, sacond is loci PyClone output table. Tables can be obtained by standard "build_table" PyClone comands.
By third and other additional arguments should be note PyClone input files (with .tsv extension) containing reads data. 
The script provide three files:
1. mut-to-cluster.tsv
2. clusterEstimates.tsv
3. mut-read.tsv

Output files are suit of a description of SCHISM example inputs in tutorial (see https://github.com/KarchinLab/SCHISM/wiki/Tutorial).

*superCuterForTSV.py*

Filtrating and sorting cna and snv from general tsv file. ´--help´ flag is available for additional details.

---

*toTSVbySet.py*
The code extracts DB and AF information (cna and baf data) from one summary file included all samples of cancer case (this format available within HERCULES project). (The code contains some templates for the unification of processing and managing tab-separated file of HERCULES project)

*bafFromBed.py*
The template of the script that takes a tab separated file with DB and AF data and extracts BAF data file transfer the data table in numpy array.

*BAFviewer.py*
Part of CNABAFSNVviewer.py script. This script can draw just BAF profile of genetic data.

*clonViewer.py*
Copy of script from CloneHD supplementary code. The code takes output file of CloneHD analysis (File with cna.subclone extension) and visualizes these results as color BAF and CNA profiles for each predicted subclones.

*cuterAdd.py*
The script takes two tab-separated files and compares them. If they have similar values the script write this line (from the second file) in the new file (Z_true2.csv)

*cuterForTSV.py*
The script takes tab-separated file with sorted genome observation from different samples and creates separated files with data for each sample. It is possible to add a sample name as the second arguments to exclude this samples from processing.

*DATAview.py*
The copy from CloneHD supplementary code. The script takes file input of CloneHD analysis and draws DP, BAF and SNV genetic profile from the raw data.

*extractADDP.py*
A template of the script which tries to extract AD and DP information from the last column of a tab-separated file and saves this information in two new files.

*extractBedSeg.py*
A template of the script which takes a tab-separated file and looks over the data. It is possible to exclude any chromosome or decrease number of considered observation (resolution of data).

*extrFiltAD.py*
A template of the script which takes a tab-separated file and looks over the data. It allows filtering data by different properties and flags.

*general_pipline.sh*
Bash script with the command for GATK for haplotype calling. It takes bam data file and reference genome file.

*getNormPosition.py*
The script takes two files. The first is data file from the normal control sample. The second is data of the target (non-control) sample. The script extracts the intersection of these two lists of DNA coordinates. This code is used during preprocessing data during CloneHD analysis for normalization of data by normal tissue sample.

*Vmeasure.py*
The script takes two files with Z matrices of subclone prediction (matrix of predicted subclone per predicted mutation cluster, with 0 and 1 elements) One matrix is predicted cluster-subclone assignment another one is know seted cluster -subclone information. The script writs V-measure metrics to evaluate of rightness of prediction.

