// Jenkins file
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build Docker image
                sh 'docker build -t world-of-games .'
            }
        }

        stage('Run') {
            steps {
                // Run Docker container
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                // Run tests using e2e.py
                sh 'python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                // Stop and remove the container
                sh 'docker-compose down'
                // Push the updated image to DockerHub
                sh 'docker push davidoh11/world-of-games'
            }
        }
    }
}
