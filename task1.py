import time
import logging


def mail_ids_creater(input_file_name):
    """
    Method: mail_ids_creater
    param input_file_name: Input file having list of names

    Purpose:
    Gets the input file having list of names and converts into list of mail ids
    and writes to the output file.

    * Mail ids will be lower case.
    * Words in name will be joined by '_'
    * Duplicate mail ids will be removed

    Author: Mukunthan Ragavan
    Created on: 5/8/2020
    """
    start_time = time.perf_counter()
    logging.basicConfig(filename='app.log', level=logging.DEBUG,  filemode='a', format='%(asctime)s %(module)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    domain = '@pydemo.com'

    with open(input_file_name, 'r') as fr:
        lines = fr.readlines()
    logger.info('Input file has been read')

    final_set = set()

    for line in lines:
        line = list(line.split())
        if len(line) > 1:
            line = '_'.join(line).lower()
        else:
            line = line[0].lower()
        final_set.add(line)

    mail_ids = [name + domain for name in final_set]
    logger.info('Mail IDs has been read')

    with open('names_updated.txt', 'w') as fw:
        for mail_id in mail_ids:
            fw.write(mail_id+'\n')
    logger.info('Output file has been read')

    end_time = time.perf_counter()

    logger.info('Time taken for script: {0:.5f} seconds'.format(end_time-start_time))


mail_ids_creater('names.txt')

print(mail_ids_creater.__doc__)
