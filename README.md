# Concierge Customer Support & SLA Resolver

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Support](https://img.shields.io/badge/Domain-Customer_Success_ITIL-blue.svg)](docs/itil_incident_management.md)
[![Standard](https://img.shields.io/badge/Standard-ITIL_4_Incident-green.svg)](docs/itil_incident_management.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An automated ITIL 4 service desk support ticket triage and SLA routing engine evaluating customer tier commitments, sentiment urgency, and escalation triggers.

```
                    ┌─────────────────────────┐
                    │ Inbound Support Tickets │
                    │ (Subject, Body, Tier)   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ triage/sla_priority     │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Urgency Detection  │         │  SLA Allocation     │
      │  (Production Down)  │         │   (P1: 1h / P3: 24h)│
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Escalation Action       │
                    │ (PagerDuty / Tier Desk) │
                    └─────────────────────────┘
```

## Features

- **ITIL 4 Incident Classification**: Stratifies inbound issues into P1 (Critical), P2 (High), and P3 (Standard).
- **Automated Escalation Dispatch**: Routes enterprise outages directly to on-call engineering.
- **Queue Benchmarks**: Includes real enterprise and consumer support ticket streams.

## Directory Structure

```
concierge-support-resolver/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint support triage provenance
├── triage/
│   └── sla_priority_matrix.py       # ITIL ticket classifier
├── fixtures/
│   └── tickets/
│       └── sample_support_queue.json # Benchmark ticket queue
├── docs/
│   └── itil_incident_management.md  # ITIL service standard
├── tests/
│   └── test_agent.py                # Support triage test suite
├── resolve.py                          # Support desk CLI
└── requirements.txt
```

## Quick Start

```bash
# Run support triage tests
pytest tests/ -v

# Triage benchmark support queue
python resolve.py --demo
```
