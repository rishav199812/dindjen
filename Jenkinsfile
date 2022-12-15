pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3 -y'
                    sh 'pip install -r requirements.txt'
                }
            }
        stage('Check') {
            steps {
                    sh 'python -m unittest test/app.py'
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
