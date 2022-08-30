# VarDial 2022 Shared Task: Identification of Languages and Dialects of Italy (ITDI)

This repository contains the instructions, scripts, and data of the ITDI shared task which was organized as part of the _Natural Language
Processing for Similar Language Varieties and Dialects (VarDial)_ workshop co-located with COLING2 2022.


## Task

**Training data**: Wikipedia dumps (“pages-articles-multistream.xml.bz2”, from 01.03.2022) of 11 languages and dialects of Italy (Piedmontese, Venetian, Sicilian, Neapolitan, Emilian-Romagnol, Tarantino, Sardinian, Ligurian, Friulian, Ladin, Lombard). 

**Dev & Test data**: Newly collected text samples (sources unknown by participants) of a subset of the given language varieties for training.

The task is classification, i.e. the model is required to discriminate between different language varieties. As the training data is provided in the form of raw Wikipedia dumps, careful pre-processing of the data is part of the task. 
The task is closed, therefore, participants are not allowed to use external data to train their models. Exceptions are off-the-shelf pre-trained language models from the HuggingFace model hub or similar, the use of which has to be clearly stated. 
The systems are evaluated on sentence level.

## Results

Please refer to the overview paper _Findings of the VarDial Evaluation Campaign 2022_ cited below, which contains short descriptions of each team’s systems including references to all system description papers published in the VarDial work shop poceedings.


## Languages & Dialects


![1024px-Dialetti_e_lingue_in_Italia](https://user-images.githubusercontent.com/32330160/187560839-b38719ff-7a47-4002-88ff-fe4996ce1012.png)


https://upload.wikimedia.org/wikipedia/commons/3/32/Dialetti_e_lingue_in_Italia.png
Antonio Ciccolella, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons



## Online Sources for DEV/TEST set


### Wikisource

```
- https:// **(lij|nap|pms|vec)** .wikisource.org/
- https://wikisource.org/wiki/Main_Page/ **(Furlan|Ladin|Lumbaart|Sicilianu)**
- https://wikisource.org/wiki/Category: **(Sardu|Sicilianu)**
- https://it.wikisource.org/wiki/Categoria:Testi_in_ **(napoletano|siciliano)**
- https://it.wikisource.org/wiki/Biancogne
```

### Other Webpages

```
- https://www.dialettando.com
- https://arlef.it/it/materiali/
- https://www.filologicafriulana.it/lenghe-e-culture/
- https://www.bulgnais.com/libri.html
- http://www.tarantonostra.com/
- https://www.istitutoladino.it
- http://www.linguasiciliana.org
- https://www.lingualombarda.it/index.php/milanese.html
- http://www.salviamoilsiciliano.com/raccolte/
- http://www.museomirabilesicilia.it/folklore-siciliano.html 
- http://www.salviamoilsiciliano.com/raccolte/poesie/ 
- http://www.salviamoilsiciliano.com/raccolte/commedie/ 
- http://rapallosalvatore.blogspot.com/p/raccolta-poesie-in-dialetto-siciliano.html 
```


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
