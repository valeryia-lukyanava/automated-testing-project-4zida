from fpdf import FPDF
from config import CELL_HEIGHT


class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation='L')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 8)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

    def add_general_info_with_border(self, title, date, border):
        self.set_font('Arial', '', 12)
        self.cell(w=80, h=CELL_HEIGHT, txt=title, ln=0, border=border)
        self.set_font('Courier', 'B', 12)
        self.cell(w=80, h=CELL_HEIGHT, txt=date, ln=0, border=border)

    def add_header(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(w=0, h=2 * CELL_HEIGHT, txt=title, ln=1, align='C')

    def add_chart(self, source_file):
        self.ln(2 * CELL_HEIGHT)
        self.image(source_file, x=10, w=270, type='PNG', link='')

    def add_link(self, site_url, link_title, link):
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 255)
        self.set_font('', 'U')
        self.cell(w=115, h=CELL_HEIGHT, txt=f"{link_title}{site_url}", ln=1, link=link, align='R')
        self.set_text_color(0, 0, 0)

    def add_general_info(self, title, site_url, new_line=0, is_link=False):
        self.set_font('Arial', '', 12)
        self.cell(w=80, h=CELL_HEIGHT, txt=title, ln=0)
        if is_link:
            self.set_text_color(0, 0, 255)
            self.set_font('', 'U')
            self.set_font('Courier', 'B', 12)
            self.cell(w=80, h=CELL_HEIGHT, txt=site_url, ln=new_line)
            self.set_text_color(0, 0, 0)
        else:
            self.set_font('Courier', 'B', 12)
            self.cell(w=80, h=CELL_HEIGHT, txt=site_url, ln=new_line)
