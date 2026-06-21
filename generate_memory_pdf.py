from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 11)
        self.set_fill_color(30, 30, 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'Level 2 - Memory System (MEMORY.md) - Python Training Notes', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 13)
        self.set_fill_color(50, 90, 160)
        self.set_text_color(255, 255, 255)
        self.cell(0, 9, title, fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def sub_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(30, 30, 120)
        self.cell(0, 8, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)

    def body(self, text):
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def code_block(self, text):
        self.set_font('Courier', '', 9)
        self.set_fill_color(240, 240, 240)
        self.set_draw_color(180, 180, 180)
        self.multi_cell(0, 5.5, text, fill=True, border=1)
        self.ln(2)

    def table(self, headers, rows, col_widths):
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(70, 70, 70)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True)
        self.ln()
        self.set_font('Helvetica', '', 9)
        self.set_text_color(0, 0, 0)
        for row in rows:
            self.set_fill_color(248, 248, 252)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 6, cell, border=1, fill=True)
            self.ln()
        self.ln(3)

    def bullet(self, items):
        self.set_font('Helvetica', '', 10)
        for item in items:
            self.cell(6, 6, '-')
            self.multi_cell(0, 6, item)
        self.ln(1)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# ── What is the Memory System ─────────────────────────────────────────────────
pdf.section_title('What Is the Memory System?')
pdf.body(
    'Claude Code has a built-in persistent memory system. It stores key facts about you, '
    'your project, and your preferences in small markdown files on your computer. These files '
    'are read automatically at the start of every new chat session.\n\n'
    'This is how Claude "remembers" who you are and what you were working on - even after '
    'closing VS Code and coming back the next day.'
)

# ── Where the files live ──────────────────────────────────────────────────────
pdf.section_title('Where the Files Live (Your Project)')
pdf.code_block(
    'C:\\Users\\Administrator\\.claude\\projects\\\n'
    '  c--Users-Administrator-Downloads-Python-Training\\\n'
    '    memory\\\n'
    '      MEMORY.md           <- the index (always loaded first)\n'
    '      user_profile.md     <- who you are\n'
    '      project_context.md  <- what the project is about\n'
    '      feedback_style.md   <- how you like Claude to behave'
)
pdf.body(
    'The folder name "c--Users-Administrator-Downloads-Python-Training" is just Claude Code\'s '
    'way of turning your project folder path into a safe folder name (replacing \\ and : with -).'
)

# ── MEMORY.md - The Index ─────────────────────────────────────────────────────
pdf.section_title('MEMORY.md - The Master Index')
pdf.body(
    'MEMORY.md is the only file Claude reads on EVERY session start. It is a short index '
    '(max 200 lines) that lists all memory files and a one-line summary of each.'
)
pdf.sub_title('Your current MEMORY.md looks like this:')
pdf.code_block(
    '# Memory Index\n\n'
    '- [User Profile](user_profile.md) - Mohammad Kamran, Python learner,\n'
    '  prefers simple analogies and layman explanations\n\n'
    '- [Project Context](project_context.md) - Python Training workshop;\n'
    '  pin_extractor.py built so far; concepts covered\n\n'
    '- [Feedback & Style](feedback_style.md) - Use 7-year-old analogies,\n'
    '  show before/after code, use user\'s own files as examples'
)
pdf.body('The 200-line limit means: key facts only, not full transcripts. Think sticky notes, not a diary.')

# ── Memory File Format ────────────────────────────────────────────────────────
pdf.section_title('Memory File Format')
pdf.body('Every individual memory file has two parts: a frontmatter header and the actual content.')
pdf.code_block(
    '---\n'
    'name: user-profile\n'
    'description: Who the user is and how they like to learn\n'
    'metadata:\n'
    '  type: user\n'
    '---\n\n'
    'Mohammad is learning Python through a workshop format.\n'
    'Prefers simple explanations with real examples.\n'
    'Uses VS Code on Windows 11.'
)
pdf.body(
    'The section between --- is the frontmatter (machine-readable metadata).\n'
    'Everything below it is the memory content Claude actually uses.'
)

# ── 4 Memory Types ────────────────────────────────────────────────────────────
pdf.section_title('The 4 Types of Memory')
pdf.table(
    ['Type', 'What It Stores', 'Example'],
    [
        ['user',      'Who you are, skill level, preferences',     'Mohammad, Python learner, likes analogies'],
        ['feedback',  'What Claude should/should not do',          'Use 7-year-old explanations; no long comments'],
        ['project',   'Goals, decisions, what has been built',     'pin_extractor.py; concepts covered so far'],
        ['reference', 'Where to find things - files, tools, links','pin_extractor.py is in Python Training folder'],
    ],
    [28, 80, 82]
)

