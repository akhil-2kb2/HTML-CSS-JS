from mininet.topo import Topo

class ComplexTopo(Topo):
    def __init__(self):
        # Initialize the topology
        Topo.__init__(self)

        # Define the number of hosts
        hosts_per_switch = {
            's1': 10,
            's2': 10,
            's3': 5,
            's4': 5
        }

        # Add switches to the topology, including the central switch S5
        switches = {}
        for switch_name in hosts_per_switch.keys():
            switches[switch_name] = self.addSwitch(switch_name)
        switches['s5'] = self.addSwitch('s5')

        # Add hosts to the topology
        host_count = 1
        for switch_name, num_hosts in hosts_per_switch.items():
            for h in range(num_hosts):
                host = self.addHost(f'h{host_count}')
                self.addLink(host, switches[switch_name])
                host_count += 1

        # Add links between switches and the central switch S5
        self.addLink(switches['s1'], switches['s5'])
        self.addLink(switches['s2'], switches['s5'])
        self.addLink(switches['s3'], switches['s5'])
        self.addLink(switches['s4'], switches['s5'])

# Create a dictionary that can be used by Mininet to run the topology
topos = {'complextopo': (lambda: ComplexTopo())}
