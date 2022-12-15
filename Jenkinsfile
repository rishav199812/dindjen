pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                    sh 'apt-get install python3 -y'
                    sh 'apt-get install python3-pip -y'
                    sh 'pip3 install -r requirements.txt'
                    sh 'pip3 show unittest'
                    sh 'pip3 freeze'
                }
            }
        stage('Check') {
            steps {
                    //sh 'pytest -m test/test.py'
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
