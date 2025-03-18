ip a | grep wlp > /dev/null

while [ $? -eq 1 ]; do ip a | grep wlp > /dev/null; done
