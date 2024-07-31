FROM python:3.12-slim-bullseye

RUN echo "### --- Ubuntu dependencies --- ###" \
    && apt-get update && \
    apt-get install -y \
    g++ \
    cmake \
    unzip \
    curl \
    poppler-utils \
    && echo "### --- Directory setup --- ###"

WORKDIR /app

COPY ./app .

# PACKAGES 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8990

# CMD ["streamlit", "run", "./1_IVR_Data_Cleaner.py"]