import os
import soundfile as sf
import librosa


def get_wav_duration(filename):
    with sf.SoundFile(filename) as f:
        return len(f) / f.samplerate

def convert_to_nemo_format(input_file: str, target_sr: int = 16_000, outfile: str = None):
    # Load audio file
    y, sr = librosa.load(input_file, sr=None, mono=True)
    y_target_sr = librosa.resample(y, orig_sr=sr, target_sr=16000)
    if outfile:
        sf.write(f"{outfile}", y_target_sr, target_sr)
    else:
        outfile = os.path.splitext(input_file)[0]
        outfile = f"{outfile}_{target_sr}.wav"
        sf.write(outfile, y_target_sr, target_sr)
    return outfile
        

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
    
