import streamlit as st
import pdfplumber
import random
import docx

used_roasts = set()

def roast_resume():
    # List of humorous roasts, including Indian meme references
    roasts = [
        "This resume reads like a script for a low-budget soap opera—lots of drama, but no real plot!",
        "I didn’t know resumes came with a side of cringeworthy clichés—this one’s a buffet!",
        "If this resume were a dish, it would be a mystery meat casserole—no one knows what’s in it, and everyone’s afraid to try it!",
        "This resume is like a GPS with no signal—just lost in the wilderness!",
        "Your experience section is like a magician's trick—now you see it, now you don’t!",
        "If this resume had a face, it would be the 'before' picture in a makeover show!",
        "This resume is so unoriginal, even Google couldn’t autocomplete it!",
        "Reading this resume is like watching paint dry—tedious and without excitement!",
        "If your achievements were any less impressive, they’d be hiding in the corner at a party!",
        "This resume is like a sitcom without a laugh track—awkward and a little uncomfortable!",
        "The skills section here is like a salad—mostly filler, with just a few croutons of actual substance!",
        "This resume could be the poster child for 'how to bore your potential employer to death!'",
        "This looks like a group project where everyone contributed, but nobody cared about the final product!",
        "Your resume is like a bad haircut—it’s just trying too hard and completely misses the mark!",
        "If you put as much effort into this resume as you do into avoiding hard work, you'd be CEO by now!",
        
        # Indian meme-inspired roasts
        "This resume is as confusing as a Bollywood plot twist—where did the character development go?",
        "If your resume was a chai, it would be missing the masala—just plain and boring!",
        "This resume looks like it was written by a person who learned English from watching Bollywood movies—lots of drama, no clarity!",
        "Your resume is like a cricket match that never ends—so much time wasted for such little result!",
        "This resume is like a long line at the local darshini—everyone’s waiting, but nobody’s getting anything done!",
        "Reading this is like watching the 'Kuch Kuch Hota Hai' climax—everyone’s confused and no one knows what happened!",
        "Your achievements are like my neighbor's noisy family—everyone knows they exist, but nobody really cares!",
        "This resume is as relatable as a 'Yeh Hai Mohabbatein' episode—too much melodrama and not enough sense!",
        "If this resume were an Indian meme, it would definitely be a 'Why this kolaveri di?' moment!",
        "This looks like the 'first draft' of a Karan Johar movie script—too much fluff, not enough substance!",
        "This resume is like the plot of 'Gully Boy'—great concept, but the execution is all over the place!"
    ]

    # Select a random roast
    selected_roast = random.choice(roasts)
    return selected_roast


def check_ats_score(extracted_text):
    keywords = [
        'Python', 
        'Machine Learning', 
        'Project Management', 
        'Data Analysis', 
        'Teamwork', 
        'Leadership',
        'Communication', 
        'Problem Solving', 
        'Collaboration', 
        'Creativity', 
        'Adaptability', 
        'Time Management', 
        'Customer Service', 
        'Critical Thinking', 
        'Negotiation', 
        'Technical Skills', 
        'Data Visualization', 
        'Agile', 
        'SQL', 
        'Java', 
        'JavaScript', 
        'HTML', 
        'CSS', 
        'Software Development', 
        'Networking', 
        'Research', 
        'Financial Analysis', 
        'Marketing Strategy', 
        'Content Creation', 
        'Public Speaking'
    ]  # Set the maximum score to 10 based on this list
    score = sum(1 for keyword in keywords if keyword.lower() in extracted_text.lower())
    return score

