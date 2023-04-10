FROM python:3.10

# Set work directory
WORKDIR="/src"

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED=1
# 2. Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# 3. Install fault handlers for the SIGSEGV, SIGFPE, SIGABRT, SIGBUS, and SIGILL signals
ENV PYTHONFAULTHANDLER 1
# 4. Disable pip's cache files in the container
ENV PIP_NO_CACHE_DIR off
# 5. Don’t periodically check PyPI to determine whether a new version of pip is available for download
ENV PIP_DISABLE_PIP_VERSION_CHECK on


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .