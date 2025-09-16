# agents/strategySimulationAgent/agent_card.py

class StrategySimulationAgentCard:
    name = "전략 & 시뮬레이션 Agent"
    description = (
        "각 에이전트의 응답을 종합해 최적의 전략을 설계하고, "
        "차량 유지보수·배송·품질·입고 정보를 바탕으로 시뮬레이션을 수행합니다."
    )
    capabilities = [
        "aggregate_agent_responses",              # 여러 에이전트의 응답 종합
        "propose_new_dispatch_and_delivery_plan", # 새로운 배차 및 배송 전략 제안
        "simulate_alternative_scenarios"          # 자원 부족/리콜 상황 등 대체 시뮬레이션
    ]
    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "strategy_simulation_agent:"