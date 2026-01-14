from models import UI_plan_llm , UI_llm
from tools import markdown_to_text
from flask import Flask, render_template, request
import time

# ui_roadmap = markdown_to_text("roadmap.md")
with open("roadmap.md","r",encoding="utf-8") as f:
    ui_roadmap = f.read()
time.sleep(4)
ui_plan = UI_plan_llm(ui_roadmap)
ui = UI_llm(ui_plan)

with open("index.jsx","w",encoding="utf-8") as f:
    f.write(ui)