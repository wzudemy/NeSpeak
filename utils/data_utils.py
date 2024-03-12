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
    
    # try using filelist_to_manifest
    # input:
    
    
    # filelist - 
    # !python {NEMO_ROOT}/scripts/speaker_tasks/filelist_to_manifest.py
    # --filelist {data_dir}/an4/wav/an4_clstk/train_all.txt
    # --id -2
    # --out {data_dir}/an4/wav/an4_clstk/all_manifest.json 
    # --split
    
    
    file_path  = os.path.dirname(filename)
    # read the file into a dataframe
    df = preprocess_df(filename)
    # client_id, speaker_id, path
    
    # go over the row in the df, and for each row:
    # 1. convert the mp3/wav audio file to nemo format (mono, 16000, agc)
    # 2. create a nemo record
    
    df.apply(concert)
    
    
    print(len(df))

def preprocess_df(filename):
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
    