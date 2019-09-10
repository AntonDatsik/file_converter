from weasyprint import HTML


def html_str_to_pdf(html_str):
    return HTML(string=html_str).write_pdf()


def html_link_to_pdf(html_link):
    return HTML(url=html_link).write_pdf()
