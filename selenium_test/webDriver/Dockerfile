FROM python:3.9

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && wget https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin \
    && rm chromedriver_linux64.zip

# Set up the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
#COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test files
#COPY new_test.py .
COPY test_memory.py .
COPY . /usr/share/nginx/html

# Set the entrypoint to run the tests
ENTRYPOINT ["python", "-m", "pytest"]