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
		bat 'docker build -f docker/Dockerfile -t devops-task-api:%BUILD_NUMBER% .'
	   }
        }

	stage('docker-verify') {
	    steps {
		bat 'docker images devops-task-api'
	   }
        }

	stage('trivy-security-scan') {
	    steps {
		bat 'trivy image --severity HIGH,CRITICAL --format json --output trivy-report.json --exit-code 0 devops-task-api:%BUILD_NUMBER%'
		archiveArtifacts artifacts: 'trivy-report.json', fingerprint: True

		bat 'trivy image --severity HIGH,CRITICAL --exit-code 1 devops-task-api:%BUILD_NUMBER%'
	   }
	}
    }
}
