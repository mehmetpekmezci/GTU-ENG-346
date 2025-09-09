#!/bin/bash
echo ""
echo "#########################################################################"
echo "############################# SSH KEYGEN       ##########################"
echo "#########################################################################"
echo ""

ssh-keygen

echo ""
echo "#########################################################################"
echo "############################# SSH KEY DISTRIBUTE ########################"
echo "#########################################################################"
echo ""

echo "dev-host-02
dev-host-03" >  nodes.txt
for node in $(cat nodes.txt)
do
    cat ~/.ssh/id_rsa.pub | ssh mpekmezci@$node "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
done

for node in $(cat nodes.txt)
do
    ssh mpekmezci@$node "hostname"
done
