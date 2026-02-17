import pytest

from src.services.studio_service import StudioService
from src.domain.studio import Studio
from tests.mocks.mock_studio_repository import MockStudioRepo


def test_add_studio_negative():
    studio = 3
    repo = MockStudioRepo()
    svc = StudioService(repo)

    with pytest.raises(TypeError) as e:
        svc.add_studio(studio)  # type: ignore

    assert str(e.value) == "Expected Studio, got something else"


def test_get_studio_by_id_negative():
    studio_id = 3
    repo = MockStudioRepo()
    svc = StudioService(repo)

    with pytest.raises(TypeError) as e:
        svc.get_studio_by_id(studio_id)  # type: ignore

    assert str(e.value) == "Expected str, got something else"


def test_get_studio_by_name_negative():
    studio_name = 3
    repo = MockStudioRepo()
    svc = StudioService(repo)

    with pytest.raises(TypeError) as e:
        svc.get_studio_by_name(studio_name)  # type: ignore

    assert str(e.value) == "Expected str, got something else"


def test_remove_studio_by_id_negative():
    studio_id = 3
    repo = MockStudioRepo()
    svc = StudioService(repo)

    with pytest.raises(TypeError) as e:
        svc.remove_studio_by_id(studio_id)  # type: ignore

    assert str(e.value) == "Expected str, got something else"


def test_update_studio_negative():
    studio = 3
    studio_id = "some_id"
    repo = MockStudioRepo()
    svc = StudioService(repo)

    with pytest.raises(TypeError) as e:
        svc.update_studio(studio_id, studio)  # type: ignore

    assert str(e.value) == "Expected Studio, got something else"
