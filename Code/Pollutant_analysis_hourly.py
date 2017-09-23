import pandas as pd
import numpy
import matplotlib.pyplot as plt


df = pd.read_csv("NO2.csv")

df['From'] = df['From'].map(lambda x: str(x)[1:])
df['To'] = df['To'].map(lambda x: str(x)[1:])
#print df['To']

df['FromTime'] = pd.to_datetime(df['Date'].str.cat(df['From'], sep=" "),format='%Y-%m-%d %H:%M:%S', errors='ignore')
df['ToTime'] = pd.to_datetime(df['Date'].str.cat(df['To'], sep=" "),format='%Y-%m-%d %H:%M:%S', errors='ignore')
print df.dtypes
print 'average ANAND VIHAR'

df1 = df[df['Station'] == 'ANANDVIHAR']
df_anand_dec = pd.DataFrame()
df_anand_jan = pd.DataFrame()
avg_anand_dec = []
avg_anand_jan = []
for hour in range(24):
    df_anand_dec = df_anand_dec.append(df1[(df1['FromTime'].apply(lambda x: x.hour) == hour) & (df1['Month'] == 'Dec')])
    df_anand_jan = df_anand_jan.append(df1[(df1['FromTime'].apply(lambda x: x.hour) == hour) & (df1['Month'] == 'Jan')])

print "Dec"

avg_anand_dec = df_anand_dec.groupby('From')['Concentration'].mean()

print "Jan"
avg_anand_jan = df_anand_jan.groupby('From')['Concentration'].mean()

print avg_anand_dec
print avg_anand_jan

print 'average MANDIR MARG'

df3 = df[df['Station'] == 'MANDIRMARG']
df_mandirmarg_dec = pd.DataFrame()
df_mandirmarg_jan = pd.DataFrame()
avg_mandirmarg_dec = []
avg_mandirmarg_jan = []
for hour in range(24):
    df_mandirmarg_dec = df_mandirmarg_dec.append(df3[(df3['FromTime'].apply(lambda x: x.hour) == hour) & (df3['Month'] == 'Dec')])
    df_mandirmarg_jan = df_mandirmarg_jan.append(df3[(df3['FromTime'].apply(lambda x: x.hour) == hour) & (df3['Month'] == 'Jan')])

avg_mandirmarg_dec = df_mandirmarg_dec.groupby('From')['Concentration'].mean()
avg_mandirmarg_jan = df_mandirmarg_jan.groupby('From')['Concentration'].mean()

print avg_mandirmarg_dec
print avg_mandirmarg_jan

print 'average PUNJABI BAGH'

df4 = df[df['Station'] == 'PUNJABIBAGH']
df_punjabibagh_dec = pd.DataFrame()
df_punjabibagh_jan = pd.DataFrame()
avg_punjabibagh_dec = []
avg_punjabibagh_jan = []

for hour in range(24):
    df_punjabibagh_dec = df_punjabibagh_dec.append(df4[(df4['FromTime'].apply(lambda x: x.hour) == hour) & (df4['Month'] == 'Dec')])
    df_punjabibagh_jan = df_punjabibagh_jan.append(df4[(df4['FromTime'].apply(lambda x: x.hour) == hour) & (df4['Month'] == 'Jan')])

avg_punjabibagh_dec = df_punjabibagh_dec.groupby('From')['Concentration'].mean()
avg_punjabibagh_jan = df_punjabibagh_jan.groupby('From')['Concentration'].mean()

print avg_punjabibagh_dec
print avg_punjabibagh_jan

print 'average R K PURAM'

df5 = df[df['Station'] == 'RKPURAM']
df_rkpuram_dec = pd.DataFrame()
df_rkpuram_jan = pd.DataFrame()
avg_rkpuram_dec = []
avg_rkpuram_jan = []
for hour in range(24):
    df_rkpuram_dec = df_rkpuram_dec.append(df5[(df5['FromTime'].apply(lambda x: x.hour) == hour) & (df5['Month'] == 'Dec')])
    df_rkpuram_jan = df_rkpuram_jan.append(df5[(df5['FromTime'].apply(lambda x: x.hour) == hour) & (df5['Month'] == 'Jan')])

avg_rkpuram_dec = df_rkpuram_dec.groupby('From')['Concentration'].mean()
avg_rkpuram_jan = df_rkpuram_jan.groupby('From')['Concentration'].mean()

print avg_rkpuram_dec
print avg_rkpuram_jan

print 'average faridabad'

df2 = df[df['Station'] == 'FARIDABAD']
df_faridabad_dec = pd.DataFrame()
df_faridabad_jan = pd.DataFrame()
avg_faridabad_dec = []
avg_faridabad_jan = []

for hour in range(24):
    df_faridabad_dec = df_faridabad_dec.append(df2[(df2['FromTime'].apply(lambda x: x.hour) == hour) & (df2['Month'] == 'Dec')])
    df_faridabad_jan = df_faridabad_jan.append(df2[(df2['FromTime'].apply(lambda x: x.hour) == hour) & (df2['Month'] == 'Jan')])

avg_faridabad_dec = df_faridabad_dec.groupby('From')['Concentration'].mean()
avg_faridabad_jan = df_faridabad_jan.groupby('From')['Concentration'].mean()
#print dfs
print avg_faridabad_dec
print avg_faridabad_jan

print 'Delhi - Faridabad for December'

avg_delhi_dec = []
avg_delhi_dec = list(numpy.array(avg_anand_dec)+numpy.array(avg_mandirmarg_dec)+numpy.array(avg_punjabibagh_dec)+numpy.array(avg_rkpuram_dec))
#print avg_delhi
avg_delhi_dec = map(lambda x: x/4, avg_delhi_dec)

delhi_faridabad_dec = []
delhi_faridabad_dec = list(numpy.array(avg_delhi_dec)-numpy.array(avg_faridabad_dec))


print delhi_faridabad_dec

print 'Delhi - Faridabad for January'

avg_delhi_jan = []
avg_delhi_jan = list(numpy.array(avg_anand_jan)+numpy.array(avg_mandirmarg_jan)+numpy.array(avg_punjabibagh_jan)+numpy.array(avg_rkpuram_jan))
#print avg_delhi
avg_delhi_jan = map(lambda x: x/4, avg_delhi_jan)

delhi_faridabad_jan = []
delhi_faridabad_jan = list(numpy.array(avg_delhi_jan)-numpy.array(avg_faridabad_jan))

print delhi_faridabad_jan

n_groups = 24
mean_dec = delhi_faridabad_dec
mean_jan = delhi_faridabad_jan

fig, ax = plt.subplots()

index = numpy.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, mean_dec, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Dec 2015')

rects2 = plt.bar(index + bar_width, mean_jan, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Jan 2016')


plt.xlabel('Hour of day')
plt.ylabel('Mean NO2 concentration in micrograms/m3')
plt.title('Delhi (minus) Faridabad')
plt.xticks(index + bar_width, ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'))
plt.legend()
plt.tight_layout()
plt.show()





