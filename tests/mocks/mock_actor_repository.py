from src.domain.actor import Actor

class MockActorRepo:
    def add_actor(self, actor:Actor):
        return 'mock_id'
    
    def get_all_actors(self) -> list[Actor]:
        return [Actor(full_name='test',nationality = 'test'),Actor(full_name='test2',nationality = 'test2')]
    
    def get_actor_by_name(self,query:str):
        return [Actor(full_name='test',nationality = 'test')]
    
    def get_actor_by_id(self,actor_id:str)-> Actor:
        return Actor(full_name = 'test', nationality = 'test')      
      
    def remove_actor_by_id(self,actor_id:str):
        return Actor(full_name = 'test', nationality = 'test')
    
    def update_actor(self,actor:Actor):
        pass

    def add_seed_records(self, actors: list[Actor]) -> None:
        return