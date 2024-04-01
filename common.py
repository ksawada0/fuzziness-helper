#!/usr/bin/env python
import pdb

# Given sets
C = [1, 0, 1]
D = [0.4, 0.5, 0.6]
E = [0.3, 0.0, 1]
F = [0.6, 0, 0]
G = [0.3, 0.3, 0.3]
H = [0.5, 0.1, 0.4]
I = [0.5, 0.9, 0.6]
J = [0.5, 0.5, 0.5]

class fuzzy:
    def __init__(self, set):
        self.set = set
    
    
    def get_complement(self, set):
        """Given a set A, return A^c = (1-a1, 1-a2...)"""
        n = len(set)
        compl_set = []
        for i in range(n):
            compl_set.append(1 - set[i])
        return compl_set
    
    def get_union(self, set1, set2):
        """Given a A and B, return (max(a1, b1), max(a2, b2)...)"""
        n = len(set1)
        union = []
        for i in range(n):
            union.append(max(set1[i], set2[i]))
        return union
    
    def get_intersection(self, set1, set2):
        """
        Given a A and B, return fuzzy intersection,
        (min(a1, b1), min(a2, b2)...)
        """
        n = len(set1)
        union = []
        for i in range(n):
            union.append(min(set1[i], set2[i]))
        return union
    
    def get_count(self, s):
        """Given a set A, return sum(A)"""
        return sum(s)
    
    def get_fuzzy_equality(self, set1, set2):
        """
        Given a A and B, return fuzzy subsethood
        S(A, B) = c(A intersection B) / c(A)
        """
        n = len(set1)
        intersection = self.get_intersection(set1, set2)
        union = self.get_union(set1, set2)
        return self.get_count(intersection) / self.get_count(union)
  
    def get_subsethood(self, set1, set2):
        """
        Given a A and B, return fuzzy subsethood
        S(A, B) = c(A intersection B) / c(A)
        """
        n = len(set1)
        intersection = self.get_intersection(set1, set2)
        return self.get_count(intersection) / self.get_count(set1)
            
    def degree_of_fuzziness(self):
        """
        Given a set A, return the degree of fuzziness
        F(A) = E(A,A^c) = S(A union A^c, A intersection A^c)
        """
        union = self.get_union(self.set, self.get_complement(self.set))
        intersection = self.get_intersection(self.set, self.get_complement(self.set))
        return self.get_count(union) - self.get_count(intersection) # Using get_count() instead of sum for readability for educational purpose