# ML Security Labs

## Setup

It is better to use Python 3.10 as we are still figuring out a compatibility with the Tesseract library.

I would also advise to create a Python virtual environment for these labs, using Python 3.10: see [here](https://docs.python.org/3/library/venv.html) for a guide on virtual environments. 

## Labs overview

This github workspace contains some example to get acquainted with the use of Machine Learning for Systems Security and Malware Detection. 

* **Lab 01: Malware detection with Machine Learning**. This lab is a warmer to introduce on the use of notebooks, and to compute the main performance metrics. Here, you will see how to embed some simple features into vector format, and how to perform classification tasks on datasets of increasing complexity. 

* **Lab 02: Time-aware evaluations**. This lab introduces the use of time-aware evaluations: to evaluate performance decay of classifiers over time, as well as mitigation strategies including active learning and classification with rejection. You will have to install the [Tesseract Library](https://github.com/s2labres/tesseract-ml-release) (see instructions below).

* **Lab 03: Adversarial Attacks**. In this lab, you will learn how to generate "security evaluation curves" for adversarial attacks against a simple linear classifier. You will start with simple weight-driven attack for the linear SVM classifier on the DREBIN feature space, which you may compare and expand against PGD of the [secml library](https://secml.readthedocs.io/en/stable/tutorials/13-Android-Malware-Detection.html).

* **Lab 04: The impact of sampling bias**. There are more subtle aspects that may affect reliability of classification. In this lab, you will evaluate how considering different subsampling strategies may lead to inflated performance. For example, the origin marketplace (e.g., "Google Play") of an app plays a role in detection accuracy. This lab is related to the Android malware experiment in the "[Dos and Don'ts of Machine Learning in Computer Security](https://www.usenix.org/system/files/sec22summer_arp.pdf)" paper.

The `datasets` folder contains simple datasets and the instruction to download a larger dataset based on the DREBIN (NDSS 2014) feature space.

## Tesseract Library

In case you need to do time-aware evaluations with: 

* [Tesseract Library](https://github.com/s2labres/tesseract-ml-release)


To install, create a Python 3.10 environment. If the instructions of the repo do now work, consider trying:
```bash
python -m build
```

To register the virtual environment on a Python notebook:
```bash
python -m ipykernel install --user --name <env-name>
```
where the <env-name> variable matches the name of the environment.

Note: do NOT install from pip, because that is a different Tesseract library.

You can refer to this publication:

* Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, and Lorenzo Cavallaro , [TESSERACT: Eliminating experimental bias in malware classification across space and time](https://fabio.pierazzi.com/assets/pdf/tesseract.pdf), In Proc. of USENIX Security Symposium, 2019


## Android Malware Dataset (with DREBIN Feature Space)

These are preprocessed datasets that are already converted into feature matrices. They use the DREBIN feature abstraction. 

* [Download Dataset](https://emckclac-my.sharepoint.com/:u:/g/personal/k1802448_kcl_ac_uk/ERWQQfXF3MxCgPe1G4qGsWcBeGDsktcQ6kuXQbsbjGyy2g?e=amOhD4)

As you download the folder, you will have `extended-features.zip`. If you unzip it, you will have a folder `extended-features` with the following files: 
* `X.json`: the feature matrix (remember to drop the `sha256` column before running classification tasks)
* `y.json`: the labels (0 for goodware, 1 for malware)
* `meta.json`: contains some metadata information, including timestamps,
* `X-10k.p` and `f-10k.p` are smaller versions with the top-10k features (f.p is the vector of feature names)

You should put these files in `datasets/drebin/` folder in this repository. You can rename the `extended-features` folder into `drebin`. 

The Python functions for loading the dataset are in `libs.utils`. 

The features correspond to the apps from 2014--2018 used in this paper:
* Federico Barbero, Feargus Pendlebury, Fabio Pierazzi, and Lorenzo Cavallaro, [Transcending Transcend: Revisiting malware classification in the presence of concept drift](https://arxiv.org/abs/2010.03856) , In IEEE Symposium on Security and Privacy (S&P), 2022

To understand the meaning of the features, read the feature extraction process here: 
* [DREBIN (NDSS 2014)](https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_3_1.pdf)
