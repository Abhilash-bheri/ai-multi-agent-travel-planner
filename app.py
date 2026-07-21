import streamlit as st
import time
from main import builder

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
    background:#EAF4FF;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:2rem;
}

.hero{
    background:linear-gradient(135deg,#2563EB,#3B82F6);
    color:white;
    border-radius:20px;
    padding:35px;
    box-shadow:0px 8px 25px rgba(0,0,0,.08);
    margin-bottom:25px;
}

.title{
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:white;
}

.subtitle{
    text-align:center;
    color:#E5E7EB;
    font-size:18px;
}

.result-card{
    background:white;
    border-radius:18px;
    padding:25px;
    box-shadow:0px 5px 18px rgba(0,0,0,.08);
    background:#FFFFFF;
    border-left:8px solid #2563EB;
}

.agent-card{
    padding:18px;
    border-radius:15px;
    margin-bottom:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,.08);
    background:#F8FAFC;
    border-left:6px solid #3B82F6;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:25px;
}
            /* Make all text inside cards dark */
.agent-card,
.agent-card *{
    color:#1E293B !important;
}

.result-card,
.result-card *{
    color:#1E293B !important;
}

/* Headings */
h1,h2,h3{
    color:#1E293B !important;
}

/* Metrics */
[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:12px;
}

[data-testid="metric-container"] *{
    color:#1E293B !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#EAF4FF;
}

section[data-testid="stSidebar"] *{
    color:#1E293B !important;
}

/* Text input */
.stTextInput input{
    background:white;
    color:#1E293B !important;
}

/* Download button */
.stDownloadButton button{
    background:#2563EB;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class='hero'>

<div class='title'>
✈️ AI Multi-Agent Travel Planner
</div>

<div class='subtitle'>
Powered by LangGraph • Gemini 2.5 Flash • Tavily • AviationStack
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("⚙️ Configuration")

    st.selectbox(
        "LLM Model",
        ["Gemini 2.5 Flash"],
    )

    st.divider()

    st.subheader("🤖 Agents")

    st.success("Intent Agent")

    st.success("Flight Agent")

    st.success("Hotel Agent")

    st.success("Planner Agent")

    st.divider()

    st.subheader("🛠 Tech Stack")

    st.info("""
LangGraph

Gemini API

Tavily Search

AviationStack

Streamlit
""")

# ---------------- INPUT ----------------

query = st.text_input(
    "Travel Request",
    placeholder="Example: Plan a 3 day trip from Hyderabad to Delhi",
)

# ---------------- BUTTON ----------------

if st.button("🚀 Generate Plan", use_container_width=True):

    if query.strip() == "":
        st.warning("Please enter a travel request.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.info("🧠 Understanding your request...")
    progress.progress(10)
    time.sleep(.4)

    status.info("✈️ Searching flights...")
    progress.progress(30)
    time.sleep(.4)

    status.info("🏨 Finding hotels...")
    progress.progress(55)
    time.sleep(.4)

    status.info("🤖 Creating itinerary...")
    progress.progress(75)

    result = builder.invoke(
        {
            "user_query": query,
            "messages": [],
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
        }
    )

    progress.progress(100)

    status.success("✅ Travel plan ready!")

    st.balloons()

    left,right = st.columns([1,2])

    # ---------------- LEFT ----------------

    with left:

        st.markdown("## 🤖 Agent Workflow")

        st.markdown("""
<div class='agent-card'>
🧠 Intent Agent

Extracted Departure, Arrival & Destination
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class='agent-card'>
✈️ Flight Agent

Fetched available flights
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class='agent-card'>
🏨 Hotel Agent

Collected hotel recommendations
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class='agent-card'>
🧳 Planner Agent

Generated final itinerary
</div>
""", unsafe_allow_html=True)

        st.divider()

        c1,c2,c3 = st.columns(3)

        c1.metric("Flights","5")

        c2.metric("Hotels","5")

        c3.metric("Agents","4")

    # ---------------- RIGHT ----------------

    with right:

        st.markdown("## 📋 Travel Plan")

        st.markdown(
        f"""
<div class='result-card'>

{result["result"]}

</div>
""",
        unsafe_allow_html=True
        )

        st.download_button(
            "📄 Download Plan",
            result["result"],
            file_name="travel_plan.txt",
        )

# ---------------- FOOTER ----------------

st.markdown("""
<div class='footer'>

Made with ❤️ using LangGraph & Gemini

</div>
""", unsafe_allow_html=True)