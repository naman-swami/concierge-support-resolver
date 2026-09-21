import os
import pytest
from triage.sla_priority_matrix import SupportTicketTriager

def test_enterprise_outage_p1():
    ticket = {"ticket_id": "T1", "customer_tier": "ENTERPRISE", "subject": "Database down", "body": "Critical service locked"}
    res = SupportTicketTriager.evaluate_ticket(ticket)
    assert res["priority_tier"] == "P1_CRITICAL"
    assert res["sla_target_hours"] == 1

def test_standard_ticket_p3():
    ticket = {"ticket_id": "T2", "customer_tier": "FREE", "subject": "Feature request", "body": "Can you add a blue theme?"}
    res = SupportTicketTriager.evaluate_ticket(ticket)
    assert res["priority_tier"] == "P3_STANDARD"
    assert res["sla_target_hours"] == 24
