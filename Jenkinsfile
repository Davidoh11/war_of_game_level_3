pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("python:3.11-slim:${BUILD_NUMBER}")
                }
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:80 -v $(pwd)/Scores.txt:/Scores.txt python:3.11-slim:${BUILD_NUMBER}'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run -v $(pwd)/e2e.py:/e2e.py --network host python:3.11-slim:${BUILD_NUMBER} python e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=python:3.11-slim:${BUILD_NUMBER})'
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        def customImage = docker.image("python:3.11-slim:${BUILD_NUMBER}")
                        customImage.push()
                    }
                }
            }
        }
    }
}
