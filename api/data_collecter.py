import requests

API_KEY = "1c50c3ba-651b-4aa3-baa3-35bf9bd635ca"

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
        
