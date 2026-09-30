import streamlit as st

# ============================================================
# DIGITAL DETECTIVE
# Class XI Computer Science Project
# ============================================================

st.set_page_config(
    page_title="Digital Detective",
    page_icon="🕵️",
    layout="centered"
)

# ============================================================
# CASE DATABASE
# ============================================================

cases = {

    "Case 01 – The Missing Prototype": {
        "icon": "🔬",
        "location": "Research Laboratory",

        "description": (
            "A valuable prototype has disappeared from a research "
            "laboratory. Three people were present in the laboratory "
            "during the relevant time."
        ),

        "details": [
            "The laboratory door was locked after the incident.",
            "The security camera stopped recording for a short period.",
            "A red access card was found near the laboratory.",
            "A partial footprint was found near the storage room."
        ],

        "clues": {
            "Red Access Card":
                "The access card belonged to a laboratory employee.",
            "Security Camera":
                "The camera stopped recording between 6:20 PM and 6:35 PM.",
            "Footprint":
                "A footprint was found near the prototype storage room.",
            "Laboratory Log":
                "The laboratory log shows that the prototype was last "
                "checked at 6:15 PM."
        },

        "evidence": {
            "Access Record":
                "The access record shows that Aarav's card was used at 6:22 PM.",
            "Camera Record":
                "The camera was inactive from 6:20 PM to 6:35 PM.",
            "Footprint":
                "The footprint is consistent with a person who entered "
                "the storage area.",
            "Laboratory Log":
                "The prototype was present at 6:15 PM but missing later."
        },

        "suspects": (
            "Aarav Mehta",
            "Riya Sharma",
            "Kabir Rao"
        ),

        "responses": {
            "Aarav Mehta":
                "Aarav says he was checking equipment near the storage area.",

            "Riya Sharma":
                "Riya says she left the laboratory before 6:15 PM.",

            "Kabir Rao":
                "Kabir says he was working in another section of the laboratory."
        },

        "culprit": "Aarav Mehta"
    },


    "Case 02 – The Vanished Manuscript": {
        "icon": "📜",
        "location": "Museum Archive",

        "description": (
            "A rare historical manuscript mysteriously disappears "
            "from a museum archive. The archive was accessible only "
            "to authorised personnel."
        ),

        "details": [
            "The archive register shows an unusual entry.",
            "A storage cabinet was found unlocked.",
            "A visitor pass was discovered near the archive.",
            "The security system recorded movement after closing time."
        ],

        "clues": {
            "Archive Register":
                "The manuscript was last recorded at 4:30 PM.",
            "Visitor Pass":
                "A visitor pass was found near the archive entrance.",
            "Storage Cabinet":
                "The cabinet containing the manuscript was unlocked.",
            "Security System":
                "Movement was recorded shortly after closing time."
        },

        "evidence": {
            "Register":
                "The archive register contains an entry made shortly "
                "before the manuscript disappeared.",
            "Visitor Pass":
                "The pass belongs to a person who had access to the museum.",
            "Cabinet":
                "There are no signs of forced entry on the cabinet.",
            "Security Record":
                "The security record shows movement at 6:42 PM."
        },

        "suspects": (
            "Dev Malhotra",
            "Ananya Kapoor",
            "Rahul Verma"
        ),

        "responses": {
            "Dev Malhotra":
                "Dev says he left the museum before the archive closed.",

            "Ananya Kapoor":
                "Ananya says she was cataloguing books in another room.",

            "Rahul Verma":
                "Rahul says he was completing archive work after closing time."
        },

        "culprit": "Rahul Verma"
    },


    "Case 03 – The Locked Digital Vault": {
        "icon": "💻",
        "location": "Secure Computer Room",

        "description": (
            "A confidential digital file disappears from a secure "
            "computer system. The system records show activity "
            "during a restricted period."
        ),

        "details": [
            "The confidential file was accessed shortly before disappearing.",
            "The system recorded a login from an authorised account.",
            "A backup copy was created unexpectedly.",
            "The access log contains a suspicious time entry."
        ],

        "clues": {
            "Login Record":
                "An authorised account logged into the system at 8:18 PM.",
            "Access Log":
                "The confidential file was opened at 8:20 PM.",
            "Backup Copy":
                "A new copy of the file was created at 8:22 PM.",
            "System Log":
                "The file disappeared immediately after the backup."
        },

        "evidence": {
            "Login":
                "The login belongs to an authorised user.",
            "Access Time":
                "The confidential file was accessed at 8:20 PM.",
            "Backup":
                "A copy was created immediately before the original disappeared.",
            "System Activity":
                "The suspicious activity occurred during a restricted period."
        },

        "suspects": (
            "Neel Joshi",
            "Sara Iyer",
            "Vivek Shah"
        ),

        "responses": {
            "Neel Joshi":
                "Neel says he was not using the secure computer at that time.",

            "Sara Iyer":
                "Sara says she was working on a different computer.",

            "Vivek Shah":
                "Vivek says he accessed the system for routine work."
        },

        "culprit": "Vivek Shah"
    }
}


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "name" not in st.session_state:
    st.session_state.name = "Naada Bindu"

