pipeline {
    agent any

    stages {

        stage('validate') {
            steps {
                bat 'python --version'
                bat 'python -m py_compile app/app.py'
            }
        }

    }
}
