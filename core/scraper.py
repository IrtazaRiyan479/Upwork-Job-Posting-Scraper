from api.data_collecter import BrightData
from models.content_parser import ContentParser
from utils.message_sender import SendMessage

# Replace this with the Upwork URL you are monitoring
TARGET_URLS = [
    ""
]

#TODO: You need to implement code so that instead of saving single job_hitory.json, you will save job_hitory.json file for each job in Target_URLS

def main():
    for TARGET_URL in TARGET_URLS:
        print(f"Fetching base URL: {TARGET_URL}")
        
        # 1. Scrape the main page
        collector = BrightData(TARGET_URL)
        raw_html = collector.get_data()

        # 2. Parse the page and check for new jobs
        parser = ContentParser(raw_html)
        new_links = parser.check_new_open_jobs()

        if not new_links:
            print("No new jobs found. Exiting.")
            return

        all_new_jobs_data = []

        # 3. Scrape the specific details for each *new* job found
        for link in new_links:
            print(f"Scraping new job details: {link}")
            job_collector = BrightData(link)
            job_html = job_collector.get_data()

            job_parser = ContentParser(job_html)
            job_data = job_parser.read_job()
            
            # Add the link to the dictionary so we can include it in the message
            job_data['link'] = link 
            all_new_jobs_data.append(job_data)

        # 4. Format the notification message (HTML formatted for Telegram)
        final_message = "<b>🚀 New Upwork Jobs Found!</b>\n\n"
        for job in all_new_jobs_data:
            final_message += f"<b>Title:</b> {job.get('job_title', 'N/A')}\n"
            final_message += f"<b>Proposals:</b> {job.get('no_of_proposals', 'N/A')}\n"
            # Truncate description to keep message clean
            final_message += f"<b>Description:</b> {job.get('description', 'N/A')[:150]}...\n"
            final_message += f"<a href='{job.get('link', '')}'>Apply Here</a>\n\n"

        # 5. Send the notification
        print("Sending notifications...")
        messenger = SendMessage(all_new_jobs_data)
        messenger.msg = final_message
        messenger.send_notification()
        print("Done!")

if __name__ == "__main__":
    main()