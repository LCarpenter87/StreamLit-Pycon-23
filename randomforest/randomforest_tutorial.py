#######
#
# Streamlit Hyperparameter Tool
# Creates a sidebar form that allows the user to tweak the hyperparameters
# of an SKLearn Random Forest Classifier
#
# Created for PyCon USA 2023 - Streamlit Tutorial with Lisa Carpenter
#
#######

import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import helpful as hf
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, precision_recall_curve, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
import timeit


@st.cache_data
def prepare_data(train, test):
    """ Read in the data, and take the first column as the target variable """
    X_train = pd.read_csv(train, header=None)
    X_test = pd.read_csv(test,  header=None)
    y_train = X_train.pop(0)
    y_test = X_test.pop(0)
    return X_train, X_test, y_train, y_test

#######
#
# Start execution and creation of the webapp
#
#######

# Configure the page and bring in the data.
st.set_page_config(page_title="Hyperparameter Tuner", layout="wide")
st.title("Hyperparameter Tuner")
X_train, X_test, y_train, y_test = prepare_data(r'data\dota2Train.csv',r'data\dota2Test.csv')

#######
# TUTORIAL - 
# CREATE THE INPUTS!
#######


## We are going to create the inputs for these hyperparameters.

hyperparameters = {
        "random_state": 42,
        "criterion": 'gini',
        "n_estimators": 25,
        "max_depth": 25,
        "min_samples_split": 50,
        "min_samples_leaf": 50,
        "max_features": 25,
        "bootstrap": True,
        "n_jobs": -1,
        "max_samples": 0.8,
    }

forest = RandomForestClassifier(**hyperparameters)
train_score, test_score, precision, recall, f1, confusion, seconds_run, fpr, tpr, roc_auc =  hf.return_scores(forest, X_train, X_test, y_train, y_test)

st.write(train_score) 
st.write(test_score) 
st.write(precision) 
st.write(recall) 
st.write(f1) 
st.write(seconds_run)