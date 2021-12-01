"""
define a network of 3 hosts and integrate with an external ryu controller
author: Ben Cravens
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSController

class single_switch_topo(Topo):
    "build single switch topology"
    def build(self, n=3):
        #add switch
        switch = self.addSwitch('s1')
        #add hosts
        for i in range(n):
            host_str="h{}".format(i+1)
            host = self.addHost(host_str)
            self.addLink(host,switch)

class ryu_net():
    "uses single switch topology to build a network controlled by external ryu SND controller"
    def __init__(self, hostnum=3):
        #build our network
        self.topo=single_switch_topo(hostnum)
        self.net = Mininet(topo=topo, controller=OVSController)
        self.net.start()
        #run ifconfig on each host
        for i in range(hostnum):
            host_str = "h{}".format(i+1)
            host = self.net.get(host_str)
            result = host.cmd('ifconfig')
            print(result)
        CLI(self.net)
        
    def stop(self):
        #stop network
        self.net.stop()

    def connect_ryu(self):
        #connect to external ryu controller..
        self.net.addController('co', controller=RemoteController, ip='127.0.0.1', port=6633)                                                   

if __name__=="__main__":
    my_net = ryu_net()
    ryu_net.stop()
