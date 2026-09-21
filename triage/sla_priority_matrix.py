"""
Customer Support Ticket Triage & SLA Priority Matrix
Evaluates sentiment urgency, customer contract tier, and ITIL SLA resolution deadlines.
"""
from typing import Dict, Any

class SupportTicketTriager:
    @staticmethod
    def evaluate_ticket(ticket: Dict[str, Any]) -> Dict[str, Any]:
        tier = ticket.get("customer_tier", "STANDARD")
        text = (ticket.get("subject", "") + " " + ticket.get("body", "")).lower()

        urgency_kws = ["down", "outage", "locked", "immediately", "critical", "losing money"]
        has_urgency = any(kw in text for kw in urgency_kws)

        if tier == "ENTERPRISE" and has_urgency:
            priority = "P1_CRITICAL"
            sla_hours = 1
            escalation = "PAGERDUTY_INCIDENT_CALL"
        elif has_urgency or tier == "ENTERPRISE":
            priority = "P2_HIGH"
            sla_hours = 4
            escalation = "SENIOR_ENGINEERING_QUEUE"
        else:
            priority = "P3_STANDARD"
            sla_hours = 24
            escalation = "GENERAL_SUPPORT_DESK"

        return {
            "ticket_id": ticket.get("ticket_id"),
            "priority_tier": priority,
            "sla_target_hours": sla_hours,
            "routing_action": escalation
        }
