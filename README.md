# Concierge Service Desk & ITIL 4 Triage Engine

> **IT Service Management (ITSM) Incident Priority Matrix & Customer Sentiment Classifier**  
> Streamlining Enterprise Support Queues, Escalation Runbooks, and Service Level Agreements.

---

### ITIL 4 Priority Matrix (Impact vs. Urgency)

```
                            INCIDENT IMPACT
                     HIGH          MEDIUM          LOW
                 ┌──────────────┬──────────────┬──────────────┐
           HIGH  │ P1: CRITICAL │ P2: HIGH     │ P3: MEDIUM   │
                 │ (1h SLA)     │ (4h SLA)     │ (12h SLA)    │
   INCIDENT      ├──────────────┼──────────────┼──────────────┤
   URGENCY MEDIUM│ P2: HIGH     │ P3: MEDIUM   │ P4: LOW      │
                 │ (4h SLA)     │ (12h SLA)    │ (24h SLA)    │
                 ├──────────────┼──────────────┼──────────────┤
           LOW   │ P3: MEDIUM   │ P4: LOW      │ P5: INQUIRY  │
                 │ (12h SLA)    │ (24h SLA)    │ (72h SLA)    │
                 └──────────────┴──────────────┴──────────────┘
```

---

### Sentiment & Churn Risk Heuristics

The triage evaluator analyzes incoming customer message streams for frustration markers and contract cancellation keywords:

- **Urgency Multipliers**: Explicit legal threat ("breach of contract", "litigation") or executive escalation ("C-level escalation") immediately promotes ticket to **P1**.
- **Churn Risk Flag**: Negative polarity sentiment combined with account ARR $> \$50,000$ triggers automated Account Executive notification.

---

### Support Ticket Triage Execution

```bash
# Ingest and triage benchmark customer support ticket queue
python resolve.py --demo

# Run ITSM classification unit tests
pytest tests/ -v
```

SLA definitions, business hours schedules, and escalation runbooks are detailed in [SLA_FRAMEWORK.md](SLA_FRAMEWORK.md).
