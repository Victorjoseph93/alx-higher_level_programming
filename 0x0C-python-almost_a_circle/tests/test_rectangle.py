#!/usr/bin/python3
"""This module contains all unittests for the ``Rectangle`` class
"""
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
import unittest
import os
import sys
import io


class rec_init_test(unittest.TestCase):
    """This method tests the init method of the base class.
    """
    def test_noarg(self):
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_singlearg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(50)

    def test_2args(self):
        a = Rectangle(50, 20)
        self.assertEqual(a.width, 50)

    def test_3args(self):
        a = Rectangle(20, 30, 5)
        self.assertEqual(a.width, 20)

    def test_4args(self):
        a = Rectangle(20, 30, 5, 7)
        self.assertEqual(a.width, 20)

    def test_5args(self):
        a = Rectangle(20, 30, 5, 7, 8)
        self.assertEqual(str(a), "[Rectangle] (8) 5/7 - 20/30")

    def test_stringinargs(self):
        with self.assertRaises(TypeError):
            a = Rectangle(20, "HI", 5, 6, 8)

    def test_floatinargs(self):
        with self.assertRaises(TypeError):
            a = Rectangle(20, 40, 4.4, 5, 6)

    def test_tuplearg(self):
        with self.assertRaises(TypeError):
            a = Rectangle((20, 3, 4), 2, 3, 4, 5)

    def test_dictarg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(40, 20, {3: 4}, 4, 5)

    def test_lastattr(self):
        a = Rectangle(40, 20, 4, 4, "FakeId")
        self.assertEqual(str(a), "[Rectangle] (FakeId) 4/4 - 40/20")

    def test_negativewidth(self):
        with self.assertRaises(ValueError):
            a = Rectangle(-40, 3, 5, 7, 3)

    def test_negativeheight(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, -3, 5, 7, 3)

    def test_negativex(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, 3, -5, 7, 3)

    def test_negativey(self):
        with self.assertRaises(ValueError):
            a = Rectangle(40, 3, 5, -7, 3)

    def test_hugenumbers(self):
        a = Rectangle(999999999999999999, 9999999999999999,
                      999999999999999999, 9999999999999999,
                      999999999999999999)
        self.assertEqual(str(a), "[Rectangle] (999999999999999999) "
                         "999999999999999999/9999999999999999 - "
                         "999999999999999999/9999999999999999")


