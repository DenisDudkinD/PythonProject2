import pytest
import src.services.actor_service as actor_service
from tests.mocks.mock_actor_repository import MockActorRepo

def test_get_all_actors_positive():
    repo = MockActorRepo()
    svc = actor_service.ActorService(repo)
    Actors = svc.get_all_actors()
    assert len(Actors) == 2

def test_find_actor_id_negative():
    id = 'sbjvhkidkbjhvsdkjh'
    repo = MockActorRepo()
    svc = actor_service.ActorService(repo)
    with pytest.raises(ValueError) as e:
        Actor = svc.get_actor_by_id(id)
    assert str(e.value) =='Invalid ID format'

def test_find_actor_id_positive():
    id = 'e81b0377-3c6b-4d79-b0a9-7921182ee89e'
    repo = MockActorRepo()
    svc = actor_service.ActorService(repo)
    actor = svc.get_actor_by_id(id)
    assert actor.full_name == 'test'
