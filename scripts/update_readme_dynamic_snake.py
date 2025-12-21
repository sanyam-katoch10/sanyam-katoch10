import os
from github import Github
import datetime
import openai

# ---------------- CONFIG ----------------
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
README_PATH = "README.md"
OUTPUT_PATH = "output/github-snake-dynamic.svg"

openai.api_key = OPENAI_API_KEY

# ---------------- FETCH WEEKLY ACTIVITY ----------------
g = Github(GITHUB_TOKEN)
user = g.get_user(GITHUB_USERNAME)
today = datetime.datetime.utcnow()
week_ago = today - datetime.timedelta(days=7)

commits = 0
for repo in user.get_repos():
    try:
        for commit in repo.get_commits(author=user, since=week_ago, until=today):
            commits += 1
    except:
        continue

prs = 0
for repo in user.get_repos():
    try:
        for pr in repo.get_pulls(state="closed", sort="updated", base="main"):
            if pr.user.login == GITHUB_USERNAME and pr.merged_at and week_ago <= pr.merged_at <= today:
                prs += 1
    except:
        continue

# ---------------- AI-GENERATED SUMMARY ----------------
prompt = f"""
Write a concise, friendly weekly GitHub activity summary for README.
This week I made {commits} commits, merged {prs} PRs.
Keep it casual, professional, and engaging.
"""
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role":"user","content":prompt}],
    te
