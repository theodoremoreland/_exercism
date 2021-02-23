number_to_word_mapping = {
    "1": {"count": "a", "order": "first"}
    , "2": {"count": "two", "order": "second"}
    , "3": {"count": "three", "order": "third"}
    , "4": {"count": "four", "order": "fourth"}
    , "5": {"count": "five", "order": "fifth"}
    , "6": {"count": "six", "order": "sixth"}
    , "7": {"count": "seven", "order": "seventh"}
    , "8": {"count": "eight", "order": "eighth"}
    , "9": {"count": "nine", "order": "ninth"}
    , "10": {"count": "ten", "order": "tenth"}
    , "11": {"count": "eleven", "order": "eleventh"}
    , "12": {"count": "twelve", "order": "twelfth"}
}

gifts = [
    "Partridge in a Pear Tree"
   , "Turtle Doves"
   , "French Hens"
   , "Calling Birds"
   , "Gold Rings"
   , "Geese-a-Laying"
   , "Swans-a-Swimming"
   , "Maids-a-Milking"
   , "Ladies Dancing"
   , "Lords-a-Leaping"
   , "Pipers Piping"
   , "Drummers Drumming"
]
 

def recite(start_verse, end_verse):
    song = []

    for verse_number in range(start_verse, end_verse + 1):
        nth_day = number_to_word_mapping[str(verse_number)]["order"]
        gifts_given = []

        for gift_countdown_number in range(verse_number, 0, -1):
            gift = gifts[gift_countdown_number - 1]
            gift_countdown_word = number_to_word_mapping[str(gift_countdown_number)]["count"]

            if verse_number > 1 and gift_countdown_number == 1:
                gifts_given.append(f'and {gift_countdown_word} {gift}')
            else:
                gifts_given.append(f'{gift_countdown_word} {gift}')

        gifts_given_string = ", ".join(gifts_given)
        verse = f'On the {nth_day} day of Christmas my true love gave to me: {gifts_given_string}.'
        song.append(verse)

    return song
