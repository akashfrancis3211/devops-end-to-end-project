pipeline {
    agent any

    stages {

	stage('diagnose') {
	    steps {
		bat 'echo %PATH%'
		bat 'where python'
		bat 'python --version'
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

    }
}
