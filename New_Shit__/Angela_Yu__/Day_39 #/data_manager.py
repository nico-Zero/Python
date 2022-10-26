class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,data):
        self.filtered_data = list(data.values())[0]
    
    pass