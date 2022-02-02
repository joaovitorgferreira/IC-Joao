import numpy as np
import pandas as pd
import requests

sequences_url = 'https://raw.githubusercontent.com/abidlabs/deep-learning-genomics-primer/master/sequences.txt'

sequences = requests.get(sequences_url).text.split('/n')
sequences = list(filter(None, sequences))

pd.DataFrame(sequences, index=np.arange(1, len(sequences)+1), columns=['Sequences'].head)