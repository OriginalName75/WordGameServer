from django.test import TestCase

from SpellChecker.Checker import _matrix_checker
from WordGameServer.settings import POINTS_2, POINTS_5, POINTS_4


# Create your tests here.
class TheTest(TestCase):
   
    def test_all(self):
        matr = [["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], 0)
        self.assertEqual(rep["dots"], [])
        
        matr = [["j","e","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], POINTS_2)
        self.assertEqual(rep["dots"], [[[0,0], [0,1]]])
        
        matr = [["j","_","_","_","_" ],\
                ["e","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], POINTS_2)
        self.assertEqual(rep["dots"], [[[0,0], [1,0]]])
        
        
        matr = [["j","e","_","_","_" ],\
                ["e","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], 2*POINTS_2)
        
        matr = [["j","_","_","_","_" ],\
                ["e","_","_","_","_" ],\
                ["p","o","c","h","e" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], POINTS_2 + POINTS_5)
        matr = [["j","_","_","_","_" ],\
                ["e","_","_","_","_" ],\
                ["p","o","r","c","e" ],\
                ["_","_","_","_","_" ],\
                ["_","_","_","_","_" ]]
        rep = _matrix_checker(matr)
        self.assertEqual(rep["points"], POINTS_2 + POINTS_4)
        