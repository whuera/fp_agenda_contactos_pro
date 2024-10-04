
"""
This module provides functionalities to manage a contact list, including loading, saving, searching, updating, 
and deleting contacts. Contacts are stored in a text file with each contact's name, phone, and email.
Functions:
    load_contacts():
        Loads contacts from the file specified by FILENAME.
        Returns a list of contacts.
    save_contacts(contacts):
        Saves the given list of contacts to the file specified by FILENAME.
    search_contacts(pattern, field):
        Searches for contacts matching the given pattern in the specified field (name, phone, or email).
        Supports wildcards (*) in the pattern.
        Returns a list of matching contacts.
    update_contact(search_field, search_pattern, update_data):
        Updates contacts matching the given search pattern in the specified search field.
        The update_data dictionary specifies the fields to update and their new values.
        Prints a message indicating whether any contacts were updated.
    delete_contact(search_field, search_pattern):
        Deletes contacts matching the given search pattern in the specified search field.
        Prints a message indicating whether any contacts were deleted.
    add_contact(name, phone, email):
        Adds a new contact with the given name, phone, and email.
        Prints a message indicating that the contact was added.
    show_contacts():
        Displays all contacts.
Usage:
    The module can be run as a standalone script, providing a command-line interface for managing contacts.
    The user can choose to show all contacts, add a new contact, search for contacts, update a contact, 
    delete a contact, or exit the program.
"""
import os
import re

# Nombre del archivo donde se almacenan los contactos
FILENAME = "/Users/whuera/Documents/Ecuador/UEES/Fundamentos de programación/TallerPractico5/contactos.txt"
# Función para cargar los contactos del archivo
def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

# Función para guardar los contactos en el archivo
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# Búsqueda avanzada de contactos con soporte de wildcards
def search_contacts(pattern, field):
    contacts = load_contacts()
    regex = re.compile(pattern.replace("*", ".*"), re.IGNORECASE)
    return [contact for contact in contacts if regex.match(contact[field])]

# Actualización de contactos por cualquier campo
def update_contact(search_field, search_pattern, update_data):
    contacts = load_contacts()
    regex = re.compile(search_pattern.replace("*", ".*"), re.IGNORECASE)
    updated = False

    for contact in contacts:
        if regex.match(contact[search_field]):
            for key, value in update_data.items():
                contact[key] = value
            updated = True
    
    if updated:
        save_contacts(contacts)
        print("Contacto(s) actualizado(s) correctamente.")
    else:
        print("No se encontraron contactos que coincidan con el patrón.")

# Eliminación de contactos por cualquier campo
def delete_contact(search_field, search_pattern):
    contacts = load_contacts()
    regex = re.compile(search_pattern.replace("*", ".*"), re.IGNORECASE)
    new_contacts = [contact for contact in contacts if not regex.match(contact[search_field])]

    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print("Contacto(s) eliminado(s) correctamente.")
    else:
        print("No se encontraron contactos que coincidan con el patrón.")

# Añadir un nuevo contacto
def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contacto añadido correctamente.")

# Mostrar todos los contactos
def show_contacts():
    contacts = load_contacts()
    for contact in contacts:
        print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Correo: {contact['email']}")
        
def menu():
    while True:
        print("\nGestión de Contactos:")
        print("1. Mostrar todos los contactos")
        print("2. Añadir un nuevo contacto")
        print("3. Buscar contactos")
        print("4. Actualizar un contacto")
        print("5. Eliminar un contacto")
        print("6. Salir")
        
        option = input("Seleccione una opción: ")
        
        if option == "1":
            show_contacts()
        elif option == "2":
            name = input("Ingrese el nombre: ")
            phone = input("Ingrese el teléfono: ")
            email = input("Ingrese el correo electrónico: ")
            add_contact(name, phone, email)
        elif option == "3":
            field = input("Buscar por (name/phone/email): ")
            pattern = input("Ingrese el patrón de búsqueda (use * como wildcard): ")
            results = search_contacts(pattern, field)
            if results:
                for contact in results:
                    print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Correo: {contact['email']}")
            else:
                print("No se encontraron contactos que coincidan con el patrón.")
        elif option == "4":
            field = input("Buscar contacto a actualizar por (name/phone/email): ")
            pattern = input("Ingrese el patrón de búsqueda (use * como wildcard): ")
            update_data = {}
            if input("¿Actualizar nombre? (s/n): ").lower() == "s":
                update_data["name"] = input("Nuevo nombre: ")
            if input("¿Actualizar teléfono? (s/n): ").lower() == "s":
                update_data["phone"] = input("Nuevo teléfono: ")
            if input("¿Actualizar correo? (s/n): ").lower() == "s":
                update_data["email"] = input("Nuevo correo: ")
            update_contact(field, pattern, update_data)
        elif option == "5":
            field = input("Buscar contacto a eliminar por (name/phone/email): ")
            pattern = input("Ingrese el patrón de búsqueda (use * como wildcard): ")
            delete_contact(field, pattern)
        elif option == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejemplo de uso de las funciones del programa
if __name__ == "__main__":
    menu()