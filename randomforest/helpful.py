#######
#
# Helpful Functions
# Cleaning up functions to make it easier for the streamlit tutorial! 
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


def round_p(n):
    """ Given n, round it and return it formatted with a % """
    return f'{round(n*100,2)}%'

def return_scores(forest, X_train, X_test, y_train, y_test):
    """ Fit the forest model, and return metrics and confusion matrix"""
    start_time = timeit.default_timer()
    forest.fit(X_train, y_train)
    y_scores = forest.predict_proba(X_test)[:, 1]
    y_pred = forest.predict(X_test)
    train_score = forest.score(X_train, y_train)
    test_score = forest.score(X_test, y_test)
    precision = precision_score(y_true= y_test, y_pred=y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    confusion = confusion_matrix(y_true = y_test, y_pred=y_pred)
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    roc_auc = auc(fpr, tpr)
    return train_score, test_score, precision, recall, f1, confusion, timeit.default_timer() - start_time, fpr, tpr, roc_auc

def produce_confusion(cm):
    """" Given the confusion matrix array output from SKLearn, create an Altair heatmap """

    data = pd.DataFrame({
        'Actual': np.array(['Positive', 'Negative', 'Positive', 'Negative']),
        'Predicted': np.array(['Positive', 'Negative', 'Negative', 'Positive']),
        'Count': np.array([cm[0, 0], cm[1, 1], cm[1, 0], cm[0, 1]]),
        'Color': np.array(['#66BB6A', '#66BB6A', '#EF5350', '#EF5350'])  # Customize the hex colors here
    })

    # Create a heatmap with appropriate colors
    heatmap = alt.Chart(data).mark_rect().encode(
        x='Actual:N',
        y='Predicted:N',
        color=alt.Color('Color:N', scale=None, legend=None),
        tooltip=['Actual:N', 'Predicted:N', 'Count:Q']
    ).properties(
        title='Confusion Matrix',
        width=300,
        height=350
    )

    # Add text to display the count
    text = alt.Chart(data).mark_text(fontSize=16, fontWeight='bold').encode(
        x='Actual:N',
        y='Predicted:N',
        text='Count:Q',
        color=alt.condition(alt.datum.Color == '#EF5350', alt.value('white'), alt.value('black'))
    )

    # Combine heatmap and text layers
    chart = (heatmap + text).configure_title(fontSize=18, fontWeight='bold', anchor='middle')

    return chart

def produce_roc(fpr, tpr, roc_auc):
    roc_data = pd.DataFrame({"False Positive Rate": fpr, "True Positive Rate": tpr})
    roc_chart = alt.Chart(roc_data).mark_line().encode(
        x=alt.X("False Positive Rate", title="False Positive Rate (FPR)"),
        y=alt.Y("True Positive Rate", title="True Positive Rate (TPR)")
    ).properties(title=f"ROC Curve (AUC = {roc_auc:.2f})")    
    return roc_chart