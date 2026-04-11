import requests

API_KEY = "75829c5f-25de-4b22-98a4-eefae9cfc120"
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
        
