import pytest
from fastapi.exceptions import HTTPException

from app.api import verify_api_key


@pytest.fixture
async def test_verify_api_key():

    with pytest.raises(HTTPException):
        await verify_api_key('asdf')

    api_key = 'fake_api_key'

    result = await verify_api_key(api_key)
    assert result == api_key
