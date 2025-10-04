import io
from django.core.management import call_command

with io.open("data.json", "w", encoding="utf-8") as f:
    call_command(
        "dumpdata",
        exclude=["auth.permission", "contenttypes", "sessions", "admin.logentry"],
        indent=4,
        stdout=f
    )
