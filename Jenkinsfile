pipeline{
    agent any
    stages{
        stage('Install dependecies'){
            steps{
                sh 'pip install pytest pytest-cov'
            }
        }
        stage('Run tests with coverage'){
            steps{
                sh 'pytest --cov=test test/'
            }
        }
        stage('Generate HTML report'){
            steps{
                sh 'pytest --cov=test --cov-report=html test/'
            }
        }
        stage('Archive the html report'){
            steps{
                archiveArtifacts artifacts: 'htmlcov/**'
            }
        }
    }
    post{
        always{
            echo 'Pipelien executed successfully'
        }
    }
}
