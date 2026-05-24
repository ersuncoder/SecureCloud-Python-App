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
                script {
                    // Kubernetes klasteriga fayllarni apply qilamiz
                    bat 'kubectl apply -f k8s/deployment.yaml'
                    bat 'kubectl apply -f k8s/service.yaml'
                
                    // Deployment muvaffaqiyatli bo'lganini tekshiramiz
                    bat 'kubectl rollout status deployment/python-cloudapp-deployment'
                }
            }
        }
    }