class rec_areamethod_test(unittest.TestCase):
    """This class tests the area method of the Rectangle
    class
    """
    def test_rectarea(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        self.assertEqual(rec.area(), 20)

    def test_givenarg(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(TypeError):
            rec.area("Hello")


class rec_settergetter_test(unittest.TestCase):
    """This class tests the various setter and getter
    methods of the attributes
    """
    def test_widthsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.width = 10
        self.assertEqual(rec.width, 10)

    def test_heightsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.height = 10
        self.assertEqual(rec.height, 10)

    def test_xsetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.x = 10
        self.assertEqual(rec.x, 10)

    def test_ysetter(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        rec.y = 10
        self.assertEqual(rec.y, 10)

    def test_invalidtype(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(TypeError):
            rec.width = "HELLO"

    def test_invalidvalue(self):
        rec = Rectangle(5, 4, 2, 3, 5)
        with self.assertRaises(ValueError):
            rec.width = -100


class rec_display_test(unittest.TestCase):
    """This class tests the display instance method.
    """
    def setUp(self):
        """redirecting stdout to output
        """
        self.output = io.StringIO()
        self.originalstdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """resetting stdout to its original
        value
        """
        sys.stdout = self.originalstdout

    def test_rectangle(self):
        rec = Rectangle(2, 3, 0, 0, 2)
        rec.display()
        self.assertEqual(self.output.getvalue(), "##\n##\n##\n")

    def test_square(self):
        s = Square(5, 0, 0)
        s.display()
        self.assertEqual(self.output.getvalue(), "#####\n#####\n#####\n"
                         "#####\n#####\n")


class rec_str_test(unittest.TestCase):
    """This class tests the str representation of a
    Rectangle or Rectangle inherited class object.
    """
    def test_rectangle(self):
        r = Rectangle(2, 3, 0, 0, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 2/3")

    def test_args(self):
        r = Rectangle(2, 3, 0, 0, 2)
        with self.assertRaises(TypeError):
            r.__str__("HI")


class rec_update_test(unittest.TestCase):
    """This class tests the update instance method for
    a rectangle or a rectangle inherited class object.
    """
    def test_updatelist(self):
        r = Rectangle(5, 4, 0, 0, 1)
        newattr = [1, 2, 3, 4, 4]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 4/4 - 2/3")

    def test_updatedict(self):
        r = Rectangle(5, 4, 0, 0, 1)
        newattr = dict(id=1, width=2, height=3, x=4, y=4)
        r.update(**newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 4/4 - 2/3")

    def test_update_listonearg(self):
        """updates only the id if one arg is given
        """
        r = Rectangle(5, 4, 0, 0, 1)
        newattr = [1]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 5/4")

    def test_update_listtwoarg(self):
        """updates  the id & width if one arg is given
        """
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = [1, 4]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 4/10")

    def test_update_listthreearg(self):
        """updates only the id, width & height if one arg is given
        """
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = [1, 4, 5]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 4/5")

    def test_update_listfourarg(self):
        """updates only the id, width, height & x if one arg is given
        """
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = [1, 4, 5, 6]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 6/0 - 4/5")

    def test_update_listfive_arg(self):
        """updates only the id, width, height, x & y if one arg is given
        """
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = [1, 4, 5, 6, 10]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 6/10 - 4/5")

    def test_update_morethanfive_arg(self):
        """ignores any list item that is indexed at more than 4
        """
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = [1, 4, 5, 6, 10, 20]
        r.update(*newattr)
        self.assertEqual(str(r), "[Rectangle] (1) 6/10 - 4/5")

    def test_update_onekeydict(self):
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = dict(id=4)
        r.update(**newattr)
        self.assertEqual(str(r), "[Rectangle] (4) 0/0 - 10/10")

    def test_update_2keydict(self):
        r = Rectangle(10, 10, 0, 0, 1)
        newattr = dict(id=4, abdu=3)
        r.update(**newattr)
        self.assertEqual(str(r), "[Rectangle] (4) 0/0 - 10/10")

    def test_update_strarg(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update("Hello")
        self.assertEqual(str(r), "[Rectangle] (Hello) 0/0 - 10/10")

    def test_update_intarg(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(3)
        self.assertEqual(str(r), "[Rectangle] (3) 0/0 - 10/10")

    def test_update_floatarg(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(4.5)
        self.assertEqual(str(r), "[Rectangle] (4.5) 0/0 - 10/10")

    def test_update_emptylist(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(*[])
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 10/10")

    def test_update_emptydict(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(**dict())
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 10/10")

    def test_update_Nonearg(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(None)
        self.assertEqual(str(r), "[Rectangle] (None) 0/0 - 10/10")

    def test_update_floatinf(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(float('inf'))
        self.assertEqual(str(r), "[Rectangle] (inf) 0/0 - 10/10")

    def test_update_floatnan(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(float('nan'))
        self.assertEqual(str(r), "[Rectangle] (nan) 0/0 - 10/10")

    def test_update_negativeid(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update([-4, 5])
        self.assertEqual(str(r), "[Rectangle] ([-4, 5]) 0/0 - 10/10")

    def test_update_multipleargs(self):
        r = Rectangle(10, 10, 0, 0, 1)
        r.update(-4, 5, 6, 4, 3, 2)
        self.assertEqual(str(r), "[Rectangle] (-4) 4/3 - 5/6")

    def test_update_negativewidth(self):
        r = Rectangle(10, 10, 0, 0, 1)
        attr = [4, -5, 3, 4, 5]
        r.update(*attr)
        self.assertEqual(str(r), "[Rectangle] (4) 4/5 - -5/3")

    def test_update_negativeheight(self):
        r = Rectangle(10, 10, 0, 0, 1)
        attr = [4, 5, -3, 4, 5]
        r.update(*attr)
        self.assertEqual(str(r), "[Rectangle] (4) 4/5 - 5/-3")

    def test_update_negativex(self):
        r = Rectangle(10, 10, 0, 0, 1)
        attr = [4, 5, 3, -4, 5]
        r.update(*attr)
        self.assertEqual(str(r), "[Rectangle] (4) -4/5 - 5/3")

    def test_update_negativey(self):
        r = Rectangle(10, 10, 0, 0, 1)
        attr = [4, 5, 3, 4, -5]
        r.update(*attr)
        self.assertEqual(str(r), "[Rectangle] (4) 4/-5 - 5/3")


class rec_todictionary_test(unittest.TestCase):
    """Tests the todictionary instance attribute.
    """
    def test_rectangletodict(self):
        r = Rectangle(10, 10, 0, 0, 1)
        self.assertEqual(r.to_dictionary(), dict(
            id=1, width=10, height=10, x=0, y=0
        ))

    def test_oneargument(self):
        r = Rectangle(10, 10, 0, 0, 1)
        with self.assertRaises(TypeError):
            mydict = r.to_dictionary("hi")
