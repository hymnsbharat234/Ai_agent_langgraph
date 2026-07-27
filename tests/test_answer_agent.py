import unittest
from types import SimpleNamespace
from unittest.mock import patch

import app.agents.answer_agent as answer_agent_module
from app.agents.answer_agent import answer_agent


class AnswerAgentTests(unittest.TestCase):
    def test_answer_agent_does_not_persist_chat_directly(self):
        mock_llm = SimpleNamespace(invoke=lambda _prompt: SimpleNamespace(content="Hello from the assistant"))

        with patch.object(answer_agent_module, "llm", mock_llm):
            state = {
                "question": "Hello there",
                "retrieved_docs": "",
                "history": [],
                "user_id": "user-123",
            }

            answer_agent(state)

        self.assertEqual(state["answer"], "Hello from the assistant")


if __name__ == "__main__":
    unittest.main()
