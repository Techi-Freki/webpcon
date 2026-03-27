import unittest

from pathlib import Path
from PIL import Image
from ..converter import Converter, Format


test_webp = 'test-webp.webp'
fail_webp = 'test.webp'
fail_webp_jpg = 'test.jpg'
test_webp_png = 'test-webp.png'
test_webp_jpg = 'test-webp.jpg'


class ConverterTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        img = Image.new('CMYK', (100, 100))
        img.save(test_webp, 'webp')

    @classmethod
    def tearDownClass(cls):
        Path(test_webp).unlink(missing_ok=True)
        Path(test_webp_png).unlink(missing_ok=True)
        Path(test_webp_jpg).unlink(missing_ok=True)

    def test_convert(self):
        self.assertRaises(FileNotFoundError,
                          lambda:Converter.convert(fail_webp, fail_webp_jpg, Format.JPEG))
        self.assertTrue(Path(test_webp).exists())
        Converter.convert(test_webp, test_webp_png)
        self.assertTrue(Path(test_webp_png).exists())
        Converter.convert(test_webp, test_webp_jpg, file_format=Format.JPEG)
        self.assertTrue(Path(test_webp_jpg).exists())