# Apache Beam - Dataflow Pipeline

Technology used: *python, Apache Beam, GCP, Google Cloud SDK Shell*

## Abstract

The project was done as part of a coding challenge. 
The goal was to perform data transformations with the public dataset on London bicycles to obtain some insights on London cycling behavior. The mein task was to get number of rides from one station to another and present the results in form of text file (start_id, end_id, number_of_rides)

## Process

1. Starting with GCP project and Google Cloud SDK authentication
2. Creating s3 bucket with input data and python script
3. Preparing rides_counter.py script and creating pipeline using apache_beam
4. Running the script to initialize the dataflow pipeline
5. Review the data

## Source code: python script & pipeline dependencies

[*rides_counter.py*](https://github.com/youssefnassar95/apache_beam_dataflow_pipeline/blob/main/rides_counter.py)

[*setup.py*](https://github.com/youssefnassar95/apache_beam_dataflow_pipeline/blob/main/setup.py)

## Output

The outcome was a [*outfile.txt*](https://github.com/youssefnassar95/apache_beam_dataflow_pipeline/blob/main/output.txt) file that presents results in expected format.
