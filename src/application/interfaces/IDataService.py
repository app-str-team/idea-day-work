from abc import ABC, abstractmethod

class IDataService(ABC):
    @abstractmethod
    def get_ideas(self):
        pass
        # shall return the json object containing all the participated ideas
    
    def get_comments(self, idea_id: int):
        pass
    
    def get_total_votes(self, idea_id: int):
        pass
    
    def get_judges(self):
        pass
    
    def get_dasboard_info(self):
        pass
   