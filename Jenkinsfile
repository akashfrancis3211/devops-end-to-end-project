pipeline {
    agent any

    stages {

        stage('diagnose') {
            steps {
                bat 'echo %PATH%'
                bat 'where python'
                bat 'python --version'
                bat 'where docker'
                bat 'docker --version'
                bat 'where trivy'
                bat 'trivy --version'
            }
        }

        stage('validate') {
            steps {
                bat 'python --version'
                bat 'python -m py_compile app/app.py'
            }
        }

        stage('test') {
            steps {
                bat 'python -m pip install -r requirements-dev.txt'
                bat 'python -m pytest -v'
            }
        }

        stage('docker-build') {
            steps {
                bat 'docker build -f docker/Dockerfile -t akashfrancis/devops-task-api:%BUILD_NUMBER% .'
            }
        }

        stage('docker-verify') {
            steps {
                bat 'docker images akashfrancis/devops-task-api'
            }
        }

        stage('trivy-security-scan') {
            steps {
                bat 'trivy image --severity HIGH,CRITICAL --format json --output trivy-report.json --exit-code 0 akashfrancis/devops-task-api:%BUILD_NUMBER%'
                archiveArtifacts artifacts: 'trivy-report.json', fingerprint: true

                bat 'trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 akashfrancis/devops-task-api:%BUILD_NUMBER%'
            }
        }

        stage('docker-push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                   
			bat '''
                		if "%DOCKER_USERNAME%"=="" (
                    			echo ERROR: Docker username is empty
                    			exit /b 1
                )

                		if "%DOCKER_PASSWORD%"=="" (
                    			echo ERROR: Docker password is empty
                    			exit /b 1
                )

                		echo Docker username is present
                		echo Docker password is present
                		echo Password length: %DOCKER_PASSWORD:~0,1%********

                		docker logout
            '''
                }
            }
        }
    }
}
