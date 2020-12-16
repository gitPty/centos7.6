
# 注意此处的els1 是部署的release名称。
helm upgrade els1 bitnami/elasticsearch --set sysctlImage.enabled=true

cat << EOF  >> /etc/sysctl.conf 
vm.max_map_count=262144
fs.file-max=65536
EOF

sysctl -p
