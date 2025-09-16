# agents/qualityAgent/agent_card.py

class QualityAgentCard:
    name = "품질 관리 Agent"
    description = (
        "반품·리콜 상품의 품질 검사를 수행하고 격리/처분을 결정하며, "
        "검사 결과에 따라 판매 가능 재고 상태를 관리합니다."
    )
    capabilities = [
        "process_return_quality_check",     # 반품 상품 QC 및 상태 판정
        "process_recall_quality_check",     # 리콜 상품 QC/격리/추적
        "manage_sellable_inventory",        # 판매 가능/불가 전환, 재고 반영
        "set_disposition_for_defect_items", # 재작업/폐기/재포장/재판매 결정
        "record_defect_codes_and_metrics"   # 결함 코드 기록 및 리포트 기초 데이터 축적
    ]
    # Ollama Mistral integration point (example)
    llm_model = "mistral"

    # Redis integration point (example)
    redis_key_prefix = "quality_agent:"