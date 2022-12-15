pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3 -y'
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
