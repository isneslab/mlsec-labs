# ML Security Labs

## Setup

It is better to use Python 3.10 as we are still figuring out a compatibility with the Tesseract library.

I would also advise to create a Python virtual environment for these labs, using Python 3.10: see [here](https://docs.python.org/3/library/venv.html) for a guide on virtual environments. 

## Labs overview

This github workspace contains some example to get acquainted with the use of Machine Learning for Systems Security and Malware Detection. 

* **Lab 01: Malware detection with Machine Learning**. This lab is a warmer to introduce on the use of notebooks, and to compute the main performance metrics. 

* **Lab 02: Time-aware evaluations**. This lab introduces the use of time-aware evaluations. 

* **Lab 03: Adversarial Attacks**. A simple weight-driven attack for the linear SVM classifier on DREBIN feature space.

* **Lab 04: Sampling Bias**. In this exercise, you will see how training on apps from different marketplaces, how this affects results.

The `datasets` folder contains simple datasets and the instruction to download a larger dataset based on the DREBIN (NDSS 2014) feature space.

## Tesseract Library

In case you need to do time-aware evaluations with: 

* [Tesseract Library](https://github.com/s2labres/tesseract-ml-release)

You can refer to this publication:

* Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, and Lorenzo Cavallaro , [TESSERACT: Eliminating experimental bias in malware classification across space and time](https://fabio.pierazzi.com/assets/pdf/tesseract.pdf), In Proc. of USENIX Security Symposium, 2019

To install, create a Python 3.10 environment. If the instructions of the repo do now work, consider trying:
```bash
python -m build
```

To register the virtual environment on a Python notebook:
```bash
python -m ipykernel install --user --name <env-name>
```
where the <env-name> variable matches the name of the environment. 

