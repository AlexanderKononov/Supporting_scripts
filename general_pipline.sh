#!/bin/bash
java -Xmx3G -jar /homes/akononov/GATK/GenomeAnalysisTK.jar \
-R /fs/projects/alexkono/GRCh38_gencod/GRCh38.primary_assembly.genome.fa \
-T HaplotypeCaller \
-I $1 \
-o $1.vcf 