if "case" not in st.session_state:
    st.session_state.case = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "clues" not in st.session_state:
    st.session_state.clues = []

if "evidence" not in st.session_state:
    st.session_state.evidence = []

if "questioned" not in st.session_state:
    st.session_state.questioned = []

if "eliminated" not in st.session_state:
    st.session_state.eliminated = []

if "accusation" not in st.session_state:
    st.session_state.accusation = ""

if "case_started" not in st.session_state:
    st.session_state.case_started = False


# ============================================================
# FUNCTIONS
# ============================================================

def go_next():
    st.session_state.page += 1


def go_previous():
    if st.session_state.page > 1:
        st.session_state.page -= 1


def reset_game():
    st.session_state.page = 1
    st.session_state.name = "Naada Bindu"
    st.session_state.case = ""
    st.session_state.score = 0
    st.session_state.clues = []
    st.session_state.evidence = []
    st.session_state.questioned = []
    st.session_state.eliminated = []
    st.session_state.accusation = ""
    st.session_state.case_started = False


def add_score(points):
    st.session_state.score += points


def clean_name(name):
    return name.strip().title()


def count_items(items):
    total = 0

    for item in items:
        total += 1

    return total


def analyse_clue(clue_name, clue_text):
    words = clue_text.split()

    if len(words) > 8:
        return (
            f"🔎 Analysis of **{clue_name}**:\n\n"
            f"{clue_text}\n\n"
            "This clue contains useful information for the investigation."
        )

    else:
        return (
            f"🔎 Analysis of **{clue_name}**:\n\n"
            f"{clue_text}"
        )


def navigation_buttons():

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.page > 1:
            if st.button("⬅️ Previous"):
                go_previous()
                st.rerun()

    with col2:
        if st.session_state.page < 15:
            if st.button("Next ➡️"):
                go_next()
                st.rerun()


# ============================================================
# PAGE 1 – WELCOME
# ============================================================

