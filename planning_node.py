from tools import read_markdown_file
from models import Planning_llm,assinger_llm
from rich.console import Console
from rich.markdown import Markdown

requirement = read_markdown_file("requirement.md")

planning = Planning_llm(requirement)


my_string = str(planning)

with open("plan.md","w",encoding="utf-8") as f:
    f.write(my_string)

plan = read_markdown_file("plan.md")

roadmap_detailed = assinger_llm(plan,requirement)

with open("roadmap.md","w",encoding="utf-8") as f:
    f.write(roadmap_detailed)


