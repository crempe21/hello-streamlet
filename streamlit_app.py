import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
from dask.distributed import Client

client = Client(n_workers=2, threads_per_worker=2, memory_limit="1GB")
client

import dask.dataframe as dd
column_names = [
    "idx","Start_Date", "Start_Time",  "Duration", 
    "Serv", "Src_Port", "Dest_Port", "Src_IP", "Dest_IP", "Attack","Score_Name"
]
column_dtypes = [
    "Start_Date", "Start_Time", "End_Time", "Duration", 
    "Serv", "Src_Port", "Dest_Port", "Src_IP", "Dest_IP", "Attack","Score_Name"
]
raw_df = dd.read_csv("/data-bigpool/largefraudmodel/data/DARPA_Intrusion_Detection/Training_data/First_week/monday/tcpdump.list.gz", compression='gzip',blocksize=None \
                    , dtype={ "Src_Port" : "string", "Dest_Port" : "string"}, sep='\s+', header=None, names=column_names)
st.write(raw_df.head(5))
