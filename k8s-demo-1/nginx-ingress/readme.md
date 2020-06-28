$ helm fetch stable/nginx-ingress
$ tar -xvf nginx-ingress-1.4.0.tgz

helm install stable/nginx-ingress --namespace kube-system --name nginx-ingress -f custom.yaml

kubectl apply -f ngdemo.yaml