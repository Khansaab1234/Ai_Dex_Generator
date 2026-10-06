import re


def parse_ai_response(response_text):

    sections = {
        "Formula": "",
        "Explanation": "",
        "Optimization": "",
        "Difficulty": "",
        "Best Practices": "",
        "Warnings": ""
    }

    current_section = None

    for line in response_text.splitlines():

        line = line.strip()

        if line.startswith("Formula:"):
            current_section = "Formula"
            sections[current_section] = line.replace("Formula:", "").strip()

        elif line.startswith("Explanation:"):
            current_section = "Explanation"
            sections[current_section] = line.replace("Explanation:", "").strip()

        elif line.startswith("Optimization:"):
            current_section = "Optimization"
            sections[current_section] = line.replace("Optimization:", "").strip()

        elif line.startswith("Difficulty:"):
            current_section = "Difficulty"
            sections[current_section] = line.replace("Difficulty:", "").strip()

        elif line.startswith("Best Practices:"):
            current_section = "Best Practices"
            sections[current_section] = line.replace("Best Practices:", "").strip()

        elif line.startswith("Warnings:"):
            current_section = "Warnings"
            sections[current_section] = line.replace("Warnings:", "").strip()

        elif current_section:
            sections[current_section] += "\n" + line

    return sections