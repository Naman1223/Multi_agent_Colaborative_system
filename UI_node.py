from models import UI_plan_llm , UI_llm
from tools import markdown_to_text
from flask import Flask, render_template, request

ui_roadmap = markdown_to_text("roadmap.md")
ui_plan = UI_plan_llm(ui_roadmap)
ui = UI_llm(ui_plan)

with open("index.jsx","w",encoding="utf-8") as f:
    f.write(ui)