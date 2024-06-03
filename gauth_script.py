import gdown
import pandas as pd
import tempfile

file_ID = '1LG3vRQsKSXAkWJzZuhBlYLyWP4Ab06n2'
url = f'https://drive.google.com/uc?id={file_ID}'

with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
    gdown.download(url, tmp.name, quiet=False)
    tmp.close

df = pd.read_excel(tmp.name)

df
