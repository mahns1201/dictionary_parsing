reserved_key = {'title' : '', 'label' : '', 'orgin' : '', 'pronunciation' : '', 'mean' : '', 'relation' : ''}

reserved_key['title'] = 'ABC'

print(reserved_key['title'])

test = reserved_key['title']
slug = test[:1] + '/' + test

print(slug)