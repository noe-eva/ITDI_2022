import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report
import sys

"""
Evaluation script for the VarDial ITDI shared task 2022.

Usage: ITDI_eval.py <GOLD_STANDARD_FILE> <PREDICTION_FILE> Output:
Input: 1) file containing the gold standard 2) file with the predictions
File format: one sentence per line: language label, tab, sentence
Output: Report showing the main classification metrics.
Warning: "zero_division=warn" in the "classification report" might
show a warning when there is a class which has never been predicted

May 2022, naepli@cl.uzh.ch
"""

if not len(sys.argv) > 2:
	print(len(sys.argv))
	raise AssertionError("Need 2 input files. Usage: ITDI_eval.py <GOLD_STANDARD_FILE> <PREDICTION_FILE>")


gs_df = pd.read_csv(sys.argv[1], sep="\t", header=None)
y_true = gs_df[0].tolist()

pred_df = pd.read_csv(sys.argv[2], sep="\t", header=None)
y_pred = pred_df[0].tolist()

if not len(y_true) == len(y_pred):
    raise AssertionError("System output does not have the same length as the Gold Standard.")

all_dev_labels = sorted(list(set((y_true + y_pred))))

# zero_division=warn: acts as 0, but warnings are raised when there is
# a zero division, i.e. when all predictions and labels are negative
print(classification_report(y_true, y_pred, target_names=all_dev_labels, zero_division='warn'))

