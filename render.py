import jinja2
import shutil
import os
import yaml

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
shutil.rmtree('./static', ignore_errors=True)
os.mkdir('./static')

    
with open('./blog.yml', 'r') as f:
    blog = yaml.safe_load(f)

# make blog dir in static
os.mkdir('./static/blog')

for post in blog['posts']:
    slug = post['slug']
    os.mkdir('./static/blog/' + slug)
    template = template_env.get_template('post.html')
    with open('./static/blog/' + slug + '/index.html', 'w') as f:
        f.write(template.render(post=post))
    shutil.copyfile('./images/' + post['image'], './static/blog/' + slug + '/' + post['image'])

template = template_env.get_template('blog.html')
with open('./static/blog/index.html', 'w') as f:
    f.write(template.render(blog=blog))

template = template_env.get_template('home.html')
with open('./static/index.html', 'w') as f:
    f.write(template.render(blog=blog))