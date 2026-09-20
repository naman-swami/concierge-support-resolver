import pytest
from src.resolver_engine import SupportResolverEngine

def test_enterprise_emergency_ticket():
    engine = SupportResolverEngine()
    ticket = {
        "ticket_id": "T-1",
        "customer_tier": "ENTERPRISE",
        "customer_mrr_usd": 50000,
        "message": "Major system outage, emergency!"
    }
    res = engine.analyze_ticket(ticket)
    assert res["priority_level"] == "P1_CRITICAL"
    assert res["sla_response_minutes"] == 15
    assert res["assigned_routing_queue"] == "EXECUTIVE_ESCALATION_DESK"

def test_standard_ticket():
    engine = SupportResolverEngine()
    ticket = {
        "ticket_id": "T-2",
        "customer_tier": "STANDARD",
        "customer_mrr_usd": 200,
        "message": "How do I update my profile picture?"
    }
    res = engine.analyze_ticket(ticket)
    assert res["priority_level"] == "P3_NORMAL"
    assert res["sla_response_minutes"] == 240
