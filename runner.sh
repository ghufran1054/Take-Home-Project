#!/usr/bin/env bash


config="$(python3 get_list_edge_nodes.py)"

if [ $? -eq 0 ]; then

    # Just make sure current connection is not up
    sudo wg-quick down wg0 > /dev/null 2> /dev/null
    echo "$config" | sudo tee /etc/wireguard/wg0.conf > /dev/null
    sudo wg-quick up wg0

fi
