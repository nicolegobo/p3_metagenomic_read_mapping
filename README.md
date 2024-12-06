# Metagenomic Read Mapping

## Overview

The Metagenomic Read Mapping Service uses [KMA](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2336-6) to align reads against antibiotic resistance genes, virulence factors, or other custom sets of genes.

## About this module

This module is a component of the BV-BRC build system. It is designed to fit into the
`dev_container` infrastructure which manages development and production deployment of
the components of the BV-BRC. More documentation is available [here](https://github.com/BV-BRC/dev_container/tree/master/README.md).

There is one application service specification defined here:
1.  [MetagenomicReadMapping](app_specs/MetagenomicReadMapping.md): Service that that provides the backend for the BV-BRC web inerface; it takes reads as input.

The code in this module provides the BV-BRC application service wrapper scripts for the Metagenomic Read Mapping service as well
as some backend utilities:

| Script name | Purpose |
| ----------- | ------- |
| [App-MetagenomicReadMapping.pl](service-scripts/App-MetagenomicReadMapping.pl) | App script for the [metagenomic read mapping service](https://www.bv-brc.org/docs/quick_references/services/metagenomic_read_mapping_service.html) |

## See also

* [Metagenomic Read Mapping Service](https://bv-brc.org/app/MetagenomicReadMapping)
* [Quick Reference](https://www.bv-brc.org/docs/quick_references/services/metagenomic_read_mapping_service.html)
* [Metagenomic Read Mapping Service Tutorial](https://www.bv-brc.org/docs/tutorial/metagenomic_read_mapping/metagenomic_read_mapping.html)



## References
Clausen, P.T., F.M. Aarestrup, and O. Lund, Rapid and precise alignment of raw reads against redundant databases with KMA. BMC bioinformatics, 2018. 19(1): p. 307.

Alcock, B.P., et al., CARD 2020: antibiotic resistome surveillance with the comprehensive antibiotic resistance database. Nucleic acids research, 2020. 48(D1): p. D517-D525.

Liu, B., et al., VFDB 2019: a comparative pathogenomic platform with an interactive web interface. Nucleic acids research, 2019. 47(D1): p. D687-D692.

Kent, W.J., BLAT—the BLAST-like alignment tool. Genome research, 2002. 12(4): p. 656-664.
