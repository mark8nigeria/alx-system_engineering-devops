# How to Install and Configure UFW – An Un-complicated FireWall in Debian/Ubuntu

###  Basic Usage ufw check if ufw is installed using 
> sudo dpkg --get-selections | grep ufw

###  install it using apt command !!by default every incoming connection is denied
> sudo apt-get install ufw

###  check whether ufw is running or not
> sudo ufw status

###  Enabling / Disabling ufw
> sudo ufw enable

> sudo ufw disable

###  List the current ufw rules
> sudo ufw status verbose

###  How to Add ufw rules  to allow ssh connection !!by default every incoming connection is denied
> sudo ufw allow ssh

> sudo ufw status

###  If you have a lot of rules, and want to put numbers on every rules on the fly, use parameter numbered.
> sudo ufw status numbered

###  to allow tcp packet only? Then you can add the parameter tcp after the port number.
> sudo ufw allow ssh/tcp

###  to Deny rule. Let say you want to deny ftp rule
> sudo ufw deny ftp

###  Adding Specific Port ssh port on our machine from 22, into 2290. Then to allow port 2290
> sudo ufw allow

###  to add port-range into the rule. If we want to open port from 2290 – 2300 with tcp
> sudo ufw allow 2290:2300/tcp

###  if you want to use udp
> sudo ufw allow 2290:2300/udp

###  Adding Specific IP to add rules based on IP Address
> sudo ufw allow from 192.168.0.104
###  can also use a subnet mask to wider the range.
> sudo ufw allow form 192.168.0.0/24

###  allow access from anywhere and from any protocol to port 22.
> sudo ufw allow to any port 22

###  Combining Parameters combining IP Address, protocol and port
###  limit the connection only from IP 192.168.0.104, only protocol tcp and to port 22
> sudo ufw allow from 192.168.0.104 proto tcp to any port 22

###  Deleting Rules delete rules that match service ftp. So the 21/tcp which mean ftp port will be deleted.
> sudo ufw delete allow ftp

> sudo ufw delete allow ssh

> sudo ufw delete allow ssh

> sudo ufw delete allow 22/tcp

> sudo ufw status numbered

> sudo ufw delete 1

###  How to Reset Rules  to delete / reset all rules
> sudo ufw reset

### Advanced Functionality
* /etc/default/ufw: The main configuration for default policies, IPv6 support and kernel modules.
* /etc/ufw/before[6].rules: rules in these files are calculate before any rules added via the ufw command.
* /etc/ufw/after[6].rules: rules in these files are calculate after any rules added via the ufw command.
* /etc/ufw/sysctl.conf: kernel network tunables.
* /etc/ufw/ufw.conf: sets whether or not ufw is enabled on boot and sets the LOGLEVEL.

### I redirected traffic for port 80 to 8080 on my machine with
> sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-ports 8080

###  for the loopback interface do not pass via the PREROUTING chain. The following should work; run as root
> sudo iptables -t nat -A OUTPUT -o lo -p tcp --dport 80 -j REDIRECT --to-port 8080
### Simple just use iptables allowing both port 80 and 8080 then redirect 80 to 8080 make sure you are assigning to the correct nic.. in example I use eth0
> sudo iptables -A INPUT -i eth0 -p tcp --dport 80 -j ACCEPT
> sudo iptables -A INPUT -i eth0 -p tcp --dport 8080 -j ACCEPT
> sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080

###
> sudo iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080

> sudo iptables -A PREROUTING -t nat -p tcp --dport 8080 -j REDIRECT --to-ports 80

### instead of the iptables, You could try: 
> sudo ssh -gL 80:127.0.0.1:8080 localhost

```
iptables -A INPUT -i ens4 -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -i ens4 -p tcp --dport 8080 -j ACCEPT
iptables -A PREROUTING -t nat -i ens4 -p tcp --dport 8080 -j REDIRECT --to-port 80
```
