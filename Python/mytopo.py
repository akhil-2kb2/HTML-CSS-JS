from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Initialize the topology
        Topo.__init__(self)

        no_of_host = 3
        no_of_switch = 1

        hosts = []
        switches = []

        # Add hosts to the topology
        for h in range(no_of_host):
            hosts.append(self.addHost('h%s' % (h+1)))

        # Add switches to the topology
        for s in range(no_of_switch):
            switches.append(self.addSwitch('s%s' % (s+1)))

        # Create links between hosts and the switch
        self.addLink(hosts[0], switches[0])
        self.addLink(hosts[1], switches[0])
        self.addLink(hosts[2], switches[0])

# Create a dictionary that can be used by Mininet to run the topology
topos = {'mytopo': (lambda: MyTopo())}
