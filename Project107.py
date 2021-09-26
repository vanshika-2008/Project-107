import csv
import pandas as pds
import plotly.express as px

DataFrame = pds.read_csv('data.csv')
Mean = DataFrame.groupby(['student_id','level'],as_index = False)['attempt'].mean()
Plot = px.scatter(Mean,x = 'student_id', y= "level",size='attempt',color='attempt')
Plot.show()