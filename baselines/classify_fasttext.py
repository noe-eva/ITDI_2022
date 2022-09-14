#!/usr/bin/env python3

"""
Sript for Baseline 1 Fasttext of VarDial ITDI shared task 2022.

The pretrained Fasttext model we worked with can be downloaded here:
https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin

Usage: baseline_fasttext.py <GOLD_STANDARD_FILE> <MODELPATH> <K>
Input: 1) file containing the gold standard; 2) path to fasttext
model 3) integer number k (we used 10) that specifies how many
predictions to consider File format: one sentence per line: language
label, tab, sentence Output: classification report

May 2022, naepli@cl.uzh.ch
"""


import fasttext
import codecs
import json
from collections import defaultdict
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report
import sys

assert len(sys.argv) == 4, "Missing argument. Usage: baseline_fasttext.py <GOLD_STANDARD_FILE> <MODELPATH> <k>"
gs_file = sys.argv[1]
modelpath = sys.argv[2]
# take k first languages into account 
# (i.e. correct prediction, if prediction in first 10)
k = int(sys.argv[3])


class LanguageIdentification:

    def __init__(self):
        pretrained_lang_model = modelpath
        self.model = fasttext.load_model(pretrained_lang_model)

    def predict_lang(self, text, k):
        predictions = self.model.predict(text, k=k) 
        return predictions

if __name__ == '__main__':

    LANGUAGE = LanguageIdentification()
    languages = defaultdict(int)
    gs = codecs.open(gs_file, "r", "utf-8").readlines()

    correct, wrong = 0, 0
    y_true, y_pred = [], []
    support = {'eml':0, 'fur':0, 'lij':0, 'lld':0, 'lmo':0, 'nap':0, 'pms':0, 'roa_tara':0, 'sc':0, 'scn':0, 'vec':0}
    
    for line in gs:

        lang, sent = line.strip().split("\t")
        y_true.append(lang.lower())
        support[lang.lower()] += 1
        
        # predict with specified fasttext model
        pred = LANGUAGE.predict_lang(sent, k)
        
        k_preds = []
        nr_preds = len(pred[0])
        
        # if less predictions than specified k, consider only k
        if nr_preds < k:
            range_max = nr_preds
        else:
            range_max = k

        for p in range(0,range_max):
            l = pred[0][p]
            l = l.replace('__label__', '')
            k_preds.append(l)

        # consider only the languages which we are interested in
        intersection = [x for x in k_preds if x in support.keys()]
       
        # take the first one of that list as prediction
        # if none of them is in the first k predictions: prediction is 'unk'
        # otherwise take the first prediction
        if len(intersection) == 0:
            wrong += 1
            y_pred.append('unk')
        elif lang.lower() == intersection[0]:
            correct+=1
            y_pred.append(lang.lower())
        else:
            wrong += 1
            y_pred.append(intersection[0])
    
    assert len(y_pred) == len(gs)
    assert correct + wrong == len(gs)

    sample_weight = []
    for value in y_true:
        sample_weight.append(support[value])

    assert len(y_true) == len(y_pred) == len(sample_weight)

    # zero_division=warn: acts as 0, but warnings are raised when there is
    # a zero division, i.e. when all predictions and labels are negative
    all_dev_labels = sorted(list(set((y_true + y_pred))))
    print(classification_report(y_true, y_pred, labels = ['eml', 'fur', 'lij', 'lld', 'lmo', 'nap', 'pms', 'roa_tara', 'sc', 'scn', 'vec'], digits=4,  zero_division='warn'))
    print(f"Classification report for baseline with {k} best FastText predictions.\n")


# F1 scores on test set with k=10
# micro avg     0.1746
# macro avg     0.1004
# weighted avg  0.1322