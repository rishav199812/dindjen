pipeline {
    agent any
    options {
    office365ConnectorWebhooks([
	    [name: "team1", url: "https://triconindia.webhook.office.com/webhookb2/517e1231-9212-4fba-a064-7519cfcf5f7b@6ba04439-8b0e-43ee-ad26-c2ac9ef9e765/IncomingWebhook/e4c7deee6c68400bb424e7c9dfb87c9f/6a34ea39-c1a0-4c78-8617-3685ab15032e", notifyBackToNormal: true, notifyFailure: true],
            [name : "team2", url: "https://triconindia.webhook.office.com/webhookb2/517e1231-9212-4fba-a064-7519cfcf5f7b@6ba04439-8b0e-43ee-ad26-c2ac9ef9e765/IncomingWebhook/f33180cbe3bd456d89fc2e3a3ad70d5d/6a34ea39-c1a0-4c78-8617-3685ab15032e", notifyBackToNormal: true, notifyFailure: true]
	    ]
			     )
			       }
    stages {
//         stage('Build') {
//             steps {
//                     sh 'apt-get install python3 -y'
//                     sh 'apt-get install python3-pip -y'
//                     sh 'pip3 install -r requirements.txt'
//                     //sh 'pip3 show unittest'
//                     sh 'pip3 freeze' nhdnandkadn
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
//                     abc =2000
//                     echo "${abc}"
//                     sh 'printenv'
//                     def check = sh 'date +%s'
//                     echo "${check}"
//             sh 'printenv'
                    dir_size = sh(script: 'date +%s',returnStdout: true).trim()
                    echo "${dir_size}"
                    sh 'printenv'
                }
            }
}
    }
    }
