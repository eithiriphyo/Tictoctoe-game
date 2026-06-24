FROM python:3.9-slim
WORKDIR /app
# We need eventlet for WebSockets to work in production/container
RUN pip install flask flask-socketio eventlet
COPY app.py .
COPY templates/ ./templates/
CMD ["python", "app.py"]