def show_ats_tips():
    tips = [
        "1. Use keywords from the job description to tailor your resume.",
        "2. Keep your formatting simple; avoid images and complex layouts.",
        "3. Use standard section headers like 'Experience,' 'Education,' and 'Skills.'",
        "4. List your skills and experiences in bullet points for clarity.",
        "5. Keep your resume to one page if you have less than 10 years of experience.",
        "6. Update your resume regularly with new skills and experiences.",
    ]

    # Convert tips into HTML string
    tips_html = ''.join(f"<div class='tip'>{tip}</div>" for tip in tips)
    
    # JavaScript for typewriter effect
    typewriter_js = f"""
    <script>
        let tips = `{tips_html}`.split("<div class='tip'>").filter(t => t).map(t => t.replace("</div>", ""));
        let index = 0;

        function typeWriter(tip, i = 0) {{
            if (i < tip.length) {{
                document.getElementById('tip-output').innerHTML += tip.charAt(i);
                setTimeout(() => typeWriter(tip, i + 1), 100);
            }} else {{
                index++;
                if (index < tips.length) {{
                    setTimeout(() => {{
                        document.getElementById('tip-output').innerHTML += '<br>'; // Add a line break
                        typeWriter(tips[index]);
                    }}, 1000); // Pause before next tip
                }}
            }}
        }}

        typeWriter(tips[index]);
    </script>
    """
    
    # Adding custom styles for tips
    tips_style = """
    <style>
        .tip {
            font-family: 'Times New Roman';
            font-size: 25px;
            color: #2E8B57;
            margin: 5px 0;
        }
        #tip-output {
            font-family: 'Times New Roman';
            font-size: 25px;
            color: #2E8B57;
            margin: 5px 0;
            white-space: pre-line; /* Preserve white space for line breaks */
        }
    </style>
    """
    
    # HTML container for output
    html_output = f"""
    <div id="tip-output"></div>
    {tips_style}
    {typewriter_js}
    """
    
    # Displaying the tips with the typewriter effect
    st.components.v1.html(html_output, height=300)

# Streamlit application setup
st.markdown(""" 
<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet"> 
<style>
    .stApp {
        background-color: #4CA1AF; /* Fallback for old browsers */
        background: -webkit-linear-gradient(to right, #C4E0E5, #4CA1AF); /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to right, #C4E0E5, #4CA1AF); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        min-height: 100vh; /* Ensures it covers full height */
        position: relative; /* Keeps the structure in place */
    }
    .custom-title {
        font-family: 'Lobster', cursive; /* Use your chosen aesthetic font */
        font-size: 48px;  
        color: #ffffff;  
        text-align: center;  
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);  
    }
    .macbook-box {
        border-radius: 12px;
        background-color: #f7f3ec;
        padding: 1rem; 
        width: 100%;
        max-width: 500px; 
        margin: 0 auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        position: relative;
        text-align: center;
    }
    .macbook-box:before {
        content: '';
        display: flex;
        gap: 8px;
        position: absolute;
        top: 10px;
        left: 15px;
        width: 10px;
        height: 10px;
        background-color: #ff5f56;
        border-radius: 50%;
        box-shadow: 15px 0 0 #ffbd2e, 30px 0 0 #27c93f;
    }
    .roast-text {
        font-family: 'Lobster'; /* Change font style for roast text */
        font-size: 24px;  
        color: #333;  
        margin: 10px 0;  
    }
    .ats-score {
        font-family: 'Times New Roman', cursive; /* Font for ATS score */
        font-size: 30px;  
        color: #555;  
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title with custom style
st.markdown('<h1 class="Lobster">🔥Roast My Resume!!!🔥</h1>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=['pdf', 'docx'])

if uploaded_file is not None:
    extracted_text = ""
    try:
        if uploaded_file.type == 'application/pdf':
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            doc = docx.Document(uploaded_file)
            for paragraph in doc.paragraphs:
                extracted_text += paragraph.text + "\n"

        used_roasts = set()  # Reset used roasts when a new file is uploaded
        roast = roast_resume()  # Call the function without arguments

        # Displaying the roast in a styled box
        st.markdown('<div class="macbook-box"><p class="roast-text">{}</p></div>'.format(roast), unsafe_allow_html=True)

        ats_score = check_ats_score(extracted_text)
        st.markdown('<p class="ats-score">ATS SCORE: {}/10</p>'.format(ats_score), unsafe_allow_html=True)

        if st.button("Show Tips"):
            show_ats_tips()
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
