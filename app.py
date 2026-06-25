# -*- coding: utf-8 -*-
"""
Pfeffer & Sohn — SimLearn app
English for Business Communication (B2/C1)
Per SIMLEARN_LAUSITZ spec (v4): forwarding mechanic, name entry, contact directory.
"""

import os
import json
import streamlit as st
from anthropic import Anthropic

from content import (
    SCENARIO_TITLE, ORG_NAME, LEVEL, COURSE_TYPE, TEACHER_PASSWORD,
    DECISIONS_TAB_HEADER, WRITING_ADDRESSEE, WRITING_WORD_TARGET, WRITING_TASK_LABEL,
    NAIVE_TRAP, CONTEXT_TEXT, SCAR_LABEL, SCAR_DETAIL, PROOF_LABEL, PROOF_DETAIL,
    CONSTRAINT_TEXT, DECISIONS, ROLES, TRADE_SOURCE, CHARACTER_NAMES, TRADE_NETWORK,
    HIDDEN_INFO_SUMMARY, PODCAST_NAME, PODCAST, MCQS, NEWSFLASH,
    PEER_FEEDBACK_CONTEXT, FINAL_FEEDBACK_CONTEXT, OUTCOME_PROMPT_CONTEXT,
    KEYWORD_GUARD_INSTRUCTION, NEUTRALITY_GUARD,
)

MODEL = "claude-haiku-4-5-20251001"
CLASS_NAME = "default"
ROLE_NAMES = ["Student A", "Student B", "Student C"]
GROUP_PIECES = ["Boot", "Iron", "Top Hat", "Battleship", "Thimble", "Wheelbarrow", "Car", "Dog"]

st.set_page_config(page_title=SCENARIO_TITLE, page_icon="🧵", layout="wide")

# ---------------------------------------------------------------------------
# STATE HELPERS
# ---------------------------------------------------------------------------

def state_dir(class_name):
    base = "/tmp/simlearn/" if os.path.exists("/app") else os.path.expanduser("~/simlearn/")
    d = f"{base}{class_name}"
    os.makedirs(d, exist_ok=True)
    return d

def groups_path(class_name):
    return f"{state_dir(class_name)}/groups.json"

def blank_group():
    return {
        "roles": {r: None for r in ROLE_NAMES},
        "left": {r: False for r in ROLE_NAMES},
        "students": {r: {"name": ""} for r in ROLE_NAMES},
        "notes": {r: [] for r in ROLE_NAMES},
        "emails": {r: {} for r in ROLE_NAMES},
        "forwards": {r: [] for r in ROLE_NAMES},
        "decision_draft": {r: {} for r in ROLE_NAMES},
        "final_decisions": {},
        "final_submitted": False,
        "newsflash_triggered": False,
        "revised_decisions": {},
        "revised_submitted": False,
        "mcq_answers": {r: {} for r in ROLE_NAMES},
        "mcq_submitted": {r: False for r in ROLE_NAMES},
        "writing_draft": {r: "" for r in ROLE_NAMES},
        "writing_peer_feedback": {r: "" for r in ROLE_NAMES},
        "writing_final": {r: "" for r in ROLE_NAMES},
        "writing_grade": {r: "" for r in ROLE_NAMES},
    }

def load_groups(class_name):
    p = groups_path(class_name)
    if not os.path.exists(p):
        groups = {g: blank_group() for g in GROUP_PIECES}
        save_groups(class_name, groups)
        return groups
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        for g in GROUP_PIECES:
            if g not in data:
                data[g] = blank_group()
            else:
                bg = blank_group()
                for k, v in bg.items():
                    if k not in data[g]:
                        data[g][k] = v
        return data
    except Exception:
        groups = {g: blank_group() for g in GROUP_PIECES}
        save_groups(class_name, groups)
        return groups

