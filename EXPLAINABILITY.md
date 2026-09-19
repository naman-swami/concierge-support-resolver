# Explainability — concierge-support-resolver

## Decision Reasoning
Concierge evaluates support incidents by identifying semantic severity, matching error patterns against verified internal runbooks, and prioritizing resolution paths based on contractual SLA thresholds.

## Data Sources and Inputs Used
Zendesk/Jira ticket archives, knowledge base runbooks, SLA contractual commitments, and status page telemetry.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, concierge-support-resolver assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, concierge-support-resolver will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, concierge-support-resolver explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
concierge-support-resolver actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Direct System Access: Does not execute destructive database commands directly against client production tenants.
- Financial Refunds: Cannot authorize commercial contract refunds without explicit finance director approval.
- Unauthenticated Access: Refuses to disclose customer PII or account details without verified cryptographic session auth.
- Live Phone Audio: Operates exclusively on text, transcriptions, and API payloads.

## Uncertainty Quantification Approach
When customer error descriptions are vague or lack reproduction logs, Concierge explicitly identifies missing diagnostic parameters (e.g., Request IDs, timestamps) and generates targeted clarifying questions.
