pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0,30 * * * *')])])
                }
                git 'https://github.com/hadas1994/DevOps_Project.git'
            }
        }
        stage('Run rest_app.py (backend)') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('Run web_app.py (frontend)') {
            steps {
                bat 'web_app.py'
            }
        }
        stage('Run backend_testing.py') {
            steps {
                bat 'start /min python backend_testing.py'
            }
        }
        stage('Run frontend _testing.py') {
            steps {
                bat 'python frontend _testing.py'
            }
        }
        stage('Run combined_testing.py') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('Run clean_environemnt.py') {
            steps {
                bat 'python clean_environemnt.py'
            }
        }
    }
}