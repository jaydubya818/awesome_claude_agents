
import pytest
import os
import json
from test_claude_agents import *

# Skip tests if no API key is available
pytestmark = pytest.mark.skipif(
    not os.getenv('ANTHROPIC_API_KEY'),
    reason="ANTHROPIC_API_KEY not set"
)

def load_test_config():
    with open('test_config.json', 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("agent_test", load_test_config()["agent_tests"])
def test_agent(agent_test):
    agent_name = agent_test["agent_name"]
    prompt = agent_test["prompt"]
    expected_keywords = agent_test["expected_keywords"]

    # Get the agent class from its name
    agent_class = globals()[agent_name]
    agent = agent_class()

    # Run the agent with the prompt
    result = agent.run(prompt)

    # Check if the result contains the expected keywords
    for keyword in expected_keywords:
        assert keyword in result.lower()

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
