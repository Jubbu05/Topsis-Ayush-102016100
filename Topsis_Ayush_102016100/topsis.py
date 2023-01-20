import numpy as np
import pandas as pd
import math
import sys
import logging

def topsis_score(inputFileName,weights,impact,outputFileName):
    try:
        df=pd.read_csv(inputFileName)
        original_df = df.copy(deep=True)
    except FileNotFoundError:
        logging.error("Input file not found")
        return
        
    if len(df.columns)<3:
        logging.error("Input file has less than 3 columns")
        return

    for i in range(1,len(df.columns)):
        try:
            df.iloc[:,i]=pd.to_numeric(df.iloc[:,i])
        except ValueError:
            logging.warning(f"Non-numeric value in {i}th column")
            return

    rows = len(df) # rows

    columns = len(df.columns)

    weights=weights
    if ',' not in weights:
        logging.error("Weights should be separated by ','")
        return

    try:
        weights=pd.to_numeric(weights.split(','))
    except ValueError:
        logging.error("Non numeric values in weights")
        return
        
    impact=impact
    if ',' not in impact:
        logging.error("Impacts should be separated by ','")
        return
    impact = impact.split(',')

    for i in impact:
        if i!='+' and i!='-':
            logging.error("Impact must contain '+' or '-'")
            return

    if columns-1!=len(weights) and columns-1!=len(impact):
        logging.error("Number of weights or impacts are not same as number of columns")
        return
        

    for i in range(1,columns):
        temp = 0
        for j in range(rows):
            temp = temp + df.iloc[j,i]**2
        temp=temp**0.5
        for j in range(rows):
            df.iloc[j,i]=df.iloc[j,i]/temp
            df.iloc[j,i]=df.iloc[j,i]*weights[i-1]


    df_new = df.drop(df.columns[0],axis=1)
    ideal_best_array = df_new.max().values
    ideal_worst_array = df_new.min().values

    best_worst_array=[]
    for i in range(len(ideal_best_array)):
        if impact[i]=='+':
            best_worst_array.append([ideal_best_array[i],ideal_worst_array[i]])
        else:
            best_worst_array.append([ideal_worst_array[i],ideal_best_array[i]])
            
    best_worst_array=np.array(best_worst_array)
    best_worst_array


    distance_pos=[]
    distance_neg=[]
    score = []

    for i in range(rows):
        temp_pos=0
        temp_neg=0
        
        for j in range(len(df_new.columns)):
            
            temp_pos=temp_pos + (best_worst_array[j,0]-df_new.iloc[i,j])**2
            temp_neg = temp_neg + (best_worst_array[j,1]-df_new.iloc[i,j])**2
        temp_pos=temp_pos**0.5
        temp_neg=temp_neg**0.5
        distance_pos.append(temp_pos)
        distance_neg.append(temp_neg)
        score.append(temp_neg/(temp_neg+temp_pos))
    # df['distance_positive']=distance_pos
    # df['distance_negative']=distance_neg
    df['Topsis score']=score
    df['Rank']=df['Topsis score'].rank(ascending=False)
    df=df.astype({'Rank':int})
    original_df['Topsis score']=df['Topsis score']
    original_df['Rank']=df['Rank']
    original_df
    original_df.to_csv(outputFileName,index=False)
    print("Output file generated")

