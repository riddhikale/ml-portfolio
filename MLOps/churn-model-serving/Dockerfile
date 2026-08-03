# Base image - slim keeps the image small, still has full Python
FROM python:3.11-slim

WORKDIR /app

# Copy dependency list first (separate layer) so Docker caches installed
# packages and doesn't re-install them every time app code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the actual app code + trained model artifact
COPY schemas.py .
COPY api_with_validation.py .
COPY model/ ./model/

EXPOSE 8000

CMD ["uvicorn", "api_with_validation:app", "--host", "0.0.0.0", "--port", "8000"]