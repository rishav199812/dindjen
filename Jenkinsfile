pipeline {
    agent  { label 'docker' }
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3'
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
