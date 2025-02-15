from fpdf import FPDF

data = [
    ['Lp.', 'Nazwa Uslugi/Towaru', 'Jm', 'Ilosc', 'Cena Netto', 'Wartosc Netto', 'VAT'],
    ['1', 'maka', 'szt.', '10kg', '  11,32  zl ', '  11,32  zl ', '23%'],
    ['2', 'ryz test text has a big size', 'szt.', '15kg', '  10,00  zl ', '  10,00  zl ', '8%'],
    ['3', 'makaron', 'szt.', '5kg', '  3,60  zl ', '  3,60  zl ', '23%'],
    ['4', 'kasza', 'szt.', '8kg', '  2,00  zl ', '  2,00  zl ', '8%', ],
    ['5', 'cukier', 'szt.', '20kg', '  20,00  zl ', '  20,00  zl ', '8%'],
    ['6', 'soda', 'szt.', '3kg', '  1,00  zl ', '  1,00  zl ', '23%'],
    ['7', 'smietana', 'szt.', '1l', '  15,00  zl ', '  15,00  zl ', '23%'],
    ['8', 'bulka tarta', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['9', 'bulka tarta XXXXX', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['10', 'maka', 'szt.', '10kg', '  11,32  zl ', '  11,32  zl ', '23%'],
    ['11', 'ryz test text has a big size', 'szt.', '15kg', '  10,00  zl ', '  10,00  zl ', '8%'],
    ['12', 'makaron', 'szt.', '5kg', '  3,60  zl ', '  3,60  zl ', '23%'],
    ['13', 'kasza', 'szt.', '8kg', '  2,00  zl ', '  2,00  zl ', '8%'],
    ['14', 'cukier', 'szt.', '20kg', '  20,00  zl ', '  20,00  zl ', '8%'],
    ['15', 'soda', 'szt.', '3kg', '  1,00  zl ', '  1,00  zl ', '23%'],
    ['16', 'smietana', 'szt.', '1l', '  15,00  zl ', '  15,00  zl ', '23%'],
    ['17', 'bulka tarta', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['18', 'bulka tarta XXXXX', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['19', 'maka', 'szt.', '10kg', '  11,32  zl ', '  11,32  zl ', '23%'],
    ['20', 'ryz test text has a big size', 'szt.', '15kg', '  10,00  zl ', '  10,00  zl ', '8%'],
    ['21', 'makaron', 'szt.', '5kg', '  3,60  zl ', '  3,60  zl ', '23%'],
    ['22', 'kasza', 'szt.', '8kg', '  2,00  zl ', '  2,00  zl ', '8%', ],
    ['23', 'cukier', 'szt.', '20kg', '  20,00  zl ', '  20,00  zl ', '8%'],
    ['24', 'soda', 'szt.', '3kg', '  1,00  zl ', '  1,00  zl ', '23%'],
    ['25', 'smietana', 'szt.', '1l', '  15,00  zl ', '  15,00  zl ', '23%'],
    ['26', 'bulka tarta', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['27', 'bulka tarta XXXXX', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['28', 'maka test text has a big size maka test text has a big size',
        'szt.', '10kg', '  11,32  zl ', '  11,32  zl ', '23%'],
    ['29', 'ryz', 'szt.', '15kg', '  10,00  zl ', '  10,00  zl ', '8%'],
    ['30', 'makaron', 'szt.', '5kg', '  3,60  zl ', '  3,60  zl ', '23%'],
    ['31', 'kasza', 'szt.', '8kg', '  2,00  zl ', '  2,00  zl ', '8%'],
    ['32', 'cukier', 'szt.', '20kg', '  20,00  zl ', '  20,00  zl ', '8%'],
    ['33', 'soda', 'szt.', '3kg', '  1,00  zl ', '  1,00  zl ', '23%'],
    ['34', 'smietana', 'szt.', '1l', '  15,00  zl ', '  15,00  zl ', '23%'],
    ['35', 'bulka tarta', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%'],
    ['36', 'bulka tarta XXXXX', 'szt.', '2kg', '  1,56  zl ', '  1,56  zl ', '23%']]

CELL_WIDTH = 20


def get_num_of_lines_in_multicell(pdf, message):
    global CELL_WIDTH
    # divide the string in words
    words = message.split(" ")
    line = ""
    n = 1
    previous_line_width = 0
    for word in words:
        line += word + " "
        line_width = pdf.get_string_width(line)
        # In the next if it is necessary subtract 1 to the WIDTH
        if line_width > (CELL_WIDTH-1) * 2 - 1:
            # the multi_cell() insert a line break
            n += 2
            # reset of the string
            line = word + " "
        elif line_width > CELL_WIDTH-1:
            # the multi_cell() insert a line break
            n += 1
            # reset of the string
            line = word + " "
    return n


def get_num_lines_max(pdf, row):
    num_lines_max = 0
    for item in row:
        num_lines = get_num_of_lines_in_multicell(pdf, item)
        if num_lines > num_lines_max:
            num_lines_max = num_lines
    return num_lines_max


def SimpleTable(spacing, path):
    global CELL_WIDTH
    pdf = FPDF()

    # pdf.add_font('Segoe Ui', '', r'C:\Windows\Fonts\seguibl.ttf')
    pdf.set_font('Times')

    pdf.add_page()
    # pdf.set_font("Segoe Ui")
    counter = 0

    col_width = pdf.w / 10
    CELL_WIDTH = col_width
    row_height = pdf.font_size

    for row in data:
        counter += 1
        new_x = 10
        saveY = 0

        if counter == 1:
            for item in row:
                pdf.set_xy(new_x, 10)
                pdf.set_fill_color(128, 128, 128)
                num_lines = get_num_of_lines_in_multicell(pdf, item)
                if num_lines == 1:
                    pdf.multi_cell(col_width, row_height*3, txt=item, border=1, align="C", fill=True)
                elif num_lines == 2:
                    pdf.multi_cell(col_width, (row_height*3)/2, txt=item, border=1, align="C", fill=True)
                else:
                    pdf.multi_cell(col_width, row_height, txt=item, border=1, align="C", fill=True)
                if pdf.get_y() > saveY:
                    saveY = pdf.get_y()
                new_x += col_width
                pdf.set_xy(new_x, 10)
            pdf.set_xy(10, saveY)
        else:
            num_lines_max = get_num_lines_max(pdf, row)
            if num_lines_max == 1:
                for item in row:
                    pdf.cell(col_width, row_height * spacing, txt=item, border=1, align="C")
                pdf.ln(row_height * spacing)
            else:
                multicell_height = row_height * num_lines_max

                if (pdf.get_y() > (pdf.w - multicell_height)):
                    pdf.add_page()
                    new_x = 10
                    saveY = 0

                y_multicell_row = pdf.get_y()
                for item in row:
                    num_lines = get_num_of_lines_in_multicell(pdf, item)
                    pdf.multi_cell(col_width, multicell_height/num_lines, txt=item, border=1, align="C", fill=False)
                    if pdf.get_y() > saveY:
                        saveY = pdf.get_y()
                    new_x += col_width
                    pdf.set_xy(new_x, y_multicell_row)
                pdf.set_xy(10, saveY)

    pdf.output(path)
