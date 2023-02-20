pipeline {
    agent any
    stages {
//         stage('Build') {
//             steps {
//                     sh 'apt-get install python3 -y'
//                     sh 'apt-get install python3-pip -y'
//                     sh 'pip3 install -r requirements.txt'
//                     //sh 'pip3 show unittest'
//                     sh 'pip3 freeze'
//                 }
//             }
//         stage('Check') {
//             steps {
//                     //sh "apt install -y curl wget apt-transport-https"
//                     //sh "wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"
//                     //sh "cp minikube-linux-amd64 /usr/local/bin/minikube"
//                     //sh "chmod +x /usr/local/bin/minikube"
//                     sh "minikube version"
                
//                 }
//             }
//             stage('Test') {
//                  steps {
//                  sh 'pwd'
//                  echo "checking the next stage"
//                }
//             }
 
//         }
        stage ('New'){
            steps {
                script {
                    sh 'printenv'
                   DIR_SIZE=sh(returnStdout: true,script: 'date +%s')
            //DIR_SIZE = sh(returnStdout: true,script: 'date -u -d "2023-02-20 08:07:00" ')
            echo ${DIR_SIZE}
            sh 'printenv'
                }
            }
}
    }
    }
