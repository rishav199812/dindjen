pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3 -y'
                    sh 'apt-get install python3-pip -y'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        stage('Check') {
            steps {
                    sh 'python3 -m unittest test.test'
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
