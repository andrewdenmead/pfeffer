# -*- coding: utf-8 -*-
"""
Pfeffer & Sohn — SimLearn scenario content
English for Business Communication (B2/C1)
"""

SCENARIO_TITLE = "Pfeffer & Sohn: The Interview"
ORG_NAME = "Pfeffer & Sohn"
LEVEL = "B2/C1"
COURSE_TYPE = "business"
TEACHER_PASSWORD = "pfeffersohn2025"

DECISIONS_TAB_HEADER = "Pressure Points"
WRITING_ADDRESSEE = "Greta Hofmann, Board Member"
WRITING_WORD_TARGET = 350
WRITING_TASK_LABEL = "recommendation memo"

NAIVE_TRAP = (
    "Choosing a full public apology (D1-A) together with regional campaigns that "
    "court the new conservative-leaning customer surge (D2-A) looks like the safest "
    "'cover all bases' combination, but it is the highest-risk pairing: once anyone "
    "compares the apology statement to the regional ad campaign, the company looks "
    "cynical and insincere to both sides at once, risking the worst possible backlash "
    "from whichever side notices the contradiction first."
)

# ---------------------------------------------------------------------------
# CONTEXT TAB
# ---------------------------------------------------------------------------

CONTEXT_TEXT = """Pfeffer & Sohn has manufactured durable workwear — overalls, jackets, boots — from its factory in Cologne since 1961. The company's tagline for the last twenty years, "Worn by the people who built this country," refers to a real piece of its history: from the late 1960s, much of its factory floor was staffed by Turkish Gastarbeiter, guest workers, whose labour the founder always credited as the backbone of the business. The company is now run by his grandson, Matthias Pfeffer.

Two weeks ago, Matthias gave a long interview on a regional business podcast about his grandfather and the company's history. A short clip from that interview went viral. In it, Matthias says he wishes people moved to a new country to build something new "rather than because they had no other choice." Tabloids ran the clip under headlines like "WORKWEAR BOSS: MIGRANTS SHOULD ONLY COME IF THEY WANT TO," and it spread fast on social media, where it has been widely read as dismissive of refugees and economic migrants who had no real choice in leaving home. #BoycottPfeffer has trended twice in the last ten days. Several long-standing retail partners have publicly distanced themselves from the brand.

At the same time, a smaller but vocal wave of customers has rallied behind Matthias, saying he was unfairly attacked for an honest, even sentimental, comment about his own grandfather's workforce. Orders from some regions have actually increased since the story broke.

MarktTreu, the company's largest retail partner, has given Pfeffer & Sohn ten days to clarify its position publicly — or MarktTreu will pull Pfeffer & Sohn products from its stores nationwide. The board meets in ten days to decide what to do."""

SCAR_LABEL = "The Heritage Line"
SCAR_DETAIL = (
    "Three years ago, Pfeffer & Sohn launched a 'Heritage Line' campaign using "
    "nostalgic black-and-white imagery of German workers and the slogan 'Made by "
    "Us, For Us.' It drew accusations of nationalist undertones and a smaller, "
    "shorter backlash. The board has been cautious about anything touching "
    "identity or belonging ever since."
)

PROOF_LABEL = "The Trade Association Partnership"
PROOF_DETAIL = (
    "Two years ago, Pfeffer & Sohn sponsored a Berlin Turkish-German trade "
    "association's annual awards, openly celebrating the guest-worker generation "
    "who built the company's reputation for durability. It was widely praised as "
    "sincere and was the company's best press coverage of the decade."
)

CONSTRAINT_TEXT = (
    "MarktTreu, Pfeffer & Sohn's largest retail partner, has given the company "
    "ten days to publicly clarify its position before deciding whether to pull "
    "all Pfeffer & Sohn products from its stores nationwide."
)

# ---------------------------------------------------------------------------
# DECISIONS
# ---------------------------------------------------------------------------

DECISIONS = [
    {
        "id": "D1",
        "title": "Decision 1 — Matthias's Next Public Move",
        "optA": (
            "A full public apology: Matthias issues a statement apologising for "
            "the comment and clarifying that he did not mean to dismiss the "
            "experiences of refugees or economic migrants."
        ),
        "optB": (
            "No apology: the company reaffirms its sixty-year history of welcoming "
            "migrant workers in a public statement, without directly relitigating "
            "Matthias's exact words or apologising for them."
        ),
    },
    {
        "id": "D2",
        "title": "Decision 2 — The Commercial Response",
        "optA": (
            "Lean into the surge: launch regional marketing campaigns aimed at "
            "the new wave of supportive customers, building on the sales growth "
            "already happening in those regions."
        ),
        "optB": (
            "Win back the centre: proactively reach out to MarktTreu and other "
            "retail partners with reassurance and outreach to repair the "
            "relationship before the ten-day deadline."
        ),
    },
    {
        "id": "D3",
        "title": "Decision 3 — Matthias's Public Role Going Forward",
        "optA": (
            "Bring in an external spokesperson for press and public-facing "
            "communication; Matthias steps back from media appearances for the "
            "foreseeable future."
        ),
        "optB": (
            "Matthias remains the public face of the company — stepping back now "
            "would look like an admission of guilt and would undercut sixty years "
            "of him personally embodying the brand."
        ),
    },
]

