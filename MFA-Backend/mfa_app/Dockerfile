# FROM python:3.10

# WORKDIR /app

# # Install system dependencies (useful for OpenCV/face libs if needed)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     cmake \
#     libsm6 \
#     libxext6 \
#     libxrender-dev \
#     libgl1-mesa-glx \
#     libglib2.0-0 \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy backend source
# COPY . .

# EXPOSE 8000
# CMD ["python", "app.py"]


FROM ubuntu:22.04

WORKDIR /app


FROM python:3.10
WORKDIR /app
# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]