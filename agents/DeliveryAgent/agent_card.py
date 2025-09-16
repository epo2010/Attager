# agents/deliveryAgent/agent_card.py

class DeliveryAgentCard:
    name = "배송 Agent"
    description = (
        "상품 배송을 총괄 관리합니다. 배송 대상 상품을 확인하고, "
        "배송 완료 여부를 추적하며, 교환 및 리콜 상품의 배송 일정을 생성·관리합니다."
    )
    capabilities = [
        "identify_delivery_items",         # 배송 대상 상품 확인
        "track_completed_deliveries",      # 배송 완료 상태 추적
        "handle_exchange_deliveries",      # 교환 요청 상품 처리
        "manage_recall_deliveries",        # 리콜 상품 회수 및 배송 일정 관리
        "schedule_delivery_dates"          # 배송 예정일 생성 및 관리
    ]
    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "delivery_agent:"
