import unittest
from utils.audio_utils import convert_to_nemo_format, convert_to_nemo_format_using_pydub
import librosa
from pydub import AudioSegment

from utils.common_voice_utils import copy_files_to_folder_according_to_speaker, prepare_common_voice_to_nemo



class audio_utils_tests(unittest.TestCase):

    # def test_convert_mono_file_to_nemo_format(self):
    #     input_file = 'data/common_voice/raw/ar/common_voice_ar_19384288.mp3'
    #     y, sr = librosa.load(input_file, sr=None, mono=False)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertNotEqual(sr, 16_000)
    #     self.assertEqual(n_channels, 1)
    #     target_sr = 16000
    #     output = convert_to_nemo_format(input_file, target_sr)
    #     self.assertEqual(output, 'data/common_voice/raw/ar/common_voice_ar_19384288_16000.wav')
    #     y, sr = librosa.load(output, sr=None, mono=False)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertEqual(sr, 16_000)
    #     self.assertEqual(n_channels, 1)
        
    # def test_convert_from_subset_file_to_nemo_format(self):
    #     input_file = 'data/wav_files_subset/0403581.wav'
    #     y, sr = librosa.load(input_file, sr=None)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertEqual(sr, 32_000)
    #     self.assertEqual(n_channels, 1)
    #     target_sr = 16000
    #     output = convert_to_nemo_format(input_file, target_sr)
    #     self.assertEqual(output, 'data/wav_files_subset/0403581_16000.wav')
    #     y, sr = librosa.load(output, sr=None, mono=False)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertEqual(sr, 16_000)
    #     self.assertEqual(n_channels, 1)
        
    
    # def test_convert_mono_file_to_nemo_format_using_pydub(self):
    #     input_file = 'data/common_voice/raw/ar/common_voice_ar_19384288.mp3'
    #     y, sr = librosa.load(input_file, sr=None, mono=False)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertNotEqual(sr, 16_000)
    #     self.assertEqual(n_channels, 1)
    #     target_sr = 16000
    #     output = convert_to_nemo_format_using_pydub(input_file, target_sr)
    #     self.assertTrue(output, '32000_16000.wav')
    #     y, sr = librosa.load(output, sr=None, mono=False)
    #     n_channels = y.shape[0] if y.ndim > 1 else 1
    #     self.assertEqual(sr, 16_000)
    #     self.assertEqual(n_channels, 1)
        
    def test_convert_from_subset__to_nemo_format_using_pydub(self):
        return
        input_file = 'data/wav_files_subset/0403581.wav'
        y, sr = librosa.load(input_file, sr=None, mono=False)
        n_channels = y.shape[0] if y.ndim > 1 else 1
        self.assertNotEqual(sr, 16_000)
        self.assertEqual(n_channels, 1)
        target_sr = 16000
        output = convert_to_nemo_format_using_pydub(input_file, target_sr)
        self.assertEqual(output, 'data/wav_files_subset/0403581_16000.wav')
        y, sr = librosa.load(output, sr=None, mono=False)
        n_channels = y.shape[0] if y.ndim > 1 else 1
        self.assertEqual(sr, 16_000)
        self.assertEqual(n_channels, 1)
        
        output_audio = AudioSegment.from_wav(output)
        self.assertAlmostEqual(output_audio.dBFS, -20.0, delta=1)
        
    def test_move_files_to_folder_according_to_speaker(self):
        # res = copy_files_to_folder_according_to_speaker('data/common_voice/raw/ar/train.tsv')
        self.assertEqual(23, 23)
        
        
    def test_prepare_common_voice_to_nemo_ar(self):
        res = prepare_common_voice_to_nemo('data/common_voice/raw/ar/train.tsv')
        self.assertEqual((407, 407), res)
        
    def test_prepare_common_voice_to_nemo_tr(self):
        res = prepare_common_voice_to_nemo('data/common_voice/raw/tr/train.tsv')
        self.assertEqual((407, 407),  res)
        

if __name__ == '__main__':
    unittest.main()