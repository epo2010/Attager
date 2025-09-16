# agents/StrategySimulationAgent/main.py

from .executor import StrategySimulationAgentExecutor

def run_strategy_simulation_agent_task(task_name, payload):
    executor = StrategySimulationAgentExecutor()
    return executor.execute_task(task_name, payload)

if __name__ == "__main__":
    print("\n--- Running Strategy Simulation Agent: Simulate Alternative Scenarios ---")
    result = run_strategy_simulation_agent_task(
        "simulate_alternative_scenarios",
        {"scenario_id": "scenario_A", "params": {}}
    )
    print(f"Simulate Alternative Scenarios Result: {result}")
