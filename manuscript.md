---
title: Cis-gene regulation does not explain chromosome 21 expression deviations from the ploidy expectation in Down syndrome
keywords:
- Down syndrome
- trisomy 21
- chromosome 21
- eQTL
- gene expression
- whole blood
lang: en-US
date-meta: '2026-10-10'
author-meta:
- Lucas A. Gillenwater
- Marc Subirana-Granés
- Mary A. Allen
- Milton Pividori
- Casey S. Greene
header-includes: |
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta property="og:type" content="article" />
  <meta name="dc.title" content="Cis-gene regulation does not explain chromosome 21 expression deviations from the ploidy expectation in Down syndrome" />
  <meta name="citation_title" content="Cis-gene regulation does not explain chromosome 21 expression deviations from the ploidy expectation in Down syndrome" />
  <meta property="og:title" content="Cis-gene regulation does not explain chromosome 21 expression deviations from the ploidy expectation in Down syndrome" />
  <meta property="twitter:title" content="Cis-gene regulation does not explain chromosome 21 expression deviations from the ploidy expectation in Down syndrome" />
  <meta name="dc.date" content="2026-10-10" />
  <meta name="citation_publication_date" content="2026-10-10" />
  <meta property="article:published_time" content="2026-10-10" />
  <meta name="dc.modified" content="2026-10-10T18:21:41+00:00" />
  <meta property="article:modified_time" content="2026-10-10T18:21:41+00:00" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Lucas A. Gillenwater" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO" />
  <meta name="citation_author_orcid" content="0000-0003-3158-9682" />
  <meta name="citation_author" content="Marc Subirana-Granés" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO" />
  <meta name="citation_author_orcid" content="0000-0003-3934-839X" />
  <meta name="citation_author" content="Mary A. Allen" />
  <meta name="citation_author_institution" content="BioFrontiers Institute, University of Colorado Boulder, Boulder, CO" />
  <meta name="citation_author_orcid" content="0000-0001-7490-0165" />
  <meta name="citation_author" content="Milton Pividori" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO" />
  <meta name="citation_author_orcid" content="0000-0002-3035-4403" />
  <meta name="citation_author" content="Casey S. Greene" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO" />
  <meta name="citation_author_orcid" content="0000-0001-8713-9213" />
  <link rel="canonical" href="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/" />
  <meta property="og:url" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/" />
  <meta property="twitter:url" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/" />
  <meta name="citation_fulltext_html_url" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/" />
  <meta name="citation_pdf_url" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/v/31904017a84c37e8baab7b663cb5fe00f75cb3b0/" />
  <meta name="manubot_html_url_versioned" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/v/31904017a84c37e8baab7b663cb5fe00f75cb3b0/" />
  <meta name="manubot_pdf_url_versioned" content="https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/v/31904017a84c37e8baab7b663cb5fe00f75cb3b0/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://greenelab.github.io/T21-cis-eqtl-Chr21-regulation-manuscript/v/31904017a84c37e8baab7b663cb5fe00f75cb3b0/))
