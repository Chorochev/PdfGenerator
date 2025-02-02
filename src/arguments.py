import argparse


def init():   

    global args 

    example_text = '''examples:
    python3 %(prog)s --help    
    python3 %(prog)s --test --fileName 'temp/test.pdf'    
    '''

    parser = argparse.ArgumentParser(description='Helper for creating pdf files.',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
       
    parser.add_argument('--test', action='store_true', help='Create a test pdf file.')

    parser.add_argument('--fileName', type=str, help='Name of file.')
    
    args = parser.parse_args()
