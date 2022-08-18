# Dialect Identification: Languages and Dialects of Italy (ITDI)

## Task

**Organizers**: Noëmi Aepli (University of Zurich) and Yves Scherrer (University of Helsinki)

**Contact**: naepli@cl.uzh.ch

**Task description**: We provide participants with Wikipedia dumps (“pages-articles-multistream.xml.bz2”, from 01.03.2022) of 11 languages and dialects of Italy for training (Piedmontese, Venetian, Sicilian, Neapolitan, Emilian-Romagnol, Tarantino, Sardinian, Ligurian, Friulian, Ladin, Lombard). The Standard Italian raw Wikipedia dump may also be used as training data, but there will not be any instances of Standard Italian in the development and test sets. Please use the provided script to download (and extract, if you wish) the dumps to make sure you work with the correct kind and date of the dump.
The task is classification, i.e. the model is required to discriminate between different language varieties. As the training data is provided in the form of raw Wikipedia dumps, careful pre-processing of the data is part of the task. The task is closed, therefore, participants are not allowed to use external data to train their models. Exceptions are off-the-shelf pre-trained language models from the HuggingFace model hub or similar, the use of which has to be clearly stated. The test set will contain newly collected text samples of a subset of the given language varieties for training. The systems will be evaluated on sentence level.

**Submission type**: Closed


## Training Data Release

**Folder Content**:
- *get_ITDI_training_data.sh*: script to get/extract training data; please use this script to make sure you work with the correct kind and date of the dump.
- *dev.txt*: development set
- *ITDI_eval.py*: evaluation script