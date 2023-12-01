import streamlit as st
import uuid

def generate_survey_link(survey_data):
    # Generate a unique survey ID using UUID
    survey_id = str(uuid.uuid4())
    # Store the survey data (you might want to save this to a database in a real-world scenario)
    survey_database = {"id": survey_id, "data": survey_data}
    # Display the survey link
    survey_link = f"Your survey has been created! Share the following link: [Survey Link](http://yourdomain.com/survey/{survey_id})"
    st.markdown(survey_link, unsafe_allow_html=True)

def survey_generator():
    st.title("Employee Engagement Survey Generator")

    # Collect survey details using a form
    with st.form("survey_form"):
        st.header("Survey Information")
        survey_name = st.text_input("Enter the survey name:")
        survey_description = st.text_area("Enter the survey description:")

        st.header("Employee Engagement Questions")
        engagement_question = st.text_input("Enter a question about engagement:")

        st.header("Job Needs Questions")
        job_needs_question = st.text_input("Enter a question about job needs:")

        st.header("Additional Questions")
        additional_questions = st.text_area("Enter additional questions (comma-separated):")
        additional_questions = [q.strip() for q in additional_questions.split(',') if q]

        submit_button = st.form_submit_button("Generate Survey")

    # Check if the form is submitted
    if submit_button:
        # Prepare survey data
        survey_data = {
            "name": survey_name,
            "description": survey_description,
            "questions": {
                "engagement": engagement_question,
                "job_needs": job_needs_question,
                "additional": additional_questions,
            },
        }

        # Generate and display the survey link
        generate_survey_link(survey_data)

if __name__ == "__main__":
    survey_generator()
