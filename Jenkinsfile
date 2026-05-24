pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Trivy File Scan') {
            steps {
                bat 'trivy fs . > trivyfs.txt'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube-Server') {
                    // To'g'ri va haqiqiy mutloq yo'l:
                    bat 'C:\\sonar-scanner-5.0.1.3006-windows\\bin\\sonar-scanner.bat'
                }
            }
        }
        stage('Docker Build & Push') {
            steps {
                bat 'docker build -t ersun7/python-cloudapp:50 .'
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    bat "echo %PASS% | docker login -u %USER% --password-stdin"
                    bat 'docker push ersun7/python-cloudapp:50'
                }
            }
        }
    }
}
