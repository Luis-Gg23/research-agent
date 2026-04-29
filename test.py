data = {
 'query': 'What happened at the last wimbledon',
 'follow_up_questions': None,
 'answer': None,
 'images': [],
 'results': [
   {'url': 'https://en.wikipedia.org/wiki/Wimbledon_Championships',
    'title': 'Wimbledon Championships - Wikipedia',
    'content': 'Due to the COVID-19 pandemic, Wimbledon 2020 was cancelled ...',
    'score': 0.62365627198,
    'raw_content': None},
   {'url': 'https://www.cbsnews.com/news/wimbledon-men-final-carlos-alcaraz-novak-djokovic/',
    'title': "Carlos Alcaraz beats Novak Djokovic at Wimbledon men's final to ...",
    'content': 'In attendance on Sunday was Catherine, the Princess of Wales ...',
    'score': 0.5154731446,
    'raw_content': None}
 ],
 'response_time': 2.3
}
output = ""
for dato in data['results']:
    output += (f"Titulo:" + dato['title'] + "Contenido:"  + dato['content'])
print(output)