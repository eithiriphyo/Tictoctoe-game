# Tic-Tac-Toe Real-Time Game
A real-time, 2-player Tic-Tac-Toe game built with Python (Flask) and Socket.IO. Designed for real-time interaction and containerized for modern cloud deployment.

# Features
 - Real-time Gameplay: Bi-directional communication using WebSockets.

 - Live Scoring: Track scores across multiple sessions.

 - Custom Personalization: Players enter their own names before starting.

 - Responsive UI: Clean, modern, and aesthetic design.

# Tech Stack

 - Backend: Python, Flask, Flask-SocketIO

 - Frontend: HTML, CSS, JavaScript

 - DevOps: Docker, Kubernetes
 - 
# Deployment
- This project is containerized for easy deployment to any Kubernetes cluster.
- Runngin Locally with Docker Dekstop and Kubernetes

- Build the image and deploy container as below
  docker build -t eithiriphyo/tictactoe:local .
  kubectl apply -f manifest/deployment.yaml
  kubectl apply -f manifest/service.yaml

# Key Learnings from this Demo Project

- Real-time State: Learned to manage game states via WebSocket events.

- Containerization: Mastered Dockerizing Python applications and optimizing image sizes.

- Orchestration: Overcame deployment challenges like CrashLoopBackOff and image caching issues in Kubernetes.

![Tictoctoe-game](images/User_login.png)
![Tictoctoe-game](images/Game_page.png)

