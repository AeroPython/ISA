'''

Created on Fri Feb 20 20:57:16 2015

@author: Siro Moreno

This is a submodule for the genetic algorithm that is explained in
https://docs.google.com/presentation/d/1_78ilFL-nbuN5KB5FmNeo-EIZly1PjqxqIB-ant-GfM/edit?usp=sharing

This script is the Genetic Step Subprograme. After the XFoil analysis of the
'N' generation, this subprogramme will calculate the population of the 
'N+1' generation. 

'''




import os
import numpy as np
import analyze as analyze
import selection as selection
import cross as cross
import mutation as mutation




def genetic_step(generation,num_parent, weights):
    '''Returns the genome of the (n+1)generation
    '''
    genome_parent_root = 'genome\generation'+ str(generation) + '.txt'    
    genome = np.loadtxt(genome_parent_root, skiprows=1)
    num_pop = genome.shape[0]
    
    scores = analyze.score(generation,num_pop, weights)
    parents = selection.selection(scores, genome, num_parent)
    children = cross.cross(parents, num_pop)
    children = mutation.mutation(children, generation, num_parent)
    
    profile_number = children.shape[0]    
    genome_root = 'genome\generation'+ str(generation + 1) + '.txt'
    title = 'generation' + str(generation + 1) + 'genome'
    
    try:
        os.remove(genome_root)
    except :
        pass
    genome_file = open(genome_root, mode = 'x')
    genome_file.write(title + '\n')
    
    for profile in np.arange(0, profile_number, 1):
        line = ''
        for gen in np.arange(0, 16,1):
            line = line + str(children[profile, gen]) +'    '
        line = line + '\n'
        genome_file.write(line)
    return children