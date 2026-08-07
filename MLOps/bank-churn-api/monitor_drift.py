import json
import pandas as pd
 
 
def load_logged_inputs(log_path="logs/predictions.log"):
    rows = []
    with open(log_path) as f:
        for line in f:
            entry = json.loads(line)
            rows.append(entry["input"])
    return pd.DataFrame(rows)


