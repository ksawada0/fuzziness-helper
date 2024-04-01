#!/usr/bin/env python

import pytest
import pdb

import common as cmn

def test_fuzzy_constructor():
    f = cmn.fuzzy(cmn.C)    
    fail_case = [-1, -1, -1]

    assert len(f.set) == len(cmn.C)
    for i in range(len(f.set)):
        assert f.set[i] == cmn.C[i]
        assert fail_case[i] != f.set[i]


def test_fuzzy_cmpl():
    f = cmn.fuzzy(cmn.D)
    fail_case = [-1, -1, -1]
    expected = [0.6, 0.5, 0.4]
    actual = f.get_complement(cmn.D)
    assert len(expected) == len(actual)
    for i in range(len(f.set)):
        assert fail_case[i] != actual[i]
        assert expected[i] == actual[i]
        

def test_fuzzy_union():
    f = cmn.fuzzy(cmn.C)
    fail_case = [-1, -1, -1]
    expected = [1, 0.5, 1]
    actual = f.get_union(cmn.C, cmn.D)
    for i in range(len(f.set)):
        assert fail_case[i] != actual[i]
        assert expected[i] == actual[i]
                     
        
def test_fuzzy_intersection():
    f = cmn.fuzzy(cmn.C)
    fail_case = [-1, -1, -1]
    expected = [0.4, 0, 0.6]
    actual = f.get_intersection(cmn.C, cmn.D)
    for i in range(len(f.set)):
        assert expected[i] == actual[i]
        assert fail_case[i] != actual[i]
        
     
def test_count():
    f = cmn.fuzzy(cmn.D)
    fail_case = -1
    expected = 1.5
    actual = f.get_count(cmn.D)
    assert expected == actual
    assert fail_case != actual
           
           
def test_equality():
    f = cmn.fuzzy(cmn.C)
    fail_case = -1
    expected = 1
    actual = f.get_fuzzy_equality(cmn.C, cmn.C)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 2/5
    actual = f.get_fuzzy_equality(cmn.C, cmn.D)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 1/5
    actual = f.get_fuzzy_equality(cmn.C, cmn.E)
    assert round(expected) == round(actual)
    assert fail_case != actual
    

def test_subsethood():
    f = cmn.fuzzy(cmn.C)
    fail_case = -1
    expected = 1
    actual = f.get_subsethood(cmn.C, cmn.C)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 1/2
    actual = f.get_subsethood(cmn.C, cmn.D)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 0.4/1.5
    actual = f.get_subsethood(cmn.D, cmn.F)
    assert round(expected) == round(actual)
    assert fail_case != actual
    

@pytest.mark.curr
def test_degree_of_fuzziness():
    f = cmn.fuzzy(cmn.C)
    fail_case = -1
    expected = 0
    actual = f.degree_of_fuzziness(cmn.C)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 1
    actual = f.degree_of_fuzziness(cmn.D)
    assert round(expected) == round(actual)
    assert fail_case != actual
    
    expected = 0.6/2.4
    actual = f.degree_of_fuzziness(cmn.F)
    assert round(expected) == round(actual)
    assert fail_case != actual
        
        
