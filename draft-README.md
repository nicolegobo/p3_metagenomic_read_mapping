# Metagenomic Read Mapping Service

## Overview

The Metagenomic Read Mapping Service uses [KMA](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2336-6) to align reads against antibiotic resistance genes, virulence factors, or other custom sets of genes.



## About this module

This module is a component of the BV-BRC build system. It is designed to fit into the
`dev_container` infrastructure which manages development and production deployment of
the components of the BV-BRC. More documentation is available [here](https://github.com/BV-BRC/dev_container/tree/master/README.md).

This module provides the following application specfication(s):
* [MetagenomicReadMapping](app_specs/MetagenomicReadMapping.md)


## See also

  * [Metagenomic Read Mapping Service](https://www.bv-brc.org/docs/https://bv-brc.org/app/MetagenomicReadMapping.html)
  * [Metagenomic Read Mapping Service Tutorial](https://www.bv-brc.org/docs//tutorial/metagenomic_read_mapping/metagenomic_read_mapping.html)



## References

* Kent, W. James. "BLAT—the BLAST-like alignment tool." Genome research 12.4 (2002): 656-664.
* Jia, Baofeng, et al. "CARD 2017: expansion and model-centric curation of the comprehensive antibiotic resistance database." Nucleic acids research (2016): gkw1004.
* Liu, Bo, et al. "VFDB 2019: a comparative pathogenomic platform with an interactive web interface." Nucleic acids research 47.D1 (2018): D687-D692.
* Philip T.L.C. Clausen, Frank M. Aarestrup & Ole Lund, "Rapid and precise alignment of raw reads against redundant databases with KMA", BMC Bioinformatics, 2018;19:307.
