pipeline {
    agent {
        docker {
            image 'python:3.9-slim' 
        }
    }
    stages {
        stage('Data Processing') {
            steps {
                echo 'Running script inside a Python Docker Container...'
                sh 'python3 data_process.py'
            }
        }
    }
}
