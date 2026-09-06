pipeline {
	agent any

	stages {

		stage('checkout') {
			steps {
				checkout scm
			}
		}


		stage('validate') {
			steps {
				sh 'python3 --version'
				sh 'python3 -m py_compile app/app.py'
			}
		}

	}
}

