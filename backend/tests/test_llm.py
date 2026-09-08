from app.llm.client import ask_llm


def test_llm_connection():
    response =  ask_llm(
        system_prompt="You're a helpful AI research assistant",
        user_prompt="Explain what an AI research agent is in one sentence."
    )

    assert response
    assert isinstance(response, str)