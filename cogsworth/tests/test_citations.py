import unittest
import cogsworth
import os


class Test(unittest.TestCase):
    def test_cite_galaxy(self):
        """Test citations for Galaxy"""
        g = cogsworth.galaxy.Frankel2018(size=100, immediately_sample=False)
        g.get_citations(filename="test.bib")

        self.assertTrue(os.path.exists("test.bib"))
        os.remove("test.bib")

    def test_cite_galaxy_no_bibs(self):
        """Test citations for Galaxy with no bibs"""
        class DummyGalaxy(cogsworth.galaxy.Galaxy):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.__citations__ = []
        g = DummyGalaxy(size=100, immediately_sample=False)
        g.get_citations(filename="test.bib")

    def test_cite_pop(self):
        """Test citations for Galaxy"""
        p = cogsworth.pop.Population(5, processes=6)
        p.create_population(with_timing=False)
        p.get_citations(filename="test.bib")

        self.assertTrue(os.path.exists("test.bib"))
        os.remove("test.bib")