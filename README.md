### Description

Flattens an XML structure by joining nested tags with an underscore.  Returns a dictionary if no output file is provided.


### Example output

	"""
		<media>
			<songs>
				<pop>Thriller</pop>
				<metal>Master of Puppets</metal>
			</songs>
			<movies>
				<comedy>Wedding Crashers</comedy>
				<comedy>Superbad</comedy>
				<horror>Frozen</horror>
			</movies>
		</media>
    """

To CSV

    | media_songs_pop | media_songs_metal | media_movies_comedy_[0] | media_movies_comedy_[1] | media_movies_horror |
    | --------------- | ----------------- | ----------------------- | ----------------------- | ------------------- |
    | Thriller        | Master of Puppets | Wedding Crashers        | Superbad                | Frozen              |

As dictionary

    {
        'media_songs_pop': 'Thriller',
        'media_songs_metal': 'Master of Puppets',
        'media_movies_comedy_[0]': 'Wedding Crashers',
        'media_movies_comedy_[1]': 'Superbad',
        'media_movies_horror': 'Frozen'
    }



### Usage

Using a file:

    import flatxml
    
    result = flatxml.parse_file('/path/to/input_file.xml')

Using a blob:

    import flatxml

    result = flatxml.parse_blob("""<a>Apple</a>""")

    print(result['a']) # Apple

Using an xmltodict.OrderedDict object:

    import flatxml
    import xmltodict

    xml = """
        <useless-tag1>
            <useless-tag2>
                <important-tag1>Cookies</important-tag1>
                <important-tag2>Butter</important-tag2>
            </useless-tag2>
        </useless-tag1>
    """

    ordered_dict = xmltodict.parse(xml)
    slim_ordered_dict = ordered_dict['useless-tag1']['useless-tag2']

    result = flatxml.parse_ordered_dict(slim_ordered_dict)

    print(result['important-tag1']) # Cookies


All parsers accept an output file path as the second argument to generate a CSV

    flatxml.parse_blob('...', '/path/to/output.csv')


### Installation

    pip install flatxml