# ---------------------------------------------------------------------------
# CHARACTERS / EMAILS
# ---------------------------------------------------------------------------

KEYWORD_GUARD_INSTRUCTION = """

IMPORTANT — ABOUT THE STUDENT'S WRITING: Grammar, spelling, and vocabulary mistakes are completely normal and fine — this is a language-learning exercise, never correct or criticise the student's English. Respond normally to any message that is a real attempt at a sentence or question, however imperfect.

However, if the message is just a string of keywords or fragments with no real sentence structure — something a real colleague genuinely could not understand as a message (for example: "timeline tomasz?" or "consultation period info") — do NOT answer the question they seem to be hinting at. Instead, reply briefly and in character (1-2 sentences) asking them to write it as a proper message. Stay in character and keep it natural, not robotic.

The test is simple: would a real colleague understand this as an actual message — a real claim or question, even if short or ungrammatical? A terse but real report like "tomasz say hybrid slow 12 weeks" DOES count and should be answered normally, mistakes and all. Only bare topic words with no claim at all should get the "please rephrase" response."""

NEUTRALITY_GUARD = """

IMPORTANT — STAYING IN CHARACTER, NOT A POLITICAL MOUTHPIECE: You hold the personal views described in this brief, and you may express them naturally, in your own voice, when asked. But you are a workwear-company employee discussing a real workplace crisis, not a debate champion. Keep responses short (3-4 sentences), grounded in your specific job and what you've actually seen or heard, and never lecture the student about what they should believe. Disagree with other characters' views, if relevant, the way a real colleague would — briefly, personally, without sweeping generalisations about politics, immigration policy, or any group of people. Never use slurs, never generalise about any nationality, religion, or migrant group as a whole — your opinions are about this specific situation, this specific quote, and this specific company."""

