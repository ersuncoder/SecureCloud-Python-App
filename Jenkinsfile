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
                    bat 'C:\\sonar-scanner-5.0.1.3006-windows\\bin\\sonar-scanner.bat'
                }
            }
        }
        stage('Docker Build & Push') {
            steps {
                bat 'docker build -t ersun7/python-cloudapp:50 .'
                withCredentials([usernamePassword(credentialsId: 'docker', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    bat "echo %PASS% | docker login -u %USER% --password-stdin"
                    bat 'docker push ersun7/python-cloudapp:50'
                }
            }
        }
        // YANGI QO'SHILGAN BOSQICH:
        stage('Joriy etish (Deployment)') {
            steps {
                // 1. Agar xuddi shu nomdagi eski konteyner bo'lsa, uni majburiy o'chiradi.
                // "|| true" yozuvi agar eski konteyner topilmasa ham pipelineni to'xtatmay, davom etishini ta'minlaydi.
                bat 'docker rm -f python-app-container || true'
                
                // 2. Yangi yuklab olingan (push qilingan) obrazni lokal portda ishga tushiradi.
                bat 'docker run -d --name python-app-container -p 8000:5000 ersun7/python-cloudapp:50'
            }
        }
    }
}
