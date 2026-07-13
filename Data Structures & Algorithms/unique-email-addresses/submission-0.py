class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_email = set()

        for email in emails:
            local, domain = email.split("@")

            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                local = local.split("+")[0]

            uniq_email.add(local + "@" + domain)

        return len(uniq_email)
