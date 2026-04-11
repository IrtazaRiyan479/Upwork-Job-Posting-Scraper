import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.data_collecter import BrightData
from models.content_parser import ContentParser
from utils.message_sender import SendMessage

TARGET_URLS = [
    "https://www.upwork.com/freelance-jobs/apply/GoHighLevel-GHL-Specialist-Funnels-Automation-Email-Marketing_~022039045451332444059/",
    "https://www.upwork.com/freelance-jobs/apply/Video-Editor-Short-Form-Content-Creator-Reels-TikTok-YouTube-Shorts_~022039108090355043475/",
    "https://www.upwork.com/freelance-jobs/apply/Webflow-Website_~022039056969403495332/",
    "https://www.upwork.com/freelance-jobs/apply/Marketing-Strategy-Consultant-CRM-Expert-for-Lead-Generation-Automation-Systems_~022038964057969254299/",
    "https://www.upwork.com/freelance-jobs/apply/Virtual-Assistant-Needed-for-Ongoing-Project_~022039053705349423003/",
    "https://www.upwork.com/freelance-jobs/apply/Shopify-Expert-Needed-for-Conversion-Focused-Store-Redesign_~022038943470851768786/",
    "https://www.upwork.com/freelance-jobs/apply/Flutter-Image-Generation-Performance-Expert-Needed-Reduce-Multi-Image-Response-Delay_~022039258829262491229/",
    "https://www.upwork.com/freelance-jobs/apply/Klaviyo-Expert-Needed-Win-Back-Upsell-Flow-Setup_~022039256541658131566/",
    "https://www.upwork.com/freelance-jobs/apply/Online-Course-Creation-Expert-Needed_~022039252441048092253/",
]

def main():
    for url in TARGET_URLS:
        print(f"MAIN URL ==== {url}")
        raw_data = None
        while raw_data == None:
            raw_data = BrightData.get_data(url)
        new_open_jobs_links = ContentParser.check_new_open_jobs(raw_data, url)

        if new_open_jobs_links:
            for link in new_open_jobs_links:
                print(f"OPEN_JOB_URL ====== {link}")
                link_data = ContentParser.read_job(BrightData.get_data(link))
                SendMessage.send_notification(link_data, link)


if __name__ == "__main__":
    main()
