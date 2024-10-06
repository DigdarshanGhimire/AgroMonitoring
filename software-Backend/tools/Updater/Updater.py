import firebase_admin
from firebase_admin import credentials, storage, firestore
import io
from PIL import Image
import time





class FireBase:
    def __init__(self) -> None:
        self.cred = credentials.Certificate("configs/firebaseConfig.json") #Path to the config file
        firebase_admin.initialize_app(self.cred, {
            'storageBucket': 'agroautomation-cc9c5.appspot.com'  
        })
        self.db = firestore.client()
        self.bucket = storage.bucket()
        
        self.statid = 'jbgqdGbHOhuMmoYkE7bi'
        self.imageid = 'TRZyDgXmkZ88Ctpdxt8x'
        
        
    def retrieve_data(self, status=True, images = False):
        if(images):
            id = self.imageid
            coll = 'images'
        else:
            id = self.statid
            coll = 'stats'
            
        doc_ref = self.db.collection(coll).document(id)
        doc = doc_ref.get()
        if doc.exists:
            stat = doc.to_dict()
            return stat
        else:
            return None
            
    def update_data(self, data):
        doc_ref = self.db.collection('stats').document(self.statid)
        doc_ref.set(data)
    
    
    def retrieve_image(self):
        blob = self.bucket.blob('plants.jpg')  
        image_data = blob.download_as_bytes()

        image = Image.open(io.BytesIO(image_data))

        image.save("images/plants.jpg")
    
    def delete_image(self):
        blob = self.bucket.blob('images/plant.jpg')  
        if blob.exists():
            blob.delete()
            return True
        else:
            return False
    

if __name__ == "__main__":
    app = FireBase()
    app.retrieve_image()
    
