git clone https://github.com/goharbor/harbor-helm
     //harbor helm下载地址
cd harbor-helm
git checkout 1.3.0 
     //切到1.3.0分支
qikqiak.yaml   自已定义的变量
创建命令  helm install --name harbor -f qikqiak-values.yaml . --namespace kube-ops