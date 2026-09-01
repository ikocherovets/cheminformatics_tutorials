import ssl, certifi, urllib.request
import pandas as pd

def read_csv(url, **kwargs):
    ctx = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url, context=ctx) as resp:
        return pd.read_csv(resp, **kwargs)