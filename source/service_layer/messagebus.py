from source.domain import events


class mail:
    def send_mail(mail_id, message):
        print(f"Event generated {mail_id} and {message}")


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


def create_product(event: events.ProductCreated):
    mail.send_mail(
        "prabin@gmail.com",
        "prabin created a product"

    )


def update_product(event: events.ProductUpdated):
    mail.send_mail(
        "prabin@gmail.com",
        "prabin updated a product"
    )


HANDLERS = {
    events.ProductCreated: [create_product],
    events.ProductUpdated: [update_product]
}
