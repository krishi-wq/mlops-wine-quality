pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/krishi-wq/mlops-wine-quality.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh './venv/bin/python train.py'
            }
        }
        stage('Test Model') {
            steps {
                sh './venv/bin/python test_model.py'
            }
        }
        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
            }
        }
    }
}