pipeline {
    agent {
        docker { image 'python:3-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                    sh 'pip install --user -r requirements.txt'
                }
            }
            stage('Test') {
                 steps {
                 sh 'pwd'
                 echo "checking the next stage"
               }
            }
 
        }
}
