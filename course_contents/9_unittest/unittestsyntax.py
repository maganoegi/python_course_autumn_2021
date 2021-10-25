
# premierement, il faut importer la librairie
import unittest

# on crée un classe de test..
class MyCustomTests( unittest.TestCase ):

    def setUp(self):
        # pour initialiser nos ressources pour les tests
        ... 

    def test_function_sum(self):
        a = 1 # variable locale
        b = 2 # variable locale

        # ce qu'on veut voir comme résultat
        expected = sum(a + b) 
        # ce qu'on a écrit
        obtained = my_sum_fonction(a + b) 
        
        # validation de résultat
        self.assertEqual(expected, obtained) 
        
    # plusieurs checks possibles...
    - self.assertEqual(a, b)
    - self.assertNotEqual(a, b)
    - self.assertTrue(x)
    - self.assertFalse(x)
    - self.assertIs(a, b)
    - self.assertIsNotNone(x)
    - self.assertRaisesRegexp(exc, r, fun, args, *kwds)
    - self.assertItemsEqual(a, b)
    #  et d'autres...