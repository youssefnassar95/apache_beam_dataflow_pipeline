import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from datetime import datetime

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()


Timestamp = datetime.now()
fileNameTimestamp_str = Timestamp.strftime('%Y%m%d%H%M%S')

# Create and set your PipelineOptions:
beam_options = PipelineOptions(
    beam_args,
    runner='DataflowRunner',
    project='londonbicycles-381417',
    job_name='job'+fileNameTimestamp_str,
    temp_location='gs://london_bicycle_challenge/temp',
    region='europe-west2')

# Create the Pipeline with the specified options:
with beam.Pipeline(options=beam_options) as pipeline:
    counter = (
        pipeline
        | beam.io.ReadFromBigQuery(
            query='SELECT start_station_id, end_station_id FROM `bigquery-public-data.london_bicycles.cycle_hire`',
            use_standard_sql=True)                                               # read data from Big Query Table
        | beam.Map(lambda row: (row['start_station_id'], row['end_station_id'])) # extract values from each row in form of tuple
        | beam.Filter(lambda x: x[0] is not None and x[1] is not None)           # remove empty cells (cleaning)
        | beam.Map(lambda x: (x, 1))                                             # create tuple with tuple from step 2 and "counter" value
        | beam.GroupByKey()                                                      # group by (start_id, end_id)
        | beam.Map(lambda x: (x[0][0], x[0][1], sum(x[1])))         # calculate sum of values for each (start_id, end_id) group
        | beam.Map(lambda x: f"{x[0]}, {x[1]}, {x[2]}")             # format as string in order: start_id, end_id, amount of rides
        | beam.io.WriteToText('gs://london_bicycle_challenge/output/output.txt', num_shards=1)            # write output to one text file
    )