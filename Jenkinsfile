pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '065a2134-4b8d-4239-8a04-08eb4832e9ef', url: 'https://github.com/julianmontague/cloud-portfolio.git']])

        sh label: 'Build container image', script: 'podman build -t django-numbers-app ./django'
      }
    }

    stage('Archive') {
      steps {
        ws {
          sh label: 'Save container image to file', script: 'podman image save -o image.tar django-numbers-app'

          archiveArtifacts artifacts: 'image.tar', followSymlinks: false, onlyIfSuccessful: true

          cleanWs()
        }
      }
    }
  }
}
