import requests

API_KEY = "d18282f4-80ee-4598-8448-5562130f4c50"
class BrightData():
    
    @staticmethod
    def get_data(link):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "zone": "upwork_job",
            "url": link,
            "format": "raw"
        }

        response = requests.post(
            "https://api.brightdata.com/request",
            json=data,
            headers=headers
        )
        
        return response.text
        
