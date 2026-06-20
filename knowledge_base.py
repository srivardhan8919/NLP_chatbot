faq_data = [
    {
        "questions": [
            "Tell me about Vaagdevi College of Engineering",
            "What is Vaagdevi College?",
            "Overview of Vaagdevi",
            "Give me some information about the college",
            "Who are you guys?"
        ],
        "answer": "Vaagdevi College of Engineering (VCE) is an autonomous, premier technical institution located in Warangal, Telangana, affiliated with JNTUH. We focus on innovation, research, and excellent industry collaborations."
    },
    {
        "questions": [
            "What undergraduate programs does Vaagdevi College offer?",
            "What courses are offered?",
            "What branches are there in BTech?",
            "List of degrees",
            "Do you have CSE?",
            "What degrees do you offer?"
        ],
        "answer": "We offer B.Tech programs in Computer Science & Engineering (CSE), Electronics & Communication (ECE), Electrical & Electronics (EEE), Civil Engineering, and Mechanical Engineering, as well as various M.Tech specializations."
    },
    {
        "questions": [
            "How do I apply for B.Tech programs?",
            "What is the admission process?",
            "How to get admission?",
            "Admissions process",
            "Can I apply online?"
        ],
        "answer": "Admissions are primarily based on the TS EAMCET state-level entrance exam for B.Tech, and TS PGECET (or GATE) for M.Tech. You can find counseling dates on the official TS EAMCET portal or our website."
    },
    {
        "questions": [
            "What's the recent placement record?",
            "Do you have good placements?",
            "Placement statistics",
            "Average salary package",
            "Highest package"
        ],
        "answer": "We have an active placement cell with excellent records! The recent average package is around ₹6.2 LPA, with the highest reaching ₹42 LPA. We maintain a high placement percentage annually."
    },
    {
        "questions": [
            "Which companies regularly recruit here?",
            "Top recruiters",
            "Which companies visit the campus?",
            "Are there good companies for placement?"
        ],
        "answer": "Top recruiters at Vaagdevi College include major tech giants like Microsoft, Amazon, TCS, Infosys, Wipro, and L&T."
    },
    {
        "questions": [
            "What hostel facilities are available?",
            "Are there hostels?",
            "Do you have a boys hostel?",
            "Do you have a girls hostel?",
            "Hostel fees"
        ],
        "answer": "Yes, we provide secure hostel facilities for girls. The hostels include furnished rooms and mess services. Hostel fees are approximately ₹23,000 per year (subject to office confirmation)."
    },
    {
        "questions": [
            "What is the fee structure?",
            "How much is the fee?",
            "Tuition fees",
            "Btech fee",
            "Cost of studying"
        ],
        "answer": "The fee structure varies depending on your admission category (Convenor quota vs. Management quota). For exact current fees, please check the latest brochure on our official website or contact the admissions office."
    },
    {
        "questions": [
            "What sports facilities does the campus have?",
            "Do you have a ground?",
            "Sports and games",
            "Is there a gym?"
        ],
        "answer": "We have excellent sports facilities including basketball courts, cricket grounds, indoor badminton courts, table tennis, and a campus gymnasium."
    },
    {
        "questions": [
            "What scholarship opportunities are available?",
            "Do you give scholarships?",
            "Financial aid",
            "Fee reimbursement"
        ],
        "answer": "Eligible students admitted through TS EAMCET convenor quota receive state government fee reimbursement. We also support students in applying for AICTE and merit-based scholarships."
    },
    {
        "questions": [
            "Are there extracurricular activities?",
            "Student clubs",
            "Hackathons",
            "Technical fests"
        ],
        "answer": "Absolutely! We host numerous student clubs (like AI Club, Robotics), cultural societies, annual hackathons, and technical fests to promote innovation and holistic development."
    },
    {
        "questions": [
            "What specific branches are there?",
            "Details about branches",
            "What are the BTech specializations?",
            "Is AI available?",
            "What branches do you have?"
        ],
        "answer": "Vaagdevi College offers highly specialized branches including B.Tech in CSE (Regular, AI & ML, Data Science), ECE, EEE, Mechanical, and Civil Engineering. We also offer M.Tech in VLSI, CSE, and an MBA program."
    },
    {
        "questions": [
            "Where is the college located?",
            "What is the location?",
            "College address",
            "How far from railway station?",
            "Where are you situated?"
        ],
        "answer": "The college is located at Bollikunta, Khila Warangal (Mandal), Warangal Urban District, Telangana – 506 005. It's situated on the Khammam highway, about 10 km from the Warangal railway station."
    },
    {
        "questions": [
            "What blocks are there?",
            "Block details",
            "Campus infrastructure",
            "Are there seminar halls?",
            "How is the campus built?"
        ],
        "answer": "The campus boasts excellent infrastructure with Wi-Fi enabled buildings, dedicated blocks for specific departments, advanced laboratories, several seminar halls, and a massive 600-seater central auditorium."
    },
    {
        "questions": [
            "Tell me about the library",
            "Is there a library?",
            "Do you have digital resources?",
            "Library facilities"
        ],
        "answer": "Our central library is state-of-the-art! It houses a vast collection of books and journals, and provides digital access to NPTEL video lectures, e-books, and e-journals via National Digital Library and JGATE."
    },
    {
        "questions": [
            "How are exams conducted?",
            "Tell me about semesters",
            "Are there internal exams?",
            "Academic system",
            "How many semesters?"
        ],
        "answer": "The academic year is divided into two semesters. The Examination Branch strictly manages all internal mid-term examinations and final end-semester examinations as per JNTUH guidelines."
    },
    {
        "questions": [
            "When are results declared?",
            "How do I check my results?",
            "Result dates",
            "Where to see marks?"
        ],
        "answer": "Results are typically declared 30 to 45 days after the end-semester exams. Students can check their marks securely via the official college portal and the CampX digital ecosystem."
    },
    # Persona Questions (Fallback if exact match fails in app.py)
    {
        "questions": [
            "Who are you?",
            "Tell me about yourself",
            "What are you?",
            "Are you a bot?"
        ],
        "answer": "I am the Vaagdevi College Inquiry Chatbot! I'm an AI assistant here to help you with any information you need about courses, admissions, placements, facilities, and more."
    },
    {
        "questions": [
            "Who created you?",
            "Who made you?",
            "Who developed you?"
        ],
        "answer": "I was developed to assist students and visitors with their queries about Vaagdevi College of Engineering."
    }
]

# We don't build flat lists here anymore. app.py will handle flattening so it can map back to the right answer index.