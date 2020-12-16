cat << EOF  >> /etc/sysctl.conf 
vm.max_map_count=262144
fs.file-max=65536
EOF

sysctl -p
