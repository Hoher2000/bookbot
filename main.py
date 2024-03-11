def main():
    path = '/home/paulina/workspace/github.com/Hoher2000/bookbot/books/frankenstein.txt'
    def count_word_letter(file=path):
        with open(file) as t:
            text = t.read()
            word_counts = len(text.split())
            letter_counts = {}
            for letter in text.lower():
                if letter.isalpha():
                    letter_counts.setdefault(letter, 0)
                    letter_counts[letter] += 1

        letter_counts = {letter: letter_counts[letter] 
                    for letter in sorted(letter_counts,
                                        key=lambda x: -letter_counts[x])}
        return file, word_counts, letter_counts
    
    book, word_counts, letter_counts = count_word_letter()
    print(f'--- Begin report of {book} ---')
    print(f'{word_counts} words found in the document')
    for letter in letter_counts:
        print(f"The '{letter}' character was found {letter_counts[letter]} times")
    print('---end report---')

if __name__ == '__main__':
    main()


