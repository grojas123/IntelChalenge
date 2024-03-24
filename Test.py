import unittest

import MaxAreaTank
import SumAllAreasWithWater

class TestAreas(unittest.TestCase):

    def test_maxAreaTank(self):
        listColumns = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(MaxAreaTank.max_area(listColumns), 49, "Should be 49")

    def test_sumAllAreas(self):
        listColumns = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(SumAllAreasWithWater.water_areas(listColumns), 156, "Should be 156")

if __name__ == '__main__':
    unittest.main()