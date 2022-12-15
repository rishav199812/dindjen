import unittest


class DataMappingTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass
	
	def test_data_mapping_with_only_passing_item(self):
		assert True
 	def test_data_mapping_with_only_failing_item(self):
 		assert False


if __name__ == "__main__":
    unittest.main()
