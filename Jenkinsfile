pipeline {
    agent any
    environment {
    registry = "hadas1994/my-repo"  // The name of your user and repository (which can be created manually)
    registryCredential = 'docker_hub' // The credentials used to your repo
    dockerImage = '' // will be overridden later
    }
    stages{
        stage('Checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('0,30 * * * *')])])
                    properties([buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))])
                }
                git 'https://github.com/hadas1994/DevOps_Project.git'
            }
        }
        stage('Run rest_app.py (backend)') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('Install pymysql') {
            steps {
                bat 'pip install pymysql'
            }
        }
        stage('Run backend_testing.py') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Run clean_environment.py') {
            steps {
                bat 'python clean_environment.py'
            }
        }
        stage('Build and push image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" // give a name and version to image
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push() // push image to hub
                    }
                }
            }
        }
        stage('Set version') {
            steps {
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
            }
        }
        stage('Start container') {
            steps {
                bat "docker-compose up -d --wait"
            }
        }
        stage('Run docker_backend_testing.py') {
            steps {
                bat 'python docker_backend_testing.py'
            }
        }
    }
    post {
    always {
        bat "docker rmi $registry:$BUILD_NUMBER" // delete the local image at the end
        }
    }
}
