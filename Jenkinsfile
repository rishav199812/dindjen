pipeline {
    agent  {
        label 'docker' { image 'python:3-alpine' }
    }
    stages {
        stage('Build') {
            steps {
                    sh 'py'
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
