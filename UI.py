from models import UI_llm
from tools import markdown_to_text
from flask import Flask, render_template, request

ui_roadmap = markdown_to_text("roadmap.md")
ui = UI_llm(ui_roadmap)

with open("index.jsx","w",encoding="utf-8") as f:
    f.write(ui)