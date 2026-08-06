"""
Logs every prediction the API makes: input features, output, and timestamp.
This is what makes monitoring (next topic) possible later - you can't detect
drift or unusual patterns in predictions you never recorded.
"""

import logging
import json
import os
from datetime import datetime, timezone

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("churn_predictions")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/predictions.log")
formatter = logging.Formatter("%(message)s")  # we'll pass pre-formatted JSON lines
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_prediction(input_data: dict, output_data: dict):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": input_data,
        "output": output_data,
    }
    logger.info(json.dumps(entry))