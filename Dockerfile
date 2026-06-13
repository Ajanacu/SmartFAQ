FROM python:3.10-slim

WORKDIR /app

# Copy backend files into the container
COPY backend/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by Hugging Face Spaces
EXPOSE 7860

# Start FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]