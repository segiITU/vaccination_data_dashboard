FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

ENV MPLBACKEND=Agg
ENV MPLCONFIGDIR=/tmp/matplotlib

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"] 