# ── Exact Flow ────────────────────────────────────────────────────────────────
pdf.add_page()
pdf.section_title('The Exact Flow - What Happens on Every New Chat')
pdf.code_block(
    'You open VS Code and start a new Claude Code chat\n'
    '                |\n'
    'Claude reads MEMORY.md first (always, automatically)\n'
    '                |\n'
    'MEMORY.md lists 3 files with one-line summaries\n'
    '                |\n'
    'Claude loads the relevant ones into its context\n'
    '                |\n'
    'Claude now knows:\n'
    '  - You are Mohammad, learning Python\n'
    '  - You are working on pin_extractor.py\n'
    '  - You like simple analogies\n'
    '  - What Python topics you have already covered\n'
    '                |\n'
    'You type: "continue where we left off"\n'
    '                |\n'
    'Claude already knows the full picture - no re-explaining needed'
)

# ── What You Can Do ───────────────────────────────────────────────────────────
pdf.section_title('What You Can Do With This System')
pdf.sub_title('Tell Claude to remember something:')
pdf.code_block(
    '"Remember that I don\'t like long code comments"\n'
    '  -> Claude writes a new memory file\n'
    '  -> Adds a line to MEMORY.md'
)
pdf.sub_title('Tell Claude to forget something:')
pdf.code_block(
    '"Forget that preference about X"\n'
    '  -> Claude finds and removes that memory file\n'
    '  -> Removes the line from MEMORY.md'
)
pdf.sub_title('Tell Claude to update memory:')
pdf.code_block(
    '"We have now also covered decorators and list comprehensions"\n'
    '  -> Claude updates project_context.md with new info'
)
pdf.sub_title('Ask Claude what it remembers:')
pdf.code_block(
    '"What do you remember about me?"\n'
    '  -> Claude reads and summarises all memory files for you'
)

# ── Your 3 Memory Files ───────────────────────────────────────────────────────
pdf.section_title('Your 3 Memory Files (Created This Session)')

pdf.sub_title('1. user_profile.md')
pdf.code_block(
    'Name: Mohammad Kamran\n'
    'Type: user\n\n'
    '- Learning Python through a structured workshop format\n'
    '- Prefers simple, layman explanations\n'
    '- Asks conceptual "why" questions alongside practical coding\n'
    '- Uses VS Code on Windows 11 with Claude Code extension\n'
    '- Interested in how tools work under the hood'
)

pdf.sub_title('2. project_context.md')
pdf.code_block(
    'Type: project\n\n'
    'Main file: pin_extractor.py\n\n'
    'Built so far:\n'
    '  - pin_extractor(poems) takes a list of poems\n'
    '  - Returns a list of secret codes\n'
    '  - Each code digit = length of the word at index = line_index\n\n'
    'Concepts covered:\n'
    '  split(), enumerate(), isinstance(), not, range(),\n'
    '  insert(), clear(), strip(), triple-quoted strings'
)

pdf.sub_title('3. feedback_style.md')
pdf.code_block(
    'Type: feedback\n\n'
    '- Use simple analogies and "7 year old" style explanations\n'
    '- Show wrong code AND corrected version side by side\n'
    '- Keep responses concise unless deep explanation is asked for\n'
    '- Use the user\'s own files as examples wherever possible'
)

# ── The One Limitation ────────────────────────────────────────────────────────
pdf.section_title('The One Limitation')
pdf.body(
    'MEMORY.md is capped at 200 lines. Once you hit that, older entries get dropped.\n\n'
    'This is why memory is for KEY FACTS only - not full conversation transcripts.\n\n'
    'Think of it like sticky notes on your desk:\n'
    '  Good: "Mohammad prefers analogies"\n'
    '  Bad:  Copy-pasting the entire conversation history'
)

# ── Memory vs Compaction ──────────────────────────────────────────────────────
pdf.section_title('Memory vs Compaction - What Is the Difference?')
pdf.table(
    ['Feature', 'Memory Files', 'Compaction'],
    [
        ['What it is',   'You write key facts to .md files',  'Claude summarises old chat messages'],
        ['When it runs', 'You tell Claude to remember',       'Automatically when context fills up'],
        ['Survives new chat?', 'YES - persists forever',      'NO - only within current session'],
        ['What is stored', 'Curated facts you chose to keep', 'Summary of conversation so far'],
        ['You control it?', 'YES - add, edit, delete anytime','NO - happens automatically'],
    ],
    [45, 73, 72]
)

out = r'c:\Users\Administrator\Downloads\Python Training\Level 2 - Memory MD.pdf'
pdf.output(out)
print(f'PDF saved: {out}')

