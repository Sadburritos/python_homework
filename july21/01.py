def get_diag_words(input):
    if not input:
        return ""

    main_diag = [input[i][i] for i in range(min(len(input), len(input[0])))]
    side_diag = [input[i][len(input) - 1 - i] for i in range(min(len(input), len(input[0])))]

    main_word = ''.join(main_diag)
    side_word = ''.join(side_diag)

    return main_word + " " + side_word

#-----------------------------------------------------------------------------------

def test_get_diag_words():
    input = [['ж', 'ф', 'л'],
             ['р', 'и', 'а'],
             ['с', 'з', 'л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б', 'ф', 'л', 'т', ' ', 'в'],
             ['р', 'е', 'а', 'о', 'о', 'щ'],
             ['е', 'и', 'л', 'р', 'э', 'к'],
             ['г', 'ы', 'о', 'а', 'ф', 'о'],
             ['н', 'н', 'а', 'а', 'я', 'ч'],
             ['а', 'з', 'л', 'ц', 'в', ' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect


test_get_diag_words()
