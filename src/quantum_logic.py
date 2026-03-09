import pennylane as qml
from pennylane import numpy as np

# Define a 2-qubit simulator for local testing
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def variational_optimizer(params, data_input):
    """
    A Quantum Neural Network (QNN) circuit used for 
    high-dimensional data classification.
    """
    qml.AngleEmbedding(data_input, wires=range(2))
    qml.BasicEntanglerLayers(params, wires=range(2))
    return qml.expval(qml.PauliZ(0))