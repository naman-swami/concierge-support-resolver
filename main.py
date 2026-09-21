import argparse
import json
import os
from triage.sla_priority_matrix import SupportTicketTriager

def main():
    parser = argparse.ArgumentParser(description="Concierge Support Resolver CLI")
    parser.add_argument("--demo", action="store_true", help="Triage sample customer support queue")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "tickets", "sample_support_queue.json")

    if args.demo:
        with open(data_file, "r") as f:
            tickets = json.load(f)
        print("=== CONCIERGE CUSTOMER SUPPORT SLA TRIAGE REPORT ===\n")
        for t in tickets:
            res = SupportTicketTriager.evaluate_ticket(t)
            print(f"Ticket [{t['ticket_id']}] Tier: {t['customer_tier']} | Subject: {t['subject']}")
            print(f"  Priority: {res['priority_tier']} | SLA Deadline: {res['sla_target_hours']} hour(s)")
            print(f"  Routing: {res['routing_action']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
