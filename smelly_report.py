from datetime import datetime

class ReportGenerator:

    def generate_daily_report(self, data):
        total = 0
        count = 0
        for item in data:
            if item.date.day == datetime.now().day:
                total += item.value
                count += 1

        average = total / count if count > 0 else 0

        report = f"Daily Report\n"
        report += f"Total: {total}\n"
        report += f"Count: {count}\n"
        report += f"Average: {average:.2f}\n"
        report += f"Generated: {datetime.now()}\n"

        return report


    def generate_weekly_report(self, data):
        total = 0
        count = 0
        for item in data:
            if item.date.isocalendar()[1] == datetime.now().isocalendar()[1]:
                total += item.value
                count += 1

        average = total / count if count > 0 else 0

        report = f"Weekly Report\n"
        report += f"Total: {total}\n"
        report += f"Count: {count}\n"
        report += f"Average: {average:.2f}\n"
        report += f"Generated: {datetime.now()}\n"

        return report


    def generate_monthly_report(self, data):
        total = 0
        count = 0
        for item in data:
            if item.date.month == datetime.now().month:
                total += item.value
                count += 1

        average = total / count if count > 0 else 0

        report = f"Monthly Report\n"
        report += f"Total: {total}\n"
        report += f"Count: {count}\n"
        report += f"Average: {average:.2f}\n"
        report += f"Generated: {datetime.now()}\n"

        return report