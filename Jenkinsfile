pipeline {
    agent  'any'
    stages {
        stage('Deployment') {
            steps {
                build quietPeriod: 2, wait: false, job: 'SportCenter'
            }
        }
    }
}