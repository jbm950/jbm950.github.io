# Google Summer of Code Blog Posts

{% for post in site.posts %}	
    <a href="{{ post.url }}">__{{ post.title }}__</a>  
    {{ post.date | date_to_long_string }}

    {{ post.excerpt }}
{% endfor %}
