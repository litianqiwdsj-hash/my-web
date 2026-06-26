with open(r'E:\web v1.2\web.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'site-card-desc' not in line:
        new_lines.append(line)

with open(r'E:\web v1.2\web.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Done! Removed', len(lines) - len(new_lines), 'lines')
