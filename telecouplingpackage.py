import pandas as pd
import statsmodels.api as sm

class TelecouplingComponent:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


class TelecouplingHypothesis:
    def __init__(self, description, systems, flows, agents, causes, effects):
        self.description = description
        self.systems = systems
        self.flows = flows
        self.agents = agents
        self.causes = causes
        self.effects = effects

    def test_hypothesis(self, data):
        X = data[['post_disaster', 'oilprice']]
        X = sm.add_constant(X)
        y = data['Last Price']
        model = sm.OLS(y, X).fit()
        return model.summary()

    def __str__(self):
        output = f"Hypothesis: {self.description}\n"
        output += f"Systems: {self.systems}\n"
        output += f"Flows: {self.flows}\n"
        output += f"Agents: {self.agents}\n"
        output += f"Causes: {self.causes}\n"
        output += f"Effects: {self.effects}\n"
        return output


class TelecouplingFramework:
    def __init__(self):
        self.hypotheses = []

    def add_hypothesis(self, hypothesis):
        self.hypotheses.append(hypothesis)

    def remove_hypothesis(self, index):
        if 0 <= index < len(self.hypotheses):
            del self.hypotheses[index]
        else:
            print("Invalid hypothesis index.")

    def test_hypotheses(self, data):
        for hypothesis in self.hypotheses:
            print(f"Testing hypothesis: {hypothesis.description}")
            print(hypothesis.test_hypothesis(data))

    def display_hypotheses(self):
        for i, hypothesis in enumerate(self.hypotheses, start=1):
            print(f"Hypothesis {i}:")
            print(hypothesis)