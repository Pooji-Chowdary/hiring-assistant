import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


st.set_page_config(page_title="Hiring Assistant ", page_icon="🤖")
st.title("🤖 TalentScout Hiring Assistant ")
st.write("Welcome! I’m your AI assistant to help with the initial screening process. Let's begin.")

# Load model once
@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")
    return tokenizer, model


tokenizer, model = load_model()

# Generate questions using local model
def generate_questions(tech_stack, level):
    prompt = (
        f"You are an expert technical interviewer. For a {level} candidate, "
        f"generate 3 relevant and practical technical interview questions for each technology "
        f"in this list: {tech_stack}. The questions should assess skill level appropriate to {level}."
        f"\n\nReturn a clearly numbered list grouped by technology."
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=512,
        num_beams=4,
        do_sample=False,
        early_stopping=True
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result


# Form input
with st.form("candidate_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, step=1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (e.g., Python, React, MySQL, Django)")
    submitted = st.form_submit_button("Submit")
    experience_level = st.selectbox(
    "Select Candidate Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if submitted:
    st.success(f"Thank you, {name}!")
    st.write(f"📧 Email: {email}")
    st.write(f"📱 Phone: {phone}")
    st.write(f"📍 Location: {location}")
    st.write(f"💼 Position: {position}")
    st.write(f"🧠 Experience: {experience} years")
    st.write(f"🛠️ Tech Stack: {tech_stack}")

    with st.spinner("Generating questions..."):
        questions = generate_questions(tech_stack, experience_level)
    st.subheader("🧪 Generated Technical Questions:")
    st.markdown(questions)
