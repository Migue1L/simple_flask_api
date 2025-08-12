FROM python:3.9-slim
WORKDIR /model
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "predictor.py"]
