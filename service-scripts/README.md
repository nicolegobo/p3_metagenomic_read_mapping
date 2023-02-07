The service-scripts directory is for back-end or server side scripts.   

App-MetagenomicReadMapping.pl runs the Metagenomic Read Mapping service on the bv-brc.org and connects to the larger codebase.

run_kma.py is a stand alone script for database. The conda environment for this script described in environment.YML. If you are unfamilair with conda environments please visit the [conda user guide](https://conda.io/projects/conda/en/latest/user-guide/index.html). This script offers the following functions:

**Update the predefined gene sets**
Download the updated database directories from the [Comprehensive Antibiotic Resistance Database (CARD)] (https://card.mcmaster.ca/) and the [Virulence Factor Database (VFDB)] (http://www.mgc.ac.cn/VFs/). The prepare reference daatabes command may need to be edited in order to include new databases from other sources. There are two steps:

**Prepare the reference databases**
This command will output a .FASTA file with headers formatted to work with the BV-BRC codebase and containa the nucleotide reads from the CARD and VFDB database.  The files will be named CARD_out.FASTA and VFDB_out.FASTA. The header follow following format for card: CARD|GenBank protein accession, NCBI taxonomy name and dna sequence. For VFDB: VFDB|vfdb gene id, NCBI function, and NCBI taxonomy name.
```
python run_kma.py prep-ref-databases \
<path to raw card data> \
<path to raw vfdb data>
```

**Create the KMA databases**
This step will crate (index) the kma database. You will need to run this command for both of the predefined databases.
```
python run_kma.py create-kma-database \
<ref_fasta> \
<path_to_kma_database/database_name>
```

**Map reads to database**
This command is for users that would like to test the database outside of the BV-BRC codebase, this command will map reads to a kma database. This is intended for trouble shooting any kma database updates.
```
python run_kma.py map-reads-to-database \
<path_to_kma_database/database_name> \
<output_mapped_database_name>
```
