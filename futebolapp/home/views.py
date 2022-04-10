from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
import numpy as np
import pandas as pd
import json

data = {}
df = pd.read_csv('templates/static/data/BRA.csv')

def HomePageView(request, page=None):  
  registers = 10
  if((page is None) | (page == 1)):
    page_number = 1
    start = 0
    end = registers
  else:
    page_number = int(page)
    start = registers * page_number - registers
    end = start + registers
  paginator = Paginator(df,registers)
  data['paginator'] = paginator.get_page(page_number)
  
  data["dados"] = df\
    .drop(['Country','League','Season','Time','MaxH','MaxD','MaxA','AvgH','AvgD','AvgA'], axis=1)\
    .iloc[start:end]\
    .to_html(index=False,classes=['table','table-striped','mt-3'])
  data['timesFilter'] = df['Home'].sort_values().unique()
    
  return render (request, 'home/index.html', data)

def timesFilter(request):
  if request.body:
    field = json.loads(request.body.decode('utf-8'))
    search = field['times']
    df2 = df
    data['dados']=df2[df2['Home'].str.contains(search)]\
      .drop(['Country','League','Season','Time','MaxH','MaxD','MaxA','AvgH','AvgD','AvgA'],axis=1)\
      .head()\
      .to_html(index=False,classes=['table','table-striped','mt-3'])
    return JsonResponse({'data':data['dados']})