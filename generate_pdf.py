from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 11)
        self.set_fill_color(30, 30, 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'Context Window & Optimization Methods - Python Training Notes', fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
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
            fill = row[0].startswith('  ')
            self.set_fill_color(248, 248, 248) if fill else self.set_fill_color(255, 255, 255)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 6, cell, border=1, fill=True)
            self.ln()
        self.ln(3)


pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# ── What Is a Context Window ──────────────────────────────────────────────────
pdf.section_title('What Is a Context Window?')
pdf.body(
    'Think of Claude\'s memory like a scrolling window. It can only see a fixed number of words '
    'at a time. As the conversation grows, old messages fall off the top. Claude Code handles this '
    'by compacting - summarizing old messages so less space is used, but some detail is lost.\n\n'
    'A context window is measured in tokens (roughly 0.75 words per token):\n'
    '  200K context  =  ~150,000 words  (about 300 pages)\n'
    '  1M context    =  ~750,000 words  (about 1,500 pages)'
)

# ── Current Claude Models ─────────────────────────────────────────────────────
pdf.section_title('Current Claude Models & Context Windows')
pdf.table(
    ['Model', 'Context Window', 'Max Output', 'Input $/1M', 'Output $/1M'],
    [
        ['Claude Fable 5',    '1M tokens',   '128K', '$10.00', '$50.00'],
        ['Claude Mythos 5',   '1M tokens',   '128K', '$10.00', '$50.00'],
        ['Claude Opus 4.8',   '1M tokens',   '128K', '$5.00',  '$25.00'],
        ['Claude Opus 4.7',   '1M tokens',   '128K', '$5.00',  '$25.00'],
        ['Claude Opus 4.6',   '1M tokens',   '128K', '$5.00',  '$25.00'],
        ['Claude Sonnet 4.6', '1M tokens',   '64K',  '$3.00',  '$15.00'],
        ['Claude Haiku 4.5',  '200K tokens', '64K',  '$1.00',  '$5.00' ],
    ],
    [55, 35, 25, 30, 32]
)
pdf.body('Note: Context windows do NOT change by plan. What changes by tier is rate limits (requests per minute).')

# ── The Full Optimization Ladder ──────────────────────────────────────────────
pdf.section_title('The Full Optimization Ladder')

pdf.sub_title('Level 1 - Basic Solutions (No Code Needed)')
pdf.table(
    ['Method', 'How It Works', 'Problem'],
    [
        ['Start fresh chats',   'New topic = new chat',                       'You lose all previous context'],
        ['Manual summarize',    'Copy summary into new chat',                 'You do it manually every time'],
        ['Keep chats short',    'One task per conversation',                  'Not practical for long projects'],
        ['Use files',           'Store notes in .md files and re-paste',      'Tedious, easy to forget'],
    ],
    [45, 75, 70]
)

pdf.sub_title('Level 2 - What Claude Code Does (Built-in Memory System)')
pdf.body(
    'Claude Code has a built-in memory system stored in files under:\n'
    '  C:\\Users\\Administrator\\.claude\\projects\\...\\memory\\\n\n'
    'Key facts are written to memory files. MEMORY.md is an index that is always loaded at the '
    'start of every chat. So even after a fresh session, Claude reads your memory and picks up context.\n\n'
    'Limitation: MEMORY.md has a 200-line limit. It stores key facts, not everything.'
)

pdf.sub_title('Level 3 - Intermediate: RAG (Retrieval Augmented Generation)')
pdf.body(
    'Instead of putting everything in context, you store knowledge in a searchable database. '
    'When you ask a question, only the RELEVANT pieces are pulled out and given to the AI.\n\n'
    'Like a library - you don\'t carry all books in your head, you look up what you need.'
)
pdf.code_block(
    'User asks: "What was the bug in pin_extractor?"\n'
    '       |\n'
    'Search database for: "pin_extractor bug"\n'
    '       |\n'
    'Find relevant chunk -> inject only that into context\n'
    '       |\n'
    'AI answers with just that piece - no context wasted'
)

pdf.sub_title('Level 3b - Chunking + Summarization')
pdf.body(
    'Break large documents into small chunks. Summarize each chunk. '
    'Only load summaries unless full detail is needed.\n\n'
    'Rolling Summary (what Claude Code compaction does):\n'
    '  1. Summarize the first half of the conversation\n'
    '  2. Drop the original messages\n'
    '  3. Keep only the summary + recent messages\n'
    '  4. Repeat as the conversation grows'
)

pdf.add_page()

pdf.sub_title('Level 4 - Advanced: Vector Databases')
pdf.body(
    'Every piece of information is turned into a mathematical fingerprint called an embedding. '
    'When you ask something, your question\'s fingerprint is compared to all stored fingerprints. '
    'The closest matches are retrieved.\n\n'
    'Popular tools: Pinecone, Weaviate, pgvector, ChromaDB'
)
pdf.code_block(
    '"Tell me about the poem function"\n'
    '       |\n'
    'Convert to vector: [0.23, 0.87, 0.12, ...]\n'
    '       |\n'
    'Find nearest stored vectors in database\n'
    '       |\n'
    'Return: pin_extractor.py, poem variable, split() explanation'
)

pdf.sub_title('Level 4b - Knowledge Graphs')
pdf.body(
    'Store information as connected nodes - like a mind map in a database. '
    'Great for projects where things relate to each other.'
)
pdf.code_block(
    'poem          -> has method  -> split()\n'
    'split()       -> returns     -> list\n'
    'list          -> used in     -> pin_extractor\n'
    'pin_extractor -> returns     -> secret_codes'
)

pdf.sub_title('Level 5 - Expert: Fine-tuning & Agent Memory')
pdf.body(
    'Fine-tuning: Train the AI model itself on your project\'s knowledge. '
    'The knowledge is baked into the model weights - no context needed at runtime. '
    'Expensive but permanent.\n\n'
    'External Memory Stores (what production agents use): Agents can read and write to external '
    'systems - databases, files, APIs - as they work. They don\'t need to hold everything in context '
    'because they can look it up on demand.'
)

# ── Summary Diagram ───────────────────────────────────────────────────────────
pdf.section_title('Summary - The Full Ladder')
pdf.code_block(
    'BASIC      ->  Start new chats / manual notes\n'
    '                    |\n'
    'BUILT-IN   ->  CLAUDE.md + memory files (what we use now)\n'
    '                    |\n'
    'SMARTER    ->  RAG - only pull relevant chunks into context\n'
    '                    |\n'
    'ADVANCED   ->  Vector databases + embeddings\n'
    '                    |\n'
    'EXPERT     ->  Knowledge graphs + fine-tuning + agent memory'
)

# ── For Your Project ──────────────────────────────────────────────────────────
pdf.section_title('For Your Python Training Project Specifically')
pdf.body(
    'Right now you have:\n'
    '  - Memory files storing key facts (your project, what you\'re learning)\n'
    '  - Compaction kicking in when the chat gets long (summarizes oldest parts)\n\n'
    'If this were a LIVE PRODUCT (like a customer support bot that learns forever), you\'d use:\n'
    '  RAG + a vector database - the most practical production solution that scales to\n'
    '  infinite knowledge without ever hitting context limits.\n\n'
    'The AI never "knows" everything upfront - it just knows where to look.'
)

out = r'c:\Users\Administrator\Downloads\Python Training\Context_Window_Optimization.pdf'
pdf.output(out)
print(f'PDF saved: {out}')
