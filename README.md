# New York Uber Rides Data Analysis Project

<p align="center">

## Business Problem: <br> 

> Uber management wants to know how to effectively manage their rental fleet on ground. 
> In order to do so, they would like to understand the trend of ride utilization by months, day of month, weekday of week and hour of the day across dispatch base location and also understand the usage by location on the map.


## Dataset:  <br> 
> Data is downloaded from below website:  <br> 
> https://www.kaggle.com/code/theoddwaffle/uber-data-analysis/data  <br> 


## Dataset Metadata/Meaning of each column in data: <br> 
>
        - Data Record Count: 4,534,327 (4.5 Miliion)
        - Number of Months: 6
        - Month Name: April, May, June, July, Aug, Sep
        - Year: 2014
        - File Data separator: Comma
        - Column Descriptions:
                These files are separated by Month and each has the following Columns:
                    •	Date/Time : The date and time of the Uber pickup.
                    •	Lat : The latitude of the Uber pickup.
                    •	Lon : The longitude of the Uber pickup.
                    •	Base : The TLC base company code affiliated with the Uber pickup.
                            
                            The Base codes description are as follows:
                                B02512 : Unter
                                B02598 : Hinter
                                B02617 : Weiter
                                B02682 : Schmecken
                                B02764 : Danach-NY

## Coding Tools:
>
        - Version Control - Using Github
        - Coding Interface - Jupyter Notebook.
        - Python Libraries used - 
                1. For Data Preparation and Transformation - Pandas, Numpy, Calendar
                2. For Data Visualization - Matplotli, Seaborn, Plotly, Folium



## Overall Tasks Performed for NY Uber Ride Data Analysis:
>
        - Step 1 - Collecting Data
                Get Data and Metadata from Kaggle for NY Uber Rides
        - Step 2 - Loading Data
                Load the data from csv file into dataframe for futher transformation.
        - Step 3 - Cleanse Data
                Clean the data by identifying and removing duplicates
        - Step 4 - Expand Data
                Add more dervied columns to the data which will be used for grouping and visualization later
        - Step 5 - Data Grouping and Visualization
                Group the data by same condition with which visualization needs to be created.
                Visualizations are mentioned in below section.



## Uber Rides Utilization Insights Calculated for:
>
        - Insight 1 - Total number of Uber Rides by Month Name
                Determine Most and least Busiest Month 
                Determine the nature of the trend

        - Insight 2 - Total number of Uber Rides By Dispatch Locaton and Month
                Determine the Base locations with Most and Least Ride Activities.
                Determine the nature of the trend

        - Insight 3 - Total number of Uber Rides By Month and Weekday
                Determine Most and least Busiest Weekday and Month 
                Determine the busiest days 

        - Insight 4 - Total number of Uber Rides by WeekDay and Hour of the Day
                Determine Most and least Busiest hour and range of it.
                Determine the nature of the trend

        - Insight 5 - Total number of Uber Rides By Dispatch Locaton and Hour
                Determine Most and least Busiest hour by Dispatch Location and range of it. Identify the Bases with Most and Least activities by time range.
                Determine the nature of the trend

        - Insight 6 - Total number of Uber Rides By Hour
                Determine Most busy hour of the day
                Determine the nature of the trend

        - Insight 7 - HeatMap - Total Number of Rides by Day of Month and Hour
                Determine consistency in most and least busiest time range of the day for all days of month
                Determine the nature of the trend

        - Insight 8 - HeatMap - Total Number of Rides by Weekday and Hour
                Determine consistency in most and least busiest time range of the day for all days of week
                Determine the nature of the trend

        - Insight 9 - HeadMap on Actual Map - Total Number of Rides by Weekday and Hour
                Determine which part the NY is busiest.



## Results:
>
        - Finding 1:
                    Busiest hour - 5 PM. 
                    Most Busy hour range - 3 PM to 9 PM (Evening). 
                    Least Busy hour range - Midnight to 6 AM (Early Morning)
            Possible Reason:
                For Most busiest hours
                    People getting off their work.
                    People going out for shopping 
                For least busiest hours
                    Few people travel after Midnight.

        - Finding 2 : 
                    Most Busy Month - Sep 2014
                    Nature of Ride Trend - Increasing Steadily by Month
            Possible Reason:
                    More people go out Fall season for outdoor activities which adds on the top of regular office busy time.

        - Finding 3 :
                    Most Busy Day - Thursday followed by Friday
                    Trend of rides is consistant through all the days of the week
            Possible Reason:
                As weekend approaches, more people start go out for activities.

        - Finding 4 :
                    Most Busiest Dispatch Base Location - Weiter
                    Least Busiest Dispatch Base Location - Unter
                    Most Consistent Dispatch Base Location - Hinter
                    Rides Trend is consistent for all the Dispatch locations for most number of hours
            Possible Reason:
                    Possibly Weiter and Hinter is able to manage the demand more effectively.
        
        - Finding 5:
                    Most Busy Location - Mid-Town Manhattan followed by Upper Manhatten
            Possible Reason:
                    Busy area with office and tourist spots.

## Overall Decision Making:
>
        - Fleet Needs to be Managed effectively at Morning 8 AM and evening hours to meet the demand. 
        - More vehicles needed as year progresses due to higher demand. 
        - Base locations Unter and Danach needs more attention to increase numnber of rides. Base locations Weiter, Hinter and Schmecken have  managed increased demand consistenly throughout the year.