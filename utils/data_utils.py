import os
import pandas as pd

from utils.audio_utils import get_wav_duration

def process_common_voice_tsv(filename: str):
    
    # convert from common voice format to a Nemo manifest format
    
    # {
        # "audio_filepath": "<absolute path to dataset>",
        # "duration": 3.9,
        # "label": "menk"
    #  }
    
    file_path  = os.path.dirname(filename)
    # read the file into a dataframe
    df = convert_to_df(filename)
    # client_id, speaker_id, path
    
    test_filename = '32000.mp3'
    
    
    
    test = (get_wav_duration(os.path.join(file_path, 'clips', test_filename)))
    print(test)
    
    
    
    print(len(df))

def convert_to_df(filename):
    df = pd.read_csv(filename, sep='\t')
    df = df[['client_id', 'path']]
    client_id_mappings = {}
    speaker_ids = []
    
    # Iterate over the client_id column
    for client_id in df['client_id']:
        if client_id not in client_id_mappings:
            # If the client_id is encountered for the first time, assign a new shortened version
            speaker_id = 'spk_{}'.format(len(client_id_mappings) + 1)
            client_id_mappings[client_id] = speaker_id
        # Append the shortened version from the dictionary
        speaker_ids.append(client_id_mappings[client_id])
    df['speaker_id'] = speaker_ids
    return df



if __name__ == "__main__":
    process_common_voice_tsv('/home/eyal/git/wzudemy/NeSpeak/data/common_voice/ar/test.tsv')
    