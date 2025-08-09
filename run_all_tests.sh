#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running unit tests..."
pytest test_agents_pytest.py

echo "Running integration tests..."
pytest test_agent_integration.py
