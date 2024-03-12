class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"이름: {self.name}, 전화번호: {self.phone_number}, 이메일: {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("연락처가 추가되었습니다.")

    def display_contacts(self):
        if self.contacts:
            print("주소록:")
            for contact in self.contacts:
                print(contact)
        else:
            print("주소록이 비어 있습니다.")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print(f"{name} 연락처가 삭제되었습니다.")
        else:
            print(f"{name}을(를) 찾을 수 없습니다.")

    def update_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            new_name = input(
                "새로운 이름을 입력하세요 (변경하지 않으려면 엔터를 누르세요): "
            )
            new_phone_number = input(
                "새로운 전화번호를 입력하세요 (변경하지 않으려면 엔터를 누르세요): "
            )
            new_email = input(
                "새로운 이메일을 입력하세요 (변경하지 않으려면 엔터를 누르세요): "
            )

            if new_name:
                contact.name = new_name
            if new_phone_number:
                contact.phone_number = new_phone_number
            if new_email:
                contact.email = new_email

            print(f"{name} 연락처가 업데이트되었습니다.")
        else:
            print(f"{name}을(를) 찾을 수 없습니다.")


def main():
    address_book = AddressBook()

    while True:
        print("\n주소록 애플리케이션")
        print("1. 연락처 추가")
        print("2. 연락처 목록 보기")
        print("3. 연락처 수정")
        print("4. 연락처 삭제")
        print("5. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            name = input("이름을 입력하세요: ")
            phone_number = input("전화번호를 입력하세요: ")
            email = input("이메일을 입력하세요: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)
        elif choice == "2":
            address_book.display_contacts()
        elif choice == "3":
            name = input("수정할 연락처의 이름을 입력하세요: ")
            address_book.update_contact(name)
        elif choice == "4":
            name = input("삭제할 연락처의 이름을 입력하세요: ")
            address_book.delete_contact(name)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택을 입력하세요.")


if __name__ == "__main__":
    main()
