def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template[:]
        for placeholder, value in attendee.items():
            processed_template = processed_template.replace(f"{{{placeholder}}}", value if value is not None else "N/A")

        # Check for any remaining placeholders and replace them with "N/A"
        processed_template = processed_template.replace("{", "").replace("}", "N/A")

        # Generate output files
        with open(f"output_{index}.txt", "w") as file:
            file.write(processed_template)
