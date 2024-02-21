import os
import uuid
import json
import pandas as pd
from tonic_validate.classes.run import Run

def get_df(run: Run):
    metrics = list(run.overall_scores.keys())
    columns = ["question"] + metrics
    scores = []      
    for r in run.run_data:
        run_score = [r.reference_question] + [r.scores.get(metric, None) for metric in metrics]
        scores.append(run_score)
    return pd.DataFrame(scores,columns=columns)

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

def get_markdown(df, num_questions):
    hidden_header = '<!--tonic_validate-->'
    title = '### Tonic Validate <img src="https://uploads-ssl.webflow.com/62e28cf08913e81176ba2c39/65d62931c9dd663f00cff8e1_TonicValidate-Icon-XS.svg"/>'
    table = df.to_markdown()
    return '\n'.join([hidden_header, title,'\n',table])
