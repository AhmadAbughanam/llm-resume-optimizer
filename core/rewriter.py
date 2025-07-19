from llama_cpp import Llama
import os
import re
import yaml

# Load model once

with open("config.yaml", "r") as f:
    cfg = yaml.safe_load(f)


LLM = Llama(
    model_path=cfg["llm_model_path"],
    n_ctx=4096,
    n_threads=6,
    n_gpu_layers=0,  # or >0 if using GPU acceleration
    verbose=False,
)


# Dynamic segmentation
def segment_resume(text):
    sections = {
        "summary": r"(summary|profile|objective)",
        "experience": r"(experience|employment|work history|professional experience)",
        "skills": r"(skills|technologies|tools|competencies)",
        "education": r"(education|academics|certifications)",
        "projects": r"(projects|portfolio|case studies)",
    }

    text_lower = text.lower()
    segmented = {}
    last_match = 0
    keys = list(sections.keys())
    positions = {}

    for key in keys:
        pattern = re.compile(sections[key], re.IGNORECASE)
        match = pattern.search(text)
        if match:
            positions[key] = match.start()

    sorted_keys = sorted(positions, key=lambda x: positions[x])
    for i, key in enumerate(sorted_keys):
        start = positions[key]
        end = positions[sorted_keys[i + 1]] if i + 1 < len(sorted_keys) else len(text)
        segmented[key] = text[start:end].strip()

    return segmented


# Llama 3.2 chat format
def generate_rewrite(section_name, section_text, jd_text):
    messages = [
        {
            "role": "system",
            "content": f"You are an expert resume editor. Rewrite the user's resume section to improve alignment with a specific job description. Use a clear, concise, and professional tone.",
        },
        {
            "role": "user",
            "content": f"""Resume Section: {section_name}\n\n{section_text}""",
        },
        {"role": "user", "content": f"""Job Description:\n{jd_text}"""},
        {
            "role": "user",
            "content": "Rewrite this section to better match the job description, in the message you are responding with just send the section without any additional notes.",
        },
    ]

    output = LLM.create_chat_completion(messages, max_tokens=500)
    return output["choices"][0]["message"]["content"].strip()


# Generator for streaming
def rewrite_sections_streaming(resume_text, jd_text):
    segments = segment_resume(resume_text)
    if not segments:
        yield "Error", "Could not segment the resume. Use standard section headers like 'Experience', 'Skills', etc."
        return

    for section, content in segments.items():
        if not content.strip():
            continue
        rewritten = generate_rewrite(section, content, jd_text)
        yield section, rewritten
