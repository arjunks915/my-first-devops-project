import datetime
import random

# 1. Generate some dummy data representing server metrics
cpu_load = f"{random.randint(5, 45)}%"
memory_sucks = f"{random.randint(60, 95)}%"
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Open our index.html file and inject the dynamic data
with open("index.html", "r") as file:
    html_content = file.read()

# This is a basic find-and-replace to insert our metrics dynamically
updated_content = html_content.replace(
    '💻 Server Load: Stable', f'💻 Server Load: {cpu_load}'
)
updated_content = updated_content.replace(
    '💾 Memory Available: 84%', f'💾 Memory Available: {memory_available}'
)
updated_content = updated_content.replace(
    'Pipeline Deployment Verification Active', f'Last System Check: {current_time}'
)

# 3. Save the changes back to index.html
with open("index.html", "w") as file:
    file.write(updated_content)

print(f"✅ Dashboard updated successfully at {current_time}!")