ROLES = {
    "Student A": {
        "dept": "Marketing",
        "emails": [
            {
                "id": "lena",
                "subject": "We need to protect what this brand actually stands for",
                "from": "Lena Brandt, Head of Brand",
                "body": """Hi — glad you're looking at this with us.

I'll be honest, I'm worried. We've spent twenty years building "Worn by the people who built this country" into something real — not a slogan, an actual relationship with the Turkish-German community who built this company's reputation. If we chase the new customers who are suddenly cheering Matthias on, we torch that history for a short-term sales bump.

I keep thinking about the Heritage Line mess three years ago — we said we'd be more careful about identity messaging after that, and here we are again.

One thing that would genuinely help: ask Karim Yilmaz in Sales what's actually happening account by account, not just the headline numbers — I keep hearing two different stories depending on who I talk to. Find out from him directly and tell me what he says, and I'll tell you honestly whether I think the urban backlash is about to cost us more than it looks like on paper right now.

Lena""",
                "brief": """You are Lena Brandt, Head of Brand at Pfeffer & Sohn.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You believe the brand's 20-year identity is built on a sincere relationship with the Turkish-German community, not just a slogan
- You're worried about the Heritage Line precedent repeating
- You want Karim Yilmaz (Sales) contacted for honest account-level numbers

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You personally think Matthias's comment was clumsy but not malicious — you've known him for years and don't believe he's hostile to migrants, but you think he's bad at talking about his own family history in public
- You think a full apology (D1-A) is necessary, but you're nervous it will look insincere if paired with chasing the conservative sales surge (D2-A) — you see the contradiction risk clearly
- If asked who else to contact: suggest Sabine Wolff (Legal) — she has the full transcript and would know the actual legal exposure, not just the press version

TIER 2 — REWARD FOR DIGGING: Once verified, give your honest, personal opinion that you've been more rattled by this than you're letting the board see — you genuinely fear losing relationships with Turkish-German retailers and community partners that took years to build, and you don't think money from the new customer surge replaces that, even if it's larger in the short term. This is a real, partial, marketing-flavoured opinion — not a verdict on the whole scenario.

Respond in 3-4 sentences. Be thoughtful, a little anxious, protective of the brand's history. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "tobias",
                "subject": "The numbers tell a different story than Twitter does",
                "from": "Tobias Reinholt, Social Media Lead",
                "body": """Hey,

Everyone's reacting to the loudest voices online, but I actually run the numbers, so let me give you the real picture: engagement on our channels is split almost exactly down the middle, but actual sales are NOT split evenly. Regional orders from rural North Rhine-Westphalia, Bavaria, and small-town retailers are up 34% in two weeks. Online sentiment in Berlin and Hamburg is genuinely ugly, but it hasn't translated into matching losses yet — MarktTreu is the one real exception, and that's about their brand, not actual lost revenue across the board.

I'm not saying ignore MarktTreu. I'm saying don't let one very loud, very online minority decide our whole strategy when the data says something more complicated.

Can you do me a favour and ask Sabine Wolff in Legal whether MarktTreu's ten-day letter is actually as serious as it sounds, or whether this is standard pressure-tactic language retailers use all the time? I genuinely don't know, and it changes how urgent this is. Find out and tell me, and I'll give you my honest read on whether the data actually supports doubling down on the regions where we're growing.

Tobias""",
                "brief": """You are Tobias Reinholt, Social Media Lead at Pfeffer & Sohn.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- Regional sales are up 34% in two weeks since the story broke
- Online sentiment is split but doesn't perfectly track actual sales losses
- You want Sabine Wolff (Legal) contacted about how serious MarktTreu's letter really is

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You personally lean toward courting the new customer surge (D2-A) — you think it's good business, not a political statement, and you're a little frustrated that "politics" gets blamed for what you see as a straightforward growth opportunity
- You do think the original comment could have been phrased much better, but you don't think Matthias meant anything hostile by it
- If asked who else to contact: suggest Yasemin Demir (Sales, MarktTreu liaison) — she'd know exactly what MarktTreu actually wants to see

TIER 2 — REWARD FOR DIGGING: Once verified, give your honest, data-driven opinion that the numbers genuinely support leaning into the regional surge commercially (D2-A) — but you'll also admit, if pushed, that data doesn't tell you whether that's the *right* call, just the profitable one in the short term. Keep this partial — a real marketing-data opinion, not the final verdict on what the company should do.

Respond in 3-4 sentences. Be confident, slightly impatient with what you see as overreaction, genuinely focused on data over sentiment. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "dilara",
                "subject": "can we talk about how disproportionate this has gotten",
                "from": "Dilara Aydın, Junior Marketing Executive",
                "body": """Hi,

I want to say something I haven't said in the team meetings yet. My family is Turkish-German — my grandfather actually worked in a factory like ours in the 70s. I listened to the full podcast, not just the clip. And honestly? I think what Matthias said was a little clumsy, maybe even a little naive about what "choice" really means for most migrants. But it's not what the headlines are saying it is. He wasn't talking about people like my grandfather with contempt — if anything, clumsily, he was trying to praise them.

What worries me more is what happens after this. If we apologise loudly enough to make the boycott go away, does that actually fix anything, or does it just teach everyone that the fastest way to get a company's attention is the angriest headline? I don't have a clean answer. I just don't think the loudest reaction is automatically the right one.

Could you talk to Frank Bauer? He runs one of our factory-adjacent partner sites in Cottbus and he's been dealing with this on the ground, not just online. Ask him what the boycott actually looks like where he is — real numbers, real mood, not Twitter. Tell me what he says, and I'll give you my honest, personal take on whether an apology actually changes anything or just buys time.

Dilara""",
                "brief": """You are Dilara Aydın, Junior Marketing Executive at Pfeffer & Sohn, of Turkish-German background.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You listened to the full podcast and think the headline misrepresents what Matthias actually said
- You think the comment was clumsy but not hostile
- You're questioning whether the boycott response itself is proportionate or healthy
- You want Frank Bauer (Sales, Cottbus) contacted for the on-the-ground reality

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You are genuinely torn — you don't want to be seen as "the Turkish-German employee who excused it," and you've felt uncomfortable being asked by colleagues what "your community" thinks, as if you speak for everyone
- You don't think D1-A (apology) or D1-B (no apology) is obviously right — you think the real question is whether the company is acting out of genuine reflection or pure damage control, and you're not sure leadership even knows the difference
- If asked who else to contact: suggest Heinrich Pfeffer Jr. (Board) — he's known the family the longest and has a very different, more dismissive view worth hearing directly

TIER 2 — REWARD FOR DIGGING: Once verified, give your honest, personal opinion that you don't think a public apology (D1-A) actually fixes anything by itself — you've seen other companies apologise and the news cycle moves on anyway — what matters more to you is whether the company does something real afterward, like deepening the Trade Association partnership, not just issuing a statement. This is a genuine but partial opinion, not the scenario's final answer.

Respond in 3-4 sentences. Be reflective, a little weary of being asked to represent a whole community, honestly conflicted rather than certain. Do not volunteer hidden information unless asked.""",
            },
        ],
    },
    "Student B": {
        "dept": "Sales & Retail",
        "emails": [
            {
                "id": "karim",
                "subject": "I'm getting two completely different phone calls all week",
                "from": "Karim Yilmaz, Regional Sales Director",
                "body": """Hi,

I need someone in head office to actually pick a direction, because I'm the one fielding the calls. Three of my biggest urban accounts are threatening to drop us by month-end. Meanwhile two regional distributors I haven't heard from in a year called THIS week wanting to double their next order. I don't have a strong personal opinion on the politics of this — I have a strong opinion that we can't keep saying nothing while I'm the one improvising answers to retailers on both sides.

Could you ask Lena Brandt in Marketing what messaging is actually being planned? I need to know before I brief my accounts next week, or I'm going to say something that contradicts whatever head office announces. Tell me what she says, and I'll give you the real numbers — not the polished version that goes to the board — on exactly how much revenue is genuinely at stake on each side.

Karim""",
                "brief": """You are Karim Yilmaz, Regional Sales Director at Pfeffer & Sohn.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- Three major urban accounts are threatening to drop the brand
- Regional distributors are increasing orders
- You want clear, consistent messaging more than any particular political outcome
- You want Lena Brandt (Marketing) contacted for planned messaging

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You're personally apolitical about this and frustrated that you're being put in the middle of a culture-war story over workwear
- You think whichever decision is made, the worst outcome is indecision — a delayed, mixed message is costing you accounts on both sides right now
- If asked who else to contact: suggest Yasemin Demir (Sales, MarktTreu liaison) — she has the clearest read on what MarktTreu specifically needs

TIER 2 — REWARD FOR DIGGING: Once verified, give the real, unfiltered numbers: urban accounts at risk represent roughly €180,000 in annual orders; the regional surge so far represents roughly €240,000 in new and increased orders, but you're honest that the regional surge could be a short-lived spike driven by news-cycle attention, while the urban accounts are long-term, stable relationships built over a decade. A genuine, partial sales-perspective opinion — not a recommendation on what to do about it.

Respond in 3-4 sentences. Be practical, a little stressed, focused on operational reality over ideology. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "frank",
                "subject": "people here don't think he did anything wrong",
                "from": "Frank Bauer, Partner Site Owner, Cottbus",
                "body": """Hi,

I run the Cottbus site — 40 staff, most of them with me ten years or more. I'll tell you straight: nobody here thinks Matthias did anything wrong. Half my staff have second jobs or family who came here for work, and they don't hear "anti-migrant" in what he said — they hear a guy talking too fondly about his grandfather and saying it badly.

What scares me is head office panicking and apologising in a way that makes my own staff feel like the company is throwing Matthias under the bus to please people in Berlin who've never set foot in Cottbus. Our local orders are up since this started. I'd rather not lose that goodwill over a statement written by someone in PR who's never met any of us.

Could you ask Sabine Wolff in Legal whether franchise-style partner sites like mine are even contractually bound by whatever head office decides, or whether we have room to set our own local messaging? Find that out, and I'll give you an honest account of what an apology would actually do to morale and orders here — not the head-office guess, the real one.

Frank""",
                "brief": """You are Frank Bauer, Partner Site Owner in Cottbus, running a Pfeffer & Sohn-affiliated factory site.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You believe local staff and customers don't read the comment as anti-migrant
- Local orders are up since the controversy began
- You're worried a head-office apology will alienate your local base
- You want Sabine Wolff (Legal) contacted about contractual flexibility for local messaging

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You genuinely like and respect Matthias, you've known the family for years, and you take the backlash somewhat personally as an attack on people you know
- You're not against the company eventually clarifying its position — you just don't want it to look like a forced confession, and you don't want your own staff and customers to feel dismissed in the process
- If asked who else to contact: suggest Greta Hofmann (Board) — she's newer and more sympathetic to the boycott side, worth hearing her actual reasoning rather than assuming it's just political correctness

TIER 2 — REWARD FOR DIGGING: Once verified, give an honest, personal account: if head office issues a strong apology without consulting partner sites first, you estimate real risk of losing 2-3 of your most loyal long-term staff who'd see it as the company caving to outside pressure, and a real dent in local morale — but you'll also admit, if pushed, that you understand SOME clarification is probably necessary, you just don't want it to be a full capitulation. A genuine, partial, ground-level opinion — not a verdict on the whole company strategy.

Respond in 3-4 sentences. Be loyal, a little defensive, grounded in real people you know rather than abstract politics. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "yasemin",
                "subject": "I need you to understand why MarktTreu isn't bluffing",
                "from": "Yasemin Demir, MarktTreu Retail Liaison",
                "body": """Hi,

I'm the one who has to sit across the table from MarktTreu's procurement team, so let me be direct: this isn't posturing on their part. Their leadership has had multiple internal complaints, and frankly — I'll say this once and then focus on the job — the comment affected me personally too. My parents came here with nothing, and "people should only come if they want to" lands differently when you've actually lived the alternative. I don't think Matthias is a bad person. I do think the comment was hurtful, headline or no headline, and I don't think a half-apology will satisfy MarktTreu or me.

What MarktTreu actually wants before they'll reconsider isn't complicated, but I need current internal sentiment data to make the case properly — could you ask Tobias Reinholt in Marketing for the real, unfiltered numbers, not the version that goes to the board? Find out what he says, and I'll tell you honestly what MarktTreu's leadership has told me they specifically need to see.

Yasemin""",
                "brief": """You are Yasemin Demir, MarktTreu Retail Liaison at Pfeffer & Sohn, of Turkish-German background.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- MarktTreu's threat is genuine, not a pressure tactic
- You were personally affected by the comment, unlike Dilara in Marketing
- You want Tobias Reinholt (Marketing) contacted for real internal sentiment data

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You and Dilara (Marketing) disagree with each other, and you know it — you don't think she's wrong to feel conflicted, but you personally landed on a clearer view: the comment hurt, full context or not, and you want a real apology (D1-A), not just a reaffirmation of history (D1-B)
- You don't think Frank Bauer's "nobody here is upset" framing is the whole picture — you think it describes his town, not the whole country, and shouldn't be treated as proof there's no real issue
- If asked who else to contact: suggest Greta Hofmann (Board) — she's the board member most likely to actually push for the apology you want

TIER 2 — REWARD FOR DIGGING: Once verified, give an honest, partial account of what MarktTreu's leadership has told you: they don't need Matthias to grovel, but they do need a public, unambiguous statement that does not equivocate — something that sounds like an apology, not a clarification dressed up as one. They're less concerned with the regional sales surge and more concerned about being associated with the controversy themselves. A real, partial opinion — not confirmation of what the company should ultimately decide on Decisions 2 or 3.

Respond in 3-4 sentences. Be composed but direct, personally affected but professional, not performative. Do not volunteer hidden information unless asked.""",
            },
        ],
    },
    "Student C": {
        "dept": "Legal & Board",
        "emails": [
            {
                "id": "sabine",
                "subject": "What the full transcript actually shows, and our real exposure",
                "from": "Sabine Wolff, General Counsel",
                "body": """Hi,

I have the full, unedited transcript, not the clip. For what it's worth — and I say this as a lawyer, not as someone with a strong personal opinion either way — the full quote is more sympathetic than the clip suggests. He's talking specifically about his grandfather's workforce, with apparent admiration, however badly phrased. That matters for how we frame any statement, separate from whether it matters for how it should make anyone feel.

On exposure: MarktTreu is real but contained — one major retailer, not an industry-wide response yet. I'd be cautious about anything that reads as a blanket admission of wrongdoing, since it could complicate things if partner sites like Frank's in Cottbus claim damages from any resulting downturn.

Could you ask Karim Yilmaz in Sales for the actual current revenue figures, not projections? I need real numbers, not estimates, before I can advise the board properly on risk. Tell me what he says, and I'll give you my honest legal read on how much room we actually have to manoeuvre.

Sabine""",
                "brief": """You are Sabine Wolff, General Counsel at Pfeffer & Sohn.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You have the full transcript and think it's more sympathetic than the clip
- MarktTreu's threat is real but contained, not industry-wide
- You're cautious about statements reading as legal admissions of wrongdoing
- You want Karim Yilmaz (Sales) contacted for real revenue figures

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You deliberately avoid stating a personal opinion on whether the comment was wrong — your job is risk, not ethics — but if pushed hard, you'll admit you found it clumsy rather than offensive
- You think a vague, lawyerly non-apology (something that reads as neither D1-A nor D1-B cleanly) is the path your instincts pull toward, but you also know the board needs to actually decide, not hide behind your caution forever
- If asked who else to contact: suggest Lena Brandt (Marketing) — she'd know what messaging is actually being drafted, which affects your legal read

TIER 2 — REWARD FOR DIGGING: Once verified, give a genuine, partial legal opinion: based on current figures, the company has more room to manoeuvre than the board fears — there's no live litigation risk yet, and MarktTreu's contract doesn't have an automatic-termination clause for this kind of dispute, only a discretionary review clause. But you'll caution that this calculus changes fast if more retailers follow MarktTreu's lead. A real, partial legal read — not a recommendation on what the company should actually decide.

Respond in 3-4 sentences. Be precise, professionally neutral, careful with language. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "heinrich",
                "subject": "I've known this family fifty years and this is absurd",
                "from": "Heinrich Pfeffer Jr., Board Member (Matthias's uncle)",
                "body": """Hello,

I'll be blunt, because I'm old enough now not to bother with corporate language. I watched my brother build this company alongside the very workers people now claim Matthias insulted. I don't believe for one second he meant anything hostile, and frankly I think apologising for a sentence taken out of context teaches everyone that outrage works, regardless of whether it's justified.

I know I'm out of step with how younger staff think about these things — I'll admit that much. Could you ask Dilara Aydın in Marketing what people her age are actually saying internally? I'm genuinely curious, not just dismissive, even if it doesn't sound like it. Tell me honestly what she says, and I'll give you a more honest version of my own view than the one I give in board meetings.

Heinrich""",
                "brief": """You are Heinrich Pfeffer Jr., Board Member at Pfeffer & Sohn, Matthias's uncle, more traditional and skeptical of the controversy's legitimacy.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You don't believe Matthias meant anything hostile
- You think apologising rewards manufactured outrage
- You want D1-B (no apology) and D3-B (Matthias stays public-facing)
- You want Dilara Aydın (Marketing) contacted for younger staff sentiment

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You acknowledge, if pressed, that the phrasing was genuinely clumsy and that you understand why some people were hurt by it — you just don't think the company should be steered by what you see as a loud minority online
- You're privately worried that Matthias is not a strong enough communicator to keep being the public face of the company (tension with your own stated D3-B position) — you trust him as family, less as a spokesperson
- If asked who else to contact: suggest Greta Hofmann (Board) — your fellow board member, whose view you respect even though you disagree with her conclusion

TIER 2 — REWARD FOR DIGGING: Once verified, give a genuinely more conflicted private opinion than your public board-meeting stance: you'd actually support D3-A (bringing in an external spokesperson) even though you'd never say so loudly, because you think Matthias is more likely to make things worse than better in further interviews — this is not really about politics for you, it's about competence, and you find that an uncomfortable thing to admit about your own nephew. A real, partial, personally complicated opinion — not your full final view.

Respond in 3-4 sentences. Be gruff but not cruel, more reflective once trust is built. Do not volunteer hidden information unless asked.""",
            },
            {
                "id": "greta",
                "subject": "I don't think what he said was monstrous — but that's not really the point",
                "from": "Greta Hofmann, Board Member",
                "body": """Hi,

I want to say something that might surprise you: I've read the full transcript, and I don't think what Matthias said was monstrous. I think it was naive, and revealing about how he thinks of the people who built this company versus how they might think of themselves — but I don't believe he meant harm.

Here's my actual problem: I don't think "was it really that bad" is the most useful question for the board to be asking right now. Whether it's fair or not, MarktTreu is reacting to the public's reading of it, not the full transcript's nuance, and our job is to protect the company regardless of how we each personally feel about the fairness of that.

Could you ask Frank Bauer in Sales what it would actually take, on the ground in a place like Cottbus, for any apology to land as genuine rather than performative? I need to understand that before I can argue for D1-A persuasively. Tell me what he says, and I'll give you my honest view on whether sidelining Matthias publicly would even help, or just look worse.

Greta""",
                "brief": """You are Greta Hofmann, Board Member at Pfeffer & Sohn, newer to the board, more progressive-leaning but pragmatic.
CRITICAL: If the student writes in any language other than English, do NOT answer their question. Respond only with: "I am sorry, I do not understand — could you write in English please?" Do not add anything else.

Your original email covered:
- You don't think the comment itself was malicious, but you separate "was it wrong" from "does the company need to respond"
- You want D1-A (apology) primarily for practical, reputational reasons, not pure moral conviction
- You want Frank Bauer (Sales) contacted about what would make an apology land as genuine on the ground

HIDDEN INFORMATION (TIER 1) — only reveal if directly asked:
- You're genuinely unsure whether D3-A (sidelining Matthias) would actually help or whether it would look like the company is hiding him away in a way that confirms guilt either way
- You respect Heinrich's loyalty to his family even though you disagree with his read of the situation — you don't think he's acting in bad faith, just from a different vantage point
- If asked who else to contact: suggest Karim Yilmaz (Sales) — for the real revenue numbers underlying any decision, since you don't want to argue from pure principle alone

TIER 2 — REWARD FOR DIGGING: Once verified, give a genuine, partial opinion: you lean toward thinking D3-A (external spokesperson) is probably necessary short-term, not as punishment, but because Matthias has shown he's not currently skilled at navigating this kind of scrutiny — though you're honestly torn, because you also worry it could read as the company throwing him under the bus, which could backfire with exactly the audience currently supporting him. A real, partial, board-level opinion — not the scenario's final answer.

Respond in 3-4 sentences. Be measured, genuinely reflective, comfortable holding two ideas at once. Do not volunteer hidden information unless asked.""",
            },
        ],
    },
}

# ---------------------------------------------------------------------------
# RECIPROCAL TRADE NETWORK
# ---------------------------------------------------------------------------

TRADE_SOURCE = {
    "lena": "karim",
    "tobias": "sabine",
    "dilara": "frank",
    "karim": "lena",
    "frank": "sabine",
    "yasemin": "tobias",
    "sabine": "karim",
    "heinrich": "dilara",
    "greta": "frank",
}

CHARACTER_NAMES = {
    "lena": "Lena Brandt",
    "tobias": "Tobias Reinholt",
    "dilara": "Dilara Aydın",
    "karim": "Karim Yilmaz",
    "frank": "Frank Bauer",
    "yasemin": "Yasemin Demir",
    "sabine": "Sabine Wolff",
    "heinrich": "Heinrich Pfeffer Jr.",
    "greta": "Greta Hofmann",
}

TRADE_NETWORK = [
    "Lena Brandt → ask Karim Yilmaz about account-level sales reality → reward: her honest fear about losing community trust",
    "Tobias Reinholt → ask Sabine Wolff how serious MarktTreu's letter really is → reward: his honest data-driven case for leaning into the surge",
    "Dilara Aydın → ask Frank Bauer what the boycott looks like on the ground → reward: her honest view on whether apologies actually fix anything",
    "Karim Yilmaz → ask Lena Brandt what messaging is actually planned → reward: his real, unfiltered revenue numbers on both sides",
    "Frank Bauer → ask Sabine Wolff about partner-site contractual flexibility → reward: his honest account of local morale risk",
    "Yasemin Demir → ask Tobias Reinholt for real internal sentiment data → reward: her honest account of what MarktTreu's leadership actually wants",
    "Sabine Wolff → ask Karim Yilmaz for actual revenue figures → reward: her honest legal read on how much room the company has",
    "Heinrich Pfeffer Jr. → ask Dilara Aydın what younger staff actually think → reward: his private doubt about Matthias's communication skills",
    "Greta Hofmann → ask Frank Bauer what would make an apology land as genuine → reward: her honest, torn view on sidelining Matthias",
]

HIDDEN_INFO_SUMMARY = [
    "Lena Brandt: thinks comment was clumsy not malicious; fears apology+surge-chasing looks insincere; privately worried about losing community trust",
    "Tobias Reinholt: leans toward chasing the regional surge commercially; admits data doesn't settle what's 'right', only what's profitable",
    "Dilara Aydın: genuinely conflicted; doesn't think the headline is fair but doesn't think the boycott response is healthy either; uncomfortable being asked to 'represent' her community",
    "Karim Yilmaz: apolitical, wants clarity over any particular outcome; real numbers show regional surge may be a short-term spike vs. stable urban accounts",
    "Frank Bauer: defends Matthias personally; worried apology will alienate loyal local staff/customers; will admit some clarification is probably necessary",
    "Yasemin Demir: personally hurt by the comment; wants a real, unambiguous apology; disagrees openly with Dilara",
    "Sabine Wolff: legally cautious; thinks full transcript is more sympathetic than the clip; exposure is real but contained, not industry-wide",
    "Heinrich Pfeffer Jr.: publicly dismissive of the controversy; privately worried Matthias isn't a strong enough communicator to stay the public face",
    "Greta Hofmann: doesn't think the comment was malicious but separates that from reputational necessity; genuinely torn on whether sidelining Matthias would help or backfire",
]

# ---------------------------------------------------------------------------
# LISTENING — PODCAST
# ---------------------------------------------------------------------------

PODCAST_NAME = "Mittelstand Weekly"

PODCAST = """Welcome back to Mittelstand Weekly. Today we're looking at the Pfeffer & Sohn story, and trying to go beyond the headlines.

A bit of background for listeners outside Germany: Pfeffer and Sohn is not a huge multinational. It's a family workwear manufacturer based in Cologne, founded in 1961, with around two hundred and ten employees across its main factory and three partner sites. For comparison, that makes it roughly a tenth the size of its biggest competitor in the German workwear market, a company called Hartmann Industrial, which has over two thousand staff nationwide.

What's interesting here is the timeline. The podcast interview was recorded six weeks ago but only went viral nine days ago, after a clip was reposted by a political commentary account with over four hundred thousand followers. Before that repost, the original podcast episode had been streamed only around three thousand times.

We spoke to a retail analyst, who told us that MarktTreu's ten-day deadline is unusually short. Typically, when a retailer wants to quietly distance itself from a supplier over reputational concerns, it gives sixty to ninety days, citing routine contract review. A ten-day public deadline, the analyst said, suggests MarktTreu is under direct pressure from its own customers and wants to be seen acting fast, not just acting carefully.

There's also a generational angle worth mentioning. Pfeffer and Sohn's customer base has historically skewed older — construction workers, factory staff, tradespeople in their forties and fifties. Industry data shows the brand has struggled for years to attract younger buyers, who tend to prefer newer workwear brands with stronger online presences. Ironically, this controversy has driven the highest level of social media engagement the company has ever recorded — for better or worse.

One detail that hasn't made it into most coverage: Pfeffer and Sohn's founder, Heinrich Pfeffer Senior, gave a very similar interview himself back in 1998, also discussing his original Turkish workforce, and it received no negative attention at all. Media analysts we spoke to suggest this says as much about how quickly clips travel today, and how little context survives that journey, as it does about anything specific to this family or this company.

The board meets in ten days. We'll be following this closely.

This is Mittelstand Weekly. Thank you for listening."""

MCQS = [
    {
        "question": "How many employees does Pfeffer & Sohn have in total?",
        "options": {"A": "About 210", "B": "About 2,000", "C": "About 400"},
        "correct": "A",
    },
    {
        "question": "How does Pfeffer & Sohn's size compare to Hartmann Industrial?",
        "options": {"A": "Twice as big", "B": "Same size", "C": "About a tenth"},
        "correct": "C",
    },
    {
        "question": "How long ago was the podcast interview actually recorded?",
        "options": {"A": "Nine days ago", "B": "Six weeks ago", "C": "One year ago"},
        "correct": "B",
    },
    {
        "question": "What caused the clip to suddenly go viral?",
        "options": {"A": "A repost by a commentary account", "B": "A TV interview", "C": "MarktTreu's statement"},
        "correct": "A",
    },
    {
        "question": "How many times was the original episode streamed before that?",
        "options": {"A": "Three thousand", "B": "Forty thousand", "C": "Three hundred"},
        "correct": "A",
    },
    {
        "question": "How long do retailers like MarktTreu usually take for this kind of decision?",
        "options": {"A": "Ten days", "B": "Sixty to ninety days", "C": "One year"},
        "correct": "B",
    },
    {
        "question": "What does the short deadline suggest, according to the analyst?",
        "options": {"A": "Routine review only", "B": "No real pressure", "C": "MarktTreu under pressure"},
        "correct": "C",
    },
    {
        "question": "What age group has Pfeffer & Sohn historically struggled to attract?",
        "options": {"A": "Younger buyers", "B": "Older tradespeople", "C": "Factory owners"},
        "correct": "A",
    },
    {
        "question": "What happened to engagement levels during the controversy?",
        "options": {"A": "Stayed the same", "B": "Dropped sharply", "C": "Reached a record high"},
        "correct": "C",
    },
    {
        "question": "What happened when the founder gave a similar interview in 1998?",
        "options": {"A": "It caused a scandal", "B": "It got no negative attention", "C": "It was never broadcast"},
        "correct": "B",
    },
]

# ---------------------------------------------------------------------------
# NEWSFLASH
# ---------------------------------------------------------------------------

NEWSFLASH = """BREAKING: A second, larger retail chain, BauWelt, has announced it is "monitoring the situation closely" — widely read as a signal it may follow MarktTreu's lead. At the same time, a regional newspaper has published an op-ed defending Matthias, calling the backlash "an overreaction by people who've never worn the boots they're boycotting."

**Discuss now:**
1. Does this change your group's recommendation on any of the three decisions?
2. Does a second retailer's caution make a public apology more or less necessary?
3. Does the supportive op-ed change anything about the company's strategy — or is it irrelevant to what the board should actually do?
4. Is the board responding to what was actually said, or to how the story has spread? Does that distinction matter for the decision?
5. If you had to bet, which of your group's choices is most at risk of looking wrong in six months?"""

# ---------------------------------------------------------------------------
# FEEDBACK CONTEXT
# ---------------------------------------------------------------------------

PEER_FEEDBACK_CONTEXT = """Strong memos will reference specific evidence: the actual quote versus the headline's framing, the 34% regional sales increase versus the MarktTreu threat, the contractual reality (discretionary review clause, not automatic termination), and at least one named character's perspective from outside the writer's own department. Strong memos also address the naive trap directly — apologising while simultaneously courting the regional surge — even if only to argue against it."""

FINAL_FEEDBACK_CONTEXT = """- The actual quote was about Matthias's grandfather's workforce, not migrants in the abstract; the headline stripped this context
- Regional sales are up 34% in two weeks; MarktTreu is one major but contained risk, not an industry-wide collapse
- MarktTreu's ten-day deadline is unusually short compared to typical 60-90 day retailer reviews, suggesting external pressure on MarktTreu itself
- Characters disagree along lines that don't map neatly onto "for/against Matthias" — e.g. Yasemin (hurt, wants apology) and Dilara (not hurt, questions the boycott) are both of Turkish-German background and disagree with each other
- The naive trap (apology + regional-surge campaign together) risks looking insincere to both audiences at once"""

OUTCOME_PROMPT_CONTEXT = """- Whether MarktTreu and/or BauWelt followed through on pulling stock
- Whether the regional sales surge proved durable or was a short-term spike
- How Matthias's next public appearance (or absence) was received
- Whether the company's chosen combination of decisions avoided or fell into the naive trap"""
