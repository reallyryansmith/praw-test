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
      parallel {
        stage('Install Pip') {
          steps {
            sh 'sudo yum install python-pip -y'
          }
        }
        stage('Install PRAW via pip') {
          steps {
            sh 'sudo pip install praw'
          }
        }
      }
    }
    stage('Run Script') {
      steps {
        sh 'sudo python praw-tutorial.py'
      }
    }
  }
}