import os
import pandas as pd
import shutil

# from utils.audio_utils import get_wav_duration

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
            speaker_id = 'spk_{:03d}'.format(len(client_id_mappings) + 1)
            client_id_mappings[client_id] = speaker_id
        # Append the shortened version from the dictionary
        speaker_ids.append(client_id_mappings[client_id])
    df['speaker_id'] = speaker_ids
    return df

def group_file_by_speaker(csv_file, src_folder, dest_folder):
    speakers = pd.read_csv(csv_file, chunksize=10)
    for chunk in speakers:
        records = chunk.to_dict('records')
        for record in records:
            speaker_folder = f'{dest_folder}/{record.get("speaker")}'
            if not os.path.exists(speaker_folder):
                os.makedirs(speaker_folder)
            file_name = record.get("file")
            src_file = f'{src_folder}/{file_name}'
            dest_file = f'{speaker_folder}/{file_name}'
            shutil.copyfile(src_file, dest_file)



if __name__ == "__main__":
    # process_common_voice_tsv('/home/eyal/git/wzudemy/NeSpeak/data/common_voice/ar/test.tsv')
    
    
    csv_file = '/home/eyal/github/wzudemy/NeSpeak/data/speakathon_data_subset/hackathon_train_subset.csv'
    wav_folder = '/home/eyal/github/wzudemy/NeSpeak/data/speakathon_data_subset/wav_files_subset'
    dst_folder = '/home/eyal/github/wzudemy/NeSpeak/data/speakathon_data_subset/nemo'
    group_file_by_speaker(csv_file, wav_folder, dst_folder)