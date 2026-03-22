import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.data_collecter import BrightData
from models.content_parser import ContentParser
from utils.message_sender import SendMessage

TARGET_URLS = [
    "https://www.upwork.com/freelance-jobs/apply/Basic-Amazon-PPC-Audit_~022033491565568189400/",
    "https://www.upwork.com/freelance-jobs/apply/Wix-Studio-Web-Designer-Needed-for-SEO-Mobile-Optimization-and-Site-Speed_~022033956900729326174",
    "https://www.upwork.com/freelance-jobs/apply/PageSpeed-fix_~022034488374860388707",
    "https://www.upwork.com/freelance-jobs/apply/generated-Product-Listing-Pictures_~022034472035155621905",
    "https://www.upwork.com/freelance-jobs/apply/Build-Simple-Chatbot-for-Website_~022034423696544337007",
    "https://www.upwork.com/freelance-jobs/apply/Amazon-New-launch-consultation_~022034320634119031919/",
    "https://www.upwork.com/freelance-jobs/apply/Video-Editing-Specialist-Needed-for-Creative-Projects_~022033561004595415785/",
    "https://www.upwork.com/freelance-jobs/apply/Wix-Website-Designer-and-Developer-for-Professional-Website-Redesign_~022034353069841338998",
    "https://www.upwork.com/freelance-jobs/apply/Data-Analysis-Specialist-for-Marketing-Insights_~022034314487697134198"
]

def main():
    for url in TARGET_URLS:
        print(f"MAIN URL ==== {url}")
        raw_data = BrightData.get_data(url)
        if raw_data is not None:
            new_open_jobs_links = ContentParser.check_new_open_jobs(raw_data)

        if new_open_jobs_links:
            for link in new_open_jobs_links:
                print(f"OPEN_JOB_URL ====== {link}")
                link_data = ContentParser.read_job(BrightData.get_data(link))
                SendMessage.send_notification(link_data, link)


if __name__ == "__main__":
    main()
