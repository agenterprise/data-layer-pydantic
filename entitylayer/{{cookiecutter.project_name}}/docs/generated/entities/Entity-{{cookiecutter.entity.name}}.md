# Entity "{{ cookiecutter.entity['name'] }}""

### Properties
  | Identifier | Type | Description |
  |------------|------|-------------|
  {% for element in cookiecutter.entity.elements %}
  |{{ element['aiurn'] | aiurnvar }}|{{element['type'] | aiurnvar}}|{{element['description'] | replace('"','')}}|
  {% endfor %}
   

