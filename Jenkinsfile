pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }
    environment {
        APP_ENV = 'PROD-DATABASE'
    }
    stages {
        stage('Process & Validate') {
            steps {
                sh 'python3 data_process.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished. Cleaning up temporary files...'
        }
        success {
            echo 'DEPLOYMENT SUCCESSFUL: Data is clean and ready for ML Model!'
        }
        failure {
            echo 'ALERT: Pipeline Failed! Check the data validation logs.'
        }
    }
}
