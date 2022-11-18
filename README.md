# New York Uber Rides Data Analysis Project

<p align="center">

## Instructions <br> 
>
<ol>
    <li> Code File name to execute : uberdata.ipynb </li>
    <li> Data is stored in Data folder and Contains csv files</li>
    <li> In order to run the code, please follow below instructions </li>
      <ul>
        <li> Step1: Install Python </li>
        <li> Step2: Set python interpreter </li>
        <li> Step3: Install Anaconda </li>
        <li> Step4: Install Jupyter Notebook </li>
        <li> Step5: Install Git </li>
        <li> Step6: Download the contents from git repo https://github.com/Adikharche19/uberrides_analysis and store it in local folder</li>
        <li> Step7: open terminal/command prompt, naviate to folder location where content was downloaded and type jupyter notebook </li>
        <li> Step8: jupyter notebook will be launched in browser. Select the uberdata.ipynb from folder and open the file </li>
        <li> Step9: Start executing the file by clicking on run button on each cell or go in Kernel option and click on Restart and Run all </li>
        <li> Step10: View the output cell by cell to understand the data flow and insights </li>
      </ul>
</ol>


## Business Problem: <br> 
>
<ul>
    <li> Uber management wants to know how to effectively manage their rental fleet on ground.  </li>
    <li> In order to do so, they would like to understand the trend of ride utilization by months, day of month, weekday of week and hour of the day across dispatch base location and also understand the usage by location on the map. </li>
<ul>

## Dataset:  <br> 
>
> Data is downloaded from below website:  <br> 
> https://www.kaggle.com/code/theoddwaffle/uber-data-analysis/data  <br> 


## Dataset Metadata/Meaning of each column in data: <br> 
>
<ol>
  <li> <strong>Data Record Count:</strong> 4,534,327 (4.5 Miliion)
  </li>
  <li> <strong>Number of Months:</strong> 6
  </li>
    <li> <strong>Month Name:</strong> April, May, June, July, Aug, Sep
  </li>
    <li> <strong>Year:</strong> 2014
  </li>
    <li> <strong>File Data separator:</strong> Comma
  </li>
  <li> <strong>Column Descriptions:</strong> These files are separated by Month and each has the following Columns:
    <ul>
      <li><strong>Date/Time :</strong> The date and time of the Uber pickup.</li>
      <li><strong>Lat :</strong> The latitude of the Uber pickup.</li>
      <li><strong>Lon :</strong> The longitude of the Uber pickup.</li>
      <li><strong>Base :</strong> The TLC base company code affiliated with the Uber pickup. Uber Dispatch Base Description are as following:
       <ul>
       <li><strong>B02512 :</strong> Unter.</li>
       <li><strong>B02598 :</strong> Hinter.</li>
       <li><strong>B02617 :</strong> Weiter</li>
       <li><strong>B02682 :</strong> Schmecken</li>
       <li><strong>B02764 :</strong> Danach-NY</li>
       </ul>
      </li>
    </ul>
  </li>
</ol>
        
## Coding Tools:
>
<ol>
  <li><strong>Version Control </strong> - Using Github
  </li>
  <li><strong>Coding Interface </strong> - Jupyter Notebook.
  </li>
  <li><strong> Python Libraries used </strong>- 
    <ul>
      <li><strong>For Data Preparation and Transformation</strong> - Pandas, Numpy, Calendar</li>
      <li><strong>For Data Visualization</strong> - Matplotli, Seaborn, Plotly, Folium</li>
    </ul>
  </li>
</ol>


## Overall Tasks Performed for NY Uber Ride Data Analysis:
>
<ol>
  <li><strong>Step 1 : Collecting Data</strong>
    <ul>
      <li>Get Data and Metadata from Kaggle for NY Uber Rides</li> <br>
    </ul>
  </li>
  <li><strong>Step 2 : Loading Data</strong>
    <ul>
      <li>Load the data from csv file into dataframe for futher transformation.</li> <br>
    </ul>
  </li>
  <li><strong>Step 3 : Cleanse Data</strong>
    <ul>
      <li>Clean the data by identifying and removing duplicates</li> <br>
    </ul>
  </li>
  <li><strong>Step 4 : Expand Data</strong>
    <ul>
      <li>Add more dervied columns to the data which will be used for grouping and visualization later</li> <br>
    </ul>
  </li>
  <li><strong>Step 5 : Data Grouping and Visualization</strong>
    <ul>
      <li>Group the data by same condition with which visualization needs to be created.</li> <br>
      <li>Visualizations are mentioned in below section.</li>
    </ul>
  </li>
</ol>


