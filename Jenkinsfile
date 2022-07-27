pipeline {
    agent {label 'release/0.0.3'}
    tools{
        maven 'maven'
    }
    environment {
        GIT_PROJECT_ADDR="git@gitee.com:tao__tao/pytest_auto_uitest_apitest.git" //项目的git地址
        JENKINS_WORKSPACE="/root/.jenkins/workspace"    //jenkins存放文件的地址
        PROJECT_NAME="${JOB_NAME}"                      // 项目名
        JAR_NAME="sample-tezst-0.0.1-SNAPSHOT.jar"   // 项目生成的jar的名字
        IMAGE_NAME="sample-tezst"                    // 镜像名一般和项目名相同
        IMAGE_ADDR="repository/qiao_namespace/${IMAGE_NAME}"    // 镜像的位置
        VERSION_ID="${BUILD_ID}"
    }
    stages {
        stage('pullCode'){
            steps{
                echo 'This is a pullCode step'
                //git branch: "${BRANCH}", credentialsId: '1001', url: "${GIT_PROJECT_ADDR}"
                checkout scm
            }
        }
        stage('Build') {
            steps{
                echo 'This is a Build step'
                // 在有Jenkinsfile同一个目录下（项目的根目录下）
                sh 'mvn clean package -Dmaven.test.skip=true'
            }
        }
        // 创建目录(如果不存在)，并把jar文件上传到该目录下
        stage('ssh') {
            steps{
                echo 'push jar to target server'
                sh '''
                    ole_image_id=`docker images|grep ${IMAGE_NAME}|grep ${VERSION_ID}|awk '{print $3}'`
                    if [[ -n "${ole_image_id}" ]]; then
                        docker rmi -f ${ole_image_id}
                    fi
                    docker build -f  Dockerfile --build-arg jar_name=${JAR_NAME} -t ${IMAGE_NAME}:${VERSION_ID} .
                    new_image_id=`docker images|grep ${IMAGE_NAME}|grep ${VERSION_ID}|awk '{print $3}'`
                    sudo docker tag ${new_image_id} ${IMAGE_ADDR}:${VERSION_ID}
                    sudo docker push ${IMAGE_ADDR}:${VERSION_ID}
                '''
            }
        }
        stage('run') {
            // 在应用服务器节点 test
            agent {
                node {
                    label 'test'
                    //customWorkspace "${SERVER_TARGET_PATH}"  //此参数会初始化目录 注意填写
                }
            }
            options {
                // 不让它切换到节点上自动从仓库拉取项目
                skipDefaultCheckout()
            }
            steps {
                echo 'pull image and docker run'
                withEnv(['JENKINS_NODE_COOKIE=dontKillMe']) {
                    sh '''
                        sudo docker login --username=yourusername --password=yourpassword ccr.ccs.tencentyun.com
                        sudo docker pull ${IMAGE_ADDR}:${VERSION_ID}

                        container_id=`docker ps|grep ${IMAGE_ADDR}:${VERSION_ID}|awk '{print $1}'`
                        if [ -n "${container_id}" ]; then
                            docker rm -f "${container_id}"
                        fi
                        old_pid=`ps -ef|grep ${JAR_NAME}|grep -v grep|awk '{print $2}'`
                        if [[ -n $old_pid ]]; then
                            kill -9 $old_pid
                        fi
                        old_image=`docker images|grep ${IMAGE_ADDR}|grep ${VERSION_ID}`
                        if [[ -n $old_image ]]; then
                            old_image_id=`echo ${old_image}|awk '{print $3}'`
                            docker rmi -f ${old_image_id}
                        fi
                        sudo docker run --name "${PROJECT_NAME}_${VERSION_ID}" -p 9001:8081 -d ${IMAGE_ADDR}:${VERSION_ID}
                    '''
                }
            }
        }
    }
}