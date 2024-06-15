import torch
import torch.optim as optim
import pytest
import numpy as np

from python.model import PolicyNet, select_action


input_dim = 16
output_dim = 3
embedding_dim = 8
device = "cpu"

@pytest.fixture
def model():
    return PolicyNet(input_dim, output_dim, embedding_dim)

def test_policy_net_output_shape(model):
    state = torch.randn((1, input_dim))
    action = torch.tensor([0], dtype=torch.long)

    output = model(state, action)
    
    assert output.shape == (1, output_dim), "Output shape is incorrect"
    assert torch.all(output >= 0) and torch.all(output <= 1), "Output values are not probabilities"
    assert torch.isclose(torch.sum(output), torch.tensor(1.0)), "Output probabilities do not sum to 1"

def test_select_action(model):
    state = np.random.rand(1, input_dim)
    action = 0

    new_action, log_prob = select_action(model, state, action, device)
    log_prob = log_prob.detach().item()

    assert log_prob < 0, "Log probability cannot be greater than 1"
    assert 0 <= new_action < output_dim, "Action value out of bounds"

def test_model_training(model):
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    state = np.random.rand(1, input_dim)
    action = 0

    log_probs = []

    action, log_prob = select_action(model, state, action, device)
    log_probs.append(log_prob)

    action, log_prob = select_action(model, state, action, device)
    log_probs.append(log_prob)

    loss = (-torch.stack(log_probs) * 1.0).sum()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    assert loss.detach().item() > 0, "Loss value less than 0"