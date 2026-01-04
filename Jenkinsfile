pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    environment {
        APP_ENV = 'PROD-PORTFOLIO-ENVIRONMENT'
    }
    stages {
        stage('Data Processing') {
            steps {
                echo "Deploying to ${env.APP_ENV}..."
                sh 'python3 data_process.py'
            }
        }
    }
}
