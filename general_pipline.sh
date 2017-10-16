#!/bin/bash

for file in "/fs/projects/akononov/bams/*.bam"
do
java -Xmx5G -jar /homes/akononov/GATK/GenomeAnalysisTK.jar \
-R /fs/projects/akononov/GRCh38_gencod/GRCh38.primary_assembly.genome.fa \
-T HaplotypeCaller \
-I $file \
-o $file.vcf 
done
