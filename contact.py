class Contact(object):
    """docstring for ClassName"""
    def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = ""
       self.email = ""

    def send_text(self, message):
        return "To:", self.phone,":", message

    def print_name(self, message):
        return "To:", self.first_name, ":", message

def main():
    contact_list = []

    contact_michelle = Contact('Michelle','Davis')
    contact_michelle.phone = 6789900000
    contact_michelle.email = 'mdavis@gmail.com'
    contact_jim = Contact('Jim','Lee')
    contact_jim.phone = 80090007000
    contact_jim.email = 'jim@aol.com'
    contact_polly = Contact('Polly','Hart')
    contact_polly.phone = 3889007665
    contact_polly.email = 'phart@gmail.com'

    contact_list.append(contact_michelle)
    contact_list.append(contact_polly)
    contact_list.append(contact_jim)

    for name in contact_list:
        print name.first_name
        print name.last_name
        print name.phone
        print name.email

    for name in contact_list:
        print name.print_name('Hello')

if __name__ == '__main__':
    main()