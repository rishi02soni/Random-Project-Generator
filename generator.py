import random

domains = [
    "AI",
    "Web Development",
    "Cybersecurity",
    "Cloud Computing",
    "Data Science",
    "Mobile Apps"
]

projects = [
    "Task Manager",
    "Portfolio Website",
    "Chatbot",
    "Expense Tracker",
    "Weather Dashboard",
    "Learning Platform"
]

def generate_project():
    domain = random.choice(domains)
    project = random.choice(projects)

    return f"Build a {project} using {domain}."
