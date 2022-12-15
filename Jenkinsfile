pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3 -y'
                }
            }
        stage('Check') {
            steps {
                    sh 'python3 -m unittest'
                    sh 'python3 -m unittest test/test.py'
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
