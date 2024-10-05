from tools.Updater.Updater import FireBase
from tools.fetchingData import Retriever
from tools.model import Models
import time



if __name__ == "__main__":
    firebase = FireBase()
    data = firebase.retrieve_data()
    latitude,longitude = data.get('lat'), data.get('long')
    
    retriever = Retriever(latitude,longitude)
    retriever.getResponses()
    retriever.average()
    evotranspiration = retriever.averages[5]
    precipitation = retriever.averages[2]
    EP = precipitation * 0.8
    NIR = max(0,evotranspiration - EP)
    retriever.currentData()
    currentdata = {'Temperature':retriever.temperature,'Humidity':retriever.humidity,'Precipitation':retriever.precipitation,'SolarRadiation':retriever.solarRadiation}
    data.update(currentdata)
    print(data)
    
    
    time.sleep(120)
