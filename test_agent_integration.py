import pytest
import os
from test_claude_agents import ScrumMasterAgent, SprintPlanningAgent

# Skip tests if no API key is available
pytestmark = pytest.mark.skipif(
    not os.getenv('ANTHROPIC_API_KEY'),
    reason="ANTHROPIC_API_KEY not set"
)

def test_scrum_master_can_call_sprint_planning():
    scrum_master = ScrumMasterAgent()
    sprint_planner = SprintPlanningAgent()

    # Mock the run method of the sprint planner to see if it gets called
    sprint_planner.run = lambda prompt: "Sprint plan generated"

    # Run the scrum master agent and check if it calls the sprint planner
    # The prompt for scrum_master.run should be something that would trigger
    # it to interact with the sprint planner.
    result = scrum_master.run("Please generate a sprint plan for the next iteration.")

    assert "Sprint plan generated" in result

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])