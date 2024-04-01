#!/usr/bin/env python
import numpy as np
import math
from itertools import permutations
import pdb

import common as cmn
import resources.logging_config as fuz_logging
log = fuz_logging.get_logger("cli", json=False)



def main():
    named_sets = {'C': cmn.C, 'D': cmn.D, 'E': cmn.E, 'F': cmn.F, 'G': cmn.G, 'H': cmn.H, 'I': cmn.I, 'J': cmn.J}
    pairs = list(permutations(named_sets.items(), 2))
    pairs = [(k1, v1, k2, v2) for k1, v1 in named_sets.items() for k2, v2 in named_sets.items()]
    f = cmn.fuzzy(cmn.C)
                
    '''Fuzzy Equality'''
    log.debug(pairs)
    matrix = {k1: {k2: round(f.get_fuzzy_equality(v1, v2), 2) for k2, v2 in named_sets.items()} for k1, v1 in named_sets.items()}


    for pair in pairs:
        log.debug(f"Pair: {pair}")
        log.debug(f"Pair[0]: {pair[0]} - {pair[1]}")
        log.debug(f"Pair[1]: {pair[2]} - {pair[3]}")
        log.debug(f"Fuzzy Equivalence: {f.get_fuzzy_equality(pair[1], pair[3])}")
    
    # Print the matrix in a tabular format
    headers = '\t'.join(named_sets.keys())
    rows = '\n'.join([f"{k1}\t" + '\t'.join([str(matrix[k1][k2]) for k2 in named_sets.keys()]) for k1 in named_sets.keys()])
    log.info("\n\n----- Fuzzy Equality -----")
    log.info("\n\t" + headers + '\n' + rows)
    
    '''Fuzzy Subsethood'''
    matrix = {k1: {k2: round(f.get_subsethood(v1, v2), 2) for k2, v2 in named_sets.items()} for k1, v1 in named_sets.items()}


    for pair in pairs:
        log.debug(f"Pair: {pair}")
        log.debug(f"Pair[0]: {pair[0]} - {pair[1]}")
        log.debug(f"Pair[1]: {pair[2]} - {pair[3]}")
        log.debug(f"Fuzzy Subsethood: {f.get_fuzzy_equality(pair[1], pair[3])}")
    
    # Print the matrix in a tabular format
    headers = '\t'.join(named_sets.keys())
    rows = '\n'.join([f"{k1}\t" + '\t'.join([str(matrix[k1][k2]) for k2 in named_sets.keys()]) for k1 in named_sets.keys()])
    log.info("\n\n----- Fuzzy Subsethood -----")
    log.info("\n\t" + headers + '\n' + rows)
        
    '''Degree of Fuzziness'''
    log.info("\n\n----- Degree of Fuzziness -----")
    for key in named_sets:
        log.info(f"\nPair: {key} and {f.get_complement(named_sets[key])}")
        # pdb.set_trace()
        # dof = f.get_complement(named_sets[key])
        log.info(f"Degree of Fuzziness: {f.degree_of_fuzziness(named_sets[key]):.2f}")
        log.info(f"Fuzzy Equivalence: {f.get_fuzzy_equality(named_sets[key], f.get_complement(named_sets[key])):.2f}")
        
        union_of_compl = f.get_union(named_sets[key], f.get_complement(named_sets[key]))
        intersection_of_compl = f.get_intersection(named_sets[key], f.get_complement(named_sets[key]))
        fuz_equality = f.get_fuzzy_equality(union_of_compl, intersection_of_compl)
        log.info(f"Fuzzy Subsethood: {fuz_equality:.2f}")
            
        

if __name__ == "__main__": main()
