import requests

headers = {
    "Authorization": "Bearer d18282f4-80ee-4598-8448-5562130f4c50",
    "Content-Type": "application/json"
}
data = {
    "zone": "upwork_job",
    "url": "https://www.upwork.com/jobs/Data-Analyst-for-Lead-Cleaning-Optimization_~022025088089905004526",
    "format": "raw"
}

response = requests.post(
    "https://api.brightdata.com/request",
    json=data,
    headers=headers
)
print(response.text)
