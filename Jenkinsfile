pipeline {
  agent any
  stages {
    stage('Print Message') {
      steps {
        echo 'Start Pipeline'
      }
    }
    stage('Uname') {
      steps {
        sh 'sudo uname -a'
      }
    }
    stage('Install Pip') {
      steps {
        sh 'sudo yum install python-pip -y'
      }
    }
  }
}