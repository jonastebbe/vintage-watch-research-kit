"""Build the original, fillable research packet. Requires reportlab."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.colors import HexColor, white

ROOT = Path(__file__).parent
INK = HexColor('#1b302e')
MUTED = HexColor('#52645f')
LINE = HexColor('#b5c5bf')


def build(size, name):
    w, h = size
    c = canvas.Canvas(str(ROOT / 'output/pdf' / name), pagesize=size)
    c.setTitle('Vintage Watch Research Packet | The Index')
    c.setAuthor('The Index')
    c.setSubject('Observations, evidence and photo requests; not authentication or appraisal')
    left, right = 42, w - 42
    width = right - left

    def text(x, y, value, font=10, bold=False, color=INK):
        c.setFillColor(color)
        c.setFont('Helvetica-Bold' if bold else 'Helvetica', font)
        c.drawString(x, y, value)

    def page(n, title, subtitle):
        text(left, h-40, 'THE INDEX  /  FIELD NOTES', 9, True)
        text(left, h-75, title, 24, True)
        text(left, h-96, subtitle, 10, color=MUTED)
        c.setStrokeColor(LINE)
        c.line(left, 49, right, 49)
        text(left, 34, 'theindex.watch  |  Original template: MIT licence  |  Research, not authentication', 8)
        c.linkURL('https://theindex.watch', (left, 28, left+72, 43), relative=0)
        text(right-32, 34, f'{n} / 3', 9)

    def field(key, label, y, height=25, x=None, fieldwidth=None):
        x = left if x is None else x
        fieldwidth = width if fieldwidth is None else fieldwidth
        text(x, y, label, 9, True)
        c.acroForm.textfield(name=key, tooltip=label, x=x, y=y-height-8,
            width=fieldwidth, height=height, fontName='Helvetica', fontSize=10,
            textColor=INK, borderColor=LINE, fillColor=white,
            borderWidth=.6, forceBorder=True,
            fieldFlags='multiline' if height>30 else '', maxlen=1500)
        return y-height-29

    def note(y, *lines):
        for line in lines:
            text(left, y, line, 9, color=MUTED)
            y -= 13
        return y-12

    page(1, 'Record before interpreting', 'One packet per watch. Type into the fields or print and write by hand.')
    y=h-125
    half=(width-16)/2
    field('research_id', 'Research ID (use this on every page)', y, x=left, fieldwidth=half)
    y=field('recorded_on', 'Recorded on / researcher', y, x=left+half+16, fieldwidth=half)
    y=field('dial', 'Visible brand and dial text - transcribe exactly', y, 42)
    y=field('reference', 'Reference marking, location and photo ID', y)
    y=field('serial', 'Case / movement numbers and locations - keep full numbers private', y)
    y=field('movement', 'Movement / calibre markings (if already safely visible)', y)
    y=field('configuration', 'Case, hands, markers, bezel, crown and bracelet observations', y, 52)
    y=field('condition', 'Visible alterations, damage, missing views or conflicting details', y, 42)
    note(y, 'Write "not visible" where appropriate. A blank does not mean a feature is absent.',
         'Keep original photographs privately. Have a qualified person handle any case opening.')
    c.showPage()

    page(2, 'Connect claims to evidence', 'Keep an observation, a seller claim and a conclusion distinct.')
    y=field('evidence_research_id', 'Research ID / evidence ID', h-125)
    y=field('claim', 'Claim being checked (reference, configuration, date or other)', y, 35)
    y=field('source', 'Source: title, author, URL or book edition + page; date accessed', y, 48)
    y=field('observation', 'What this source actually shows; exact specimen / component covered', y, 48)
    y=field('limits', 'What it does NOT establish; conflicts or repeated sources', y, 42)
    y=field('dates', 'Date claim + kind: number allocation / manufacture / assembly / delivery / sale / service', y, 35)
    y=field('conclusion', 'Current conclusion and qualifications; evidence still needed', y, 48)
    note(y, 'Copy this page for each significant claim. Retain sources that disagree.',
         'A plausible serial date does not show that every component left the factory together.')
    c.showPage()

    page(3, 'Request the missing view', 'Ask for the photograph that answers your unresolved question.')
    y=field('photo_research_id', 'Research ID', h-125)
    y=field('question', 'The specific question I need to resolve', y, 38)
    text(left, y, 'VIEWS TO CONSIDER', 10, True)
    y-=26
    views=[('dial_front', 'Straight-on dial: printing and minute track in focus'),
           ('dial_angle', 'Angled dial: surface texture and reflections'),
           ('hands', 'Hands, hour markers and display details'),
           ('case', 'Both case sides, crown and pushers'),
           ('back', 'Caseback, inscriptions and hallmarks'),
           ('markings', 'Reference markings with location identifiable'),
           ('bracelet', 'Bracelet, end links and clasp markings'),
           ('measure', 'Dimensions, with measurement method and crown inclusion'),
           ('inside', 'Movement / inner caseback, only with qualified handling'),
           ('documents', 'Documents relevant to the claim; private details redacted')]
    for key,label in views:
        c.acroForm.checkbox(name=key, tooltip=label, x=left, y=y-3, size=11,
            borderColor=LINE, fillColor=white, textColor=INK, buttonStyle='check')
        text(left+20, y, label, 10)
        y-=25
    y-=8
    y=field('request', 'My request: "Could you photograph ... so I can check ...?"', y, 48)
    y=note(y, 'Do not ask an inexperienced owner to open or dismantle a watch.',
           'Photos alone do not prove authenticity, water resistance or component originality.')
    text(left, y, 'REFERENCE STARTING POINTS', 9, True)
    for label,url in [('References: theindex.watch/watches','https://theindex.watch/watches'),
                      ('Dating limits: theindex.watch/serial-check','https://theindex.watch/serial-check'),
                      ('Further reading: theindex.watch/books','https://theindex.watch/books')]:
        y-=16
        text(left, y, label, 9)
        c.linkURL(url, (left,y-3,right,y+10), relative=0)
    c.showPage()
    c.save()


if __name__ == '__main__':
    (ROOT / 'output/pdf').mkdir(parents=True, exist_ok=True)
    build(A4, 'vintage-watch-research-a4.pdf')
    build(letter, 'vintage-watch-research-letter.pdf')
