import logging
from groq import Groq
from app.config import settings

logger = logging.getLogger(__name__)

client =Groq(api_key=settings.groq_api_key)


def ask_llm(system_prompt: str, user_prompt: str) -> str:
    """ Calling the groq chat completion model"""

    logger.info("Calling Groq model=%s",settings.groq_model)

    response = client.chat.completions.create(
        model = settings.groq_model,
        messages=[
            {
                "role": "system",
                "content" : system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0,
    )

    content =  response.choices[0].message.content

    if not content:
        raise ValueError("Groq returned an empty response.")

    return content 
