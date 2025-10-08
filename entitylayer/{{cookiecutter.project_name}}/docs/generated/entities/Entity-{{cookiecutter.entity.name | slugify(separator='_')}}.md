# Entity {{ cookiecutter.entity['name'] }}

## Properties
  | Identifier | Type | Description |
  |------------|------|-------------|
  {%- for element in cookiecutter.entity.elements %}
  |{{ element['aiurn'] | aiurnvar }}|{% if element['ref'] |length == 0 %}{{element['type']}}{%else%}{{element['ref'] | aiurnvar | capitalize }}Entity{%endif%}|{{element['description'] | replace('"','')}}|
  {%- endfor %}
   

