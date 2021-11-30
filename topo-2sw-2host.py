"""
topo-2sw-2host.py
implements a custom mininet topology with 2 switches, 2 hosts.
to initialize with this topology: (assuming you have mininet installed)
sudo mn —custom ./topo-2sw-2host.py —topo mytopo
"""

from mininet.topo import Topo

class MyTopo( Topo ):
	“Simple topology example”

	def build( self ):
		“Create custom network topography”
		
		#add hosts and switches
		leftHost = self.addHost( ‘h1’ )
		rightHost = self.addHost( ‘h2’ )
		leftSwitch = self.addSwitch( ’s3’ )
		rightSwitch = self.addSwitch( ’s4’ )

		#add links between nodes
		self.addLink( leftHost, leftSwitch)
		self.addLink( rightHost, rightSwitch)
		self.addLink( rightSwitch, rightHost)

topos = { ‘mytopo’ : (lambda: MyTopo() ) }
