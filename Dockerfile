# Use Python 3.10 (compatible with your PyArmor runtime)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose the port your Gradio app uses (default: 7860)
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
