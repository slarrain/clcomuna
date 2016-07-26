from unittest import TestCase

import clcomuna

class TestComuna(TestCase):
    def test_get_code(self):
        self.assertTrue(clcomuna.get_code("peumo")=="06112")
        self.assertTrue(clcomuna.get_code("santo domingo")=="05606")
        self.assertTrue(clcomuna.get_code("o'HIGGins")=="11302")
        self.assertTrue(clcomuna.get_code("alrarobo")==None)


    def test_get_fuzzy(self):
        self.assertTrue(clcomuna.get_code(clcomuna.get_fuzzy("puemo"))=="06112")
        self.assertTrue(clcomuna.get_code(clcomuna.get_fuzzy("sato dimingo"))=="05606")
        self.assertTrue(clcomuna.get_code(clcomuna.get_fuzzy("HIGGins"))=="11302")
        self.assertTrue(clcomuna.get_fuzzy("alrarobo")=="ALGARROBO")
        self.assertTrue(clcomuna.get_fuzzy("alrarobo", True, 83)==None)

    # def test_get_code(self):
    #     self.assertTrue(clcomuna.get_code("peumo")=="06112")
    #     self.assertTrue(clcomuna.get_code("santo domingo")=="05606")
    #     self.assertTrue(clcomuna.get_code("o'HIGGins")=="11302")
