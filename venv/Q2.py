
class Node:
    """ base class """
    def __init__(self, name, cost):

        self.name = name
        self.cost = cost

    def get_expected_cost(self):

        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_health_utility(self):

        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs):

        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):

        exp_cost = self.cost
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_health_utility(self):

        exp_health_utility=0
        i = 0
        for node in self.futureNodes:
            exp_health_utility += self.probs[i]*node.get_expected_health_utility()
            i += 1
        return exp_health_utility


class TerminalNode(Node):

    def __init__(self, name, cost, health_utility):

        Node.__init__(self, name, cost)
        self.health_utility=health_utility

    def get_expected_cost(self):

        return self.cost

    def get_expected_health_utility(self):

        return self.health_utility



class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes):
        Node.__init__(self, name, cost)
        self.futureNode = future_nodes

    def get_expected_costs(self):

        outcomes_cost = dict()
        for node in self.futureNode:
            outcomes_cost[node.name] = node.get_expected_cost()

        return outcomes_cost


    def get_expected_health_utility(self):

        outcomes_health_utility = dict()
        for node in self.futureNode:
            outcomes_health_utility[node.name] = node.get_expected_health_utility()

        return outcomes_health_utility


# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2
C2 = ChanceNode('C2', 35, [T1, T2], [0.7, 0.3])
# create C1
C1 = ChanceNode('C1', 25, [C2, T3], [0.2, 0.8])
# create C3
C3 = ChanceNode('C3', 45, [T4, T5], [0.1, 0.9])

# create D1
D1 = DecisionNode('D1', 0, [C1, C3])

# print the expect cost of C1
print("costs", D1.get_expected_costs(),"health utility", D1.get_expected_health_utility())
