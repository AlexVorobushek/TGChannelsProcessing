from Settings import Settings
import re

class FindMarkersResult(dict):
    def __add__(self, other):
        result = FindMarkersResult()
        for key in list(self.keys())+list(other.keys()):
            result[key] = self.get(key, 0) + other.get(key, 0)
        return result

class DataHandler:
    @staticmethod
    def find_markers_in_message(message: str) -> FindMarkersResult:
        result = FindMarkersResult()
        for marker in Settings.MessagesHandler.markers.keys():
            result[marker] = len(re.findall(Settings.MessagesHandler.markers[marker], message))
        return result
