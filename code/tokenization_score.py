import csv
import os


def read_conll_file(address):
    ret = []
    line_number = 0
    print('Opening file ', address)
    with open(address, encoding='UTF-8') as f:
        line = f.readline()
        while line:
            l = line.strip()
            if len(l) == 0:
                ret.append([])  # End of sentence
            elif line:
                item = line.split('\t')
                if len(item) > 6:
                    print('Warning Line [ ', line_number, '] has  ', len(item), ' tokens it must be 6')
                    item = item[0:7]
                elif len(item) < 6:
                    print('Warning Line [ ', line_number, '] has  ', len(item), ' tokens it must be 6')
                    item[len(item):6] = '_' * (6 - len(item))
            stripped = []
            for it in item:
                s = it.strip()
                if len(s) == 0:
                    s = '_'
                stripped.append(s)
            line = f.readline()
            line_number += 1
            ret.append(stripped)
    return ret


def longest_common_subsequence_length(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m):
        c[i][0] = 0
    for j in range(1, n):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[m][n]


"""
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest = 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
            else:
                m[x][y] = 0
    return longest
"""


def compare_term(ref_items, out_items, ind):  # ind 1:normalized token, 2:stem, 3:lemma
    ref_item = reduce_column(ref_items, ind)
    out_item = reduce_column(out_items, ind)
    count = longest_common_subsequence_length(ref_item, out_item)

    return count


def compare_segment(ref_sentences, out_sentences):
    count = longest_common_subsequence_length(ref_sentences, out_sentences)
    return count / ref_sentences.count()


def extract_scores():
    path = '../data'
    files = os.scandir(path)
    references = []
    with open('../tokenization.csv', 'w', newline='\r\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    for f in files:
        if f.is_dir():
            print('Processing Folder : ', f.name)
            if os.path.isfile(path + '/' + f.name + '/' + f.name + '.ref'):
                references.append(f.name)
            else:
                print('Warning folder ' + f.name + ' Missing Reference file')

    all_results = []
    for f in os.scandir(path):
        if f.is_dir():
            output_files = os.listdir(path + '/' + f.name + '/');
            for of in output_files:
                if of.endswith('.out'):
                    other_folder = of[:-4]
                    if other_folder in references:
                        print('Evaluating Team ' + f.name + ' Output on Team ' + other_folder + ' Data')
                        scores = score_file(path + '/' + f.name + '/' + of,
                                            path + '/' + other_folder + '/' + other_folder + '.ref')
                        all_results.append([f.name, other_folder] + scores)

    with open('../scores/tokenization.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Team', 'Reference Team', 'Token Score', 'Stem Score', 'Lemma Score'])
        for r in all_results:
            writer.writerow(r)


def reduce_column(lst, column):
    ret = []
    for l in lst:
        if len(l) == 0:
            continue
        if column < len(l):
            ret.append(l[column])
        else:
            ret.append('_')
    return ret


def score_file(output_file, ref_file):
    ref_items = read_conll_file(ref_file)
    out_items = read_conll_file(output_file)
    # segment_score = compare_segment(ref_sentences, out_sentences)
    token_score = compare_term(ref_items, out_items, 1)
    stem_score = compare_term(ref_items, out_items, 2)
    lemma_score = compare_term(ref_items, out_items, 3)

    print('Token score:', token_score, ' Stem Score: ', stem_score, ' Lemma Score: ', lemma_score)
    return [token_score, stem_score, lemma_score]


def main():
    print('Scoring tool for SBU NLP Project')
    # score_file('../data/sample/sample.out', '../data/sample/sample.ref')
    extract_scores()


main()
