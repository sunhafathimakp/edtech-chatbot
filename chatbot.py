import json
import logging

# Load dataset
with open("data/dataset.json", encoding="utf-8") as f:
    data = json.load(f)

# Logging setup
logging.basicConfig(
    filename="logs/chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

last_course = None


def normalize_text(text):
    """Basic typo correction"""
    corrections = {
        "colle": "college",
        "engg": "engineering",
        "med": "medical"
    }
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    return text


def get_response(user_input):
    global last_course

    text = normalize_text(user_input.lower().strip())

    # ------------------ Greeting ------------------
    if text in ["hi", "hello", "hey"]:
        response = "Hello! How can I assist you with courses or colleges today?"

    # ------------------ BEST COLLEGE (ALL TYPES) ------------------
    elif "best" in text:

        categories = ["engineering", "arts", "medical", "dental"]
        selected_category = None

        for cat in categories:
            if cat in text:
                selected_category = cat
                break

        locations = ["kochi", "kozhikode", "thrissur", "kannur", "trivandrum", "kollam", "muvattupuzha"]
        selected_location = None

        for loc in locations:
            if loc in text:
                selected_location = loc
                break

        filtered = []

        for college in data["colleges"]:
            name_lower = college["name"].lower()

            if selected_category and college["category"] != selected_category:
                continue

            if selected_location and selected_location not in name_lower:
                continue

            filtered.append(college)

        if filtered:
            top = sorted(filtered, key=lambda x: x["rating"], reverse=True)[:3]

            response = "Top colleges:\n"
            for c in top:
                response += f'{c["name"]} (Rating: {c["rating"]})\n'
        else:
            response = "No matching colleges found."

    # ------------------ Colleges ------------------
    elif "college" in text:
        colleges = [c["name"] for c in data["colleges"]]
        response = "Here are some colleges:\n" + "\n".join(colleges[:10])

    # ------------------ Degree Courses ------------------
    elif any(word in text for word in ["degree", "b.tech", "bsc", "mba", "bca", "mbbs"]):
        courses = []
        for college in data["colleges"]:
            for course in college["courses"]:
                courses.append(f'{course["name"]} - {college["name"]}')

        response = "Degree courses available:\n" + "\n".join(courses[:15])

    # ------------------ Hostel ------------------
    elif "hostel" in text:
        if last_course:
            response = f'Hostel info for {last_course["name"]}: {last_course.get("hostel", "Not specified")}'
        else:
            response = "Most colleges provide hostel or nearby accommodation (₹3000–6000/month)"

    # ------------------ Placement ------------------
    elif "placement" in text or "place" in text:
        if last_course:
            companies = last_course.get("placement_companies", [])
            if companies:
                response = f'Placement support includes {", ".join(companies)}.'
            else:
                response = "Placement details not available."
        else:
            response = "Placement support varies by domain (IT, healthcare, finance, core industries)."

    # ------------------ Fees ------------------
    elif "fee" in text or "fees" in text:
        if last_course:
            response = f'The fees for {last_course["name"]} is {last_course["fees"]}.'
        else:
            response = "Please specify the course name to get fee details."

    # ------------------ Short-term Courses ------------------
    elif "course" in text:

        matched_courses = []

        for course in data["short_term_courses"]:
            name = course["name"].lower()
            category = course["category"].lower()

            if name in text or category in text:
                matched_courses.append(course)

        if matched_courses:
            last_course = matched_courses[0]

            if len(matched_courses) == 1:
                c = matched_courses[0]
                response = (
                    f'{c["name"]} is a {c["duration"]} course with fees {c["fees"]}. '
                    f'Placement companies include {", ".join(c["placement_companies"])}.'
                )
            else:
                course_list = [f'{c["name"]} ({c["duration"]}, {c["fees"]})' for c in matched_courses]
                response = "Matching courses:\n" + "\n".join(course_list)
        else:
            all_courses = [f'{c["name"]} ({c["duration"]}, {c["fees"]})' for c in data["short_term_courses"]]
            response = "Available short-term courses:\n" + "\n".join(all_courses)

    # ------------------ Admission ------------------
    elif "admission" in text:
        response = "Admissions are open. Apply through official portals."

    # ------------------ Help ------------------
    elif "help" in text:
        response = "You can ask about colleges, courses, placements, hostel, or short-term courses."

    # ------------------ Default ------------------
    else:
        response = "Sorry, I didn't understand your query. Please try asking in a different way."

    logging.info(f"User: {user_input} | Bot: {response}")

    return response