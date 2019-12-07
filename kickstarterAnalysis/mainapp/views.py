from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


def index(request):
    input_file = "./ks-projects-201612.csv"
    data_frame = pd.read_csv(input_file, 'utf-8', header=0, index_col=0, engine='python')
    print(data_frame.columns)
    # data_frame.sort_values(by=['goal'], axis=0)
    # corr_heatmap = sns.heatmap(data = data_frame.corr(), annot=True, fmt = '.2f', linewidths=.5, cmap='Blues')
    # corr_heatmap.savefig("output.png")
    return render(request, 'index.html', {'dataframe' : data_frame})
# Create your views here.
