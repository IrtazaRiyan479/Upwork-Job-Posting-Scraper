from bs4 import BeautifulSoup
import json
import os


class ContentParser:
    def __init__(self, raw_content):
        self.raw_content = raw_content
        self.new_job_data = {}

    def read_job(self):
        soup = BeautifulSoup(self.raw_content, 'html.parser')
        self.new_job_data["job_title"] = soup.title.string
        self.new_job_data["description"] = soup.find('div', attrs={'data-test': "Description"}).text
        self.new_job_data["no_of_proposals"] = soup.find('span', class_='title', string='Proposals:').find_parent('li').find('span', class_='value').text
        return

    def check_new_open_jobs(self):
        soup = BeautifulSoup(self.raw_content, 'html.parser')
        other_open_jobs = soup.find('div', class_='other-jobs').select('section ul#otherOpenJobs li')
        total_open_jobs = []
        for job in other_open_jobs:
            anchor = job.find('strong').find('a')
            open_job_title = anchor.get_text(strip=True)
            link = "https://www.upwork.com" + anchor['href']
            total_open_jobs.append({
            "title": open_job_title,
            "link": link
            })

        DB_FILE = "database/job_history.json"
        new_links_found = []

        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                old_jobs = json.load(f)
        else:
            old_jobs = []

        old_titles = [job['title'] for job in old_jobs]

        for job in total_open_jobs:
            if job['title'] not in old_titles:
                new_links_found.append(job['link'])
                print(f"NEW JOB FOUND: {job['title']}")

        with open(DB_FILE, "w") as f:
            json.dump(total_open_jobs, f)

        if new_links_found:
            print("\nLinks to new jobs:")
            for link in new_links_found:
                print(link)