import csv


def save_to_file(jobs):
    # open : 파일을 여는 함수(없으면 생성)
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return None