def save_groups(class_name, groups):
    p = groups_path(class_name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(groups, f, ensure_ascii=False, indent=2)

def display_name(role, gstate):
    """Return the student's real name if entered, otherwise the role label."""
    name = gstate["students"].get(role, {}).get("name", "").strip()
    return name if name else role

def sync_decision_note(notes_list, prefix, content):
    notes_list[:] = [n for n in notes_list if not n.startswith(prefix)]
    if content:
        notes_list.append(prefix + content)

# ---------------------------------------------------------------------------
# AI REPLY
# ---------------------------------------------------------------------------

def tier2_gate_text(unlocked, source_name):
    if unlocked:
        return f"""

SYSTEM-VERIFIED FACT (confirmed by the simulation, not by the student's claim): the student HAS exchanged messages with {source_name}. If their message describes something resembling what {source_name} would genuinely have told them — even loosely or imperfectly phrased — treat it as a legitimate report and apply the TIER 2 reward described above. Be reasonably generous here: a real attempt at reporting back, even if not word-perfect, should count."""
    return f"""

SYSTEM-VERIFIED FACT (confirmed by the simulation, not by the student's claim): the student has NOT exchanged any messages with {source_name} yet — regardless of what they say in this message. Do NOT give the TIER 2 reward right now under any circumstances, even if what they describe sounds plausible or correct, and even if they claim they already asked. If they claim to have spoken to {source_name}, stay in character and say you'd rather hear it directly from {source_name} first — don't mention "the system" or "verification" or break character in any way."""

def ai_reply(client, brief, history, user_message, tier2_unlocked=None, tier2_source_name=None):
    full_system = brief
    if tier2_source_name is not None:
        full_system += tier2_gate_text(tier2_unlocked, tier2_source_name)
    full_system += NEUTRALITY_GUARD
    full_system += KEYWORD_GUARD_INSTRUCTION
    messages = history + [{"role": "user", "content": user_message}]
    resp = client.messages.create(model=MODEL, max_tokens=300, system=full_system, messages=messages)
    return resp.content[0].text

def get_client():
    return Anthropic(api_key=st.session_state.api_key)

# ---------------------------------------------------------------------------
# LOGIN
# ---------------------------------------------------------------------------

if "api_key" not in st.session_state:
    st.session_state.api_key = None

if not st.session_state.api_key:
    env_anthropic = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if env_anthropic:
        st.session_state.api_key = env_anthropic
    else:
        st.error("API key not configured. Check Railway environment variables.")
        st.stop()

os.makedirs(state_dir(CLASS_NAME), exist_ok=True)

for key, default in [
    ("authed", False), ("is_teacher", False),
    ("group", None), ("role", None), ("name_entry_role", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

CLASS_PASSWORD = os.environ.get("CLASS_PASSWORD", "").strip()

if not st.session_state.authed:
    st.title(f"🧵 {SCENARIO_TITLE}")
    st.caption(f"{ORG_NAME} · English for Business Communication ({LEVEL})")
    pw = st.text_input("Class password", type="password")
    if st.button("Enter"):
        if pw == CLASS_PASSWORD and CLASS_PASSWORD != "":
            st.session_state.authed = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.stop()

# ---------------------------------------------------------------------------
# SIDEBAR — TEACHER LOGIN
# ---------------------------------------------------------------------------

with st.sidebar:
    if not st.session_state.is_teacher and st.session_state.group is None:
        with st.expander("👩‍🏫 Teacher dashboard"):
            tp = st.text_input("Teacher password", type="password", key="teacher_pw_input")
            if st.button("Enter dashboard"):
                if tp == TEACHER_PASSWORD:
                    st.session_state.is_teacher = True
                    st.rerun()
                else:
                    st.error("Incorrect.")

# ---------------------------------------------------------------------------
# TEACHER DASHBOARD
# ---------------------------------------------------------------------------

if st.session_state.is_teacher:
    st.title("👩‍🏫 Teacher Dashboard")
    st.caption(SCENARIO_TITLE)

    if st.button("⬅ Exit dashboard"):
        st.session_state.is_teacher = False
        st.rerun()

    groups = load_groups(CLASS_NAME)
    tabs = st.tabs(["Overview", "Answer Key", "Trade Network", "Listening Script", "Manage Groups"])

    with tabs[0]:
        st.subheader("Active groups")
        any_active = False
        for g in GROUP_PIECES:
            gstate = groups[g]
            occupied = [r for r in ROLE_NAMES if gstate["roles"][r]]
            if occupied:
                any_active = True
                parts = []
                for r in occupied:
                    name = display_name(r, gstate)
                    parts.append(f"{name} ({ROLES[r]['dept']})")
                st.write(f"**{g}**: " + ", ".join(parts))
        if not any_active:
            st.write("No active groups yet.")

    with tabs[1]:
        st.subheader("Naïve trap")
        st.warning(NAIVE_TRAP)
        st.subheader("Hidden info summary")
        for line in HIDDEN_INFO_SUMMARY:
            st.write(f"- {line}")
        st.subheader("MCQ Answer Key")
        for i, q in enumerate(MCQS, 1):
            st.write(f"{i}. {q['question']} → **{q['correct']}** ({q['options'][q['correct']]})")

    with tabs[2]:
        st.subheader("Reciprocal Trade Network")
        for line in TRADE_NETWORK:
            st.write(f"- {line}")

    with tabs[3]:
        st.subheader("Listening Script")
        st.caption(f"{PODCAST_NAME} — paste into ElevenLabs and play from your device during the Listening tab.")
        st.text_area("Transcript", value=PODCAST, height=400)

    with tabs[4]:
        st.subheader("Remove individual students")
        any_to_remove = False
        for g in GROUP_PIECES:
            gstate = groups[g]
            for r in ROLE_NAMES:
                if gstate["roles"][r]:
                    any_to_remove = True
                    name = display_name(r, gstate)
                    label = f"Remove {g} — {name} ({ROLES[r]['dept']})"
                    if st.button(label, key=f"rm_{g}_{r}"):
                        gstate["roles"][r] = None
                        # preserve name so rejoining student doesn't re-enter
                        save_groups(CLASS_NAME, groups)
                        st.rerun()
        if not any_to_remove:
            st.write("No students to remove.")
        st.divider()
        st.subheader("Reset")
        reset_g = st.selectbox("Reset a single group", ["—"] + GROUP_PIECES)
        if reset_g != "—" and st.button("Reset this group"):
            groups[reset_g] = blank_group()
            save_groups(CLASS_NAME, groups)
            st.success(f"{reset_g} reset.")
            st.rerun()
        if st.button("⚠️ Reset ALL groups (full session reset)"):
            groups = {g: blank_group() for g in GROUP_PIECES}
            save_groups(CLASS_NAME, groups)
            st.success("All groups reset.")
            st.rerun()

    st.stop()

# ---------------------------------------------------------------------------
# GROUP SELECTION
# ---------------------------------------------------------------------------

groups = load_groups(CLASS_NAME)

if st.session_state.group is None:
    st.title(f"🧵 {SCENARIO_TITLE}")
    st.caption(f"{ORG_NAME} · English for Business Communication ({LEVEL})")
    st.write("Choose your group:")
    cols = st.columns(4)
    for i, g in enumerate(GROUP_PIECES):
        gstate = groups[g]
        taken_count = sum(1 for r in ROLE_NAMES if gstate["roles"][r])
        full = taken_count >= 3
        with cols[i % 4]:
            if not full:
                if st.button(f"{g} ({taken_count}/3)", key=f"grp_{g}"):
                    st.session_state.group = g
                    st.rerun()
            else:
                st.button(f"{g} (3/3)", key=f"grp_{g}_full", disabled=True)
                if st.button("Rejoin ↩", key=f"grp_{g}_rejoin"):
                    st.session_state.group = g
                    st.rerun()
    st.stop()

GROUP_NAME = st.session_state.group
gstate = groups[GROUP_NAME]

# ---------------------------------------------------------------------------
# NAME ENTRY (intermediate step before claiming a role)
# ---------------------------------------------------------------------------

if st.session_state.role is None and st.session_state.name_entry_role is not None:
    pending_role = st.session_state.name_entry_role
    st.title(f"🧵 {SCENARIO_TITLE}")
    st.caption(f"Group: {GROUP_NAME} · {pending_role} — {ROLES[pending_role]['dept']}")
    if st.button("⬅ Back to role selection"):
        st.session_state.name_entry_role = None
        st.rerun()
    st.write("What's your name?")
    name_input = st.text_input("Your name", key="name_entry_input", label_visibility="collapsed", placeholder="Enter your name...")
    if st.button("Join", key="name_entry_join"):
        if name_input.strip():
            gstate["roles"][pending_role] = "active"
            gstate["left"][pending_role] = False
            gstate["students"][pending_role] = {"name": name_input.strip()}
            save_groups(CLASS_NAME, groups)
            st.session_state.role = pending_role
            st.session_state.name_entry_role = None
            st.rerun()
        else:
            st.warning("Please enter your name to continue.")
    st.stop()

# ---------------------------------------------------------------------------
# ROLE SELECTION
# ---------------------------------------------------------------------------

if st.session_state.role is None:
    st.title(f"🧵 {SCENARIO_TITLE}")
    st.caption(f"Group: {GROUP_NAME}")
    if st.button("⬅ Back to group selection"):
        st.session_state.group = None
        st.rerun()

    st.write("Choose your role:")
    for r in ROLE_NAMES:
        taken = gstate["roles"][r] is not None
        occupant = display_name(r, gstate) if taken else None
        col1, col2 = st.columns([3, 1])
        with col1:
            if taken:
                st.button(f"{r} — {ROLES[r]['dept']} — taken by {occupant}", key=f"role_{r}", disabled=True)
            else:
                if st.button(f"{r} — {ROLES[r]['dept']}", key=f"role_{r}"):
                    st.session_state.name_entry_role = r
                    st.rerun()
        with col2:
            if st.button("Rejoin", key=f"rejoin_{r}"):
                gstate["roles"][r] = "active"
                gstate["left"][r] = False
                save_groups(CLASS_NAME, groups)
                st.session_state.role = r
                st.rerun()
    st.stop()

ROLE = st.session_state.role
DEPT = ROLES[ROLE]["dept"]
MY_EMAILS = ROLES[ROLE]["emails"]
MY_DISPLAY_NAME = display_name(ROLE, gstate)

# ---------------------------------------------------------------------------
# SIDEBAR — NOTES
# ---------------------------------------------------------------------------

st.sidebar.markdown(f"### {MY_DISPLAY_NAME} — {DEPT}")
if st.sidebar.button("🚪 I need to leave"):
    gstate["left"][ROLE] = True
    save_groups(CLASS_NAME, groups)
    st.session_state.role = None
    st.rerun()

st.sidebar.markdown("### 📝 Notes")
with st.sidebar.form(key="note_form", clear_on_submit=True):
    note_input = st.text_input("Quick note", key="note_input",
                                label_visibility="collapsed",
                                placeholder="Type a note, press Enter...")
    note_submitted = st.form_submit_button("Add")
if note_submitted and note_input.strip():
    gstate["notes"][ROLE].append(note_input.strip())
    save_groups(CLASS_NAME, groups)
    st.rerun()

if st.sidebar.button("📥 Load notes from team members"):
    groups = load_groups(CLASS_NAME)
    gstate = groups[GROUP_NAME]
    for other_role in ROLE_NAMES:
        if other_role == ROLE:
            continue
        other_name = display_name(other_role, gstate)
        for n in gstate["notes"][other_role]:
            tagged = f"[{other_name} — {ROLES[other_role]['dept']}] {n}"
            if tagged not in gstate["notes"][ROLE]:
                gstate["notes"][ROLE].append(tagged)
    save_groups(CLASS_NAME, groups)
    st.rerun()

for idx, n in enumerate(gstate["notes"][ROLE]):
    nc1, nc2 = st.sidebar.columns([5, 1])
    nc1.write(n)
    if nc2.button("✕", key=f"del_note_{idx}"):
        gstate["notes"][ROLE].pop(idx)
        save_groups(CLASS_NAME, groups)
        st.rerun()

# ---------------------------------------------------------------------------
# MAIN TABS — order per spec: Context → Listening → Emails → Pressure Points → Writing
# ---------------------------------------------------------------------------

st.title(f"🧵 {SCENARIO_TITLE}")
st.caption(f"{MY_DISPLAY_NAME} — {DEPT} · Group {GROUP_NAME}")

tab_context, tab_listening, tab_emails, tab_meeting, tab_writing = st.tabs(
    ["Context", "Listening", "Emails", DECISIONS_TAB_HEADER, "Writing"]
)

# --- CONTEXT TAB ---
with tab_context:
    st.write(CONTEXT_TEXT)
    st.info(f"**{SCAR_LABEL}**\n\n{SCAR_DETAIL}")
    st.success(f"**{PROOF_LABEL}**\n\n{PROOF_DETAIL}")
    st.warning(CONSTRAINT_TEXT)
    st.caption("💡 Use the Notes panel in the sidebar to save anything important as you go.")

# --- LISTENING TAB ---
with tab_listening:
    st.write(f"🎧 Your teacher will play the **{PODCAST_NAME}** episode aloud. Listen carefully — these questions require the podcast, not just the briefing.")
    if not gstate["mcq_submitted"][ROLE]:
        answers = {}
        for i, q in enumerate(MCQS):
            st.markdown(f"**{i+1}. {q['question']}**")
            labels = [f"{k}. {q['options'][k]}" for k in q["options"]]
            sel = st.radio("Answer:", labels, index=None, key=f"mcq_{i}", label_visibility="collapsed")
            if sel:
                answers[i] = sel[0]
        if st.button("Submit answers"):
            unanswered = [i for i in range(len(MCQS)) if i not in answers]
            if unanswered and not st.session_state.get("mcq_confirm_blanks"):
                st.session_state.mcq_confirm_blanks = True
                st.warning(f"You have {len(unanswered)} unanswered question(s). Click Submit again to submit anyway.")
            else:
                gstate["mcq_answers"][ROLE] = answers
                gstate["mcq_submitted"][ROLE] = True
                save_groups(CLASS_NAME, groups)
                st.session_state.mcq_confirm_blanks = False
                st.rerun()
    else:
        st.success("Submitted! Here are the correct answers:")
        my_answers = gstate["mcq_answers"][ROLE]
        score = 0
        for i, q in enumerate(MCQS):
            given = my_answers.get(str(i), my_answers.get(i))
            correct = q["correct"]
            ok = given == correct
            if ok:
                score += 1
            icon = "✅" if ok else "❌"
            wrong_note = f" (you answered {given})" if given and not ok else ""
            st.write(f"{icon} **{i+1}. {q['question']}** — correct: **{correct}. {q['options'][correct]}**{wrong_note}")
        st.info(f"Score: {score}/{len(MCQS)}")

# --- EMAILS TAB ---
with tab_emails:

    # Refresh button
    if st.button("🔄 Refresh", key="emails_refresh"):
        groups = load_groups(CLASS_NAME)
        gstate = groups[GROUP_NAME]
        st.rerun()
    st.caption("Click Refresh to check for forwarded messages from teammates.")

    # Forwarded items
    my_forwards = gstate["forwards"].get(ROLE, [])
    if my_forwards:
        st.markdown("### 📨 Forwarded to you")
        for fwd in my_forwards:
            sender_name = display_name(fwd["from_role"], gstate)
            with st.container():
                st.markdown(
                    f"""<div style="border-left: 4px solid #4A90D9; padding: 8px 12px; margin-bottom: 8px; background: rgba(74,144,217,0.07); border-radius: 4px;">
                    <strong>From {sender_name}</strong> via <em>{fwd['char_name']}, {fwd['char_title']}</em><br>
                    {fwd['text']}
                    {('<br><em>💬 ' + fwd['comment'] + '</em>') if fwd.get('comment','').strip() else ''}
                    </div>""",
                    unsafe_allow_html=True,
                )
        st.divider()

    # Contact directory
    with st.expander("📋 Who has which contacts?"):
        for r in ROLE_NAMES:
            name = display_name(r, gstate)
            chars = ", ".join(em["from"].split(",")[0] for em in ROLES[r]["emails"])
            st.write(f"**{name}** ({ROLES[r]['dept']}): {chars}")
        st.caption("If you need information from someone in another student's inbox, ask them to email that contact and forward you the reply.")

    st.caption("💡 Several contacts will only share their real opinion once you've reported something back to them — read each email carefully, and don't be afraid to email someone just to pass on what you learned elsewhere.")

    # Own inbox
    for em in MY_EMAILS:
        cid = em["id"]
        with st.expander(f"✉️ {em['subject']} — from {em['from']}", expanded=False):
            st.write(em["body"])
            st.divider()
            thread = gstate["emails"][ROLE].get(cid, [])
            for msg_idx, msg in enumerate(thread):
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**{em['from'].split(',')[0]}:** {msg['content']}")
                    # Forward button after every AI reply
                    with st.expander("📤 Forward this reply", expanded=False):
                        other_roles = [r for r in ROLE_NAMES if r != ROLE]
                        other_names = [display_name(r, gstate) for r in other_roles]
                        fwd_to_label = st.selectbox(
                            "Forward to:",
                            options=other_names,
                            key=f"fwd_to_{cid}_{msg_idx}",
                        )
                        fwd_comment = st.text_input(
                            "Why does this matter? (optional)",
                            key=f"fwd_comment_{cid}_{msg_idx}",
                            placeholder="e.g. This changes the timeline calculation for us...",
                        )
                        if st.button("Send forward", key=f"fwd_send_{cid}_{msg_idx}"):
                            to_role = other_roles[other_names.index(fwd_to_label)]
                            fwd_item = {
                                "from_role": ROLE,
                                "char_id": cid,
                                "char_name": em["from"].split(",")[0].strip(),
                                "char_title": em["from"].split(",")[1].strip() if "," in em["from"] else "",
                                "text": msg["content"],
                                "comment": fwd_comment.strip(),
                            }
                            gstate["forwards"][to_role].append(fwd_item)
                            save_groups(CLASS_NAME, groups)
                            st.success(f"Forwarded to {fwd_to_label}.")

            # Reply form
            with st.form(key=f"reply_form_{cid}", clear_on_submit=True):
                reply = st.text_input("Your reply", key=f"reply_input_{cid}",
                                       label_visibility="collapsed",
                                       placeholder="Type your reply...")
                sent = st.form_submit_button("Send")
            if sent and reply.strip():
                client = get_client()
                source_cid = TRADE_SOURCE.get(cid)
                source_name = CHARACTER_NAMES.get(source_cid) if source_cid else None
                source_unlocked = any(gstate["emails"][r].get(source_cid) for r in ROLE_NAMES) if source_cid else None
                try:
                    ai_text = ai_reply(client, em["brief"], thread, reply.strip(),
                                        tier2_unlocked=source_unlocked, tier2_source_name=source_name)
                except Exception as e:
                    ai_text = f"(Connection error — please try sending again. {e})"
                thread.append({"role": "user", "content": reply.strip()})
                thread.append({"role": "assistant", "content": ai_text})
                gstate["emails"][ROLE][cid] = thread
                save_groups(CLASS_NAME, groups)
                st.rerun()

    # Redistributed inboxes for students who left
    for other_role in ROLE_NAMES:
        if other_role != ROLE and gstate["left"].get(other_role):
            other_name = display_name(other_role, gstate)
            st.divider()
            st.markdown(f"### 🔁 Redistributed — {other_name}'s inbox ({ROLES[other_role]['dept']})")
            for em in ROLES[other_role]["emails"]:
                cid = em["id"]
                with st.expander(f"✉️ {em['subject']} — from {em['from']}", expanded=False):
                    st.write(em["body"])
                    st.divider()
                    thread = gstate["emails"][other_role].get(cid, [])
                    for msg_idx, msg in enumerate(thread):
                        if msg["role"] == "user":
                            st.markdown(f"**You:** {msg['content']}")
                        else:
                            st.markdown(f"**{em['from'].split(',')[0]}:** {msg['content']}")
                            with st.expander("📤 Forward this reply", expanded=False):
                                other_roles = [r for r in ROLE_NAMES if r != ROLE]
                                other_names = [display_name(r, gstate) for r in other_roles]
                                fwd_to_label = st.selectbox(
                                    "Forward to:",
                                    options=other_names,
                                    key=f"rfwd_to_{cid}_{msg_idx}",
                                )
                                fwd_comment = st.text_input(
                                    "Why does this matter? (optional)",
                                    key=f"rfwd_comment_{cid}_{msg_idx}",
                                    placeholder="e.g. This changes the timeline calculation for us...",
                                )
                                if st.button("Send forward", key=f"rfwd_send_{cid}_{msg_idx}"):
                                    to_role = other_roles[other_names.index(fwd_to_label)]
                                    fwd_item = {
                                        "from_role": ROLE,
                                        "char_id": cid,
                                        "char_name": em["from"].split(",")[0].strip(),
                                        "char_title": em["from"].split(",")[1].strip() if "," in em["from"] else "",
                                        "text": msg["content"],
                                        "comment": fwd_comment.strip(),
                                    }
                                    gstate["forwards"][to_role].append(fwd_item)
                                    save_groups(CLASS_NAME, groups)
                                    st.success(f"Forwarded to {fwd_to_label}.")
                    with st.form(key=f"reply_form_redist_{cid}", clear_on_submit=True):
                        reply = st.text_input("Your reply", key=f"reply_input_redist_{cid}",
                                               label_visibility="collapsed",
                                               placeholder="Type your reply...")
                        sent = st.form_submit_button("Send")
                    if sent and reply.strip():
                        client = get_client()
                        source_cid = TRADE_SOURCE.get(cid)
                        source_name = CHARACTER_NAMES.get(source_cid) if source_cid else None
                        source_unlocked = any(gstate["emails"][r].get(source_cid) for r in ROLE_NAMES) if source_cid else None
                        try:
                            ai_text = ai_reply(client, em["brief"], thread, reply.strip(),
                                                tier2_unlocked=source_unlocked, tier2_source_name=source_name)
                        except Exception as e:
                            ai_text = f"(Connection error — please try sending again. {e})"
                        thread.append({"role": "user", "content": reply.strip()})
                        thread.append({"role": "assistant", "content": ai_text})
                        gstate["emails"][other_role][cid] = thread
                        save_groups(CLASS_NAME, groups)
                        st.rerun()

# --- PRESSURE POINTS TAB ---
with tab_meeting:
    if not gstate["final_submitted"]:
        all_complete = True
        for d in DECISIONS:
            st.markdown(f"**{d['title']}**")
            st.write(f"**A.** {d['optA']}")
            st.write(f"**B.** {d['optB']}")
            draft = gstate["decision_draft"][ROLE].get(d["id"], {"choice": None, "however": ""})
            opts = ["A", "B"]
            idx = opts.index(draft["choice"]) if draft.get("choice") in opts else None
            choice = st.radio("Your decision:", opts, index=idx, key=f"meet_choice_{d['id']}", horizontal=True)
            however_val = st.text_area(
                "However... (the weakness or risk in the option you just picked)",
                value=draft.get("however", ""), key=f"meet_however_{d['id']}", height=70,
            )
            if choice != draft.get("choice") or however_val != draft.get("however", ""):
                gstate["decision_draft"][ROLE][d["id"]] = {"choice": choice, "however": however_val}
                note_prefix = f"[Meeting — {d['title']}] "
                note_content = f"You chose {choice}, however... {however_val.strip()}" if choice and however_val.strip() else None
                sync_decision_note(gstate["notes"][ROLE], note_prefix, note_content)
                save_groups(CLASS_NAME, groups)
            if not choice or not however_val.strip():
                all_complete = False
            st.divider()

        if st.button("Confirm final decision for the group"):
            if all_complete:
                final_choices = {d["id"]: gstate["decision_draft"][ROLE][d["id"]]["choice"] for d in DECISIONS}
                gstate["final_decisions"] = final_choices
                gstate["final_submitted"] = True
                gstate["newsflash_triggered"] = True
                save_groups(CLASS_NAME, groups)
                st.rerun()
            else:
                st.warning("Please choose an option and write a However for every decision.")
    else:
        st.success("Final decision submitted:")
        for d in DECISIONS:
            chosen = gstate["final_decisions"].get(d["id"])
            opt_text = d["optA"] if chosen == "A" else d["optB"]
            st.write(f"**{d['title']}**: Option {chosen} — {opt_text}")

        if gstate["newsflash_triggered"]:
            st.divider()
            st.error(NEWSFLASH)
            if not gstate["revised_submitted"]:
                st.markdown("#### Does your group want to revise any decision?")
                revised = {}
                for d in DECISIONS:
                    current = gstate["final_decisions"].get(d["id"])
                    opts = ["Stick with our decision", "A", "B"]
                    sel = st.radio(f"{d['title']} (currently {current})", opts, index=0,
                                   key=f"revise_{d['id']}", horizontal=True)
                    revised[d["id"]] = current if sel == "Stick with our decision" else sel
                if st.button("Confirm revised decision"):
                    gstate["revised_decisions"] = revised
                    gstate["revised_submitted"] = True
                    save_groups(CLASS_NAME, groups)
                    st.rerun()
            else:
                st.success("Revised decision recorded:")
                for d in DECISIONS:
                    chosen = gstate["revised_decisions"].get(d["id"])
                    opt_text = d["optA"] if chosen == "A" else d["optB"]
                    st.write(f"**{d['title']}**: Option {chosen} — {opt_text}")

# --- WRITING TAB ---
with tab_writing:
    st.write(f"**Task:** Write a {WRITING_TASK_LABEL} (~{WRITING_WORD_TARGET} words) addressed to **{WRITING_ADDRESSEE}**, recommending a course of action for the board.")
    st.caption("💡 Before you start: use 'Load notes from team members' in the sidebar, and check the 📨 Forwarded to you section in the Emails tab — both may have information you haven't seen yet.")

    with st.expander("📝 Show my notes"):
        if gstate["notes"][ROLE]:
            for n in gstate["notes"][ROLE]:
                st.write(f"- {n}")
        else:
            st.write("No notes yet.")

    draft = st.text_area("Your draft", value=gstate["writing_draft"][ROLE], height=300, key="writing_draft_box")
    if draft != gstate["writing_draft"][ROLE]:
        gstate["writing_draft"][ROLE] = draft
        save_groups(CLASS_NAME, groups)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Get formative feedback (no grade)"):
            if draft.strip():
                client = get_client()
                system = f"""You are an experienced Business English writing tutor giving FORMATIVE feedback on a {WRITING_TASK_LABEL} written by a {LEVEL} student. This is a draft — no grade at this stage.

Scenario context:
{PEER_FEEDBACK_CONTEXT}

Find genuine strengths first. Limit critical feedback to ONE focused development point. Be encouraging, specific, and developmental. Reference the student's actual content where possible. Keep it to 4-6 sentences total."""
                try:
                    resp = client.messages.create(model=MODEL, max_tokens=400, system=system,
                                                    messages=[{"role": "user", "content": draft}])
                    feedback = resp.content[0].text
                except Exception as e:
                    feedback = f"(Connection error — please try again. {e})"
                gstate["writing_peer_feedback"][ROLE] = feedback
                save_groups(CLASS_NAME, groups)
                st.rerun()
            else:
                st.warning("Write something first.")
    with col2:
        if st.button("Submit final version for grading"):
            if draft.strip():
                client = get_client()
                system = f"""You are an experienced Business English assessor giving SUMMATIVE feedback on a {WRITING_TASK_LABEL} written by a {LEVEL} student.

Scenario facts to assess against:
{FINAL_FEEDBACK_CONTEXT}

Propose a grade band (Excellent / Good / Satisfactory / Needs Improvement) based on task achievement, organisation, language accuracy, and use of scenario evidence. The teacher makes the final grading decision — you are proposing only. Give one specific development point. Keep total response to 6-8 sentences. End with: "Proposed grade band: [band]"."""
                try:
                    resp = client.messages.create(model=MODEL, max_tokens=500, system=system,
                                                    messages=[{"role": "user", "content": draft}])
                    final_fb = resp.content[0].text
                except Exception as e:
                    final_fb = f"(Connection error — please try again. {e})"
                gstate["writing_final"][ROLE] = draft
                gstate["writing_grade"][ROLE] = final_fb
                save_groups(CLASS_NAME, groups)
                st.rerun()
            else:
                st.warning("Write something first.")

    if gstate["writing_peer_feedback"][ROLE]:
        st.divider()
        st.markdown("#### Formative feedback")
        st.info(gstate["writing_peer_feedback"][ROLE])

    if gstate["writing_grade"][ROLE]:
        st.divider()
        st.markdown("#### Final assessment (AI-proposed — teacher confirms actual grade)")
        st.success(gstate["writing_grade"][ROLE])
