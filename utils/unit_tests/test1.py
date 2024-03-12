import unittest
from utils.audio_utils import convert_to_nemo_format

class TestCodeAssistant(unittest.TestCase):

    def test_convert_to_nemo_format(self):
        input_file = '32000.mp3'
        target_sr = 16000
        output = convert_to_nemo_format(input_file, target_sr)
        self.assertTrue(output, '32000_16000.wav')

if __name__ == '__main__':
    unittest.main()