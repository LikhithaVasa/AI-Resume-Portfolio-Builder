from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    for line in text.split("\n"):

        content.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(content)

    return filename