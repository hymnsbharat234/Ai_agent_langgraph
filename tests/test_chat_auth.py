import unittest

from app.services.security import get_current_user_optional


class DummyRequest:
    def __init__(self, headers=None):
        self.headers = headers or {}


class ChatAuthTests(unittest.TestCase):
    def test_missing_authorization_header_returns_none(self):
        request = DummyRequest()
        self.assertIsNone(get_current_user_optional(request))


if __name__ == "__main__":
    unittest.main()
