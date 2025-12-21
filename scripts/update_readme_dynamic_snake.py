import os
from github import Github
import datetime
import openai
from openai import OpenAI
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


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role":"user","content":prompt}],
    temperature=0.6
)

summary = response.choices[0].message.content.strip()


# ---------------- DYNAMIC SNAKE SVG ----------------
glow_intensity = min(5 + commits, 25)  # Cap glow intensity
snake_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="100">
  <defs>
    <filter id="glow">
      <feDropShadow dx="0" dy="0" stdDeviation="{glow_intensity}" flood-color="#A855F7"/>
    </filter>
  </defs>
  <path d="M0 50 C100 0, 300 100, 700 50" stroke="#A855F7" stroke-width="8" fill="transparent" filter="url(#glow)">
    <animate attributeName="d" dur="4s" repeatCount="indefinite"
      values="M0 50 C100 0, 300 100, 700 50;
              M0 50 C100 20, 300 80, 700 50;
              M0 50 C100 0, 300 100, 700 50"/>
  </path>
</svg>
"""
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(snake_svg)

# ---------------- UPDATE README ----------------
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Update weekly activity
start_marker = "<!-- WEEKLY_ACTIVITY_START -->"
end_marker = "<!-- WEEKLY_ACTIVITY_END -->"
new_activity_section = f"{start_marker}\n{summary}\n{end_marker}"

if start_marker in content and end_marker in content:
    content = content.split(start_marker)[0] + new_activity_section + content.split(end_marker)[1]
else:
    content += "\n" + new_activity_section

# Update snake SVG
start_snake = "<!-- SNAKE_START -->"
end_snake = "<!-- SNAKE_END -->"
snake_img_tag = f"{start_snake}\n<p align='center'>\n  <img src='{OUTPUT_PATH}' width='700'/>\n</p>\n{end_snake}"
if start_snake in content and end_snake in content:
    content = content.split(start_snake)[0] + snake_img_tag + content.split(end_snake)[1]
else:
    content += "\n" + snake_img_tag

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)
