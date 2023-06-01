**Data Transformation Application**

This Python application performs data transformation and cleansing operations on a CSV file,
calculates totals for grid_purchase and grid_feedin by hour and writes the transformed data to an output file.


**Folder Structure**

1. README : Please read through this file to be able to run the date transformation application 
2. dockerfile : This text file is used to build the docker image 
3. measurments.csv: Input dataset provided to work on. 
4. output.csv:  The transformed data with the added boolean column
5. python_application.py: The python code of carrying on the required cleansing and transformation 
6. requirements.txt: Dependincies and packages used in python app and used by docker to build the docker image
7. Documentation.pdf: Application documentation and output screenshots

**Prerequisites**

1. Python 3.9 or higher installed on your local machine.
2. Required Python packages: pandas, pandasql.
3. Docker installation on the local machine

**Getting Started**

Clone the repository or download the application code locally.

You can run the python application directly from the terminal or using Docker. 

**Python**
1. Open the terminal and navigate to the cloned folder
2. Install the required Python packages using pip:
    > pip install pandas pandasql
3. Run the application:
    > python python_application.py

**Dockerization**

To run the application within a Docker container, follow these steps:
1. In the terminal or command prompt, navigate to the project directory containing the Dockerfile.
2. Build the Docker image using the following command 
    > docker build -t data-transformation-app .
3. After the Docker image is successfully built, run the following command to start a container from the Docker image:
    > docker run --name data-trans-cont data-transformation-app
4. After the container finishes running, access the output file output.csv by copying it 
   from the container to your local machine:
    > docker cp data-trans-cont:/app/output.csv ./output.csv




