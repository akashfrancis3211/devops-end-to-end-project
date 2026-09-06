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

    }
}
