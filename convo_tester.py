from LLM import VeraAI   # make sure filename is llm.py
import sys

# =========================
# CONFIG
# =========================

MODEL_PATH = r"C:\Users\User\Documents\Fine_Tuning_Projects\LLAMA_LLM_3B"

# =========================
# INIT VERA
# =========================

vera = VeraAI(model_path=MODEL_PATH)

# =========================
# CHAT STATE
# =========================

messages = [
    {
        "role": "system",
        "content": vera.base_system_prompt
    }
]

print("=== VERA AI Chat ===")
print("Type 'exit' to quit.\n")

# =========================
# CHAT LOOP
# =========================

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("VERA: Goodbye.")
        break

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate reply using the SAME logic as production
    reply = vera.generate(messages)

    print("VERA:", reply, "\n")

    # Add assistant reply to memory
    messages.append({
        "role": "assistant",
        "content": reply
    })
