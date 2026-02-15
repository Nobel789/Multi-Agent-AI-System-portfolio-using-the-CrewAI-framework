Multi-Agent-AI-Workflows
demonstrates how to orchestrate autonomous AI agents (like "Nephrologists" and "Nutritionists") to collaborate on complex tasks.

🤖 Medical Collaboration System
The core project simulates a Virtual Medical Board for Chronic Kidney Disease (CKD) management.

Agents:

Dr. Nephro (Kidney Specialist): Analyzes clinical labs (eGFR, Creatinine).

NutriCare (Renal Nutritionist): Generates kidney-safe, diabetes-friendly meal plans.

Dr. Mindwell (Psychologist): Provides coping strategies for chronic illness anxiety.

Workflow: Agents receive raw patient data (e.g., "54yo male, eGFR 25") and sequentially build a comprehensive care plan.

🏗️ Design Patterns
Sequential Process: A linear pipeline where the output of the "Researcher" becomes the input for the "Writer".

Role-Based Agent Design: Defining specific goals, roles, and backstories to steer LLM behavior.

🛠️ Tech Stack
Framework: CrewAI

LLM: GPT-4o-mini (via OpenAI API)

Environment: Python 3.10+
