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
		bat 'kubectl --kubeconfig C:\\Users\\91998\\.kube\\config get nodes'
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

				echo %DOCKER_PASSWORD%>docker-password.txt

		                docker login -u %DOCKER_USERNAME% --password-stdin < docker-password.txt
				if errorlevel 1 (
					del /q docker-password.txt
					exit /b 1
					)

				del /q docker-password.txt
            '''
                
		       bat 'docker push akashfrancis/devops-task-api:%BUILD_NUMBER%'
		}
            }
        }
	stage('k8s-connectivity') {
	    steps {
		bat 'whoami'
		bat 'where kubectl'
		bat 'kubectl --kubeconfig C:\\Users\\91998\\.kube\\config config current-context'
		bat 'kubectl --kubeconfig C:\\Users\\91998\\.kube\\config get nodes'
		bat 'C:\\Users\\91998\\AppData\\Local\\Microsoft\\WinGet\\Links\\helm.exe version'
		bat 'C:\\Users\\91998\\AppData\\LOcal\\Microsoft\\WinGet\\Links\\helm.exe list --kubeconfig C:\\Users\\91998\\.kube\\config'
		}
	}   
    }
}
