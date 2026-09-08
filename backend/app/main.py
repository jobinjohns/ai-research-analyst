import logging

from app.llm.client import ask_llm

logging.basicConfig(
    level=logging.INFO
)

def main() ->  None:
    response = ask_llm(
        system_prompt = (
            "You are an AI research assistant."
            "Answer clearly and concisely."
        ),
        user_prompt=(
            "what are the major challenges facing"
            "the electric vehicle market in India?"
        ),
    )

    logging.info("LLM response:\n%s", response)

if __name__ == "__main__":
    main()