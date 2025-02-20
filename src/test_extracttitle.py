import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_heading(self):
        # Test extracting title from markdown with a heading
        markdown = "# This is a heading\n\nThis is a paragraph."
        expected = "This is a heading"
        self.assertEqual(extract_title(markdown), expected)

    def test_extract_title_with_multiple_headings(self):
        # Test extracting title from markdown with multiple headings
        markdown = "# First heading\n\n## Second heading\n\nThis is a paragraph."
        expected = "First heading"
        self.assertEqual(extract_title(markdown), expected)

    def test_extract_title_with_no_heading(self):
        # Test extracting title from markdown with no heading
        markdown = "This is a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No heading block found" in str(context.exception))

    def test_extract_title_with_heading_and_whitespace(self):
        # Test extracting title from markdown with a heading and leading/trailing whitespace
        markdown = "  # This is a heading  \n\nThis is a paragraph."
        expected = "This is a heading"
        self.assertEqual(extract_title(markdown), expected)

    def test_extract_title_with_heading_and_special_characters(self):
        # Test extracting title from markdown with a heading and special characters
        markdown = "# This is a heading with special characters! @#$%^&*()"
        expected = "This is a heading with special characters! @#$%^&*()"
        self.assertEqual(extract_title(markdown), expected)

if __name__ == "__main__":
    unittest.main()