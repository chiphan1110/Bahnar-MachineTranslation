# Files must be untokenized/unsubworded
# Run this file from CMD/Terminal
# Example Command: python3 eval-metrics.py test_file_name.txt mt_file_name.txt


import sys
import sacrebleu

target_test = sys.argv[1]  # Test file argument
target_pred = sys.argv[2]  # MTed file argument

# Open the test dataset human translation file and detokenize the references
refs = []

with open(target_test) as test:
    for line in test: 
        line = line.strip()
        refs.append(line)

refs = [refs]  # Yes, it is a list of list(s) as required by sacreBLEU


# Open the translation file by the NMT model and detokenize the predictions
preds = []

with open(target_pred) as pred:  
    for line in pred: 
        line = line.strip()
        preds.append(line)


# Calculate and print the BLEU score
bleu = sacrebleu.corpus_bleu(preds, refs)
print("BLEU: ", round(bleu.score, 2))

# Calculate CHRF
chrf = sacrebleu.corpus_chrf(preds, refs)
print("CHRF:", round(chrf.score, 2))

# Calculate TER
metric = sacrebleu.metrics.TER()
ter = metric.corpus_score(preds, refs)
print("TER:", round(ter.score, 2))