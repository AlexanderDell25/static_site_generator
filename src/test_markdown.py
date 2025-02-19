import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images_empty_text(self):
        # Test extracting images from empty text
        text = ""
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_empty_text(self):
        # Test extracting links from empty text
        text = ""
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_no_images(self):
        # Test extracting images from text with no images
        text = "This is text with no images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_no_links(self):
        # Test extracting links from text with no links
        text = "This is text with no links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_multiple_images(self):
        # Test extracting multiple images from text
        text = "![Image 1](https://example.com/image1.png) and ![Image 2](https://example.com/image2.png)"
        expected = [("Image 1", "https://example.com/image1.png"), ("Image 2", "https://example.com/image2.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links_multiple_links(self):
        # Test extracting multiple links from text
        text = "This is a link [to example 1](https://example.com/1) and [to example 2](https://example.com/2)"
        expected = [("to example 1", "https://example.com/1"), ("to example 2", "https://example.com/2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_images_and_links_mixed(self):
        # Test extracting images and links from mixed content
        text = "![Image](https://example.com/image.png) and a link [to example](https://example.com)"
        expected_images = [("Image", "https://example.com/image.png")]
        expected_links = [("to example", "https://example.com")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    """ def test_extract_markdown_malformed(self):
        # Test extracting from malformed markdown
        text = "[missing closing parenthesis](http://example.com"
        expected_links = []
        self.assertEqual(extract_markdown_links(text), expected_links)

        text = "![missing alt text](http://example.com)"
        expected_images = [("", "http://example.com")]
        self.assertEqual(extract_markdown_images(text), expected_images) """

    """ def test_extract_markdown_nested_brackets(self):
        # Test extracting from markdown with nested brackets
        text = "This is a link [to [nested] example](https://example.com)"
        expected_links = [("to [nested] example", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected_links)

        text = "![Image with [nested] alt text](https://example.com/image.png)"
        expected_images = [("Image with [nested] alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected_images) """

    def test_extract_markdown_special_characters(self):
        # Test extracting from markdown with URLs containing special characters
        text = "This is a link [to example](https://example.com/path?query=param&another=param)"
        expected_links = [("to example", "https://example.com/path?query=param&another=param")]
        self.assertEqual(extract_markdown_links(text), expected_links)

        text = "![Image](https://example.com/image.png?query=param&another=param)"
        expected_images = [("Image", "https://example.com/image.png?query=param&another=param")]
        self.assertEqual(extract_markdown_images(text), expected_images)

if __name__ == "__main__":
    unittest.main()