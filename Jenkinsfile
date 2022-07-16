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
        stage('install pymysql') {
            steps {
                bat 'pip install pymysql'
            }
        }
        stage('Run web_app.py (frontend)') {
            steps {
                bat 'start /min web_app.py'
            }
        }
        stage('install requests') {
            steps {
                bat 'pip install requests'
            }
        }
        stage('Run backend_testing.py') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Run frontend_testing.py') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage('Run combined_testing.py') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('Run clean_environment.py') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }
}