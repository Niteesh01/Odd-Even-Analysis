import pandas as pd
import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='Niteesh', api_key='bSrAzhqaQbMzL3r2Q3pl')
import plotly.graph_objs as go




df = pd.read_csv("NO2LIne.csv")
print df.dtypes

df_faridabad = df[df['Station'] == "FARIDABAD"]
df_faridabad = df_faridabad['Concentration']
#print df_faridabad


df_delhi = df[df['Station'] != "FARIDABAD"]
df_delhi_mean = df_delhi.groupby('Month')['Concentration'].mean()
print df_delhi_mean


df_delhi_mean_list = []
df_delhi_mean_list.append(df_delhi_mean['Jun'])
df_delhi_mean_list.append(df_delhi_mean['Jul'])
df_delhi_mean_list.append(df_delhi_mean['Aug'])
df_delhi_mean_list.append(df_delhi_mean['Sep'])
df_delhi_mean_list.append(df_delhi_mean['Oct'])
df_delhi_mean_list.append(df_delhi_mean['Nov'])
df_delhi_mean_list.append(df_delhi_mean['Dec'])
df_delhi_mean_list.append(df_delhi_mean['Jan'])
print df_delhi_mean_list




months_list = ['JUN15', 'JUL15', 'AUG15', 'SEP15', 'OCT15', 'NOV15', 'DEC15', 'JAN16']

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


# Plot and embed in ipython notebook!
fig = go.Figure(data=data)
py.plot(fig, filename='Parag_monthly')