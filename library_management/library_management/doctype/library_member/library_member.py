# Copyright (c) 2023, Saba Fadhl and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	