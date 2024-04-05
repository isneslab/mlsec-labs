# Lab 02: Time-aware evaluations

In this lab, you will perform a time-aware evaluation to see the performance of a classifier over time. 

## Android Malware Dataset (Feature Space)

These are preprocessed datasets that are already converted into feature matrices. They use the DREBIN feature abstraction. 

* [Download Dataset](https://emckclac-my.sharepoint.com/:u:/g/personal/k1802448_kcl_ac_uk/ERWQQfXF3MxCgPe1G4qGsWcBeGDsktcQ6kuXQbsbjGyy2g?e=amOhD4)

These are the major files in the dataset `.zip`: 
* `X.json`: the feature matrix (remember to drop the `sha256` column before running classification tasks)
* `y.json`: the labels (0 for goodware, 1 for malware)
* `meta.json`: contains some metadata information, including timestamps,
* `X-10k.p` and `f-10k.p` are smaller versions with the top-10k features (f.p is the vector of feature names)

The features correspond to the apps from 2014--2018 used in this paper:
* Federico Barbero, Feargus Pendlebury, Fabio Pierazzi, and Lorenzo Cavallaro, [Transcending Transcend: Revisiting malware classification in the presence of concept drift](https://arxiv.org/abs/2010.03856) , In IEEE Symposium on Security and Privacy (S&P), 2022

To understand the meaning of the features, read the feature extraction process here: 
* [DREBIN (NDSS 2014)](https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_3_1.pdf)

## Tesseract Library

In case you need to do time-aware evaluations with: 

* [Tesseract Library](https://github.com/s2labres/tesseract-ml-release)

You can refer to this publication:

* Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, and Lorenzo Cavallaro , [TESSERACT: Eliminating experimental bias in malware classification across space and time](https://fabio.pierazzi.com/assets/pdf/tesseract.pdf), In Proc. of USENIX Security Symposium, 2019