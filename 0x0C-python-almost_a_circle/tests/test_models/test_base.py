#!/usr/bin/python3
''' module for test Base class '''
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    ''' suite to test Base class '''

    def setUp(self):
        ''' method invoked for each test '''
        Base._Base__nb_objects = 0

    def test_id(self):
        ''' test assigned id '''
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        ''' test default id '''
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        ''' test nb object attribute '''
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        ''' test nb object attributes and assigned id '''
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        ''' test string id '''
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        ''' test passing more args to init method '''
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        ''' test accessing to private attributes '''
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        ''' test JSON file '''
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_2(self):
        ''' test JSON file '''
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
