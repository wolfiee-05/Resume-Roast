import streamlit as st
import pdfplumber
import random
import docx

def roast_resume(extracted_text, used_roasts):
    roasts = []

    # A list of humorous roasts based on specific keywords
    contextual_roasts = []
    if 'leadership' in extracted_text.lower():
        contextual_roasts.append("Your leadership skills seem more like a suggestion than a requirement! 😅")
    if 'team player' in extracted_text.lower():
        contextual_roasts.append("I hope you're not just a team player; we need a team leader! 🏆")
    if 'self-motivated' in extracted_text.lower():
        contextual_roasts.append("Self-motivated? More like self-medicating! 💊")
    if 'dynamic' in extracted_text.lower():
        contextual_roasts.append("Dynamic? This is as dynamic as the 'dandiya' dance at Garba—lots of spinning but going nowhere! 💃")
    if 'problem solver' in extracted_text.lower():
        contextual_roasts.append("If you’re such a problem solver, why does your resume look like the plot twist in a typical Bollywood drama? 🎬")
    if 'detail-oriented' in extracted_text.lower():
        contextual_roasts.append("Detail-oriented? This looks like a Rangoli made by a toddler—more mess than design! 🎨")
    if 'hardworking' in extracted_text.lower():
        contextual_roasts.append("Hardworking? I see more effort in finding excuses to skip work than in actually working! 😅")
    if 'creative' in extracted_text.lower():
        contextual_roasts.append("Creative? This is as creative as remaking a classic movie—same old, just in a new wrapper! 🎥")
    if 'go-getter' in extracted_text.lower():
        contextual_roasts.append("Go-getter? More like go-get-the-remote-and-watch memes instead! 🍿")
    if 'communication skills' in extracted_text.lower():
        contextual_roasts.append("Communication skills? Your messages are as clear as a meme with no context! 📜")
    if 'passionate' in extracted_text.lower():
        contextual_roasts.append("Passionate? The only passion I see is for eating during festivals! 🍬")
    if 'analytical' in extracted_text.lower():
        contextual_roasts.append("Analytical? This analysis is as confusing as deciphering a bad roast! 🤔")
    if 'innovative' in extracted_text.lower():
        contextual_roasts.append("Innovative? This is about as innovative as a reused meme format! 🔄")
    if 'motivated' in extracted_text.lower():
        contextual_roasts.append("Motivated? The only thing you’re motivated to do is watch viral videos! 🎥")
    if 'dedicated' in extracted_text.lower():
        contextual_roasts.append("Dedicated? If this is dedication, I'd hate to see your procrastination during exams! 📚")
    if 'strategic' in extracted_text.lower():
        contextual_roasts.append("Strategic? This is as well-planned as a last-minute Holi celebration! 🎉")
    if 'results' in extracted_text.lower():
        contextual_roasts.append("Results-oriented? The only results I see are from your failed cooking experiments! 🍳")
    if 'collaborative' in extracted_text.lower():
        contextual_roasts.append("Collaborative? This is as cooperative as a cast of a multi-starrer fighting for screen time! 🎭")

    # If no contextual roasts were added, add generic roasts
    if not contextual_roasts:
        roasts.extend([
            "This resume is so bland, it could put a coffee addict to sleep! ☕",
            "This resume is so generic, it could be the next viral meme template! 😂"
        ])
    else:
        roasts.extend(contextual_roasts)

    # Select a roast that hasn't been used yet
    available_roasts = list(set(roasts) - used_roasts)
    if available_roasts:
        selected_roast = random.choice(available_roasts)
        used_roasts.add(selected_roast)
        return selected_roast
    else:
        return "You've run out of roasts! Try again later! 😂"

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

        used_roasts = set()
        roast = roast_resume(extracted_text, used_roasts)

        # Displaying the roast in a styled box
        st.markdown('<div class="macbook-box"><p class="roast-text">{}</p></div>'.format(roast), unsafe_allow_html=True)

        ats_score = check_ats_score(extracted_text)
        st.markdown('<p class="ats-score">ATS SCORE: {}/10</p>'.format(ats_score), unsafe_allow_html=True)

        if st.button("Show Tips"):
            show_ats_tips()
        
    except Exception as e:
        st.error(f"Error processing file: {e}")
