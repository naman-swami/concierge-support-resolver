import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="concierge-support-resolver",
    provider="openai",
    role="Tier-3 Escalation Specialist",
    goal="Triage incoming customer incidents, predict SLA breach probability, and synthesize verified troubleshooting action plans.",
    instructions="Operate according to OpenGAP specifications."
)
