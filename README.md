---                                                                             
layout: post
title:  Project: Voomerang 
date: 2020-04-01T22:55:48
author: cerberus
summary: >
Project is aimed at detecting phishing emails  
categories: Projects 
thumbnail: 
tags:
 -  - 

---


# Overview
  Project Voomerang is aimed at stopping phishing emails by using machine learning. A [Naive Bayes classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html) will be used to read the email content and predict if the email is phishing or not based on the data you feed it.
  
# Requirements
>  VMware or Virtual Box

>  8 GB RAM

>  30 GB HDD/SSD (min.)

>  Python 3.7.x

### steps
 If downloading from source do a gitclone and use pip3 to install requirements by running command listed below

```
# pip3
run pip3 install -r requirements.txt
# if pip3 not installed
apt-update
apt-get install python3-pip
```
[Voomerang gitclone](https://www.youtube.com/watch?v=Tf1Zdledf8c)


## Demo 
[Voomerang demo](https://www.youtube.com/watch?v=HrRXbCytF5E)


## References
  
[Multinomial Naive Bayes Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)

[Naive Bayes Classifier](https://www.geeksforgeeks.org/naive-bayes-classifiers/)

[Reading emails with Python](https://docs.python.org/3/library/email.examples.html)

[Spam filtering with Naive Bayes](https://towardsdatascience.com/spam-filtering-using-naive-bayes-98a341224038)

