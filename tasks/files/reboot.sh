#!/bin/bash

while :; do
        wget -q --spider http://google.com

        if [ $? -eq 0 ]; then
                /usr/bin/ansible-pull -o -U https://github.com/educatm/educatmos.git -C master > /home/ansible/last_log
                /usr/bin/python3 /home/ansible/stats/stats.py
		[ $(uname -m) == "armv7l" ] && sudo su -c "cat /dev/null > /var/log/wtmp"
                break
        fi
        sleep 10
done
