pipeline {
  agent { docker { image 'python:2.7.5' } }
  environment {
    CI = 'true'
  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python database_setup.py'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
  }
}
