![Flask Microservices with Centralized Logging](./assets/Flask-Microservices-with-Centralized-Logging.png) 
    A lightweight microservices architecture demonstrating Docker containerization, service isolation, and centralized MongoDB logging.
    Three independent Flask services communicate asynchronously with unified event tracking.

**Quick Overview**

    MicroLog consists of three containerized Flask microservices:
    
    Auth Service (Port 8001) - User authentication
    Order Service (Port 8002) - Order management
    Payment Service (Port 8003) - Payment processing

    All services log events to a centralized MongoDB Atlas database for monitoring and debugging.

Architecture

                                Client
                                  ↓
                    ┌─────────┬─────────┬─────────┐
                    │  Auth   │  Order  │ Payment │
                    │  :8001  │  :8002  │  :8003  │
                    └────┬────┴────┬────┴────┬────┘
                         └─────────┴─────────┘
                                  ↓
                           MongoDB Atlas
                          (Centralized Logs)

 Project Structure

     Flask-Microservices-with-Centralized-Logging/
      auth-service/
        - app.py             (Flask authentication service)
        - Dockerfile         (Container definition)
        - requirements.txt   (Dependencies)
      
      order-service/
        - app.py             (Flask order service)
        - Dockerfile         (Container definition)
        - requirements.txt   (Dependencies)
      
      payment-service/
        - app.py             (Flask payment service)
        - Dockerfile         (Container definition)
        - requirements.txt   (Dependencies)
      
      docker-compose.yml     (Multi-service orchestration)
      .env                   (Environment variables)

Quick Start

1. Clone Repository
 
    git clone https://github.com/<YOUR_USERNAME>/MicroLog.git
    cd Flask-Microservices-with-Centralized-Logging

2. Set Up MongoDB Atlas

    Create account at mongodb.com/atlas
    Create cluster (M0 Free tier)
    Create database user
    Whitelist IP: 0.0.0.0/0
    Get connection string

3. Configure Environment (MongoDB Atlas connection string)

    Create .env file:
    MONGO_URL=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/microservice_logs?retryWrites=true&w=majority

4. Build & Run
   
   bash# Build and start all services
   docker compose up -d

    # View logs
    docker compose logs -f
    
    # Check running containers
    docker compose ps
    
    🧪 Test Services
    bash# Auth Service
    curl -X POST http://localhost:8001/login
    
    # Order Service
    curl -X POST http://localhost:8002/order
    
    # Payment Service
    curl -X POST http://localhost:8003/pay
    Expected Response:
    json{
      "status": "order confirmed"
    }
    
    View Logs in MongoDB
    Connect to MongoDB Atlas and check the microservice_logs database:
    
5. MongoDB Schema

    Database: microservice_logs
    Collection: logs
    Document Structure:
    json{
      "_id": ObjectId("..."),
      "Service": "order-service",
      "level": "INFO",
      "message": "Order placed",
      "timestamp": ISODate("2026-01-26T03:25:30.859Z"),
      "host": "container-hostname"
    }


Service Details

    Auth Service (Port 8001)
    Endpoint: POST /login
    Function: User authentication and login
    Log Message: "User login attempt"
    
    Order Service (Port 8002)
    Endpoint: POST /order
    Function: Order creation and confirmation
    Log Message: "Order placed"
    
    Payment Service (Port 8003)
    Endpoint: POST /pay
    Function: Payment processing
    Log Message: "Payment initiated"

Key Concepts

    Service Isolation - Each service has its own container
    Shared Database - All services log to same MongoDB
    Environment Config - Credentials via .env file
    Production Setup - Gunicorn, non-root users, proper permissions

Troubleshooting

    docker exec -it <container_id> bash
    python
    >>> from pymongo import MongoClient
    >>> client = MongoClient("mongodb+srv://username:password@cluster0.abcd.mongodb.net/mydb?retryWrites=true&w=majority", serverSelectionTimeoutMS=5000)
    >>> client.server_info()  # id it does not then you will error

Learning Outcomes
This project demonstrates:


    Microservices architecture patterns
    Docker containerization best practices
    Multi-container orchestration with Docker Compose
    Centralized logging strategies
    Production-ready Python web services
    Security hardening (non-root users, permissions)
    Environment-based configuration
    Service isolation and independence