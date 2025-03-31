FROM ubuntu

# Install necessary dependencies
RUN apt update && apt -y upgrade && apt install -y \
    python3-pip python3-venv libpq-dev git

# Set working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv venv

# Clone and install Holehe inside the virtual environment
RUN git clone https://github.com/megadose/holehe.git
WORKDIR /app/holehe
RUN /app/venv/bin/pip install .

# Ensure Holehe is globally accessible
RUN ln -s /app/venv/bin/holehe /usr/local/bin/holehe

# Return to /app
WORKDIR /app

# Copy application files
COPY app app
COPY requirements.txt .
COPY .env .env

# Install Python dependencies inside the virtual environment
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the FastAPI app using the virtual environment
CMD ["/app/venv/bin/python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
