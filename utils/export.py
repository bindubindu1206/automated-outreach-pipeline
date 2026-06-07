import csv


def export_contacts(contacts):

    with open(
        "results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Title",
            "Email",
            "Lead Score"
        ])

        for contact in contacts:

            writer.writerow([
                contact["name"],
                contact["title"],
                contact["email"],
                contact["score"]
            ])

    print("\nResults saved to results.csv")