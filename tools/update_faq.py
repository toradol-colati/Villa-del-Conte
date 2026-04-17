with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* FAQ Accordion Styling */
.faq-accordion {
    text-align: left;
    margin-top: 30px;
}
.faq-item {
    border-bottom: 1px solid #e0e0e0;
    margin-bottom: 10px;
}
.faq-question {
    width: 100%;
    text-align: left;
    background: none;
    border: none;
    padding: 15px 0;
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 500;
    color: #4a9d5f;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: color 0.3s;
}
.faq-question:hover {
    color: #3b824e;
}
.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease-out, padding 0.4s ease-out;
    padding: 0;
}
.faq-answer p {
    color: #666;
    margin: 0;
    padding-bottom: 15px;
    line-height: 1.6;
}
.faq-question.active i {
    transform: rotate(180deg);
    transition: transform 0.3s;
}
.faq-question i {
    transition: transform 0.3s;
}
""")

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

faq_js = """
    // === FAQ ACCORDION ===
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(q => {
        q.addEventListener('click', () => {
            // Toggle current
            q.classList.toggle('active');
            const answer = q.nextElementSibling;
            if (q.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + "px";
            } else {
                answer.style.maxHeight = 0;
            }
        });
    });
"""
# Append right before the close of DOMContentLoaded
content = content.replace("const fadeElements = document.querySelectorAll('.fade-in-up');", faq_js + "\n    const fadeElements = document.querySelectorAll('.fade-in-up');")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated FAQ CSS and JS")
