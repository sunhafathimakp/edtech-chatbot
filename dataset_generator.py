import json
import random

engineering_colleges = [
"College of Engineering Trivandrum",
"Government Engineering College Thrissur",
"Government Engineering College Kozhikode",
"Model Engineering College Kochi",
"Rajagiri School of Engineering Kochi",
"TKM College of Engineering Kollam",
"Mar Athanasius College of Engineering Kothamangalam",
"Federal Institute of Science and Technology Kochi",
"LBS College of Engineering Kasaragod",
"SCMS School of Engineering Kochi",
"Amal Jyothi College of Engineering Kanjirappally",
"Saintgits College of Engineering Kottayam",
"Vidya Academy of Science and Technology Thrissur",
"Ilahia College of Engineering Muvattupuzha",
"MES College of Engineering Kuttippuram",
"Government Engineering College Kannur",
"Government Engineering College Idukki",
"College of Engineering Adoor",
"University College of Engineering Kariavattom",
"Government College of Engineering Barton Hill"
]

arts_colleges = [
"St Teresa’s College Kochi",
"Sacred Heart College Thevara",
"St Joseph’s College Devagiri",
"Farook College Kozhikode",
"Zamorin’s Guruvayurappan College Kozhikode",
"Mar Ivanios College Trivandrum",
"Christ College Irinjalakuda",
"Government College Thrissur",
"Brennen College Thalassery",
"Maharaja’s College Kochi",
"CMS College Kottayam",
"St Thomas College Thrissur",
"SN College Kollam",
"Government Victoria College Palakkad",
"Pazhassi Raja College Pulpally",
"Payyanur College Kannur",
"MMNSS College Kottiyam",
"St Albert’s College Kochi",
"NSS College Ottapalam",
"SD College Alappuzha"
]

medical_colleges = [
"Government Medical College Thiruvananthapuram",
"Government Medical College Kozhikode",
"Government Medical College Kottayam",
"Government Medical College Thrissur",
"Government Medical College Kannur",
"Government Medical College Ernakulam",
"Government Medical College Manjeri",
"Government Medical College Kollam",
"Amrita Institute of Medical Sciences Kochi",
"Aster Medcity Kochi",
"Jubilee Mission Medical College Thrissur",
"Pushpagiri Medical College Thiruvalla",
"KMCT Medical College Kozhikode",
"Malabar Medical College Kozhikode",
"Sree Gokulam Medical College Trivandrum",
"Believers Church Medical College Thiruvalla",
"Dr Somervell Memorial CSI Medical College Karakonam",
"Travancore Medical College Kollam"
]

dental_colleges = [
"Government Dental College Thiruvananthapuram",
"Government Dental College Kozhikode",
"Amrita School of Dentistry Kochi",
"Pushpagiri College of Dental Sciences",
"KMCT Dental College Kozhikode",
"Royal Dental College Chalissery",
"Annoor Dental College Muvattupuzha",
"Indira Gandhi Institute of Dental Sciences Nellikuzhi",
"Educare Institute of Dental Sciences Malappuram",
"Malabar Dental College Edappal"
]

engineering_courses = ["B.Tech Computer Science", "B.Tech Mechanical", "B.Tech Civil", "B.Tech Electrical", "B.Tech Electronics"]
arts_courses = ["BCA", "BSc Computer Science", "BCom", "BBA", "BA English"]
medical_courses = ["MBBS", "BSc Nursing", "B.Pharm", "BPT", "BSc MLT"]
dental_courses = ["BDS", "MDS", "Dental Hygiene", "Dental Technology", "Oral Pathology"]

# COMPANY GROUPS
it_companies = ["TCS", "Infosys", "Wipro", "UST", "Cognizant"]
core_companies = ["L&T", "Tata Projects", "Bosch"]
finance_companies = ["HDFC Bank", "ICICI Bank", "EY", "Deloitte"]
healthcare_companies = ["Apollo", "Aster", "Sunrise Hospital", "Lakeshore Hospital"]
dental_companies = ["Dental Clinics", "Private Dental Hospitals"]


def get_companies(category):
    if category == "engineering":
        return random.sample(it_companies + core_companies, 3)
    elif category == "arts":
        return random.sample(it_companies + finance_companies, 3)
    elif category == "medical":
        return random.sample(healthcare_companies, 3)
    elif category == "dental":
        return random.sample(dental_companies, 2)
    else:
        return ["General Company"]


# COLLEGE CREATOR
def create_college(name, category):

    if category == "engineering":
        courses = engineering_courses
        base_fee = random.randint(40000, 90000)

    elif category == "arts":
        courses = arts_courses
        base_fee = random.randint(15000, 35000)

    elif category == "medical":
        courses = medical_courses
        base_fee = random.randint(100000, 500000)

    else:
        courses = dental_courses
        base_fee = random.randint(150000, 400000)

    course_data = []

    for c in courses:
        course_data.append({
            "name": c,
            "fees": f"₹{base_fee + random.randint(-5000, 15000)}/year"
        })

    return {
        "name": name,
        "category": category,
        "rating": round(random.uniform(3.8, 4.7), 1),
        "placement_support": {
            "available": True,
            "companies": get_companies(category),
            "training": "Aptitude + Technical + Interview prep"
        },
        "hostel": {
            "college_hostel": random.choice(["Available", "Not Available"]),
            "nearby_hostel": f"₹{random.randint(3000,6000)}/month"
        },
        "courses": course_data
    }


# DATASET GENERATION
colleges = []

for c in engineering_colleges:
    colleges.append(create_college(c, "engineering"))

for c in arts_colleges:
    colleges.append(create_college(c, "arts"))

for c in medical_colleges:
    colleges.append(create_college(c, "medical"))

for c in dental_colleges:
    colleges.append(create_college(c, "dental"))


# SHORT TERM COURSES (UNCHANGED, JUST FIXED POSITION)
short_term_courses = [
    {
        "name": "Python Programming",
        "category": "IT",
        "duration": "3 months",
        "fees": "₹5000",
        "placement_companies": ["TCS", "Infosys", "Wipro", "UST"],
        "hostel": "Available near institute (₹3000/month)"
    },
    {
        "name": "Full Stack Development",
        "category": "IT",
        "duration": "6 months",
        "fees": "₹18000",
        "placement_companies": ["Zoho", "Freshworks", "Infosys", "TCS"],
        "hostel": "Available (₹4000/month)"
    }
]


# FINAL DATASET
dataset = {
    "colleges": colleges,
    "short_term_courses": short_term_courses
}


# SAVE
with open("data/dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)

print("Dataset generated successfully!")