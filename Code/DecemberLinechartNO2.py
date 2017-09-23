import pandas as pd
import numpy
import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='paragjuneja', api_key='ZBX9Wg9JXmnmlS0H2m8q')
py.sign_in('paragjuneja', 'ZBX9Wg9JXmnmlS0H2m8q')
import plotly.graph_objs as go

#Reading the csv file using pandas
df = pd.read_csv("hourly_NO2.csv")

df['From'] = df['From'].map(lambda x: str(x)[1:])
df['To'] = df['To'].map(lambda x: str(x)[1:])

df['FromTime'] = pd.to_datetime(df['Date'].str.cat(df['From'], sep=" "),format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['ToTime'] = pd.to_datetime(df['Date'].str.cat(df['To'], sep=" "),format='%Y-%m-%d %H:%M:%S', errors='coerce')

df['Concentration'] = df['Concentration'].apply(lambda x: pd.to_numeric(x, errors='ignore'))

#Calculating the average of all the stations
df1 = df[df['Station'] == 'ANANDVIHAR']
df_anand_dec = pd.DataFrame()
avg_anand_dec = []
for hour in range(24):
    df_anand_dec = df_anand_dec.append(df1[(df1['FromTime'].apply(lambda x: x.hour) == hour) & (df1['Month'] == 'Dec')])
avg_anand_dec = df_anand_dec.groupby('From')['Concentration'].mean()

df3 = df[df['Station'] == 'MANDIRMARG']
df_mandirmarg_dec = pd.DataFrame()
avg_mandirmarg_dec = []
for hour in range(24):
    df_mandirmarg_dec = df_mandirmarg_dec.append(df3[(df3['FromTime'].apply(lambda x: x.hour) == hour) & (df3['Month'] == 'Dec')])
avg_mandirmarg_dec = df_mandirmarg_dec.groupby('From')['Concentration'].mean()

df4 = df[df['Station'] == 'PUNJABIBAGH']
df_punjabibagh_dec = pd.DataFrame()
avg_punjabibagh_dec = []
for hour in range(24):
    df_punjabibagh_dec = df_punjabibagh_dec.append(df4[(df4['FromTime'].apply(lambda x: x.hour) == hour) & (df4['Month'] == 'Dec')])
avg_punjabibagh_dec = df_punjabibagh_dec.groupby('From')['Concentration'].mean()

df5 = df[df['Station'] == 'RKPURAM']
df_rkpuram_dec = pd.DataFrame()
avg_rkpuram_dec = []
for hour in range(24):
    df_rkpuram_dec = df_rkpuram_dec.append(df5[(df5['FromTime'].apply(lambda x: x.hour) == hour) & (df5['Month'] == 'Dec')])
avg_rkpuram_dec = df_rkpuram_dec.groupby('From')['Concentration'].mean()

df2 = df[df['Station'] == 'FARIDABAD']
df_faridabad_dec = pd.DataFrame()
avg_faridabad_dec = []
for hour in range(24):
    df_faridabad_dec = df_faridabad_dec.append(df2[(df2['FromTime'].apply(lambda x: x.hour) == hour) & (df2['Month'] == 'Dec')])
avg_faridabad_dec = df_faridabad_dec.groupby('From')['Concentration'].mean()

print 'Delhi - Faridabad for December'

avg_delhi_dec = []
avg_delhi_dec = list(numpy.array(avg_anand_dec)+numpy.array(avg_mandirmarg_dec)+numpy.array(avg_punjabibagh_dec)+numpy.array(avg_rkpuram_dec))
avg_delhi_dec = map(lambda x: x/4, avg_delhi_dec)
delhi_faridabad_dec = []
delhi_faridabad_dec = list(numpy.array(avg_delhi_dec)-numpy.array(avg_faridabad_dec))
print delhi_faridabad_dec

#Plotting the graph using pyplot
hours = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
trace0 = go.Scatter(
    x = hours,
    y = avg_delhi_dec,
    mode = 'lines',
    name = 'delhi_december'
)

trace1 = go.Scatter(
    x = hours,
    y = avg_faridabad_dec,
    mode = 'markers',
    name = 'faridabad_december'
)
data = [trace0, trace1]
layout = go.Layout(
    title='Hourly Analysis of NO2 for December',
    xaxis=dict(
        range=[1, 24],
        title='Hours',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
            )
         ),
    yaxis=dict(
        range=[0, 400],
        title='Mean NO2 Concentration in mg/m3',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
            )
        )
    )
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='HourlyAnalysisofNO2forDecember')






