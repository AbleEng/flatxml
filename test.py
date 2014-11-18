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

print result['important-tag1'] # Cookies
