import requests
import json
from colorama import Fore, Style

def parse_problems(problems: dict) -> str:
    res = ""
    for problem in problems:
        stat = problem['stat']
        title = f"title: {Fore.YELLOW}{stat['question__title']}{Fore.WHITE} (#{stat['question_id']})"
        if problem['paid_only']:
            title += f" {Fore.RED}[PAID ONLY]{Fore.WHITE}"
        if stat['is_new_question']:
            title += f" [NEW]"
        res += title
        submissions = f"total submissions: {Fore.GREEN}{stat['total_submitted']}{Fore.WHITE}"
        res += f"{(90-len(title))*' '}{submissions}{(50-len(submissions))*' '}"
        res += f"difficulty: {Fore.GREEN}{problem['difficulty']['level']}{Fore.WHITE}\n"

    return res


response = requests.get("https://leetcode.com/api/problems/all")
content = response.json()
with open("all.json", "w", encoding='utf-8') as f:
    json.dump(content, f, indent="\t", ensure_ascii=False)


output = (f"username: {content['user_name']}\n"
          f"problems solved: {content['num_solved']}\n"
          f"total problems: {content['num_total']}\n"
          f"problems:\n\n{parse_problems(content['stat_status_pairs'])}")
print(output.encode("utf-8", errors="replace").decode("utf-8"))