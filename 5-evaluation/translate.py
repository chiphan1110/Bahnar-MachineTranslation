# First convert your OpenNMT-py to a CTranslate2 model.
# pip3 install ctranslate2
# • OpenNMT-py:
# ct2-opennmt-py-converter --model_path model.pt --output_dir enja_ctranslate2 --quantization int8

import sys
import ctranslate2
import sentencepiece as spm

# Set file paths
source_file_path =  sys.argv[1] 
target_file_path =  source_file_path + ".translated"

sp_source_model_path = sys.argv[2] 
sp_target_model_path = sys.argv[3] 

ct_model_path = sys.argv[4]


# Load the source SentecePiece model
sp = spm.SentencePieceProcessor()
sp.load(sp_source_model_path)

# Open the source file
with open(source_file_path, "r") as source:
  lines = source.readlines()

source_sents = [line.strip() for line in lines]

# Subword the source sentences
source_sents_subworded = sp.encode_as_pieces(source_sents)

# Translate the source sentences
translator = ctranslate2.Translator(ct_model_path, device="cpu")  # or "cuda" for GPU
translations = translator.translate_batch(source_sents_subworded, batch_type="tokens", max_batch_size=4096)
translations = [translation.hypotheses[0] for translation in translations]

# Load the target SentecePiece model
sp.load(sp_target_model_path)

# Desubword the target sentences
translations_desubword = sp.decode(translations)


# Save the translations to the a file
with open(target_file_path, "w+", encoding="utf-8") as target:
  for line in translations_desubword:
    target.write(line.strip() + "\n")

print("Done")