was automatically generated
from [greenelab/T21-cis-eqtl-Chr21-regulation-manuscript@3190401](https://github.com/greenelab/T21-cis-eqtl-Chr21-regulation-manuscript/tree/31904017a84c37e8baab7b663cb5fe00f75cb3b0)
on October 10, 2026.
</em></small>



## Authors



+ **Lucas A. Gillenwater**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0003-3158-9682](https://orcid.org/0000-0003-3158-9682)
    <br>
  <small>
     Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO
  </small>

+ **Marc Subirana-Granés**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0003-3934-839X](https://orcid.org/0000-0003-3934-839X)
    <br>
  <small>
     Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO
  </small>

+ **Mary A. Allen**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-7490-0165](https://orcid.org/0000-0001-7490-0165)
    <br>
  <small>
     BioFrontiers Institute, University of Colorado Boulder, Boulder, CO
  </small>

+ **Milton Pividori**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-3035-4403](https://orcid.org/0000-0002-3035-4403)
    <br>
  <small>
     Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO
  </small>

+ **Casey S. Greene**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-8713-9213](https://orcid.org/0000-0001-8713-9213)
    <br>
  <small>
     Department of Biomedical Informatics, University of Colorado Anschutz, Aurora, CO
  </small>


::: {#correspondence}
✉ — Correspondence possible via [GitHub Issues](https://github.com/greenelab/T21-cis-eqtl-Chr21-regulation-manuscript/issues)

:::


## Abstract {.page_break_before}

Down syndrome (DS) results from trisomy 21 (T21), the triplication of human chromosome 21 (HSA21).
On average, genes on HSA21 are overexpressed at the expected 1.5-fold increase.
A small subset of HSA21 genes is expressed closer to euploid levels.
Could local genetic regulatory variation explain deviations from the expected dosage?
Using the largest DS-specific transcriptomic dataset to date from the Human Trisome Project (HTP) and GTEx expression quantitative trait loci (eQTLs), we tested whether local genetic regulatory variation contributes to gene-specific buffering or amplification of HSA21 dosage effects in DS.

We compared the bulk RNA-seq profiles of protein-coding genes, lncRNAs, and pseudogenes from whole-blood samples of 274 participants with T21 and 80 euploid (D21) participants.
We filtered out genes with low read counts or high genomic repeat content and applied ploidy correction to the differential expression analysis.
We found 13 genes that differed significantly from the expected fold change.
We cross-referenced GTEx whole-blood eQTLs (*cis* window ±1 Mb) with the 13 deviating genes.
A common *cis*-eQTL was detected for 8 of the 10 testable genes.
However, 59 of 99 HSA21 genes that had the expected fold change had significant *cis*-eQTLs.
Additionally, T21 participants carry the eQTL alleles at similar frequencies to GTEx donors.
Therefore, *cis*-eQTLs explain differences between people with T21, not the difference between T21 and D21.

Overall, common *cis*-regulatory variation acts on HSA21 genes in T21 as it does in euploid blood, but it does not explain which genes deviate from the ploidy expectation.


## Introduction {.page_break_before}

The triplication of human chromosome 21 (HSA21), trisomy 21 (T21), causes Down syndrome (DS).
Multiple studies report that genes on HSA21 are expressed, on average, at the expected 1.5-fold change when compared to people with euploid karyotypes (disomic 21, D21) [@doi:10.1038/s41588-023-01399-7; @doi:10.1126/sciadv.adg6218; @doi:10.1016/j.celrep.2022.111883; @doi:10.1038/s41467-024-49781-1].
A small subset of HSA21 genes is expressed closer to euploid levels.
Potential causes for lower-than-expected HSA21 gene expression include confounding cell-type proportions, genetic effects, and compensatory regulation.
This study assesses the genetic effect hypothesis while controlling for cell-type proportions.

Previous researchers have noted that differences in genetic composition affect clinical and molecular phenotypes in DS.
Rachubinski et al. hypothesized that genetic variations beyond T21 may explain the development of autism spectrum disorder in some individuals with DS [@doi:10.1002/PD.4957].
Valentini et al. assessed genomic effects with a genome-wide association study (GWAS) in a cohort of 84 children with DS and found that the *PNPLA3* variant rs738409 on HSA22 was associated with liver steatosis [@doi:10.1016/j.numecd.2020.05.012].
A review by Antonarakis et al. noted that ~80% of T21 conceptuses are lost during pregnancy and inferred that a specific combination of genetic variants allows T21 conceptuses to survive to term [@doi:10.1038/s41572-019-0143-7].
In 388 live-born individuals with DS, Popadin et al. found signatures of embryonic selection: a deficit of deleterious variants on HSA21 and reduced transcriptome-wide variation in the expression of highly constrained genes [@doi:10.1101/gr.228411.117].

Hunter et al. tested whether the genotype of common expression quantitative trait loci (eQTLs) explained lower-than-expected gene expression of HSA21 genes in a child with DS compared to family members (i.e., brother, mother, and father euploid for HSA21) [@doi:10.1186/s12915-023-01700-4].
The authors introduced a methodology to control for common factors that bias differential expression studies in DS research.
Specifically, the methodology accounted for genes with no reads, low gene expression, high genomic repeats, and karyotype.
Overall, the analysis confirmed that the majority of HSA21 genes show the expected 1.5-fold change.
There were 5 genes that fell below the expected fold change.
Of those 5 genes, 3 had common eQTLs in the general population.
Genotyping confirmed that the allele dosage at those eQTLs explained the lower-than-expected gene expression in the individual with DS.

Here we extend the methodology of Hunter et al. to the population level.
We assess how *cis*-eQTLs on HSA21 affect whole-blood gene expression in a large cohort of individuals with and without DS.
We account for triploidy and cell-type composition in the differential expression analysis.
We perform ploidy-aware genotyping of HSA21 in people with T21 to accurately represent allele counts.
We compare the sample genotypes against common eQTLs found in whole blood of disomic individuals in the GTEx cohort.
Overall, common *cis*-eQTLs affect HSA21 gene expression in people with T21 as they do in D21 individuals, but they do not explain which genes deviate from the expected 1.5-fold change.
The genotype of one person can account for that person's deviations, as in Hunter et al., but common *cis*-regulatory variation does not explain the deviation at the population level.

## Methods {.page_break_before}

### Study consent
As part of the INCLUDE project, the Linda Crnic Institute for Down Syndrome at the University of Colorado Anschutz Medical Campus enrolled participants under a study protocol approved by the Colorado Multiple Institutional Review Board (COMIRB #15-2170).
Human Trisome Project (HTP) researchers at the Linda Crnic Institute for Down Syndrome obtained written informed consent from all participants over 7 years old, as allowed by their cognitive ability, or from their legally authorized representative.
Regardless of study participant age or cognitive ability, researchers explained study procedures to the participant.
HTP researchers recorded age, sex, and body mass index (BMI) during the visit.

### Whole-blood transcriptome quantification
Waugh et al. [@doi:10.1038/s41588-023-01399-7] describe the process of blood collection, processing, and quantification in detail.
Briefly, researchers collected peripheral blood in PAXgene RNA tubes (QIAGEN), performed poly-A+ RNA enrichment, and used the Illumina NovaSeq 6000 (Novogene) for paired-end sequencing before additional bioinformatic processing to produce gene-level count data.
The libraries were globin-depleted and strand-specific (NEBNext Ultra II Directional), and gene-level counts were obtained by strand with HTSeq-count against the GENCODE v33 annotation (GEO GSE190125).

### Mass cytometry of white blood cells
For a detailed account of the quantification of white blood cells, see Galbraith et al. [@doi:10.1126/sciadv.adg6218].
Whole-blood samples underwent red blood cell lysis and white blood cell fixation, followed by barcoding with a Cell-ID 20-Plex Pd kit and pooling.
Pooled samples were stained with antibodies, with surface marker staining performed before permeabilization and intracellular transcription factor/phospho-epitope staining performed after.
Cells were then labeled with Cell-ID Intercalator-Ir and quantified on a Helios mass cytometer.
Batched FCS files were demultiplexed and individual samples were normalized across batches.

### Whole genome sequencing
Whole genome sequencing of Human Trisome Project participants was performed at the Broad Institute as part of the NIH INCLUDE and Gabriella Miller Kids First projects, and the cohort is described by Feldman et al. [@doi:10.1002/gepi.70010].
PCR-free libraries were prepared from genomic DNA sheared to approximately 385 bp using the KAPA Hyper Prep kit without amplification, and sequenced on an Illumina NovaSeq 6000 (S4 flow cells) to a target read depth of ~30x coverage to produce 151 bp paired-end reads.

Reads were aligned to the GRCh38 reference genome (Homo_sapiens_assembly38) with BWA-MEM v0.7.15, duplicate-marked with Picard v2.20.4, and base quality score recalibrated with GATK v4.0.10.1 using the Broad WholeGenomeGermlineSingleSample workflow.
These analysis-ready CRAM files were used as the input for variant calling, without further preprocessing.

### Ploidy-aware variant calling on HSA21
Standard germline genotyping workflows assume a diploid genome and therefore misassign allele dosage on HSA21 in individuals with T21; for this reason, chromosome 21 was excluded from the association analyses of Feldman et al. [@doi:10.1002/gepi.70010].
We therefore re-called HSA21 variants directly from the aligned CRAM files with a ploidy-aware caller.
Variants on HSA21 were called in 433 Human Trisome Project participants with whole genome sequencing data, comprising 419 participants with T21 and 14 D21 participants.
Variants were called against the same GRCh38 reference with Octopus v0.7.4 [@doi:10.1038/s41587-021-00861-3], using the individual caller on each sample independently and restricting calling to HSA21 (--regions chr21).
The ploidy of HSA21 was set to 3 for participants with T21 (--contig-ploidies chr21=3), whereas D21 samples were called at the default ploidy of 2.
All other Octopus parameters were left at their default values.

Calls were filtered with the default Octopus hard-filter expression (QUAL < 10, MQ < 10, MP < 10, AD < 1, AF < 0.01, AFB > 0.25, SB > 0.98, BQ < 15, DP < 1, ADP < 1), and only records with FILTER = PASS were retained using BCFtools v1.21 [@doi:10.1093/gigascience/giab008].
Filtering retained approximately 85% of raw calls, corresponding to a median of 81,667 variants per T21 sample (range, 59,473 to 104,854) and 66,238 variants per D21 sample (range, 63,054 to 80,735).

Within each group, PASS-filtered per-sample calls were merged with bcftools merge, keeping distinct alternate alleles at the same position as separate records (--merge none).
Samples with no call at a merged site were assigned the homozygous reference genotype (--missing-to-ref; 0/0/0 in T21, 0/0 in D21).
The resulting call sets comprised 688,787 variant records in the T21 group and 189,474 in the D21 group.
Of these, 529,386 T21 and 142,792 D21 records contained an SNV, and 160,468 T21 and 46,845 D21 records contained an indel; a multiallelic record can contain both, so the two counts overlap.
The workflow was implemented in Snakemake v9.16.3 [@doi:10.12688/f1000research.29032.2] and run on the Alpine high-performance computing cluster (University of Colorado Boulder Research Computing).

### Cohort filtering
To assess genetic effects, we required samples to have matched whole-blood bulk RNA sequencing counts, whole genome sequencing, cell-type composition, and all demographic and technical data (i.e., age, sex, BMI, and sample source) (Figure {@fig:s1-covariates}A).
Additionally, while ~95% of individuals with DS have full T21, translocation accounts for ~5% and mosaicism for ~2% of cases [@doi:10.1038/s41572-019-0143-7].
Mosaicism affects expression levels (Figure {@fig:s1-covariates}C).
Therefore, we removed samples with mosaic T21 (9 samples).
We kept samples with translocation DS, whose HSA21 expression was similar to that of samples with full T21 (Figure {@fig:s1-covariates}C).
The 274 T21 participants in the analysis cohort comprised 235 with full T21, 7 with translocation DS, and 32 whose karyotype subtype was not recorded (we therefore assume full T21).

### Ploidy-aware differential expression analysis
Generally, we followed the methods of Hunter et al. [@doi:10.1186/s12915-023-01700-4].
We compared DESeq2 [@doi:10.1186/s13059-014-0550-8] fits using default parameters against fits that set the expected fold change to 1.5 for HSA21 genes in T21 samples and to 1 for all other gene-karyotype combinations.
We excluded HSA21 from the size-factor (library normalization) calculation so that HSA21's own inflated counts do not bias normalization for the rest of the genome.
As a negative control, we assessed the change in distribution for HSA22 genes between the run with default parameters and the ploidy-adjusted run.

The model included age, sex, BMI, and sample source as covariates.
In addition, cell-type proportions affect gene expression (Figure {@fig:s1-covariates}B).
Therefore, we included 19 cell-type proportions as covariates in the model.
P-values were adjusted for multiple testing across genes using the Benjamini-Hochberg procedure [@doi:10.1111/j.2517-6161.1995.tb02031.x].

We restricted HSA21 gene biotypes in whole blood to protein-coding, lncRNA, and pseudogenes since those are the gene biotypes covered by the GTEx eQTL data.
We excluded genes with low average read counts (baseMean < 30) or that fall in genomic regions with high repeat content that cannot be reliably quantified.
A gene was classified as deviating from the 1.5-fold ploidy expectation if its ploidy-corrected fold change differed from 1.5 by at least 33% (adjusted p < 0.01).
Deviating genes were further stratified into tier 1 (≥50% deviation from the 1.5-fold expectation) and tier 2 (33–50% deviation).

### *cis*-eQTL association testing
For each deviating gene, we retrieved all variants within ±1 Mb that GTEx v10 annotates as at least nominally associated (GTEx nominal p ≤ 10^−4^) with that gene's expression in whole blood.
The minor allele refers to the GTEx whole-blood minor allele frequency and checked against gnomAD v4.1 (Supplementary Table S2).
We regressed expression against genotype dosage (0-3 copies of the alternate minor allele) within T21 participants, with the covariates of the primary analysis (age, sex, BMI, sample source, and 19 cell-type proportions) regressed out of both expression and genotype dosage and retained each gene's strongest-associated variant.
For each gene, we report the effect per copy of whichever allele, minor or major, correlates with the dirction of the fold-change between T21 and D21 participants.
<!-- Milton's comment: are you running more permutations for genes that are borderline significant? -->
Statistical significance was assessed by a gene-level permutation test where the covariate-adjusted expression values were shuffled across participants 1,000 times, the same variant search was repeated on each shuffle, and the fraction of shuffles producing an association at least as strong as the observed one gave a gene-level permutation p-value.
Permutation p-values were adjusted for multiple testing across genes using the Benjamini-Hochberg procedure [@doi:10.1111/j.2517-6161.1995.tb02031.x].

### *cis*-eQTL comparisons
Under an additive model, each copy of HSA21 contributes to gene expression.
The T21/D21 ratio is then 1.5 × (1 + *r* × *p*~T21~) / (1 + *r* × *p*~D21~), where *r* is the output of the alternate allele relative to the reference allele, and *p* is the frequency of the alternate allele in each group.
If the allele has the same frequency in both populations, the ratio is 1.5.

The cohort had 14 D21 participants with WGS, only 2 of which had matching transcriptomic data.
Therefore, we estimated D21 allele frequencies from the GTEx whole-blood donors.
The T21 participants contribute 822 alleles (3 each), and the 800 GTEx whole-blood donors contribute 1,600 (Supplementary Table S2 also gives the frequencies in gnomAD v4.1 and in the 14 genotyped D21 participants).
Confidence intervals for the difference assume binomial sampling in both groups.
Therefore, a T21 participant's three copies are assumed independent, although two come from the same parent.
We did not have parental WGS and therefore could not determine which parent experienced nondisjunction prior to mating.

For each tested gene's best variant, we obtained *r* from the within-T21 slope (*r* = 2^3*b*^ − 1, where *b* is the slope in log~2~ units per copy) and took the two allele frequencies from the T21 participants and from GTEx.
The ratio between T21 and D21 reveals the shift from 1.5 that the variant produces at the observed frequencies.
We then artificially set the T21 frequency to 0 and to 1 to find the largest shift the variant could produce at any frequency.
We solved the ratio for the T21 frequency that would produce the entire deviation.
We also report how much of the expression variance among T21 participants the best variant explains.

We compared the deviating genes with the HSA21 genes at the expected dosage.
We applied the identical test (same variant selection, participants, covariates, and 1,000 permutations) to every expected-dosage gene with a GTEx variant to test, adjusting for multiple testing across those genes.
Detection depends on the strength of an eQTL, so we compared the deviating genes with expected-dosage genes whose eQTLs are of similar strength in GTEx.
Among the expected-dosage genes that are GTEx whole-blood eGenes (i.e., have an eQTL at q < 0.05), we fit a logistic regression of detection on the log2 of the absolute GTEx allelic fold change (aFC) [@doi:10.1101/gr.216747.116] at the GTEx lead variant, and compared the observed number of detected deviating genes with the distribution of the sum of their predicted probabilities.
To compare effect sizes, we estimated the aFC in T21 by least squares, modeling each of the three HSA21 copies as contributing its own expression and fitting the covariates jointly.
Each dataset's effect was taken at its own strongest variant, so that both carry the same selection: the T21 aFC at the variant selected by the within-T21 test, signed by the GTEx direction at that variant, was divided by the absolute GTEx aFC at the GTEx lead variant.
We compared this ratio between the deviating genes and the expected-dosage eGenes whose absolute GTEx aFC lay within the deviating genes' range, using a Wilcoxon rank-sum test.
To estimate the power of the test for each tested deviating gene, we permuted its expression across participants, added an allelic effect at its GTEx lead variant under the three-copy model, and repeated the gene-level test, 200 times for each of a grid of effect sizes; a simulation counted as a detection at gene-level permutation p < 0.05, and power at the gene's GTEx aFC was interpolated from the grid.
As a negative control, we regressed the expression of every assessable HSA21 gene on every common HSA21 variant at least 5 Mb from its transcription start site, where no *cis* effect is expected, and measured the genomic inflation factor (Supplement F).

### Expression of the HSA21 genes in blood
To check that the deviating genes are expressed in blood, we took the median expression of each HSA21 gene in 68 tissues from GTEx v10, in transcripts per million (TPM) [@doi:10.1126/science.aaz1776].
We compared the whole-blood TPM of the deviating and expected-dosage genes with a Wilcoxon rank-sum test.
We also placed each deviating gene at its percentile among the expected-dosage genes.

To relate expression to eQTL detection, we compared whole-blood TPM between GTEx eGenes and non-eGenes, and between genes with and without a *cis*-eQTL detected in T21, with Wilcoxon rank-sum tests.
We ranked each deviating gene's whole-blood TPM among its 68 GTEx tissues to assess the typical representation in blood.

We also compared expression in the T21 participants with GTEx whole blood.
We converted the participants' read counts to TPM, using the union of exons in the GENCODE v44 basic annotation as gene length [@doi:10.1093/nar/gkac1071].
Since the HTP libraries are globin-depleted and the GTEx libraries are not, we measured the overall offset between the two datasets on the non-HSA21 genes.

### Sensitivity analysis
To quantify the effect of covariate adjustment and mosaic exclusion, we compared the adjusted results to the outputs from the identical pipeline without covariate adjustment and without excluding mosaic participants (Figures {@fig:s1-covariates}D and {@fig:s3-comparison}).
Additionally, we refit the adjusted model with an interaction between karyotype and each of the 19 cell fractions.
The fractions were centered, so the karyotype effect is the T21 effect at the cohort-mean composition.
The interaction terms widened the standard error of the karyotype effect by a median of 1.76-fold for HSA21 genes, so we compared effect estimates rather than significance across the models (Supplement C).

## Results {.page_break_before}

### Most chromosome 21 genes show a gene-dosage-dependent increase in expression
To determine whether HSA21 genes in whole blood from people with T21 are expressed in proportion to their extra copy, we compared transcript levels between T21 and D21 participants before and after ploidy correction.

The HTP RNA-seq cohort consisted of 399 participants, 304 with T21 and 95 D21.
Filtering removed samples missing cell-type composition (22) or BMI metadata (12), and samples with mosaic karyotypes for HSA21 (9).
We also removed samples from T21 participants who did not have WGS data (2).
We compared whole-blood bulk RNA transcript counts between 274 T21 samples and 80 D21 samples, a total of 354 samples.
T21 participants had significantly higher body mass index (BMI) than D21 participants (Table {@tbl:cohort-characteristics}).
The D21 participants were older than the T21 participants (median 27.4 vs. 24.0 years), but the difference was not significant.
The sex composition did not significantly differ by karyotype.
Though processed at the same facility, the samples were collected at 3 different locations.

| Characteristic | Level | T21 (n=274) | D21 (n=80) |  P-value |
|---|---|---|---|---|
| Age at visit (years) | median [IQR] | 24.0 [16.1-32.5] | 27.4 [16.3-37.8] |  0.0802 |
| BMI | median [IQR] | 27.6 [23.1-33.4] | 24.2 [20.4-27.4] |  < 0.0001 |
| Sex | Female | 124 (45.3%) | 45 (56.2%) | 0.0982 |
| | Male | 150 (54.7%) | 35 (43.8%) | |
| Sample source | Local | 81 (29.6%) | 54 (67.5%) | 0.0005 |
| | NDSC2018 | 81 (29.6%) | 7 (8.8%) | |
| | NDSC2019 | 112 (40.9%) | 19 (23.8%) | |


Table: Analysis cohort assembly and baseline characteristics, stratified by karyotype. {#tbl:cohort-characteristics}

We assessed the effects of ploidy correction on the differential expression analysis.
Of the 318 HSA21 genes, 153 had baseMean coverage $\ge$ 30 and were not in high-repeat regions.
Before ploidy correction, statistically significant (adjusted p < 0.01) fold changes of at least 1.33 in either direction were observed in 76% (117) of the HSA21 genes passing thresholds.
After ploidy correction, 13 genes (8.5%) still deviated from the expected 1.5-fold change by at least 33% in either direction, at adjusted p < 0.01 (Table {@tbl:chr21-classification} and Figures {@fig:volcano-chr21} and {@fig:s2-volcano-all}).
The deviations of *OLIG2*, *BACE2*, *OLIG1*, and *RUNX1* were the most robust to the choice of covariate model (Supplement C).
Per-gene statistics for all 318 genes are given in Supplementary Table S1.
The magnitude of the correction matches the ploidy expectation.
Across the 318 HSA21 genes, the median log2 fold change shifted from 0.593 (close to log2(1.5) = 0.585) before correction to 0.008 after correction.
Chromosome 22 showed no shift, confirming that the correction is specific to HSA21 (Figure {@fig:ploidy-correction}).

![Differential expression of the 318 targeted HSA21 genes between T21 and D21 participants, before (A) and after (B) ploidy correction. Each point is one gene, plotted by its log~2~ fold change and the −log~10~ of its adjusted p-value. The dotted line in A marks the 1.5-fold expectation (log~2~ 1.5 = 0.585), and the dashed horizontal line marks adjusted p = 0.01. The 13 deviating genes are labeled and colored by direction (red, higher than expected; blue, lower than expected), with tier 1 genes in bold; other HSA21 genes are grey. One gene in A exceeds the plotted range and is drawn as a triangle at the top edge.](images/figures/fig_volcano_chr21.png){#fig:volcano-chr21 width="90%"}

![Effect of ploidy correction on the log~2~ fold change (T21 vs D21) of HSA21 genes. (A) Density and (B) empirical cumulative distribution for the 318 targeted HSA21 genes (purple) and 650 HSA22 genes (grey), on the uncorrected (light) and ploidy-corrected (dark) scales. Vertical lines mark 0 and log~2~ 1.5. The correction shifts the HSA21 median by −0.585 and leaves HSA22 unchanged; after correction the two distributions are similar (Kolmogorov–Smirnov D = 0.095).](images/figures/fig_ploidy_correction_distributions.png){#fig:ploidy-correction width="90%"}

| Category | Genes |
|---|---|
| Expected dosage | 129 |
| Low expression (not assessable) | 153 |
| High repeats (not assessable) | 12 |
| Near-threshold, not significant | 11 |
| Deviates, higher (DE_high) | 6 |
| Deviates, lower (DE_low) | 7 |

Table: Classification of all 318 targeted HSA21 genes in the primary (adjusted) analysis. {#tbl:chr21-classification}

### Common *cis*-eQTLs affect gene expression in T21, but do not explain deviations in gene expression
To assess potential genetic effects explaining deviating genes, we compared the ploidy-aware genotypes and covariate-adjusted whole-blood gene expression of 274 T21 participants to common whole-blood eQTLs.
Three of the 13 deviating genes had no variant to test: GTEx tested *ATP5PF* and *RUNX1* in whole blood but found no eQTL (q = 0.22 and 0.21) [@doi:10.1126/science.aaz1776], and GTEx did not test *AP000282.1* in whole blood (the GTEx gene model excluded the exon it shares with *OLIG1*; Supplement G).
Of the remaining 10 testable genes, 8 have a detected *cis*-eQTL and 2 do not (*BACE2*, *OLIG2*) (Table {@tbl:eqtl-genes}, Figures {@fig:flow-map}A and {@fig:s6-eqtl-dosage}).
The expression of *ABCC13* (q = 0.034) is also associated with HSA21 genotype far from its own locus (Supplement F).
All 13 deviating genes sit on the q arm, between 14.2 and 46.3 Mb (Figure {@fig:flow-map}B).
Allele frequencies for every tested variant, in GTEx whole blood, in gnomAD, and in this cohort, are given in Supplementary Table S2.

The deviating genes are measurably expressed in blood (Supplement G, Figure {@fig:s5-gtex-expression}A).
Expression level in GTEx did not correspond with eQTL detection (Figure {@fig:s5-gtex-expression}B).
*OLIG2* and *BACE2* are among the least expressed in GTEx whole blood (0.27 and 0.71 TPM), yet GTEx detects strong whole-blood eQTLs for both (q = 1.2 × 10^−13^ and 6.2 × 10^−16^).

| Gene | Direction | Tier | *cis*-eQTL status |
|---|---|---|---|
| *ABCC13* | Higher | 1 | Detected |
| *CBR3* | Higher | 2 | Detected |
| *ADAMTS1* | Higher | 2 | Detected |
| *YBEY* | Higher | 2 | Detected |
| *COL6A2* | Higher | 2 | Detected |
| *ATP5PF* | Higher | 2 | Not testable (no GTEx whole-blood eQTL) |
| *OLIG2* | Lower | 1 | Tested, not detected |
| *OLIG1* | Lower | 1 | Detected |
| *AP000282.1* | Lower | 1 | Not testable (not tested by GTEx in whole blood) |
| *BACE2* | Lower | 2 | Tested, not detected |
| *KCNE1* | Lower | 2 | Detected |
| *PCBP3* | Lower | 2 | Detected |
| *RUNX1* | Lower | 2 | Not testable (no GTEx whole-blood eQTL) |

Table: *cis*-eQTL status of the 13 genes that deviate from the ploidy expectation in the primary (adjusted) analysis. {#tbl:eqtl-genes}

To ask whether a detected *cis*-eQTL is more common among the deviating genes than among HSA21 genes at the expected dosage, we applied the identical test to the 99 testable expected-dosage genes, of which 59 (60%) had a detected *cis*-eQTL.
Among the 97 of these that are GTEx whole-blood eGenes, detection rose with the strength of the GTEx eQTL (p < 0.001), and at the deviating genes' own GTEx effect sizes it predicted 7.4 detections, against the 8 observed (probability of 8 or more, 0.49).
The effects in T21 were also similar in size: relative to the GTEx effect, the median T21 allelic fold change was 0.73 for the deviating genes and 0.76 for the 49 expected-dosage eGenes with GTEx effects in the same range (Wilcoxon p = 0.64; Figure {@fig:eqtl-overview}A).
*BACE2* and *OLIG2* were not missed for lack of power: with their GTEx effect added to their own permuted expression, the test detected it in 100% and 99% of simulations (Figure {@fig:eqtl-overview}B).
Their T21 effects relative to GTEx (0.33 and 0.36) lay within the range of the 11 matched expected-dosage eGenes without a detected *cis*-eQTL (median 0.44).
As a negative control, the expression of the assessable HSA21 genes regressed on common HSA21 variants at least 5 Mb away showed no inflation beyond its permutation range (λ = 1.020; Supplement F).

The detected *cis*-eQTLs cannot account for the deviations in gene expression.
The T21 participants carried the tested alleles at frequencies that did not differ systematically from those of the 800 GTEx whole-blood donors.
Across the 2,076 tested *cis* variants, the median difference was −0.0005({@fig:af-bound}A).
At each tested gene's best variant, the observed frequency difference predicted between −8% and +4% of the deviation (Figure {@fig:af-bound}B).
Even if T21 participants carried the allele on every copy or on none, the best variant could not produce the observed deviation.
The best variants explain 2% to 33% of the expression variance among T21 participants (Figure {@fig:af-bound}C).

![Classification of the 318 targeted HSA21 genes and the positions of the deviating genes. (A) Flow of every gene from the full set through the dosage classification (expected dosage, 129; outside the dosage expectation, 24, of which 11 did not reach significance, 6 are higher than expected and 7 lower; not assessable, 165, of which 153 have low expression and 12 lie in high-repeat regions) to the *cis*-eQTL outcome of the 13 deviating genes (detected, 8; tested without detection, 2; no variant to test, 3). (B) Chromosome 21 (GRCh38) with a band at the transcription start site of each deviating gene, colored by *cis*-eQTL outcome: detected (black), tested without detection (white), or no variant to test, either because GTEx tested the gene in whole blood and found no eQTL (dark grey; *ATP5PF*, *RUNX1*) or because GTEx did not test it (light grey; *AP000282.1*). Bands of neighboring genes are stacked. The short arm is light grey and the centromere dark grey. Labels above the bar are genes higher than expected; labels below are genes lower than expected.](images/figures/fig_lane_flow_and_map.png){#fig:flow-map width="100%"}

![Effect size and power of the *cis*-eQTL test. (A) For each gene, the T21 allelic fold change at its strongest variant in T21 relative to the GTEx whole-blood allelic fold change at the GTEx lead variant, for the 10 testable deviating genes and the 49 expected-dosage GTEx eGenes whose GTEx effect lies in the same range (|log~2~ aFC| 0.32 to 1.39). Each ratio is signed by the GTEx direction at the T21 variant, so the dashed line marks an effect equal to GTEx's and the dotted line none; bars mark the medians (0.73 vs 0.76, Wilcoxon p = 0.64). Filled points have a *cis*-eQTL detected in T21 and open points do not; deviating genes are colored by direction and expected-dosage genes are grey. (B) Power of the gene-level test for each tested deviating gene, from 200 simulations per effect size with the gene's own genotypes, variant set, and expression noise; points mark each gene's GTEx effect, and the dashed line marks 80%.](images/figures/fig_eqtl_detection_overview.png){#fig:eqtl-overview width="100%"}

![How much of each deviation a *cis*-eQTL could produce. (A) Alternate allele frequency of the 2,076 tested *cis* variants in the 274 T21 participants (822 copies) against the 800 GTEx whole-blood donors (1,600 copies), with the deviating genes' best variants labeled (filled, *cis*-eQTL detected in T21; open, tested without detection). *OLIG1* and *OLIG2* share a best variant. The median difference is −0.0005 and the median absolute difference 0.012, against 0.009 expected from sampling alone. (B) For each tested deviating gene, the observed deviation of log~2~(T21/D21) from log~2~ 1.5 (point, 95% CI), the shift predicted by the observed frequency difference at its best variant (diamond, 95% CI), and the largest shift possible, with the alternate allele on every T21 copy or on none, taken at the 95% confidence edge of the slope (grey bar). (C) Fraction of expression variance among T21 participants explained by the best variant.](images/figures/fig_af_deviation_bound.png){#fig:af-bound width="100%"}

In summary, after ploidy correction most HSA21 genes showed the expected increase with gene dosage, and 13 deviated.
A common *cis*-eQTL was detected for 8 of the 10 testable deviating genes, about as often as for HSA21 genes at the expected dosage with eQTLs of the same GTEx strength, and with similar effect sizes.
The T21 participants have allele frequencies that do not differ systematically from those of GTEx donors.
*cis*-eQTLs explain differences between people with T21, not the difference between T21 and D21.
Our work does not support the genetic hypothesis for expression deviations for any of the 13 genes outside of the 1.5-fold difference, including the 2 tested without a detected eQTL (*BACE2*, *OLIG2*) and the 3 that could not be tested (*ATP5PF*, *RUNX1*, *AP000282.1*) (Figure {@fig:flow-map}).

## Discussion {.page_break_before}

Trisomy 21 increases the expression of most HSA21 genes by the expected 1.5-fold, yet there is a subset of HSA21 genes with expression more similar to that of disomic individuals [@doi:10.1186/s12915-023-01700-4; @doi:10.1038/s41467-024-49781-1].
Lower- or higher-than-expected gene expression may reflect genetic variation across the population, compensatory regulation, or technical artifacts.
Hunter et al. tested the genetic regulation hypothesis within a family cohort consisting of one T21 child, one D21 child, and the two D21 parents [@doi:10.1186/s12915-023-01700-4].
No one had yet assessed the genetic variation hypothesis for deviating gene expression using transcriptomic and WGS profiles from a large, population-level cohort of people with DS.
Here we demonstrate that common *cis*-eQTLs affect HSA21 gene expression in people with T21. 
However, the common *cis*-regulatory variation does not explain gene expression deviation from the expected 1.5-fold difference at the population level.

Hunter et al. found that only 5 genes had expression levels similar to D21 levels after considering coverage, high-repeat regions, and proper ploidy in the differential expression analysis.
Through cross-referencing common *cis*-eQTLs from GTEx whole-blood profiles, the authors found that the genotype of the individual with DS explained the variance in *CLIC6*, *ITSN1*, and *C2CD2*, but not for *LINC02246* or *BRWD1*.
In the present study, we did not find the same 5 deviating genes that Hunter et al. found.
*ITSN1*, *C2CD2*, and *BRWD1* are expressed in whole blood and sit at the expected dosage.
*CLIC6* and *LINC02246* had low coverage.

In a cohort of 4, where one individual had T21, the authors could attribute deviations in gene expression to the genotype of that person [@doi:10.1186/s12915-023-01700-4].
The present study evaluated 354 whole-blood profiles and found that people with T21 carry the tested alleles at frequencies similar to those of euploid GTEx donors (Figure {@fig:af-bound}A).
While both studies demonstrate the genomic effects on gene expression in people with DS (Figure {@fig:eqtl-overview}A), the higher powered study did not support the conclusion that eQTLs explain deviation from the expected 1.5-fold change (Figure {@fig:af-bound}B).

We demonstrated that the majority of HSA21 genes show the expected 1.5-fold change in gene expression if we filter out genes in high-repeat regions and genes with low coverage, and adjust the differential expression pipeline for sample ploidy.
We tested for deviation both above and below the expected dosage.
The compensation hypothesis predicts that genes are downregulated toward euploid levels, whereas eQTLs can raise or lower expression.
Of the 10 deviating genes with a GTEx variant to test, 5 were higher than expected and 5 lower, and 8 had a detected *cis*-eQTL.
The two genes that did not have *cis*-eQTLs were *BACE2* and *OLIG2*.
*BACE2* codes for a homolog of β-secretase BACE1, a protein involved in amyloid precursor processing and associated with Alzheimer's disease in people with DS [@doi:10.1111/ejn.70623].
*OLIG2* codes for a transcription factor involved in mammalian central nervous system development [@doi:10.3390/ijms25052968].
Both were found to have lower expression in the population than expected, closer to the euploid level.
Both are known for their roles in brain tissue and are expressed at low levels in blood, but GTEx detects strong whole-blood eQTLs for both, and the test had full power at their GTEx effect sizes (Figure {@fig:eqtl-overview}B; Supplement G).
Their T21 effects relative to GTEx (0.33 and 0.36) are within the range of matched expected-dosage eGenes in GTEx that were also not detected, and their deviations are among the most robust to the choice of covariate model (Supplement C).

Overall, the genomic hypothesis does not explain deviating genes in this cohort.
A *cis*-eQTL was detected for 60% of the expected-dosage HSA21 genes that could be tested, so the deviating genes were not unique.
The eQTL effects in T21 had the same direction and a similar size as in GTEx (Figure {@fig:eqtl-overview}A).
The mechanism for the deviation of these genes therefore remains open.

There are multiple other factors that may explain deviations in gene expression.
Candidate non-genetic mechanisms for lower-than-expected transcript counts include autoregulatory feedback loops, post-transcriptional silencing by triplicated HSA21 miRNAs, alternative splicing into unstable isoforms, and chromatin remodeling.
Six of the 13 deviating genes are in the 21q22.1 region where Wu et al. observed A/B compartment switches in T21 fetal brain high throughput chromosome conformation capture (Hi-C) [@doi:10.1093/gpbjnl/qzaf054].
In either direction, genetic effects not captured by common *cis*-eQTLs, such as rare regulatory variants, splicing QTLs (sQTLs), or *trans*-eQTLs, may also contribute.
Integrating evidence from additional omic profiles would enable the direct testing of multiple alternative hypotheses.

Our study has several limitations.
The eQTLs we tested were mapped in euploid GTEx whole blood.
GTEx mapped them in bulk tissue, which dilutes cell-type-specific effects [@doi:10.1038/s41586-026-10577-6].
Donovan et al. found that whole-blood cell-type composition differed in subpopulations of this cohort [@doi:10.1038/s41467-024-49781-1].
Cell-type-specific eQTLs, from single-cell data such as OneK1K [@doi:10.1126/science.abf3041], might be detected where bulk eQTLs were not.
Moreover, ancestry may affect the observed eQTLs.
Ancestry structure in the cohort was handled through covariates rather than genotype principal components (Supplement F).

The covariates, chosen for their association with karyotype, also affected which genes deviate.
The unadjusted and adjusted analyses share 6 deviating genes.
The composition adjustment covers leukocytes only, so a gene expressed in erythroid or platelet lineages, such as *KCNE1*, could deviate through a composition difference the model cannot see.
*OLIG2* and *BACE2* deviate in all tested models.
Even in the adjusted model, 9 of the 13 deviating genes lie between 33% and 50% from the expected dosage, within about one standard error of the threshold, and a larger cohort would resolve them.

These results are relevant for the genomic hypothesis of embryonic selection.
About 80% of T21 conceptions are lost before birth [@doi:10.1038/s41572-019-0143-7], and live-born people with DS carry fewer deleterious variants on HSA21 than expected [@doi:10.1101/gr.228411.117].
If survival to term favored embryos whose common *cis*-regulatory alleles dampen dosage-sensitive HSA21 genes, live-born people with T21 would carry those alleles at shifted frequencies.
We saw no such shift: across the 2,076 tested *cis* variants, the T21 frequencies did not differ systematically from those of GTEx donors.
Future work should consider rare variants, effects across many loci, and interactions between loci.

In the largest cohort to date with matched transcriptomes and ploidy-aware genotypes, common *cis*-eQTLs act on HSA21 genes in people with T21 as they do in D21 blood.
Common eQTLs do not explain deviations in gene expression from the expected fold change since similar allele frequencies were observed in T21 and D21. 
Therefore, deviations must arise from other mechanisms related to the trisomy itself.

## Data and Code Availability
The demographics and clinical data for research participants in the HTP study are available on both the Synapse data sharing platform (https://doi.org/10.7303/syn31488784) and the INCLUDE Data Hub (https://portal.includedcc.org/).
Whole-blood transcriptome data for research participants are available through Synapse (https://doi.org/10.7303/syn31488780), the INCLUDE Data Hub, and Gene Expression Omnibus (GSE190125).
Mass cytometry data for 380+ research participants are available in Synapse (https://doi.org/10.7303/syn31488783).
Whole genome sequencing data are available under controlled access in the NIH database of Genotypes and Phenotypes (dbGaP) under accession phs002981.v2.p1 and require a Data Access Request approved by the NHLBI Data Access Committee (https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs002981.v2.p1).
Whole-blood *cis*-eQTL data were obtained from the GTEx Portal (release v10; https://gtexportal.org/).

All original code for ploidy-aware variant calling on HSA21 has been deposited at https://github.com/pivlab/dosage_comp and is publicly available as of the date of publication.
Code for the ploidy-aware differential expression and common eQTL comparisons is available at https://github.com/greenelab/T21-eQTL.


## Acknowledgements

This work was funded by NIH grant R01 HD109765.

The results analyzed and published here use data generated by the INCLUDE Project (dbGaP accession phs002981.v2.p1), and were accessed from the INCLUDE Data Hub and/or dbGaP (www.ncbi.nlm.nih.gov/gap).
We thank the Human Trisome Project investigators at the Linda Crnic Institute for Down Syndrome, who submitted these data. Moreover, we thank the study  participants and their families. 
The GTEx Project was supported by the Common Fund of the Office of the Director of the National Institutes of Health, and by the National Cancer Institute, the National Human Genome Research Institute, the National Heart, Lung, and Blood Institute, the National Institute on Drug Abuse, the National Institute of Mental Health, and the National Institute of Neurological Disorders and Stroke.
The data used for the analyses described in this manuscript were obtained from the GTEx Portal (release v10) on May 4, 2026.


## Declaration of interests

The authors declare no competing interests.

## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>


## Supplement {.page_break_before}

### Supplement A: Evidence for covariate adjustment
Before attributing a gene's deviation from the 1.5-fold expectation to HSA21 dosage rather than age, BMI, or blood-cell composition, we confirmed, in the full cohort, that: (1) several clinical and demographic factors differ significantly by karyotype (age p = 0.033, BMI p < 0.0001; sex did not differ as strongly); (2) directly measured blood-cell-type composition is associated with expression of thousands of genes genome-wide; and (3) the 9 mosaic-DS participants, whose cells do not all carry the extra chromosome, show a smaller chromosome-21 dosage effect (mean composite HSA21 index ≈ 1.07x) than participants with full trisomy (≈1.35--1.45x), a sanity check that the dosage measurement itself behaves as expected.
These findings motivate adjusting for age, sex, BMI, sample source, and cell-type composition in the primary analysis (Figure {@fig:s1-covariates}).

![Covariate evidence for the adjusted analysis. (A) Association of each candidate covariate with karyotype (−log~10~ p), colored by whether it entered the adjusted model; the dotted line marks p = 0.05. (B) Number of genes associated with each CyTOF cell fraction within T21 at 5% FDR. (C) HSA21 expression index (median ratio of HSA21 gene expression to D21) by karyotype subtype as recorded in the INCLUDE Data Hub (DS T21, Down syndrome with the subtype unspecified), with reference lines at 1 and 1.5; mosaic participants sit near 1. (D) For each gene that deviates in either analysis, the contribution of each covariate to the shift in log~2~ fold change between the unadjusted and adjusted analyses, colored by covariate.](images/figures/fig_S1_covariate_evidence.png){#fig:s1-covariates tag="S1" width="100%"}

### Supplement B: Whole genome differential expression
![Differential expression of all genes of the targeted biotypes (protein-coding, lncRNA, pseudogene) genome-wide, before (A) and after (B) ploidy correction, with HSA21 genes highlighted and all other genes in grey. The dotted line in A marks the 1.5-fold expectation; before correction the HSA21 genes cluster around it and are almost uniformly significant, and after correction they center on zero.](images/figures/fig_volcano_all_genes.png){#fig:s2-volcano-all tag="S2" width="100%"}

### Supplement C: Comparison across covariate models
Running the identical pipeline without covariate adjustment and without excluding mosaic participants (397 participants: 302 T21, 95 D21) identified 23 deviating genes (10 higher, 13 lower) rather than 13, and detected a *cis*-eQTL for 14 of 20 testable genes rather than 8 of 10.
Of the 13 genes that deviate in the primary (adjusted) analysis, 6 also deviate in the unadjusted analysis (*OLIG2*, *PCBP3*, *BACE2*, *YBEY*, *COL6A2*, *ABCC13*); the other 7 deviate only once age, BMI, and cell-type composition are accounted for (*KCNE1*, *OLIG1*, *RUNX1*, *AP000282.1*, *CBR3*, *ADAMTS1*, *ATP5PF*).
Of the 23 genes that deviate in the unadjusted analysis, 17 drop out once adjusted — though for 11 of those, the effect size is similar in the adjusted model and the gene simply falls short of the stricter significance threshold in the smaller, more heavily parameterized model, rather than the underlying effect disappearing. This comparison is the basis for reporting the adjusted analysis as primary while retaining the unadjusted analysis for transparency (Figure {@fig:s3-comparison}).

The adjusted model assumes that each cell fraction affects expression in the same way in T21 and D21.
An interaction model, with a karyotype × cell-fraction interaction, raised the standard error of the T21 effect by a median of 1.76-fold for every HSA21 gene.
We compared effect estimates rather than significance across the three models (Table {@tbl:s3-model-comparison}).
Four genes deviated under both the adjusted and the interaction models, all lower than expected: *OLIG2*, *BACE2*, *OLIG1*, and *RUNX1*.
*OLIG2* and *BACE2* also deviated without adjustment.
*OLIG1* and *RUNX1* were lower than expected without adjustment as well, but below the magnitude cut.
Five genes kept similar estimates under the interaction model but lost significance: *YBEY*, *ADAMTS1*, *ABCC13*, *AP000282.1*, and *COL6A2*, which also fell just below the magnitude cut.
The estimates for *KCNE1* and *PCBP3* shrank by about a third.
The estimates for *CBR3* and *ATP5PF* disappeared, and neither gene deviated without adjustment, so their deviations depend on the assumption that composition relates to expression alike in both groups.
None of the six genes higher than expected deviated under the interaction model, and no gene outside the 13 began to deviate.
*OLIG1*, *OLIG2*, and *AP000282.1* lie within 60 kb of each other and their expression is correlated (Supplement G), so the four most robust genes may reflect three independent deviations.

| Gene | Direction | Unadjusted | Adjusted | Interaction |
|:--|:--|:--|:--|:--|
| *OLIG2* | Lower | **−1.19 (−1.44, −0.94)** | **−2.18 (−2.63, −1.72)** | **−2.65 (−3.43, −1.88)** |
| *BACE2* | Lower | **−0.43 (−0.56, −0.30)** | **−0.58 (−0.79, −0.36)** | **−0.89 (−1.27, −0.51)** |
| *OLIG1* | Lower | −0.36 (−0.50, −0.23) | **−0.76 (−0.99, −0.52)** | **−0.97 (−1.37, −0.56)** |
| *RUNX1* | Lower | −0.31 (−0.37, −0.26) | **−0.43 (−0.53, −0.33)** | **−0.42 (−0.60, −0.25)** |
| *YBEY* | Higher | **0.50 (0.40, 0.59)** | **0.47 (0.30, 0.64)** | 0.49 (0.18, 0.79) |
| *ADAMTS1* | Higher | 0.21 (0.02, 0.39) | **0.48 (0.22, 0.73)** | 0.51 (0.06, 0.97) |
| *ABCC13* | Higher | **1.45 (1.17, 1.73)** | **1.01 (0.49, 1.52)** | 0.83 (−0.08, 1.73) |
| *AP000282.1* | Lower | −0.27 (−0.43, −0.11) | **−0.70 (−0.99, −0.42)** | −0.87 (−1.37, −0.37) |
| *COL6A2* | Higher | **0.56 (0.41, 0.71)** | **0.42 (0.19, 0.64)** | 0.38 (−0.01, 0.77) |
| *KCNE1* | Lower | −0.38 (−0.52, −0.24) | **−0.50 (−0.72, −0.28)** | −0.36 (−0.74, 0.03) |
| *PCBP3* | Lower | **−0.43 (−0.57, −0.29)** | **−0.50 (−0.76, −0.25)** | −0.31 (−0.75, 0.14) |
| *CBR3* | Higher | 0.10 (−0.05, 0.25) | **0.53 (0.27, 0.78)** | 0.00 (−0.43, 0.44) |
| *ATP5PF* | Higher | 0.27 (0.13, 0.41) | **0.48 (0.22, 0.74)** | 0.19 (−0.24, 0.62) |

Table: Ploidy-corrected log~2~ fold change (95% CI) of the 13 deviating genes under the unadjusted, adjusted (primary), and karyotype × cell-fraction interaction models. Bold estimates deviate in that model (adjusted p < 0.01 and a fold change of at least 1.33 in either direction). Genes are ordered from the most to the least robust. {#tbl:s3-model-comparison tag="S3"}

![Comparison of the adjusted (primary) and unadjusted analyses. One row per gene that deviates in either analysis, showing its ploidy-corrected log~2~ fold change under the unadjusted (orange) and adjusted (purple) analyses, joined by a line; the dotted line marks zero.](images/figures/fig_run_comparison_adjusted_vs_baseline.png){#fig:s3-comparison tag="S3" width="90%"}


### Supplement D: HSA21 differential expression (Supplementary Table S1)
`data/supplementary_table_S1_hsa21_differential_expression.csv` holds one row for each of the 318 targeted HSA21 genes: the DESeq2 base mean, the uncorrected and ploidy-corrected log2 fold change and adjusted p-value, the coverage and repeat flags, the dosage classification, and, for the genes that deviate, the gene-level *cis*-eQTL permutation result together with the best variant, its minor allele, and that allele's frequency.
It is the source for Tables {@tbl:chr21-classification} and {@tbl:eqtl-genes}, and Figure {@fig:flow-map}.

### Supplement E: Common allele overlap (Supplementary Table S2)
`data/supplementary_table_S2_common_allele_overlap.csv` holds one row for each of the 2,076 *cis* variants tested within T21: position, reference and alternate allele, the alternate allele frequency in GTEx whole blood, in gnomAD v4.1 (global and non-Finnish European), and in this cohort, the minor allele each of those frequencies implies, and whether the three sources agree.
It supports the minor-allele labels used in the figures, and shows where a variant's two alleles are too close in frequency for those labels to be stable.
It is also the source for Figure {@fig:af-bound}A.

### Supplement F: Genotype structure in the within-T21 eQTL tests
The *cis*-eQTL model does not include genotype principal components, so we measured genotype structure in the within-T21 tests directly.
For each of the 153 assessable HSA21 genes (not repeat-flagged, base mean ≥ 30), T21 expression was regressed on every common variant on the HSA21 long arm (minor allele frequency ≥ 0.05 and call rate ≥ 0.95 among the T21 participants analyzed; 97,438 variants) at least 5 Mb from the gene's transcription start site, one ordinary least-squares regression per gene–variant pair (11.1 million pairs).
At that distance a variant cannot tag the gene's own *cis* locus, so in the absence of structure the p-values are uniform and the genomic inflation factor λ is 1.
Variants on the short arm and around the centromere were set aside: GRCh38 places false duplications of 21q22.3 there [@doi:10.1126/science.abl3533; @doi:10.1186/s13059-023-02863-7], so a variant's coordinate can put a long-arm gene's own *cis* signal more than 5 Mb away (for *GATD3A*, *PWP2*, *SIK1*, and *ICOSLG*, down to p ≈ 10^−46^); including them changes λ by less than 0.02.
Two references were used to read λ.
The same regressions were run for 400 expressed HSA22 genes: population structure would inflate their tests as much as those of HSA21 genes, whereas a signal tied to HSA21 copy number would not.
Participant labels were also permuted 200 times, jointly across genes, which keeps the correlation between genes and the linkage disequilibrium between variants; the spread of λ over these permutations is its sampling range for these correlated tests, about ±0.04 for a gene set.

Without covariate adjustment (302 T21 participants), λ was 1.074 for HSA21 genes and 1.044 for HSA22 genes, both above their permutation ranges, and 26 HSA21 genes lay outside their own permutation range, against a permutation median of 3 (Figure {@fig:s4-distal-inflation}A, B).
In the primary analysis (274 T21 participants), with age, sex, BMI, sample source, and cell-type composition regressed out of both expression and genotype dosage as in the *cis*-eQTL test, λ was 1.020 for HSA21 genes (permutation range 0.966–1.031), 1.016 for the 13 deviating genes, and 1.017 for HSA22 genes, all within their permutation ranges.
Three of the 24 adjustment covariates were themselves associated with HSA21 genotype across the chromosome, against a permutation median of 0 (Figure {@fig:s4-distal-inflation}D): recruitment at NDSC2019 and the CD27+ B-cell and CD4+ central memory T-cell fractions.
The adjusted tests are therefore not inflated beyond their permutation range at the level of the gene set, but the adjustment reaches that through covariates that track genotype structure rather than through a direct measure of ancestry, and some gene-level structure may remain: 11 HSA21 genes lay outside their own permutation range against a permutation median of 3 (p = 0.04), among them two deviating genes, *COL6A2* and *ABCC13* (permutation p = 0.020 and 0.025; Figure {@fig:s4-distal-inflation}C).

![Genotype structure in the within-T21 tests. (A) Quantile–quantile plots of T21 expression regressed on common HSA21 long-arm variants at least 5 Mb from each gene, for the assessable HSA21 genes (top) and for HSA22 reference genes (bottom), without covariate adjustment (unadjusted) and with the covariates regressed out of expression and genotype (adjusted); shaded, 95% range over 200 participant permutations. Each plot shows expected −log~10~ p up to 4, where most tests lie; the inset shows the full range with that window outlined. (B) Genomic inflation factor λ per gene set with its permutation 95% range. (C) Per-gene λ in the adjusted analysis, HSA21 assessable and HSA22 reference genes, with deviating genes colored by direction (red, higher than expected; blue, lower than expected); filled points lie outside the gene's own permutation 95% range. The five genes with the highest λ and the deviating genes outside their own range are labeled. (D) Each covariate of the adjusted analysis regressed on every common HSA21 long-arm variant; filled points lie outside their own permutation 95% range.](images/figures/fig_distal_inflation.png){#fig:s4-distal-inflation tag="S4" width="100%"}

### Supplement G: Expression of the HSA21 genes in blood
We compared HSA21 gene expression in GTEx v10 whole blood and other tissues.
The deviating genes' whole-blood expression was lower than that of the expected-dosage genes, but not significantly (median 1.3 vs 3.1 TPM, Wilcoxon p = 0.34; Figure {@fig:s5-gtex-expression}A).

Expression did not predict eQTL detection (Figure {@fig:s5-gtex-expression}B).
Among the 211 HSA21 genes GTEx tested in whole blood, eGenes and non-eGenes had similar expression (median 1.28 vs 1.18 TPM, p = 0.36).
Genes with a *cis*-eQTL detected in T21 were, if anything, less expressed than those without (median 2.4 vs 3.9 TPM, p = 0.13).

Whole blood ranks low among the GTEx tissues for most genes (median rank 64 of 68 for the expected-dosage genes; Figure {@fig:s5-gtex-expression}C). 
Expression in the T21 participants tracked GTEx closely (Spearman 0.87 across the 309 HSA21 genes; Figure {@fig:s5-gtex-expression}D).
The HTP values were 2.8-fold higher overall.
Part of this offset may come from globin depletion: the three main hemoglobin genes take 0.4% of HTP TPM, against 30% in GTEx whole blood.

*AP000282.1* has zero expression in GTEx whole blood but a median of 4.6 TPM in the T21 participants.
Its first exon lies inside the single exon of *OLIG1*, on the opposite strand.
GTEx libraries are unstranded, so GTEx removes exon regions shared between genes before counting [@doi:10.1126/science.aaz1776].
The HTP libraries are stranded and were counted by strand, so the T21 counts belong to *AP000282.1* itself.
*AP000282.1* is correlated with *OLIG1* (Spearman 0.67 in T21 after covariate adjustment).
*OLIG1*, *OLIG2*, and *AP000282.1* may deviate as one locus rather than independently.

![Expression of the HSA21 genes in blood. (A) GTEx v10 whole-blood median TPM of the classified HSA21 genes by classification. Deviating genes are colored by direction. (B) GTEx whole-blood eGene q-value (−log~10~) against whole-blood TPM for the 211 HSA21 genes that GTEx tested in whole blood. Filled points have a *cis*-eQTL detected in T21, open points were tested in T21 without detection, and crosses were not tested in T21 (102 genes); deviating genes are colored by direction and the dashed line marks q = 0.05. (C) Median TPM of each deviating gene in the 68 GTEx tissues. Whole blood (large point) is on the gene's line, and the other tissues are grouped by organ system below it. Labels give the rank of whole blood among the 68 tissues. (D) Median TPM in the 274 T21 participants against GTEx whole-blood TPM for the 309 classified HSA21 genes in GTEx, with point shapes as in B. The dotted line marks equality, and the dashed line marks the genome-wide HTP/GTEx offset (2.8-fold).](images/figures/gtex_tissue_expression.png){#fig:s5-gtex-expression tag="S5" width="100%"}

### Supplement H: Expression by genotype at the best variant
![Expression against genotype at the best variant for the 10 testable deviating genes, in the 274 T21 participants. Each panel plots covariate-adjusted expression against the number of copies (0 to 3) of the allele that GTEx links to the gene's direction of deviation, so a panel trends upward in A (genes higher than expected) and downward in B (genes lower than expected) when the cohort reproduces the GTEx direction. Boxes show the median and interquartile range, and the line is the within-T21 fit. Each panel names the gene and states whether the within-T21 trend agrees with GTEx; the variant, the plotted allele, and the minor allele and its frequency are given in Supplementary Table S1.](images/figures/fig_eqtl_dosage_panels.png){#fig:s6-eqtl-dosage tag="S6" width="100%"}

