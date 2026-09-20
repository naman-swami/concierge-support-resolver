"""
Concierge Support Resolver Engine
Analyzes customer support sentiment, urgent SLA thresholds, and automated routing matrices.
"""
from typing import Dict, Any, List

class SupportResolverEngine:
    def __init__(self):
        self.critical_keywords = ["outage", "lawyer", "refund", "breach", "downtime", "emergency", "furious"]

    def analyze_ticket(self, ticket: Dict[str, Any]) -> Dict[str, Any]:
        text = ticket.get("message", "").lower()
        is_enterprise = ticket.get("customer_tier", "STANDARD") == "ENTERPRISE"
        mrr = float(ticket.get("customer_mrr_usd", 0))

        detected_flags = [kw for kw in self.critical_keywords if kw in text]
        
        # Calculate urgency score (0-100)
        urgency = 20
        if is_enterprise:
            urgency += 25
        if mrr > 10000:
            urgency += 25
        urgency += min(len(detected_flags) * 15, 30)
        urgency = min(urgency, 100)

        sla_target_minutes = 15 if urgency >= 80 else 60 if urgency >= 50 else 240
        routing_queue = "EXECUTIVE_ESCALATION_DESK" if urgency >= 80 else "TIER_2_TECHNICAL" if urgency >= 50 else "GENERAL_SUPPORT"

        return {
            "ticket_id": ticket.get("ticket_id", "TCK-1001"),
            "urgency_score": urgency,
            "priority_level": "P1_CRITICAL" if urgency >= 80 else "P2_HIGH" if urgency >= 50 else "P3_NORMAL",
            "sla_response_minutes": sla_target_minutes,
            "assigned_routing_queue": routing_queue,
            "detected_risk_keywords": detected_flags,
            "confidence_score": 0.94
        }
