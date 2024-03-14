import nemo.collections.asr as nemo_asr
import wget
import os
# from scripts.speaker_tasks.filelist_to_manifest import convert_filelist_to_manifest

def main():
    print("starting ...")
    
    # nemo sanity
    print(nemo_asr.models.EncDecSpeakerLabelModel.list_available_models())
    
    
    
    # filelist = "/home/eyal/git/wzudemy/NeSpeak/data/common_voice/ar/train.tsv"
    # convert_filelist_to_manifest(filelist, --id -2 --out {data_dir}/an4/wav/an4_clstk/all_manifest.json --split
                                 
    
    # url = "https://raw.githubusercontent.com/NVIDIA/NeMo/main/scripts/speaker_tasks/filelist_to_manifest.py"
    # os.makedirs('./scripts/speaker_tasks', exist_ok=True)
    # wget.download(url=url, out='./scripts/speaker_tasks/filelist_to_manifest.py')
    
    # !wget -P scripts/speaker_tasks/ https://raw.githubusercontent.com/NVIDIA/NeMo/$BRANCH/scripts/speaker_tasks/filelist_to_manifest.py

    
    # finetune model
    
    # data
    # Each line in the manifest file describes a training sample - audio_filepath contains the path to the wav file, duration it's duration in seconds, and label is the speaker class label:
    # {"audio_filepath": "<absolute path to dataset>data/an4/wav/an4test_clstk/menk/cen4-menk-b.wav", "duration": 3.9, "label": "menk"}
    from utils.speaker_tasks import filelist_to_manifest
    
    filelist_to_manifest(
        '/home/eyal/github/wzudemy/NeSpeak/data/speakathon_data_subset/nemo',
        'manifest',
        -2,
        'out',
        min_count=0
        )
    
    # config
    
    # create a trainer
    
    # Setting the trainer to the restored model

    # Fine-tune training step

    # Saving .nemo file
    
    # Speaker Verification ???

    # Extract Speaker Embeddings
    
    # Verification


    
    

if __name__ == "__main__":
    main()