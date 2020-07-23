kubectl apply -f kube-logging.yaml

kubectl apply -f elasticsearch-svc.yaml

kubectl apply -f elasticsearch-pvc.yaml

kubectl apply -f elasticsearch-storageclass.yaml

kubectl apply -f elasticsearch-statefulset.yaml

临时测试

kubectl port-forward es-cluster-0 9200:9200 --namespace=logging

重开一个端口

curl http://localhost:9200/_cluster/state?pretty

kubectl apply -f kibana.yaml

kubectl apply -f fluentd-configmap.yaml
kubectl apply -f fluentd-daemonset.yaml
