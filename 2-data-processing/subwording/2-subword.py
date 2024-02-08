#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Subwording the source and target files
# Command: python3 subword.py <sp_source_model_path> <sp_target_model_path> <source_file_path> <target_file_path>


import sys
import sentencepiece as spm


model = sys.argv[1]
raw = sys.argv[2]
subworded = sys.argv[3]

print("Model:", model)
print("Dataset:", raw)

sp = spm.SentencePieceProcessor()


# Subwording the train source

sp.load(model)

with open(raw, encoding='utf-8') as data, open(subworded, "w+", encoding='utf-8') as subword:
    for line in data:
        line = line.strip()
        line = sp.encode_as_pieces(line)
        # line = ['<s>'] + line + ['</s>']    # add start & end tokens; optional
        line = " ".join([token for token in line])
        subword.write(line + "\n")

print("Done subwording the file! Output:", subworded)
