import argparse


def init():

    global args

    example_text = '''examples:
    python3 %(prog)s --help
    python3 %(prog)s --test --fileName 'temp/test.pdf'
    python3 %(prog)s --configs
    python3 %(prog)s --report 'employee'
    python3 %(prog)s --report 'simple_table1'
    python3 %(prog)s --report 'simple_table2'
    python3 %(prog)s --getSqlServerDriver
    '''

    parser = argparse.ArgumentParser(description='Helper for creating pdf files.',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--test', action='store_true',
                        help='Create a test pdf file.')

    parser.add_argument('--fileName', type=str, help='Name of file.')

    parser.add_argument('--configs', action='store_true',
                        help='Show configurations.')

    parser.add_argument('--report', type=str, help='Get report.')

    parser.add_argument('--getSqlServerDriver', action='store_true',
                        help='Detect Sql server driver.')

    args = parser.parse_args()
