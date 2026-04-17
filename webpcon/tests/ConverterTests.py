import unittest

from pathlib import Path
from PIL import Image
from ..converter import Converter, Format


test_webp = 'test-webp.webp'
fail_io_webp = 'io_err.webp'
fail_io_png = 'io_err.png'
fail_webp = 'test.webp'
fail_webp_jpg = 'test.jpg'
test_webp_png = 'test-webp.png'
test_webp_jpg = 'test-webp.jpg'


class ConverterTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        img = Image.new('CMYK', (100, 100))
        img.save(test_webp, 'webp')
        with open(fail_io_webp, 'w') as err_file:
            err_file.write('\n')

    @classmethod
    def tearDownClass(cls):
        parm = { 'missing_ok': True }
        Path(test_webp).unlink(**parm)
        Path(test_webp_png).unlink(**parm)
        Path(test_webp_jpg).unlink(**parm)
        Path(fail_io_webp).unlink(**parm)

    def test_convert_success_png(self):
        self.assertTrue(Path(test_webp).exists())
        Converter.convert(test_webp, test_webp_png)
        self.assertTrue(Path(test_webp_png).exists())
        with Image.open(test_webp_png) as img:
            self.assertTrue(img.mode == 'RGB')

    def test_convert_success_jpg(self):
        self.assertTrue(Path(test_webp).exists())
        Converter.convert(test_webp, test_webp_jpg, Format.JPEG)
        self.assertTrue(Path(test_webp_jpg).exists())
        with Image.open(test_webp_jpg) as img:
            self.assertTrue(img.mode == 'RGB')

    def test_convert_fail_FileNotFound(self):
        self.assertRaises(FileNotFoundError,
                          lambda:Converter.convert(
                              fail_webp,
                              fail_webp_jpg,
                              Format.JPEG
                          ))

    def test_convert_fail_IOError(self):
        self.assertRaises(IOError,
                          lambda:Converter.convert(
                              fail_io_webp,
                              fail_io_png
                          ))
