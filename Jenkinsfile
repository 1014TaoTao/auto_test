node("cd-server") {
    stage('Prepare') {
        echo ">>>>>>>>>> Stage 1. Prepare"
    }

    stage('Clone Code') {
        echo ">>>>>>>>>> Stage 2. Clone Code"
        git credentialsId: '07f48ec0-75ad-45d5-9352-9xxxxxxxx6d', url: 'git@github.com:fusu192/Interface-automation-test.git'
    }

    stage('Exec Test Suit') {
        echo ">>>>>>>>>> Stage 3. Exec Test Suit for ${env.USER_STORY_ID} from ${env.SERVICE_URL}"
        sh "chmod +x run.sh"
        USER_STORY_ID = "${env.USER_STORY_ID}"
        SERVICE_URL = "${env.SERVICE_URL}"

        SHELL_RESULT = 0
        if(USER_STORY_ID == "HY-0"){
            SHELL_RESULT = sh(script: "./run.sh -h ${SERVICE_URL}", returnStatus: true)

        } else {
            SHELL_RESULT = sh(script: "./run.sh -h ${SERVICE_URL} -t ${USER_STORY_ID}", returnStatus: true)
        }
    }
    stage('Generate Report') {
        echo ">>>>>>>>>> Stage 4. Generate Report for ${env.USER_STORY_ID}, please check http://autotest.baogao.com/ for more information"
        //todo sendEmail if test failure
        if (SHELL_RESULT != 0){
           mail bcc: '', body: 'Ops! auto-test failed, pls check more information from http://autotest.baogao.com', cc: '', from: 'xiaohong@name.com', replyTo: '', subject: 'Auto-test Failure Report', to: 'xiaoming1@name.com,xiaoming2@name.com,xiaoming3@name.com,xiaoming4@name.com'
        }
    }
}
