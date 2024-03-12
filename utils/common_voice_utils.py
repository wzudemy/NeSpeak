from concurrent.futures import ProcessPoolExecutor
import os
import pandas as pd
from tqdm import tqdm
from utils.audio_utils import convert_to_nemo_format_using_pydub, mp3_to_wav

from utils.data_utils import preprocess_df
from utils.file_utils import change_extension, copy_file_with_path, get_immediate_parent, write_list_to_file

import os
from glob import glob

from utils.speaker_tasks import filelist_to_manifest

tqdm.pandas()



def copy_file_to_its_client_folder(row):
    path = row['path']
    src_path = os.path.join(row['clips_path'], path)
    if os.path.exists(src_path):
        
        # convert to nemo
        # src_path = convert_to_nemo_format_using_pydub(src_path)
        # dst_filename = change_extension(path, '.wav')
        
        # without converstion
        dst_filename = path
        
        speaker_id = row['speaker_id']
        dst_path = f'data/common_voice/nemo/{speaker_id}/{dst_filename}'
        copy_file_with_path(src_path, dst_path)
    else:
        print(f"copy_file_to_its_client_folder: {src_path} does not exists")
    

def copy_files_to_folder_according_to_speaker(tsv_file, out_dir=None, chunk_size=100):
    df = preprocess_df(tsv_file)
    # df = df.head(1000)
    df_spk =f'{tsv_file}_spk.tsv'
    df.to_csv(df_spk, sep='\t')
    df_chunked = pd.read_csv(df_spk, sep='\t', chunksize=chunk_size)
    
    # Read the CSV file in chunks
    for chunk in tqdm(df_chunked):
        # Process the chunk
        chunk['clips_path'] = os.path.join(os.path.dirname(tsv_file), 'clips')
        
        # for each row, copy the filename to a folder with the client id name
        chunk.progress_apply(copy_file_to_its_client_folder, axis=1)
        
        
    return df['speaker_id'].nunique()

def prepare_common_voice_to_name(common_voice_file_list: str):
    
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
    
    lang = get_immediate_parent(common_voice_file_list)
    
    copy_files_to_folder_according_to_speaker(common_voice_file_list)
    
    data_dir = "/home/eyal/github/wzudemy/NeSpeak/data/common_voice/nemo"
    
    os.path.join(data_dir, lang)
        
    mp3_files_list = glob(os.path.join(data_dir, "**", "*.mp3"), recursive=True)
    
    with ProcessPoolExecutor() as pool:
        wav_files = pool.map(convert_to_nemo_format_using_pydub, mp3_files_list)
        
    wav_files_list = glob(os.path.join(data_dir, "**", "*.wav"), recursive=True)
    
    filelist_txt_file = change_extension(common_voice_file_list, ".txt")
    
    write_list_to_file(wav_files_list, filelist_txt_file)
    
    manifest_file = change_extension(common_voice_file_list, ".filelist.json")
    # /home/eyal/github/wzudemy/NeSpeak/data/common_voice/nemo/spk_1/common_voice_ar_24032301_16000.wav
    filelist_to_manifest(filelist_txt_file, None, -2, manifest_file, False, False, min_count=0)
    
    return len(mp3_files_list), len(list(wav_files))
 