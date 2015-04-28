'''
The below method uses positional arguments for concatenating through the string.format() procedure provided by python.
The first positional argument is declared in the concept-title section which accepts a title and the second positional argument
is declared in concept-description
'''
def generate_concept_html(title, description):
        html = '''
	<div class="concept">
        <div class="concept-title">'''+ title +'''</div>
        <div class="concept-description"><p>'''+description+'''</p></div></div>'''
        return html

def make_html(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_html(concept_title, concept_description)

LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def make_html_for_many_concepts(list_of_concepts):
    html = ""
    for concept in list_of_concepts:
        html = html + make_html(concept)
    return html

print make_html_for_many_concepts(LIST_OF_CONCEPTS)
