from fpdf import FPDF


def SimpleTable(path):
    pdf = FPDF()
    pdf.set_font(family='helvetica')
    pdf.add_page()

    def remove_empty_map_colspan(table_data: list, empty_cell: str) -> tuple[list, list]:
        """
        Remove the table cells with the specified value for empty_cell,
        and maps the cleaned data based on the following rules:
        - If the item/cell is not empty, it is mapped to 1.
        - If the item/cell is empty, it is mapped to 2, and the next item in the row is skipped.

        Args:
            table_data (list): Nested list representing the table data.
            empty_cell (string): Value representing an empty cell.

        Returns:
            tuple: A tuple containing the mapped colspan data and the cleaned data.

        Example:
            table_data = [
                ['0', '1', '2', '3'],
                ['A1', 'A2', '', 'A4'],
                ['B1', '', 'B3', 'B4'],
            ]
            empty_removed_table, colspans = remove_empty_map_colspan(table_data)
            print(empty_removed_table)
            # Output: [['0', '1', '2', '3'], ['A1', 'A2', 'A4'], ['B1', 'B3', 'B4']]
            print(colspans)
            # Output: [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1]]
        """

        colspans = []
        skip_next = False

        for row in table_data:
            new_row = []
            for item in row:
                if skip_next:
                    skip_next = False
                    continue
                if item != empty_cell:
                    new_row.append(1)
                else:
                    new_row.append(2)
                    skip_next = True
            colspans.append(new_row)

        empty_removed_table = [
            [item for item in row if item != empty_cell] for row in table_data
        ]

        return empty_removed_table, colspans

    table_data = [
        ['0', '1', '2', '3'],
        ['A1', 'A2', '-', 'A4'],
        ['B1', '-', 'B3', 'B4'],
    ]
    table_data, colpans = remove_empty_map_colspan(table_data, empty_cell='-')

    with pdf.table(width=120) as table:
        for data_row, colspan_row in zip(table_data, colpans):
            row = table.row()
            for cell, colspan in zip(data_row, colspan_row):
                row.cell(cell, colspan=colspan)

    pdf.output(path)
