import json
import argparse
from src.resolver_engine import SupportResolverEngine

def main():
    parser = argparse.ArgumentParser(description="Concierge Support Resolver CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated support triage")
    args = parser.parse_args()

    engine = SupportResolverEngine()
    sample_ticket = {
        "ticket_id": "TICKET-7731",
        "customer_tier": "ENTERPRISE",
        "customer_mrr_usd": 25000,
        "message": "Production database downtime affecting all our checkout flows! Need emergency intervention immediately."
    }

    report = engine.analyze_ticket(sample_ticket)
    print("="*60)
    print(" CONCIERGE SUPPORT RESOLUTION AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
