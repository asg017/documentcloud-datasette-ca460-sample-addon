"""
This is a hello world add-on for DocumentCloud.

It demonstrates how to write a add-on which can be activated from the
DocumentCloud add-on system and run using Github Actions.  It receives data
from DocumentCloud via the request dispatch and writes data back to
DocumentCloud using the standard API
"""

import requests

from documentcloud.addon import AddOn


class HelloWorld(AddOn):
    """An example Add-On for DocumentCloud."""

    def main(self):
        """The main add-on functionality goes here."""
        base_url = self.data["base_url"].rstrip("/")
        database = self.data["database"]
        token = self.data["token"]
        ingest_url = f"{base_url}/{database}/-/ca460/api/ingest"

        self.set_message("Hello World start!")

        for document in self.get_documents():
            print(document, document.canonical_url)
            response = requests.post(
                ingest_url,
                headers={"Authorization": f"Bearer {token}"},
                json={"url": document.canonical_url},
            )
            print(response.status_code)
            response.raise_for_status()

        self.set_message("Hello World end!")


if __name__ == "__main__":
    HelloWorld().main()
