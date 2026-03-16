import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.data_collecter import BrightData
from models.content_parser import ContentParser
from utils.message_sender import SendMessage

TARGET_URLS = [
    "https://www.upwork.com/freelance-jobs/apply/Operations-Assistant-Needed-for-Startups_~022033666226081862036/",
    "https://www.upwork.com/freelance-jobs/apply/Basic-Amazon-PPC-Audit_~022033491565568189400/"
]

def main():
    for url in TARGET_URLS:
        raw_data = BrightData.get_data(url)
        if raw_data:
            new_open_jobs_links = ContentParser.check_new_open_jobs(raw_data)

        if new_open_jobs_links:
            for link in new_open_jobs_links:
                new_open_job_data = ContentParser.read_job(BrightData.get_data(link))
                SendMessage.send_notification(new_open_job_data, link)


if __name__ == "__main__":
    main()