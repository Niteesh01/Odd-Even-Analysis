import pandas as pd
import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='paragjuneja', api_key='ZBX9Wg9JXmnmlS0H2m8q')
import plotly.graph_objs as go

# Import the data file
df = pd.read_csv("monthly_NO2.csv")

# Extracting the monthly data for Faridabad
df_faridabad = df[df['Station'] == "FARIDABAD"]
df_faridabad = df_faridabad['Concentration']

# Extracting the monthly data for Delhi
df_delhi = df[df['Station'] != "FARIDABAD"]
df_delhi_mean = df_delhi.groupby('Month')['Concentration'].mean()


df_delhi_mean_list = []
df_delhi_mean_list.append(df_delhi_mean['Jun'])
df_delhi_mean_list.append(df_delhi_mean['Jul'])
df_delhi_mean_list.append(df_delhi_mean['Aug'])
df_delhi_mean_list.append(df_delhi_mean['Sep'])
df_delhi_mean_list.append(df_delhi_mean['Oct'])
df_delhi_mean_list.append(df_delhi_mean['Nov'])
df_delhi_mean_list.append(df_delhi_mean['Dec'])
df_delhi_mean_list.append(df_delhi_mean['Jan'])

print "Mean NO2 Concentrations for individual months in mg/m3"
print df_delhi_mean_list

# List of Months that are to be considered
months_list = ['JUN15', 'JUL15', 'AUG15', 'SEP15', 'OCT15', 'NOV15', 'DEC15', 'JAN16']


#Plotting the LineGraph

trace0 = go.Scatter(
    x = months_list,
    y = df_faridabad,
    mode = 'lines',
    name = 'Faridabad'
)

trace1 = go.Scatter(
    x = months_list,
    y = df_delhi_mean_list,
    mode = 'lines',
    name = 'Delhi'
)

data = [trace0, trace1]

layout = go.Layout(
     barmode='group',
        title='Mean Monthly Concentration Analysis For NO2',
    xaxis=dict(
        title='Months',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Mean NO2 Concentration in mg/m3',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Mean_Monthly_Concentration_Analysis_For_NO2')