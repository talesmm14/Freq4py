FROM python:3.8

EXPOSE 8000

WORKDIR /app
COPY . /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        locales \
        locales-all \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV LC_ALL pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install pip requirements
COPY Pipfile Pipfile.lock ./ 
RUN pipenv install

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'Frequinpy'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "frequinpy.wsgi"]