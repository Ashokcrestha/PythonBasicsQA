#16.Create a BugReport class with:
#bug_id
#itle
#severity
#method show_report() 


class BugReport:
    def __init__(self, bug_id, title, severity):
        self.bug_id = bug_id
        self.title = title
        self.severity = severity

    def show_report(self):
        print("Bug ID:", self.bug_id)
        print("Title:", self.title)
        print("Severity:", self.severity)


report = BugReport(101, "Login button not working", "High")
report.show_report()
