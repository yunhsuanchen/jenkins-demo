pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Starting code checkout stage.'
                sh '''
                    #!/bin/sh
                    rm -rf
                '''
                git credentialsId: 'nadia-git', url: 'https://github.com/cmu-seai/jenkins-demo.git'
                echo 'Code checked out successfully.'
            } // steps
        } // stage

        stage('Install Dependencies') {
           steps {
               echo 'Installing dependencies'
                sh '''
                    #!/bin/sh
                    pip3 install -r requirements.txt
                '''
           }
        }

        stage('Evaluate Code Quality') {
           steps {
            	echo 'Run tests'
                sh '''
                    #!/bin/sh
                    python3 -m pytest --cov=./ --cov-report=xml ./
                '''
                cobertura coberturaReportFile: 'coverage.xml'
                echo 'Code quality check completed.'
            } // steps
        } // stage

        stage('Run Pipeline') {
           steps {
                echo 'Run pipeline'
                sh '''
                    #!/bin/sh
                    python3 ./pipeline.py
                '''
                echo 'Pipeline run completed.'
            } // steps
        } // stage

//        stage('Data Collection') {
//            steps {
//                echo 'Starting data collection.'
//                sh '''
//                    cd 01_data_collection
//                    python3 collect_from_kafka.py
//                '''
//                echo 'Data collection completed.'
//            } // steps
//        } // stage
//
//        stage('Data Clean') {
//            steps {
//                echo 'Starting data clean.'
//                sh '''
//                    cd 02_data_clean
//                    python3 clean_data.py
//                '''
//                echo 'Data clean completed.'
//            } // steps
//        }
//
//        stage('Data Quality Check') {
//            steps {
//                echo 'Starting data quality check.'
//                sh '''
//                    cd 03_data_quality
//                    python3 data_quality_check.py
//                    
//                '''
//                echo 'Data quality check completed.'
//            } // steps
//        } // stage

 //       stage('Train Model and Evaluate') {
 //           steps {
 //               echo 'Start model training and evaluation.'
 //                sh '''
        //             cd 04_model_training
        //             python3 collect_telemetry.py 
        //         '''
 //               echo 'Model training and evaluation completed.'
 //           } // steps
 //       }

        // stage("Collect Telemetry ") {
        //      steps {
        //         echo 'Start collecting telemetry data '
        //         sh '''
        //             cd 05_online_evaluation_and_telemetry
        //             python collect_telemetry.py 
        //         '''
        //         echo 'Telemetry Collection Complete.'

        //         plot csvFileName: 'telemetry.csv', csvSeries: [[file: 'telemetry_logs11112020.csv']], group: 'Measures', title: 'Online Metric 1', style: 'line', yaxis: 'Metric 1'

        //     } // steps


    } // stages
}