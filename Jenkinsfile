// pipeline {
//     agent {
//         docker { image 'python:3-alpine' }
//     }
//     stages {
//         stage('Build') {
//             steps {
//                     sh 'pip install --user -r requirements.txt'
//                 }
//             }
//             stage('Test') {
//                  steps {
//                  sh 'pwd'
//                  echo "checking the next stage"
//                }
//             }
 
//         }
// }
pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'gradle:6.7-jdk11'
                    // Run the container on the node specified at the
                    // top-level of the Pipeline, in the same workspace,
                    // rather than on a new node entirely:
                    reuseNode true
                }
            }
            steps {
                sh 'gradle --version'
            }
        }
    }
}
