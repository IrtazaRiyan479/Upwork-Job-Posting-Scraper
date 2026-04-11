from bs4 import BeautifulSoup
import json
import os


class ContentParser:
    def __init__(self):
        return
    
    @staticmethod
    def read_job(content):
        soup = None
        while soup == None:
            soup = BeautifulSoup(content, 'html.parser')
        new_job_data = {}
        new_job_data["job_title"] = soup.title.get_text(strip=True) if soup.title else ""
        
        desc_tag = soup.find('div', attrs={'data-test': "Description"})
        new_job_data["description"] = desc_tag.get_text(strip=True) if desc_tag else ""
        
        prop_tag = soup.find('span', class_='title', string='Proposals:')
        if prop_tag:
            val_tag = prop_tag.find_parent('li').find('span', class_='value')
            new_job_data["no_of_proposals"] = val_tag.get_text(strip=True) if val_tag else ""
        else:
            new_job_data["no_of_proposals"] = ""
        return new_job_data

    @staticmethod
    def check_new_open_jobs(raw_content, url):
        soup = None
        while soup == None:
            soup = BeautifulSoup(raw_content, 'html.parser')
        
        if soup.title:
            main_job_title = soup.title.get_text(strip=True)
        else:
            main_job_title = url[:100] if url else "untitled_job"
            
        for char in ['|', '/', ':', '*', '?', '"', '<', '>', '\\']:
            main_job_title = main_job_title.replace(char, "-")

        open__jobs = soup.find('div', class_='other-jobs')
        open_jobs = open__jobs.select('section ul#otherOpenJobs li') if open__jobs else []
        total_open_jobs = []
        for job in open_jobs:
            anchor = job.find('strong').find('a')
            open_job_title = anchor.get_text(strip=True)
            link = "https://www.upwork.com" + anchor['href']
            total_open_jobs.append({
            "title": open_job_title,
            "link": link
            })

        DB_FILE = f"database/{main_job_title}.json"

        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                old_jobs = json.load(f)
        else:
            old_jobs = []

        new_links_found = []
        old_titles = [job['title'] for job in old_jobs]

        for job in total_open_jobs:
            if job['title'] not in old_titles:
                new_links_found.append(job['link'])

        with open(DB_FILE, "w") as f:
            json.dump(total_open_jobs, f)

        return new_links_found
