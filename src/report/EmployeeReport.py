from fpdf import FPDF


class EmployeeReport(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=14)  # Setting font
        self.cell(50)  # Moving cursor to the right
        # Printing title
        self.cell(100, 10, "the employee Report", border=1, align="C")
        self.ln(20)  # Performing a line break

    def footer(self):
        self.set_y(-15)  # Position cursor at 1.5 cm from bottom
        self.set_font("helvetica", style="I", size=8)  # Setting font

        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")  # Printing page number

    def chapter_body(self, records):
        self.set_font("Times", size=12)
        for r in records:
            self.set_font("Times", size=12)  # Setting font: Times 12
            # Printing justified text:
            strTitle = f"'{r.BusinessEntityID}\t{r.FirstName}\t{r.LastName}'"
            strWidth = self.get_string_width(strTitle)
            strTitle += f"\t (Width={strWidth})"
            self.multi_cell(0, 5, strTitle)
            self.ln()  # Performing a line break

    def create(self, records, filepath):
        self.add_page()
        self.chapter_body(records)
        self.output(filepath)
