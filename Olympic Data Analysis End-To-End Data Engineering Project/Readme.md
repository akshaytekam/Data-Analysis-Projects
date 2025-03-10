# Olympic Data Analysis End-To-End Data Engineering Project
### Project Flow:-
Data Source --> Data Factory (Data Integration) --> Data Lake Gen2 (Raw Data Storge) --> Azure Databricks (Transformation) --> Data Lake Gen2 (Transformed Data) --> Azure Synapse Analytics --> Power BI (Dashboard)

**Note:- We can make use of Azure Synapse service only and do all the task there, or we can make use of different services listed above.**

Once we enter into the Microsoft Azure, we first create the Azure Storage Account. Inside the Storage Account we'll create a Container and inside the Containe we'll create two folders/directory named as (raw-data, transformed-data).
This is what the Data Lake is. Now we go to the Azure Factory and create the new data factory. Once created just Launch it. Here we can create the pipeline to extract data from different sources and upload that data to the target locations.
Now here after creating a pipeline we give it a name like (data-ingestion). The first activity we do in this pipeline is that we copy the data from source and put it into destination(sink). For doing that we need to first link out
source to the data factory. So put all the data on github and copy the Raw URL from github to the data factory source option. Then fill the Sink option to put the data into target location(Data Lake Gen2 raw-data).
