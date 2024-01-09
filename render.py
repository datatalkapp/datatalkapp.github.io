import jinja2
import shutil
import os
import yaml
import datetime

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))

# Delete and recreate static folder
shutil.rmtree('./static', ignore_errors=True)
os.mkdir('./static')

# Copy font files
shutil.copytree('./fonts', './static/fonts')

# Blog
with open('./blog.yml', 'r') as f:
    blog = yaml.safe_load(f)
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

# Home
template = template_env.get_template('home.html')
with open('./static/index.html', 'w') as f:
    f.write(template.render(blog=blog))

# copy all files from ./images to ./static
shutil.copytree('./images', './static/images')
shutil.copyfile('./videos/movie_with_audio.mp4', './static/movie_with_audio.mp4')


# Sitemap
urls = []
for post in blog['posts']:
    urls.append('https://datatalk.app/blog/' + post['slug'] + '/')
urls.append('https://datatalk.app/blog/')
urls.append('https://datatalk.app/')
sitemap = [
    {"loc": url, "lastmod": datetime.datetime.now().strftime("%Y-%m-%d"), "changefreq": "monthly"} for url in urls
]

# Render sitemap.xml and robots.txt
template = template_env.get_template('sitemap.xml')
with open('./static/sitemap.xml', 'w') as f:
    f.write(template.render(sitemap=sitemap))
template = template_env.get_template('robots.txt')
with open('./static/robots.txt', 'w') as f:
    f.write(template.render())