if st.session_state.page == 1:

    st.title("🕵️ DIGITAL DETECTIVE")

    st.subheader("An Interactive Mystery Solver")

    st.write(
        "Welcome to Digital Detective — a Python-based mystery-solving "
        "application where you investigate fictional cases, examine clues, "
        "analyse evidence, question suspects and make a final accusation."
    )

    st.divider()

    st.info(
        "Your mission is to use logic and the available evidence "
        "to solve the selected mystery."
    )

    st.write("### 🔍 Investigation Flow")

    st.write(
        "Case Selection → Case Information → Examine Clues → "
        "Analyse Evidence → Investigate Suspects → Question Suspects → "
        "Eliminate Suspects → Final Accusation → Display Result"
    )

    if st.button("🚀 Start Investigation"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 2 – DETECTIVE REGISTRATION
# ============================================================

elif st.session_state.page == 2:

    st.title("🪪 Detective Registration")

    st.write("Enter your detective details.")

    name = st.text_input(
        "Detective Name",
        value="Naada Bindu"
    )

    if st.button("Register Detective"):

        if name.strip() == "":
            st.warning("Please enter your detective name.")

        else:
            st.session_state.name = clean_name(name)
            st.success(
                f"Welcome, Detective {st.session_state.name}! 🕵️"
            )

            if st.button("Continue Investigation"):
                go_next()
                st.rerun()


# ============================================================
# PAGE 3 – INSTRUCTIONS
# ============================================================

elif st.session_state.page == 3:

    st.title("📋 How to Investigate")

    st.write("### Rules of Investigation")

    instructions = [
        "Select one of the fictional mystery cases.",
        "Read the case information carefully.",
        "Examine the available clues.",
        "Analyse the evidence.",
        "Question the suspects.",
        "Eliminate suspects using the evidence.",
        "Make your final accusation.",
        "Check your final detective report."
    ]

    for number, instruction in enumerate(instructions, start=1):
        st.write(f"**{number}.** {instruction}")

    st.divider()

    st.info(
        "Remember: this is a fictional educational mystery-solving "
        "application. The cases and information are pre-programmed."
    )

    navigation_buttons()


# ============================================================
# PAGE 4 – INVESTIGATION MENU
# ============================================================

elif st.session_state.page == 4:

    st.title("🗂️ Investigation Menu")

    st.write(
        f"Welcome, **Detective {st.session_state.name}**."
    )

    st.write("Choose your investigation path.")

    menu_items = [
        "Select a Case",
        "Examine Clues",
        "Analyse Evidence",
        "Question Suspects",
        "Eliminate Suspects",
        "Make Final Accusation"
    ]

    for item in menu_items:
        st.write("🔹", item)

    st.divider()

    if st.button("📁 Proceed to Case Selection"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 5 – CASE SELECTION
# ============================================================

elif st.session_state.page == 5:

    st.title("📁 Case Selection")

    selected_case = st.selectbox(
        "Choose a mystery case:",
        list(cases.keys())
    )

    case = cases[selected_case]

    st.write(
        f"### {case['icon']} {selected_case}"
    )

    st.write(case["description"])

    if st.button("🔐 Open Case File"):

        st.session_state.case = selected_case
        st.session_state.case_started = True
        st.session_state.score = 0
        st.session_state.clues = []
        st.session_state.evidence = []
        st.session_state.questioned = []
        st.session_state.eliminated = []
        st.session_state.accusation = ""

        go_next()
        st.rerun()


# ============================================================
# PAGE 6 – OUTPUT 1: CASE INFORMATION
# ============================================================

elif st.session_state.page == 6:

    case = cases[st.session_state.case]

    st.title("📂 CASE INFORMATION")

    st.success("CASE FILE OPENED")

    st.write(f"**Detective:** {st.session_state.name}")
    st.write(f"**Case:** {st.session_state.case}")
    st.write(f"**Location:** {case['location']}")

    st.divider()

    st.write("### 📝 Case Description")

    st.write(case["description"])

    st.write("### 🔍 Initial Details")

    for detail in case["details"]:
        st.write("•", detail)

    st.success("Output 1: Case information displayed successfully.")

    if st.button("Continue to Clue Investigation"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 7 – CLUE SELECTION
# ============================================================

elif st.session_state.page == 7:

    case = cases[st.session_state.case]

    st.title("🔎 Examine Clues")

    st.write(
        "Select the clues you want to investigate."
    )

    selected_clues = st.multiselect(
        "Available Clues:",
        list(case["clues"].keys())
    )

    if st.button("Analyse Selected Clues"):

        st.session_state.clues = selected_clues

        points = len(selected_clues) * 5
        add_score(points)

        go_next()
        st.rerun()


# ============================================================
# PAGE 8 – OUTPUT 2: CLUE ANALYSIS
# ============================================================

elif st.session_state.page == 8:

    case = cases[st.session_state.case]

    st.title("🔍 CLUE ANALYSIS RESULT")

    if len(st.session_state.clues) == 0:

        st.warning(
            "No clues were selected. The investigation has limited information."
        )

    else:

        for clue in st.session_state.clues:

            st.write(
                analyse_clue(
                    clue,
                    case["clues"][clue]
                )
            )

            st.divider()

    st.write(
        f"**Clues examined:** "
        f"{count_items(st.session_state.clues)}"
    )

    st.success(
        f"Current Score: {st.session_state.score}"
    )

    st.success("Output 2: Clue analysis displayed successfully.")

    if st.button("Continue to Evidence"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 9 – EVIDENCE INVESTIGATION
# ============================================================

elif st.session_state.page == 9:

    case = cases[st.session_state.case]

    st.title("🧪 Evidence Investigation")

    st.write(
        "Select the pieces of evidence you want to examine."
    )

    selected_evidence = st.multiselect(
        "Available Evidence:",
        list(case["evidence"].keys())
    )

    if st.button("Examine Evidence"):

        st.session_state.evidence = selected_evidence

        points = len(selected_evidence) * 5
        add_score(points)

        go_next()
        st.rerun()


# ============================================================
# PAGE 10 – OUTPUT 3: EVIDENCE ANALYSIS
# ============================================================

elif st.session_state.page == 10:

    case = cases[st.session_state.case]

    st.title("🧪 EVIDENCE ANALYSIS RESULT")

    if len(st.session_state.evidence) == 0:

        st.warning(
            "No evidence was selected."
        )

    else:

        for evidence in st.session_state.evidence:

            st.write(f"### 🔬 {evidence}")

            st.write(
                case["evidence"][evidence]
            )

            st.divider()

    st.write(
        f"**Evidence analysed:** "
        f"{count_items(st.session_state.evidence)}"
    )

    st.success(
        f"Current Score: {st.session_state.score}"
    )

    st.success(
        "Output 3: Evidence analysis displayed successfully."
    )

    if st.button("Continue to Suspect Investigation"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 11 – SUSPECT INVESTIGATION
# ============================================================

elif st.session_state.page == 11:

    case = cases[st.session_state.case]

    st.title("👤 Suspect Investigation")

    st.write(
        "Choose a suspect to question."
    )

    suspect = st.selectbox(
        "Select Suspect:",
        case["suspects"]
    )

    if st.button("❓ Question Suspect"):

        if suspect not in st.session_state.questioned:

            st.session_state.questioned.append(suspect)

            add_score(5)

        st.session_state.selected_suspect = suspect

        go_next()
        st.rerun()


# ============================================================
# PAGE 12 – OUTPUT 4: SUSPECT RESPONSE
# ============================================================

elif st.session_state.page == 12:

    case = cases[st.session_state.case]

    st.title("🗣️ SUSPECT RESPONSE")

    suspect = st.session_state.get(
        "selected_suspect",
        case["suspects"][0]
    )

    st.write(f"### 👤 {suspect}")

    st.info(
        case["responses"][suspect]
    )

    st.write(
        "Use this response together with the clues and evidence "
        "to decide whether the suspect should be eliminated."
    )

    st.write(
        f"**Suspects questioned:** "
        f"{count_items(st.session_state.questioned)}"
    )

    st.success(
        f"Current Score: {st.session_state.score}"
    )

    st.success(
        "Output 4: Suspect response displayed successfully."
    )

    if st.button("Continue to Elimination"):
        go_next()
        st.rerun()


# ============================================================
# PAGE 13 – ELIMINATE SUSPECTS
# ============================================================

elif st.session_state.page == 13:

    case = cases[st.session_state.case]

    st.title("🚫 Eliminate Suspects")

    st.write(
        "Select suspects you believe can be eliminated "
        "based on the evidence."
    )

    selected_eliminations = st.multiselect(
        "Suspects:",
        case["suspects"]
    )

    if st.button("Confirm Eliminations"):

        for suspect in selected_eliminations:

            if suspect not in st.session_state.eliminated:

                st.session_state.eliminated.append(suspect)

                if suspect != case["culprit"]:
                    add_score(5)

        go_next()
        st.rerun()


# ============================================================
# PAGE 14 – FINAL ACCUSATION
# ============================================================

elif st.session_state.page == 14:

    case = cases[st.session_state.case]

    st.title("⚖️ Final Accusation")

    st.write(
        "Review your investigation and select the person "
        "you believe is responsible for the case."
    )

    st.write("### Investigation Summary")

    st.write(
        f"🔎 Clues examined: "
        f"{count_items(st.session_state.clues)}"
    )

    st.write(
        f"🧪 Evidence analysed: "
        f"{count_items(st.session_state.evidence)}"
    )

    st.write(
        f"👤 Suspects questioned: "
        f"{count_items(st.session_state.questioned)}"
    )

    st.write(
        f"🚫 Suspects eliminated: "
        f"{count_items(st.session_state.eliminated)}"
    )

    accusation = st.selectbox(
        "Your Final Accusation:",
        case["suspects"]
    )

    if st.button("🔨 Submit Final Accusation"):

        st.session_state.accusation = accusation

        if accusation == case["culprit"]:
            add_score(20)
        else:
            add_score(0)

        go_next()
        st.rerun()


# ============================================================
# PAGE 15 – OUTPUT 5: FINAL DETECTIVE REPORT
# ============================================================

elif st.session_state.page == 15:

    case = cases[st.session_state.case]

    st.title("🏆 FINAL DETECTIVE REPORT")

    st.success("INVESTIGATION COMPLETE")

    st.write(f"### 🕵️ Detective: {st.session_state.name}")

    st.write(f"**Case:** {st.session_state.case}")

    st.write(
        f"**Clues Examined:** "
        f"{count_items(st.session_state.clues)}"
    )

    st.write(
        f"**Evidence Analysed:** "
        f"{count_items(st.session_state.evidence)}"
    )

    st.write(
        f"**Suspects Questioned:** "
        f"{count_items(st.session_state.questioned)}"
    )

    st.write(
        f"**Suspects Eliminated:** "
        f"{count_items(st.session_state.eliminated)}"
    )

    st.write(
        f"### Final Accusation: "
        f"{st.session_state.accusation}"
    )

    st.divider()

    if st.session_state.accusation == case["culprit"]:

        st.success(
            "🎉 CASE SOLVED!\n\n"
            "Your final accusation matches the programmed solution."
        )

    else:

        st.error(
            "❌ CASE NOT SOLVED\n\n"
            "The final accusation does not match the programmed solution."
        )

    st.write(
        f"## ⭐ Final Score: {st.session_state.score}"
    )

    if st.session_state.score >= 60:

        st.info(
            "Excellent investigation. You used the available "
            "clues and evidence effectively."
        )

    elif st.session_state.score >= 40:

        st.info(
            "Good investigation. More evidence analysis "
            "could improve your result."
        )

    else:

        st.info(
            "Investigation completed. Try examining more clues "
            "and evidence in your next case."
        )

    st.divider()

    st.caption(
        "Digital Detective — Class XI Computer Science Project"
    )

    st.caption(
        "A fictional educational mystery-solving application."
    )

    if st.button("🔄 Start New Investigation"):

        reset_game()
        st.rerun()
