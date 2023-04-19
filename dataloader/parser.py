## Save the dataset in trainable format (jsonl of input/output pairs)
## Parse the data such that each paragraph is split by sentences and 
## the input/out pairs are the sentences in order, where the output sentence is next used as the input sentence
## This is done for each paragraph in the dataset

import json

def parse(self, data, save_path):
    with open(save_path, 'w') as f:
        for paragraph in data:
            for i in range(len(paragraph) - 1):
                f.write(json.dumps({
                    'input': paragraph[i],
                    'output': paragraph[i + 1]
                }))