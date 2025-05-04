import pytest
from datetime import timedelta
from app.auth import (
    create_access_token,
    verify_token,
    pwd_context,
    SECRET_KEY,
    ALGORITHM
)

def test_password_hash_and_verify():
    password = "mysecret"
    hashed = pwd_context.hash(password)
    assert pwd_context.verify(password, hashed)
    assert not pwd_context.verify("wrongpassword", hashed)

def test_create_access_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=5))
    assert isinstance(token, str)
    assert len(token) > 10

def test_verify_valid_token():
    data = {"sub": "testuser"}
    token = create_access_token(data, expires_delta=timedelta(minutes=5))
    payload = verify_token(token)
    assert payload is not None
    assert payload["sub"] == "testuser"

def test_verify_invalid_token():
    invalid_token = "this.is.not.valid"
    payload = verify_token(invalid_token)
    assert payload is None
