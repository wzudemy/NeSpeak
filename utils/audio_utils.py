import os
import soundfile as sf
import librosa
from pydub import AudioSegment


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)



def get_wav_duration(filename):
    with sf.SoundFile(filename) as f:
        return len(f) / f.samplerate

def convert_to_nemo_format(input_file: str, target_sr: int = 16_000, outfile: str = None):
    # Load audio file
    y, sr = librosa.load(input_file, sr=None, mono=True)
    y_target_sr = librosa.resample(y, orig_sr=sr, target_sr=16000)
    if outfile:
        sf.write(f"{outfile}_{target_sr}", y_target_sr, target_sr)
    else:
        outfile = os.path.splitext(input_file)[0]
        outfile = f"{outfile}_{target_sr}.wav"
        sf.write(outfile, y_target_sr, target_sr)
    return outfile

def convert_to_nemo_format_using_pydub(
    input_file: str,
    target_sr: int = 16_000, 
    outfile: str = None,
    target_dBFS: float = -20.0,
    ):
    input_audio = AudioSegment.from_mp3(input_file)
    output_audio = input_audio.set_channels(1)
    output_audio = output_audio.set_frame_rate(target_sr)
    
    # Apply AGC (Automatic Gain Control)
    output_audio = match_target_amplitude(output_audio, target_dBFS=target_dBFS)
    
    if outfile:
        output_audio.export(f"{outfile}", format="wav")
    else:
        outfile = os.path.splitext(input_file)[0]
        outfile = f"{outfile}_{target_sr}.wav"
        output_audio.export(outfile, format="wav")
    return outfile



def mp3_to_wav(mp3_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    
    # Change the file extension to ".wav"
    wav_file = os.path.splitext(mp3_file)[0] + ".wav"
    
    # Export the audio as WAV
    audio.export(wav_file, format="wav")
    
    return wav_file


def normalize(filename):
    audio = AudioSegment.from_wav(filename)
    # Apply AGC (Automatic Gain Control)
    normalized_audio = audio.normalize()
    normalized_audio.export("output_normalized.wav", format="wav")


        

# {% load def main(input_file):
#     # Check if the file exists
#     if not os.path.exists(input_file):
#         print("File not found.")
#         return
    
#     # Convert to wav if needed and resample to 16000 Hz
#     sound = convert_to_wav(input_file)
    
#     # Convert stereo to mono
#     if sound.channels == 2:
#         sound = sound.set_channels(1)
    
#     # Construct the output filename
#     output_file = os.path.splitext(input_file)[0] + "_processed.wav"
    
#     # Export the processed audio
#     sound.export(output_file, format="wav")
    # print("File processed successfully. Saved as:", output_file)_tags %}

if __name__ == "__main__":
    
    test_file = '32000.mp3'
    
    convert_to_nemo_format(test_file)
    