## Uber Rides Utilization Insights Calculated for:
>
<ol>
  <li><strong>Insight 1 : Total number of Uber Rides by Month Name</strong>
    <ul>
      <li>Determine Most and least Busiest Month </li>
      <li>Determine the nature of the trend</li><br>
    </ul>
  </li>
  <li><strong>Insight 2 : Total number of Uber Rides By Dispatch Locaton and Month</strong>
    <ul>
      <li>Determine the Base locations with Most and Least Ride Activities.</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>
  <li><strong>Insight 3 : Total number of Uber Rides By Month and Weekday</strong>
    <ul>
      <li>Determine Most and least Busiest Weekday and Month </li>
      <li>Determine the busiest days</li> <br>
    </ul>
  </li>
  <li><strong>Insight 4 : Total number of Uber Rides by WeekDay and Hour of the Day</strong>
    <ul>
      <li>Determine Most and least Busiest hour and range of it.</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>
  <li><strong>Insight 5 : Total number of Uber Rides By Dispatch Locaton and Hour</strong>
    <ul>
      <li>Determine Most and least Busiest hour by Dispatch Location and range of it. Identify the Bases with Most and Least activities by time range.</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>
  <li><strong>Insight 6 : Total number of Uber Rides By Hour</strong>
    <ul>
      <li>Determine Most busy hour of the day</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>
  <li><strong>Insight 7 : HeatMap - Total Number of Rides by Day of Month and Hour</strong>
    <ul>
      <li>Determine consistency in most and least busiest time range of the day for all days of month</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>  
  <li><strong>Insight 8 : HeatMap - Total Number of Rides by Weekday and Hour</strong>
    <ul>
      <li>Determine consistency in most and least busiest time range of the day for all days of week</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>  
  <li><strong>Insight 9 : HeadMap on Actual Map - Total Number of Rides by Weekday and Hour</strong>
    <ul>
      <li>Determine which part the NY is busiest.</li>
      <li>Determine the nature of the trend</li> <br>
    </ul>
  </li>  
</ol>



## Results:
> 
<p><strong>Finding 1:</strong></p>
<ol>
    <ul>
      <li>Busiest hour - 5 PM.  </li>
      <li>Most Busy hour range - 3 PM to 9 PM (Evening)</li>
      <li>Least Busy hour range - Midnight to 6 AM (Early Morning)</li> <br> 
    </ul> 
        <ul> <strong>Possible Reason:</strong>
                    <ul>
                        <li>For Most busiest hours 
                            <ul>
                                <li>People getting off their work.  </li>
                                <li>People going out for shopping   </li>
                            </ul>
                        </li>
                        <li>For least busiest hours
                            <ul>
                                <li>Few people travel after Midnight.  </li>
                            </ul>
                        </li>
                    </ul>
     </ul> 
</ol>

<p><strong>Finding 2:</strong></p>
<ol>
    <ul>
      <li>Most Busy Month - Sep 2014  </li>
      <li>Nature of Ride Trend - Increasing Steadily by Month</li> <br> 
    </ul> 
        <ul> <strong>Possible Reason:</strong> 
                    <ul>
                        <li>More people go out Fall season for outdoor activities which adds on the top of regular office busy time. </li>
                    </ul>
        </ul>            
</ol>


<p><strong>Finding 3:</strong></p>
<ol>
    <ul>
      <li>Most Busy Day - Thursday followed by Friday  </li>
      <li>Trend of rides is consistant through all the days of the week</li> <br> 
    </ul> 
        <ul> <strong>Possible Reason:</strong> 
                    <ul>
                        <li>As weekend approaches, more people start go out for activities. </li>
                    </ul>
        </ul>            
</ol>



<p><strong>Finding 4:</strong></p>
<ol>
    <ul>
      <li>Most Busiest Dispatch Base Location - Weiter </li>
      <li>Least Busiest Dispatch Base Location - Unter </li>
      <li>Most Consistent Dispatch Base Location - Hinter </li>
      <li>Rides Trend is consistent for all the Dispatch locations for most number of hours </li> <br> 
    </ul> 
        <ul> <strong>Possible Reason:</strong>
                    <ul>
                        <li>Possibly Weiter and Hinter is able to manage the demand more effectively.
                        </li>
                    </ul>
        <ul>
</ol>



<p><strong>Finding 5:</strong></p>
<ol>
    <ul>
      <li>Most Busy Location - Mid-Town Manhattan followed by Upper Manhatten  </li> <br> 
    </ul> 
        <ul> <strong>Possible Reason:</strong> 
                    <ul>
                        <li>Busy area with office and tourist spot </li>
                    </ul>
        </ul>            
</ol>


## Overall Decision Making Facts:
>

<ul>
    <li> Fleet Needs to be Managed effectively at Morning 8 AM and evening hours to meet the demand.   </li>
    <li> More vehicles needed as year progresses due to higher demand.    </li>
    <li> Fleet Needs to be Managed effectively at Morning 8 AM and evening hours to meet the demand.   </li>
    <li> Base locations Weiter, Hinter and Schmecken have  managed increased demand consistenly throughout the year.   </li>
<ul>