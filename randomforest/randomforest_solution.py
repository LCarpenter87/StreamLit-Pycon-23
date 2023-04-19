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

# inputs for the sidebar 
with st.sidebar.form(key="hyperparameters_form"):

    submit_button = st.form_submit_button("Click here to run model")    
    col1, col2 = st.columns(2)
    n_jobs = col1.slider("# of Jobs", min_value=-1, max_value=8, value = -1, help='How many cores to use, -1 is all')
    n_estimators = col2.slider("# of Estimators", min_value=1, max_value=250, value=25, help="How many decision trees in forest")  
    col3, col4 = st.columns(2)    
    criterion = col3.selectbox("Criterion", options=["gini", "entropy", "log_loss"], help="Method for decision logic")
    max_features = col4.selectbox("Max Features", options=["sqrt", "log2", None])
    max_depth = st.slider("Max Depth", min_value=1, max_value=50, value = 25, help="Max level of decisions per tree")
    max_samples = st.slider("% of Samples", min_value=0.01, max_value=1.0, step=0.01, value= 0.8, help="% of data to use in each tree")
    min_samples_split, min_samples_leaf = st.columns(2)
    min_samples_split = min_samples_split.slider("Min Samples Split", min_value=1, max_value=10000, value = 50, help="Min # of samples to split")
    min_samples_leaf = min_samples_leaf.slider("Min Samples Leaf", min_value=1, max_value=10000, value = 50, help="Min samples in a leaf node")
    
    bootstrap = st.checkbox("Bootstrap", value=True, help = 'Random Sampling with replacement of data')
    

if submit_button:
    hyperparameters = {
        "random_state": 42,
        "criterion": criterion,
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "max_features": max_features,
        "bootstrap": bootstrap,
        "n_jobs": n_jobs,
        "max_samples": max_samples,
    }
    
    if not hyperparameters['bootstrap']:
        hyperparameters['max_samples'] = None

    forest = RandomForestClassifier(**hyperparameters)
    train_score, test_score, precision, recall, f1, confusion, seconds_run, fpr, tpr, roc_auc =  hf.return_scores(forest, X_train, X_test, y_train, y_test)

    st.write(f'Model ran in: {round(seconds_run,4)} seconds')
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric(label='Training Score', value = hf.round_p(train_score))
    col2.metric(label='Test Score', value= hf.round_p(test_score), delta= hf.round_p(test_score-train_score))
    col3.metric(label='Precision', value = hf.round_p(precision))
    col4.metric(label ='Recall', value = hf.round_p(recall))
    col5.metric(label = 'F1', value = hf.round_p(f1))
    
    col6, col7 = st.columns(2)
    col6.altair_chart(hf.produce_confusion(confusion), use_container_width = True)
    col7.altair_chart(hf.produce_roc(fpr, tpr, roc_auc), use_container_width=True)