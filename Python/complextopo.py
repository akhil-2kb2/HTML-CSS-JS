from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self, enable_all=True):
        Topo.__init__(self)

        no_of_host = 32
        no_of_switch = 5

        hosts = []
        switches = []

        # Add hosts to the topology
        for h in range(no_of_host):
            hosts.append(self.addHost('h' + str(h+1)))

        # Add switches to the topology
        for s in range(no_of_switch):
            switches.append(self.addSwitch('s' + str(s+1)))

        # Create links between hosts and switches
        for i in range(0, 11):
            self.addLink(hosts[i], switches[0])

        for i in range(11, 22):
            self.addLink(hosts[i], switches[1])

        for i in range(22, 27):
            self.addLink(hosts[i], switches[2])

        for i in range(27, 32):
            self.addLink(hosts[i], switches[3])

        # Connect every switch to switch[4] (fifth switch)
        for s in range(no_of_switch - 1):  # Iterate over switches 0 to 3
            self.addLink(switches[s], switches[4])


topos = {'mytopo': (lambda: MyTopo())}

