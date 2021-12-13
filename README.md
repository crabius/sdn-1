# summer-project

The aim of my project is to document the process for integrating the network traffic analyser Zeek with a software defined network controller (Like Ryu). By doing this, we can detect suspicious traffic and then quarantine malicious hosts.

Right now there is a basic integration between ryu and mininet. You can run a mininet virtual network of 3 hosts with a switch connected to a ryu controller by running 

```Bash
sudo ./fresh_install.sh
```

As for the ryu controller, it implements a learning switch where the traffic is blocked between hosts 2 and 3. This was just a wee excersize to get me up to speed with writing ryu applications. Note that this bash script assumes you are running it on a fresh ubuntu VM.
