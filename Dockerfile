FROM python:3.9
RUN apt-get update && apt-get install -y \
    python3-pygame \
    xvfb \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN pip install pygame
CMD ["xvfb-run", "python", "tetris.py"]
