---
layout: page
title: Software
permalink: /Tools/Software/
menu: tools
published: true
---

### NemaScan

To enable genome-wide assiciation mappings and simulations using <em>Caenorhabditis</em> data, we build a wrapper for the Genome-wide Complex Trait Analysis package [GCTA](https://yanglab.westlake.edu.cn/software/gcta/#Overview) called NemaScan. Please follow the vignettes for use cases. Also, the <em>Caenorhabditis</em> Natural Diversity Resource [CaeNDR](www.elegansvariation.org) uses this mapping package for GWAS.

* [NemaScan](https://github.com/AndersenLab/NemaScan)


### EasyXpress

Our lab has developed an R package to manage, process, and plot high-throughput imaging data obtained using the Molecular Devices ImageXpress platform. 

* [easyXpress](https://github.com/AndersenLab/easyXpress)

### EasyFulcrum

For labs interested in field sampling wild strains, we built an R package to read-in, process, analyze, and plot sampling data collected using Fulcrum (apps are below). A procotol for nematode sampling is [here](https://www.jove.com/t/63486/a-highly-scalable-approach-to-perform-ecological-surveys-selfing).

* [easyFulcrum](https://github.com/AndersenLab/easyfulcrum)

### Fulcrum Apps

Our lab has developed Fulcrum forms/applications for gathering data when collecting wild <em>Caenorhabditis</em> species.

* [Nematode Field Sampling](http://www.fulcrumapp.com/apps/nematode-field-sampling)
* [Nematode Isolation App](http://www.fulcrumapp.com/apps/nematode-isolation/)


### [VCF-kit](http://www.github.com/andersenlab/VCF-kit) - [Documentation](https://github.com/AndersenLab/VCF-kit)

---

<a href='http://www.github.com/andersenlab/VCF-kit'><img src='/assets/img/vcfkit.png' style='float:left; width: 150px; margin-right: 20px;' /></a>

VCF-kit is a command-line based collection of utilities for performing analysis on Variant Call Format (VCF) files. A summary of the commands is provided below. See documentation for details on installation and usage.

<div style='clear:both;'></div>
<br />

<table class='table table-hover'><thead>
<tr>
<th align="left">Command</th>
<th>Description</th>
</tr>
</thead><tbody>
<tr>
<td align="left"><strong>calc</strong></td>
<td>Obtain  frequency/count of  genotypes and alleles.</td>
</tr>
<tr>
<td align="left"><strong>call</strong></td>
<td>Compare variants  identified  from  sequences obtained  through alternative methods against a VCF.</td>
</tr>
<tr>
<td align="left"><strong>filter</strong></td>
<td>Filter  variants  with  a minimum or  maximum number  of  REF,  HET,  ALT,  or  missing calls.</td>
</tr>
<tr>
<td align="left"><strong>geno</strong></td>
<td>Various operations  at  the genotype  level.</td>
</tr>
<tr>
<td align="left"><strong>genome</strong></td>
<td>Reference genome  processing  and management.</td>
</tr>
<tr>
<td align="left"><strong>hmm</strong></td>
<td>Hidden-markov model for use in  imputing  genotypes from  parental  genotypes in  linkage studies.</td>
</tr>
<tr>
<td align="left"><strong>phylo</strong></td>
<td>Generate  dendrograms from  a VCF.</td>
</tr>
<tr>
<td align="left"><strong>primer</strong></td>
<td>Generate  primers for variant validation.</td>
</tr>
<tr>
<td align="left"><strong>rename</strong></td>
<td>Add a prefix, suffix, or  substitute  a string  in  sample  names.</td>
</tr>
<tr>
<td align="left"><strong>tajima</strong></td>
<td>Calculate Tajima’s  D.</td>
</tr>
<tr>
<td align="left"><strong>vcf2tsv</strong></td>
<td>Convert a VCF to  TSV.</td>
</tr>
</tbody></table>

<div style='clear:both;'></div>

### [Cegwas](http://www.github.com/andersenlab/cegwas)
----

A set of functions to process phenotype data, perform GWAS, and perform post-mapping data processing for *C. elegans*.

#### Install

```r
devtools::install_github("AndersenLab/cegwas")
```


#### Usage
```r
pheno <- spike(snps, c(80, 1020))
processed_phenotypes = process_pheno(pheno)
mapping_df = gwas_mappings(processed_phenotypes, cores = 4, only_sig = FALSE)
processed_mapping_df = process_mappings(mapping_df, phenotype_df = processed_phenotypes, CI_size = 50, snp_grouping = 200)
                manplot(processed_mapping_df)
```

<br /><br />

### [linkagemapping](https://github.com/AndersenLab/linkagemapping)

---

This package includes all data and functions necessary to complete a mapping for the phenotype of your choice using the recombinant inbred lines from _Andersen, et al. 2015 (G3)_. Included with this package are the cross and map objects for this strain set as well a markers.rds file containing a lookup table for the physical positions of all markers used for mapping. See the [github page](https://github.com/AndersenLab/linkagemapping) for more information on usage.

#### Install

```r
devtools::install_github("AndersenLab/linkagemapping")
library("linkagemapping")
```

#### Usage

```r

# Get the cross object
data("N2xCB4856cross")
cross <- N2xCB4856cross

# Get the phenotype data
pheno <- readRDS("~/Dropbox/AndersenLab/LabFolders/PastMembers/Tyler/ForTrip/RIAILs2_processed.rds")

# Merge the cross object and the phenotype data
cross <- mergepheno(cross, pheno)

# Perform a mapping with only 10 iterations of the phenotype data for FDR calc
map <- fsearch(cross, permutations = 10)

# Annotate the LOD scores
annotatedlods <- annotate_lods(map, cross)
```

<br /><br />

### [easysorter](https://github.com/AndersenLab/easysorter)
----

`easysorter` is effectively version 2 of the COPASutils package (Shimko and Andersen, 2014). This package is specialized for use with worms and includes additional functionality on top of that provided by COPASutils, including division of recorded objects by larval stage and the ability to regress out control phenotypes from those recorded in experimental conditions. The package is rather specific to use in the Andersen Lab and, therefore, is not available from CRAN. To install you will need the [devtools](https://github.com/hadley/devtools) package. You can install both the devtools package and easy sorter using the commands below:

#### Install

```r
install.packages("devtools")
devtools::install_github("AndersenLab/easysorter")
```
<br /><br />

#### [COPASutils](https://github.com/AndersenLab/COPASutils)

An R package that presents a logical workflow for the reading, processing, and visualization of data obtained from the Union Biometrica Complex Object Parametric Analyzer and Sorter (COPAS) platform large-particle flow cytometers and a powerful suite of functions for the rapid processing and analysis of large high-throughput screening data sets. It combines the speed of dplyr with the elegance of ggplot2 to make analysis of COPAS data fast and painless.

#### Install

```r
install.packages("COPASutils")
```

#### Additional Resources

* [Vignette](/files/COPASutilsVignette.html)
* [CPAN](http://cran.rstudio.com/web/packages/COPASutils/index.html) 
* [Supplementary Files](/files/COPASutils.zip)

<br /><br />

### [liftover-utils](https://github.com/AndersenLab/liftover-utils)
----

Liftover is a python script that wraps the `remap_gff_between_releases.pl` script by Gary Williams. It expands upon the number of filetypes you can liftover:

* VCF/BCF (Requires bcftools)
* GFF
* BED

Additionally, _custom_ file formats can be lifted over by specifying chromosome, start position column, and optionally an end position column.

#### Install

```bash
pip install https://github.com/AndersenLab/liftover-utils/archive/v0.1.tar.gz
```

#### Usage

Note that the end_pos_column parameter is optional, meaning you only need to specify a chromosome and base pair location to be lifted over.

```python
liftover <file> <release1> <release2> (bcf|vcf|gff|bed)
liftover <file> <release1> <release2> <chrom_col> <start_pos_column> [<end_pos_column>] [options]


Options:
  -h --help     Show this screen.
  --delim=<delim>  File Delimiter; Default is a tab [default: TAB].
```
