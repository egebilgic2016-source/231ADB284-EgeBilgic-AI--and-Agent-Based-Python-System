import unittest
from agent import WikipediaTool

class TestWikipediaTool(unittest.TestCase):
    def setUp(self):
        # Initialize  tool before each of test
        self.wiki_tool = WikipediaTool()

    def test_valid_search(self):
        # Scenario 1: Test with a known and discovered valid topic
        result = self.wiki_tool.search("Python_(programming_language)")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 10) # Summary should have some text

    def test_invalid_search(self):
        # Scenario 2: Test with gibberish in order to safely trigger error handling
        result = self.wiki_tool.search("asdfghjkl123456789000")
        self.assertTrue("Error" in result or "Not Found" in result)

if __name__ == "__main__":
    unittest.main()
