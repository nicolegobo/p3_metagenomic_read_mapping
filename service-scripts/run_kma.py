#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:39:55 2023

@author: nbowers
This is a script that formats the headers from the FASTAs for the CARD and VFDB
to match previous headers used by the current codebase for the BV-BRC.org
##### Add descriptions for each commmand #####
"""

import click
import glob
import os
import pandas as pd



def parse_card_json(data): # card_output):
    lines = []
    for i in data:
        model_name = data[i]['model_name']
        aro_id = data[i]['ARO_id']
        model_seq = data[i]['model_sequences']
        # pass reads that do not have a dictionary
        if type(model_seq) != dict:
            pass
        else:
            k = next(iter(model_seq['sequence']))
            ncbi_taxonomy = model_seq['sequence'][k]['NCBI_taxonomy']['NCBI_taxonomy_name']
            protein_accession = model_seq['sequence'][k]['protein_sequence']['accession']
            dna_seq = model_seq['sequence'][k]['dna_sequence']['sequence']
            temp = ['>CARD|', protein_accession, ' ', model_name, ' [',ncbi_taxonomy,']','\n', dna_seq, '\n']
            line=''.join(temp)
            lines.append(line)
    return lines


def edit_vfdb_headers(vfdb_raw_data_dir):
    lines = []
    temp = []
    vfdb_input = glob.glob(os.path.join(vfdb_raw_data_dir,'*fas'))[0]
    with open(vfdb_input, 'r') as f:
        for line in f:
            if line.startswith('>'):
                line_sp=line.split('(')
                line_sp[0]= '>VFDB|'+line_sp[0].strip('>')
                # protein id
                line_sp[1] = line_sp[2].split('[')[0].split(')')[-1]
                # function
                line_sp[2] = line_sp[3].split('-')[-1].strip(']')
                # appending to a temp list because the length of inconsistencies in the header values
                temp = line_sp[0:3]
                temp.append((line_sp[-1].split(']')[1])+']\n')
                line = ''.join(temp).replace('   ','')
            lines.append(line)
            print(line)
    f.close()
    return lines



def op_json(raw_data_dir):
    card_json = glob.glob(os.path.join(raw_data_dir,'card.json'))[0]
    assert os.path.exists(card_json)
    with open(card_json, 'r') as f:
        data = pd.read_json(card_json)
    return data


def write_out(seqs, output):
    with open(output, 'w') as out:
        for line in seqs:
            out.write(line)
        out.close()
    return output


def run_kma_index(ref_fasta, database_name):
    os.system('kma index -i {} -o {}'.format(ref_fasta, database_name))
    return

def map_to_kma_database(database_name, output, input_type, input_fastqs):
    if not os.path.exists(output):
        os.makedirs(output)
    if input_type == 'paired_read_lib':
        type = '-ipe'
    if input_type == 'single_read_lib':
        type = '-i'
    input_fastqs = ' '.join(input_fastqs)
    os.system('kma -ID 70 -t_db {} {} {} -o {}'.format(database_name, type, input_fastqs.values(), output))


@click.group()
def main(args=None):
    pass

@main.command()
@click.argument('card_raw_data_dir', type=click.Path(exists=True))
@click.argument('vfdb_raw_data_dir', type=click.Path(exists=True))
def prep_ref_databases(card_raw_data_dir, vfdb_raw_data_dir):
    ## CARD ##
    data = op_json(card_raw_data_dir)
    card_seq = parse_card_json(data)
    card_out = write_out(card_seq, 'card_out.fasta')
    ## VFDB ##
    vfdb_seq = edit_vfdb_headers(vfdb_raw_data_dir)
    vfdb_out = write_out(vfdb_seq, 'vfdb_out.fasta')

# this command should work for CARD, VFDB, or feature group as long as it is a .FASTA
@main.command()
@click.argument('ref_fasta', type=click.Path(exists=True))
@click.argument('database_name', type=str)
def create_kma_database(ref_fasta, database_name):
    run_kma_index(ref_fasta, database_name)

## addd a new command function to map to the database
# this needs to be able to take in
# paired read library
# single read library
@main.command()
@click.argument('database_name', type=str, required=True)
@click.argument('output', type=click.Path())
@click.option('--input_type', type=click.Choice(['paired_end_libs', 'single_end_libs'], case_sensitive=False))
@click.argument('input_fastqs', nargs =-1, type=click.Path(exists=True))

def map_reads_to_database(database_name, output, input_type, input_fastqs):
    map_to_kma_database(database_name, output, input_type, input_fastqs)


if __name__ == '__main__':

    main()
