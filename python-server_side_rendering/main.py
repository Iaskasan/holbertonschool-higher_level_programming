from task_00_intro import generate_invitations
# Main file content


# Get the full path of the template file
template_file = 'python-server_side_rendering/template.txt'

# Read the template from the file
with open(template_file, 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
