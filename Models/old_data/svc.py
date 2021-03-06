#!/usr/bin/env python3

import pandas as pd
from sklearn import svm
from evaluations import Evaluation

def extractData(fileName, exclude):
    df = pd.read_csv("../team_data/" + fileName)
    columnsSelected = list(df.columns.values)
    columnsSelected = columnsSelected[2:25]
    if exclude is not None:
        columnsSelected.pop(exclude)
    data = df.loc[:, list(columnsSelected)]
    labels = df["Playoff"]
    return data, labels

if __name__ == '__main__':
    # read team data for a given year
    teamData = pd.read_csv('../team_data/teamFiles.csv')
    exclusions = [None]
    exclusions += list(range(0,23))
    for exclude in exclusions:
        print(exclude)
       	for index, year in teamData.iterrows():
            train_data, train_label = extractData(year["Year1"], exclude)
            test_data, test_label = extractData(year["Year2"], exclude)
            clf = svm.SVC()
            y_pred = clf.fit(train_data,train_label)
            predictions = clf.predict(test_data)
            eval= Evaluation(predictions, test_label)
            # print(eval.getAccuracy())
            # print(eval.getPrecision())
            # print(eval.getRecall())
            # print(eval.getF1())
            # print("------------------------------")
            #
