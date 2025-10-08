from pydantic import BaseModel, Field
{% for element in cookiecutter.entity.elements %}{% if element['ref'] |length > 0 %}
from app.gen.entities.{{element['ref']| aiurnimport }}.entity import {{element['ref'] | aiurnvar | capitalize }}Entity
{% endif %}{% endfor %}

type TEXT = str
type LIST = list[str]
type NUMBER = float
type ANY = any
type BOOL = bool
type DICT = dict

class {{cookiecutter.entity.uid | aiurnvar | capitalize }}Entity(BaseModel):
    {%- if cookiecutter.entity.elements|length == 0 %}
    pass
    {%- endif %}
    {%- for element in cookiecutter.entity.elements %}
    {{ element['aiurn'] | aiurnvar }}:{% if element['ref'] |length == 0 %}{{element['type']}}{%else%}{{element['ref'] | aiurnvar | capitalize }}Entity{%endif%} = Field("",description="{{element['description'] | replace('"','')}}")
    {%- endfor %}