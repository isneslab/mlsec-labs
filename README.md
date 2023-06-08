# mlsec-lab

## Lab 01: Introduction

Learn how to use notebooks, and compute Precision, Recall, F1-Score and ROC Curves for malware detection.

## Lab 02: Use Tesseract-ML for time-aware evaluations

There are four major versions of the dataset: 
1. `extended-features-X` with `extended-features-y-updated`: Original dataset of TESSERACT (2014--2016), extended with the Transcendent dataset (2017--2018), with features re-extracted.
2. `extended-features-X-updated` with `extended-features-y-updated`: Same as (1) but with updated labels: VirusTotal was queried again, and the labels have been updated. 
3. `extended-features-X-updated-reduced-1k` and `extended-features-X-updated-reduced-1k`: Variant of dataset (2) with a pre-applied feature reduction of 10k and 1k features.

Compare the time-aware evaluations of the three classifiers. Install `tesseract` using `python setup.py install` after downloading the library. 

If time allow, try also impelmenting uncertainty sampling active learning with 1% re-training.
