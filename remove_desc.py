import re

with open(r'E:\web v1.2\web.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all <p class="site-card-desc" ...> ... </p> elements
# Use non-greedy match to handle the entire element
pattern = r'<p class="site-card-desc"[^>]*>.*?</p>\s*'
content_new, count = re.subn(pattern, '', content, flags=re.DOTALL)

print(f'Removed {count} site-card-desc elements')

with open(r'E:\web v1.2\web.html', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('Done!')
