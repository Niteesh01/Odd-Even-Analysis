***************************
Project:-Odd Even Analysis
***************************
************
Participants
************

Akurati, Niteesh Kumar, F16-IG-3001, akuratin, akuratin@umail.iu.edu

Juneja, Parag, F16-IG-3009, paragjuneja, pjuneja@iu.edu

***************************
Description of the problem
***************************

There are total of eight program files one for each visualization.The flow of each program is mentioned below:-
###############################################################################################################
.. note::  All the code and datasets should reside in one folder

- barchart_NO2.py :-This program uses hourly_NO2.csv file and computes averages of all the stations and 
  displays the difference of averages for Delhi as a whole and Faridabad in the form of bar chart in plotly



- barchart_PM25.py :-This program uses hourly_PM25.csv file and computes averages of all the stations and 
  displays the difference of averages for Delhi as a whole and Faridabad in the form of bar chart in plotly

- monthly_NO2.csv :-This program uses monthly_NO2.csv file and computes averages of all the stations and 
  displays the averages for Delhi as a whole for a period of 6 months on a line chart in plotly.

- monthly_PM25.csv :-This program uses monthly_PM25.csv file and computes averages of all the stations and 
  displays the averages for Delhi as a whole for a period of 6 months on a line chart in plotly.

- DecemberLinechartNO2.py :-This program uses hourly_NO2.csv file and computes averages of all the  
  stations and displays the averages for Delhi vs Fariadabad on a line chart in plotly.
    
- DecemberLinechartPM25.py :-This program uses hourly_PM25.csv file and computes averages of all the  
  stations and displays the averages of December for Delhi vs Fariadabad on a line chart in plotly.

- JanuaryLinechartNO2.py :-This program uses hourly_NO2.csv file and computes averages of all the  
  stations and displays the averages of January for Delhi vs Fariadabad on a line chart in plotly.

- JanuaryLinechartPM25.py :-This program uses hourly_PM25.csv file and computes averages of all the  
  stations and displays the averages of January for Delhi vs Fariadabad on a line chart in plotly.


***************************
Description of the Data
***************************

The dataset used for the project are:- The datasets we used are pollutants(NO2 and PM2.5) data downloaded from the CPCB(central pollution for control board) website. The datasets are small in size hence uploaded in the code repository of the project folder
#################################################################################################################################################################################################################################################################


- barchart_NO2.py 

- barchart_PM25.py 

- monthly_NO2.csv 

- monthly_PM25.csv

All the datasets are continuous data downloaded from CPCB(central pollution for control board) website.     The datasets are downloaded for a range of stations based on pollutants necessary and the data is hourly

************************************************************************************************
Description of the Data Cleanup or extraction.
************************************************************************************************

All the datasets here are manually preprocessed
################################################
In the hourly datasets( hourly_NO2.csv and hourly_PM25.csv) the hourly data for all the stations for the pollutants PM2.5 and NO2 are downloaded individually as allowed by the website. The data from all these stations are further combined into one single file manually. All the columns are removed accordingly
In the monthly datasets(monthly_NO2.csv and monthly_PM25.csv) the mean average data for all the stations for the pollutants PM2.5 and NO2 are downloaded individually as allowed by the website.The data from all these stations are further combined into one single file manually. All the columns are removed accordingly.

**************
Program output
**************

- `barchart_NO2.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/barchart_NO2.py>`_ :-
  .. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/hourly_NO2.jpg
  .The above code displays the difference of averages of NO2 concentration for Delhi vs Faridabad as a   
  bar-chart

-  `barchart_PM25.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/barchart_PM25.py>`_
   :-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/hourly_PM25.jpg.The     
   above code displays the difference of averages of PM25 concentration for Delhi vs Faridabad as a   
   bar-chart
- `DecemberLinechartNO2.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/DecemberLinechartNO2.py>`_:-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/Linechart_December_NO2.jpeg.The above code displays the  averages of NO2 concentration for Delhi vs Faridabad for December as a line-chart
- `DecemberLinechartPM25.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/DecemberLinechartPM25.py>`_:-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/Linechart_December_PM25.jpeg.The above code displays the  averages of PM2.5 concentration for Delhi vs Faridabad for December as a line-chart
- `JanuaryLinechartNO2.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/JanuaryLinechartNO2.py>`_:-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/Linechart_January_NO2.jpeg.The above code displays the  averages of NO2 concentration for Delhi vs Faridabad for January as a line-chart
- `JanuaryLinechartPM25.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/JanuaryLinechartPM25.py>`_.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/Linechart_January_PM25.jpeg.The above code displays the  averages of PM25 concentration for Delhi vs Faridabad for January as a line-chart
- `linechart_monthlyanalysis_NO2.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/linechart_monthlyanalysis_NO2.py>`_:-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/monthly_NO2.jpg. The above code displays the monthly averages of NO2 concentration for Delhi vs Faridabad for a period of 6 months as a line-chart
- `linechart_monthlyanalysis_PM25.py <https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/code/linechart_monthlyanalysis_PM25.py>`_:-.. image:: https://gitlab.com/cloudmesh_fall2016/project-036/blob/master/report/monthly_PM25.jpg. The above code displays the monthly averages of PM25 concentration for Delhi vs Faridabad for a period of 6 months as a line-chart















