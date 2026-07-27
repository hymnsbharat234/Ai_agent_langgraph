from app.services.security import hash_password, verify_password


def test_long_password_is_supported_by_bcrypt():
    password = "a" * 80

    hashed = hash_password(password)

    assert hashed != ""
    assert verify_password(password, hashed) is True


def test_multibyte_password_is_supported_by_bcrypt():
    password = "é" * 40

    hashed = hash_password(password)

    assert hashed != ""
    assert verify_password(password, hashed) is True
