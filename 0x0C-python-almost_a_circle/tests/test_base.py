#!/usr/bin/python3
"""This module contains all unittests for the ``Base`` class
"""
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json
import unittest


class base_init_test(unittest.TestCase):
    """This method tests the init method of the base class.
    """
    def test_noarg(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

    def test_singlearg(self):
        a = Base(50)
        self.assertEqual(a.id, 50)

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            a = Base(50, 1)

    def test_strinit(self):
        a = Base("Hello")
        self.assertEqual(a.id, "Hello")

    def test_strfloat(self):
        a = Base(5.4)
        self.assertEqual(a.id, 5.4)

    def test_listarg(self):
        a = Base([1, 2, 3])
        self.assertEqual(a.id, [1, 2, 3])

    def test_dictarg(self):
        a = Base({1: 2, 2: 3})
        self.assertEqual(a.id, {1: 2, 2: 3})

    def test_none(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_NaN(self):
        num = float('nan')
        a = Base(num)
        self.assertNotEqual(a.id, num)

    def test_inf(self):
        num = float('inf')
        a = Base(num)
        self.assertEqual(a.id, num)

    def test_changeid(self):
        a = Base(50)
        a.id = 20
        self.assertEqual(a.id, 20)

    def test_accessprivattr(self):
        a = Base(None)
        with self.assertRaises(AttributeError):
            id = a.__nb_instances

    def test_bool(self):
        a = Base(True)
        self.assertTrue(a.id)
        b = Base(False)
        self.assertFalse(b.id)

    def test_complex_id(self):
        a = Base(complex(5))
        self.assertEqual(a.id, complex(5))

    def test_tuple(self):
        a = Base((1, 2, 3))
        self.assertEqual(a.id, (1, 2, 3))

    def test_set(self):
        a = Base({1, 2, 3})
        self.assertEqual(a.id, {1, 2, 3})

    def test_range(self):
        a = Base(range(5))
        self.assertEqual(a.id, range(5))


class base_tojsonstring_test(unittest.TestCase):
    """This method tests the ``to_json_string`` method of the base class.
    Testing is done and compared to the standard json.dumps method.
    """
    def test_rec_dictlist(self):
        rec1 = Rectangle(1, 4, 5, 0, 1)
        rec2 = Rectangle(5, 5, 6, 1, 0)
        dictlist = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_square_dictlist(self):
        squ1 = Square(4, 5, 0, 1)
        squ2 = Square(5, 5, 6)
        dictlist = [squ1.to_dictionary(), squ2.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_mixed_dictlist(self):
        squ = Square(5, 6, 0, 1)
        rec = Rectangle(2, 4, 5, 1, 0)
        dictlist = [squ.to_dictionary(), rec.to_dictionary()]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_emptylist(self):
        dictlist = []
        self.assertEqual(Base.to_json_string(dictlist), "[]")

    def test_Nonelist(self):
        dictlist = None
        self.assertEqual(Base.to_json_string(dictlist), "[]")

    def test_no_dictlist(self):
        dictlist = [1, "Hello", 4.5]
        self.assertEqual(Base.to_json_string(dictlist), '[1, "Hello", 4.5]')

    def test_singledictarg(self):
        dictlist = dict(id=3, width=4, height=5, x=2, y=4)
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_stringarg(self):
        dictlist = "Abdu"
        self.assertEqual(Base.to_json_string(dictlist), '"Abdu"')

    def test_intarg(self):
        dictlist = 500
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_floatarg(self):
        dictlist = 2.3
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_tuplearg(self):
        dictlist = (5, 6, 7)
        self.assertEqual(Base.to_json_string(dictlist), '[5, 6, 7]')

    def test_setarg(self):
        dictlist = {1, 3, 3, 5}
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist)

    def test_listoflists(self):
        dictlist = [[dict(id=1, size=4, x=2, y=1)],
                    [dict(id=4, size=6, x=0, y=3)]]
        self.assertEqual(Base.to_json_string(dictlist), json.dumps(dictlist))

    def test_emptyargs(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_morethanonearg(self):
        dictlist = [dict(id=1, size=5, x=2, y=1)]
        dictlist2 = [dict(id=3, size=10, x=3, y=5)]
        with self.assertRaises(TypeError):
            Base.to_json_string(dictlist, dictlist2)


class base_savetofile_test(unittest.TestCase):
    """This class tests the ``load_from_file``
    """
    def tearDown(self):
        """removes files created during testing.
        """
        try:
            os.remove('Rectangle.json')
        except Exception:
            pass
        try:
            os.remove('Square.json')
        except Exception:
            pass
        try:
            os.remove('Base.json')
        except Exception:
            pass

    def test_listrectangles(self):
        rec1 = Rectangle(1, 4, 5, 0, 1)
        rec2 = Rectangle(5, 5, 6, 1, 0)
        listrecs = [rec1, rec2]
        listdicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        Rectangle.save_to_file(listrecs)
        with open("Rectangle.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps(listdicts))

    def test_listsquares(self):
        s1 = Square(1, 4, 5, 0)
        s2 = Square(5, 5, 6, 1)
        listsquares = [s1, s2]
        listdicts = [s1.to_dictionary(), s2.to_dictionary()]
        Square.save_to_file(listsquares)
        with open("Square.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps(listdicts))

    def test_mixedlist_rectangle_class(self):
        s1 = Square(1, 4, 5, 0)
        r1 = Rectangle(4, 5, 6, 7, 1)
        listobjs = [s1, r1]
        listdicts = [s1.to_dictionary(), r1.to_dictionary()]
        Rectangle.save_to_file(listobjs)
        with open("Rectangle.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps(listdicts))

    def test_mixedlist_square_class(self):
        s1 = Square(1, 4, 5, 0)
        r1 = Rectangle(4, 5, 6, 7, 1)
        listobjs = [s1, r1]
        listdicts = [s1.to_dictionary(), r1.to_dictionary()]
        Square.save_to_file(listobjs)
        with open("Square.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps(listdicts))

    def test_singleobj(self):
        s1 = Square(1, 4, 5, 0)
        with self.assertRaises(TypeError):
            Square.save_to_file(s1)

    def test_emptylist(self):
        listobjs = []
        Square.save_to_file(listobjs)
        with open("Square.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_Nonelist(self):
        listobjs = None
        Square.save_to_file(listobjs)
        with open("Square.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_strarg(self):
        listobjs = "I SWEAR IM A LIST"
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(listobjs)

    def test_intarg(self):
        listobjs = 5
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(listobjs)

    def test_floatarg(self):
        listobjs = 5.23
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(listobjs)

    def test_dictarg(self):
        listobjs = dict(id=1, size=5, x=1, y=0)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(listobjs)

    def test_listofdifftypes(self):
        listobjs = [dict(id=1, size=5, x=1, y=0), "RECTANGLE", 5]
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(listobjs)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_morethanonearg(self):
        s1 = [Square(1, 4, 5, 0)]
        r1 = [Rectangle(4, 5, 6, 7, 1)]
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(s1, r1)

    def test_Basesavetofile(self):
        s1 = Square(1, 4, 5, 0)
        s2 = Square(5, 6, 7, 8)
        listobjs = [s1, s2]
        listdicts = [s1.to_dictionary(), s2.to_dictionary()]
        Base.save_to_file(listobjs)
        with open("Base.json", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps(listdicts))


class base_fromjsonstring_test(unittest.TestCase):
    """This class tests the staticmethod
    from_json_string method
    """
    def test_normalrecargs(self):
        a = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        ajson = json.dumps(a)
        b = Base.from_json_string(ajson)
        self.assertEqual(b, a)

    def test_randomjson(self):
        a = ["I am a random json", 1, 2]
        ajson = json.dumps(a)
        b = Base.from_json_string(ajson)
        self.assertEqual(a, b)

    def test_string(self):
        a = "Random string"
        with self.assertRaises(json.JSONDecodeError):
            b = Base.from_json_string(a)

    def test_num(self):
        a = 5
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_float(self):
        a = 5.5
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_list(self):
        a = ["hi", 1, 2]
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_dict(self):
        a = dict(id=1, size=4, x=0, y=0)
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_tuple(self):
        a = (5, 4, 6, 7)
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_set(self):
        a = {1, 2, 4}
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a)

    def test_noargs(self):
        with self.assertRaises(TypeError):
            b = Base.from_json_string()

    def test_morethanone(self):
        a = json.dumps(Square(1, 6, 4, 0).to_dictionary())
        b = json.dumps(Square(2, 4, 65, 7).to_dictionary())
        with self.assertRaises(TypeError):
            b = Base.from_json_string(a, b)


class base_create_test(unittest.TestCase):
    """This class tests the create classmethod
    of the base class
    """
    def test_normalargs_square(self):
        a = dict(id=1, size=5, x=2, y=1)
        b = Square.create(**a)
        self.assertEqual(b.to_dictionary(), Square(5, 2, 1, 1).to_dictionary())

    def test_normalargs_Rectangle(self):
        a = dict(id=1, width=5, height=2, x=2, y=1)
        b = Rectangle.create(**a)
        self.assertEqual(b.to_dictionary(),
                         Rectangle(5, 2, 2, 1, 1).to_dictionary())

    def test_rec_with_squareclass(self):
        a = dict(id=1, width=5, height=2, x=2, y=1)
        b = Square.create(**a)
        self.assertEqual(b.to_dictionary(),
                         Square(5, 2, 1, 1).to_dictionary())

    def test_squ_with_rectangleclass(self):
        a = dict(id=1, size=10, x=2, y=1)
        b = Rectangle.create(**a)
        self.assertEqual(b.to_dictionary(),
                         Rectangle(10, 10, 2, 1, 1).to_dictionary())

    def test_randomkeydict(self):
        a = dict(id=4, abdu=1, hany=10, hi=2, bye=1)
        b = Rectangle.create(**a)
        self.assertEqual(b.to_dictionary(),
                         Rectangle(1, 1, 0, 0, 4).to_dictionary())

    def test_listarg(self):
        a = [1, 2, 3, 6]
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_strarg(self):
        a = "HI"
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_intarg(self):
        a = 5
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_floatarg(self):
        a = 5.4
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_tuplearg(self):
        a = (3, 4, 5)
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_setarg(self):
        a = {1, 2, 4}
        with self.assertRaises(TypeError):
            b = Rectangle.create(**a)

    def test_noarg(self):
        b = Rectangle.create()
        self.assertEqual(type(b), type(Rectangle(1, 1)))

    def test_morethanonearg(self):
        dict1 = Rectangle(5, 4, 3, 5, 2).to_dictionary()
        dict2 = Rectangle(6, 5, 2, 4, 5).to_dictionary()
        with self.assertRaises(TypeError):
            b = Rectangle.create(**dict1, **dict2)


class base_loadfromfile_test(unittest.TestCase):
    """This class tests the loadfromfile
    """
    def tearDown(self):
        """removes files created during testing.
        """
        try:
            os.remove('Rectangle.json')
        except Exception:
            pass
        try:
            os.remove('Square.json')
        except Exception:
            pass

    def test_normalcase_rectangle(self):
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec2 = Rectangle(3, 4, 5, 6, 7)
        Rectangle.save_to_file([rec1, rec2])
        a = Rectangle.load_from_file()
        self.assertEqual(a[0].to_dictionary(), rec1.to_dictionary())

    def test_normalcase_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(3, 4, 5, 6)
        Square.save_to_file([s1, s2])
        a = Square.load_from_file()
        self.assertEqual(a[0].to_dictionary(), s1.to_dictionary())

    def test_sfiledoesntexist(self):
        a = Square.load_from_file()
        self.assertEqual(a, [])

    def test_rfiledoesntexist(self):
        a = Rectangle.load_from_file()
        self.assertEqual(a, [])

    def test_onearg(self):
        with self.assertRaises(TypeError):
            a = Square.load_from_file([1, 2])

    def test_loadSquare_Rec_class(self):
        s1 = Square(1, 2, 3, 4)
        Rectangle.save_to_file([s1])
        a = Rectangle.load_from_file()
        self.assertEqual(str(a[0]), "[Rectangle] (4) 2/3 - 1/1")

    def test_loadRec_Square_class(self):
        r1 = Rectangle(1, 2, 5, 3, 4)
        Square.save_to_file([r1])
        a = Square.load_from_file()
        self.assertEqual(str(a[0]), "[Square] (4) 5/3 - 1")

    def test_loadBase_class(self):
        r1 = Rectangle(1, 2, 5, 3, 4)
        with self.assertRaises(TypeError):
            a = Base.load_from_file([r1])


class base_csvsavetofile_test(unittest.TestCase):
    """This class tests the ``load_from_file``
    """
    def tearDown(self):
        """removes files created during testing.
        """
        try:
            os.remove('Rectangle.csv')
        except Exception:
            pass
        try:
            os.remove('Square.csv')
        except Exception:
            pass

    def test_listrectanglescsv(self):
        rec1 = Rectangle(1, 4, 5, 0, 1)
        rec2 = Rectangle(5, 5, 6, 1, 0)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), "id,width,height,x,y\n"
                             "1,1,4,5,0\n0,5,5,6,1\n")

    def test_listsquarescsv(self):
        s1 = Square(1, 4, 5, 0)
        s2 = Square(5, 5, 6, 1)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r", encoding='utf-8') as f:
            self.assertEqual(f.read(), "id,size,x,y\n"
                             "0,1,4,5\n1,5,5,6\n")


if __name__ == "__main__":
    unittest.main()
