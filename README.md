# VarDial 2022 Shared Task: Identification of Languages and Dialects of Italy (ITDI)

This repository contains the instructions, scripts, and data of the ITDI shared task which was organized as part of the _Natural Language
Processing for Similar Language Varieties and Dialects (VarDial)_ workshop co-located with COLING2 2022.


## Task

**Training data**: Wikipedia dumps (“pages-articles-multistream.xml.bz2”, from 01.03.2022) of 11 languages and dialects of Italy (Piedmontese, Venetian, Sicilian, Neapolitan, Emilian-Romagnol, Tarantino, Sardinian, Ligurian, Friulian, Ladin, Lombard). 

**Dev & Test data**: Newly collected text samples (sources unknown by participants) of a subset of the given language varieties for training. For details please check the paper _Findings of the VarDial Evaluation Campaign 2022_ cited below.

The task is classification, i.e. the model is required to discriminate between different language varieties. As the training data is provided in the form of raw Wikipedia dumps, careful pre-processing of the data is part of the task. 
The task is closed, therefore, participants are not allowed to use external data to train their models. Exceptions are off-the-shelf pre-trained language models from the HuggingFace model hub or similar, the use of which has to be clearly stated. 
The systems are evaluated on sentence level.

## Results

Please refer to the overview paper _Findings of the VarDial Evaluation Campaign 2022_ cited below, which contains short descriptions of each team’s systems including references to all system description papers published in the VarDial work shop poceedings.


## Reference

Please cite the overview paper of the VarDial 2022 evaluation campaign:

```
@inproceedings{2022-findings-vardial,
 title = "Findings of the {V}ar{D}ial Evaluation Campaign 2022",
 author = "Aepli, No{\"e}mi  and
   Anastasopoulos, Antonios  and
   Chifu, Adrian  and
   Domingues, William  and
   Faisal, Fahim  and
   G{\u{a}}man, Mihaela  and
   Ionescu, Radu Tudor  and
   Scherrer, Yves",
 booktitle = "Proceedings of the Ninth Workshop on NLP for Similar Languages, Varieties and Dialects",
 month = oct,
 year = "2022",
 address = "Gyeongju, Republic of Korea",
 publisher = "International Committee on Computational Linguistics (ICCL)"
}
```
