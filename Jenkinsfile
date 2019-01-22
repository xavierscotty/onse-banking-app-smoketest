def git_repository = 'https://github.com/ONSdigital/onse-banking-app-smoketest'
def app_url = 'http://banking-demo.apps.onse-training.co.uk'

def label = "build-${UUID.randomUUID().toString()}"
def build_pod_template = """
kind: Pod
metadata:
  name: build-pod
spec:
  containers:
  - name: python-test
    image: aklearning/onse-pg-python:0.0.1
    tty: true
"""

podTemplate(name: 'smoketest-build', label: label, yaml: build_pod_template) {
  node(label) {
    git git_repository

    stage('Smoke Test') {
        container(name: 'python-test', shell: '/bin/sh') {
            sh 'pipenv install --dev'
            sh "URL=${app_url} pipenv run behave"
        }
    }
  }
}
