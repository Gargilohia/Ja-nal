# Stage 1: Build the React frontend
FROM node:16 AS frontend-build

# Set working directory for the frontend
WORKDIR /app

# Copy the frontend source code
COPY page/ /app/

# Install dependencies and build the frontend
RUN npm install && npm run build

# Stage 2: Set up the Flask backend
FROM python:3.10-slim

# Set working directory for the backend
WORKDIR /app

# Copy the backend source code
COPY api/ /app/

# Set up virtual environment and install dependencies
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir Flask

# Copy the built frontend from the previous stage into the backend's static folder
COPY --from=frontend-build /app/build /app/static

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["sh", "-c", "source venv/bin/activate && python application.py"]
