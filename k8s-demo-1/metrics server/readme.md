$ helm fetch stable/metrics-server
$ tar -xvf metrics-server-2.7.1.tgz
$ cd metrics-server

helm install --name metric --namespace kube-system -f custom-values.yaml .