from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from books.models import Transaction
from datetime import date

class Command(BaseCommand):
    help = 'Send email notifications for overdue books'

    def handle(self, *args, **kwargs):
        overdue_transactions = Transaction.objects.filter(return_date__isnull=True)
        for transaction in overdue_transactions:
            if transaction.is_overdue():
                user_email = transaction.user.user.email
                book_title = transaction.book.title
                due_date = transaction.check_out_date + timedelta(days=14)

                send_mail(
                    subject='Overdue Book Notification',
                    message=f'Dear {transaction.user.user.username},\n\nThe book "{book_title}" you borrowed is overdue. It was due on {due_date}. Please return it as soon as possible.\n\nThank you.',
                    from_email='lawrencenjobo9@gmail.com',
                    recipient_list=[user_email],
                )

        self.stdout.write(self.style.SUCCESS('Overdue notifications sent successfully.'))