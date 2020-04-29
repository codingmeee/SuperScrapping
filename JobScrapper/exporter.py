import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        try:
            writer.writerow(list(job.values()))
        except:
            print(list(job.values()))
    print(jobs)
    return