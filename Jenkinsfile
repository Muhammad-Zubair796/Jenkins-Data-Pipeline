pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        stage('Build & Test') {
            steps {
                echo 'Running Data Cleaning Script...'
                sh 'python3 data_process.py'
            }
        }
    }
}
