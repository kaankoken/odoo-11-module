from odoo.addons.account_invoices import account_invoices
from num2words import num2words as nb
from googletrans import Translator


class CustomAccountInvoice(account_invoices.account_invoices):
    _name = "custom_invoice"
    destination = 'tr'
    
    def num_to_text(amount_total):
        temp_amount_tot = amount_total.replace(",", "")
        temp_amount_tot = temp_amount_tot.split(".")
        
        if contain_except_zero(temp_amount_tot[1]) == 0:
            this.text_amount = "#" + translation(temp_amount_tot[0]) + "#"
        else:
            this.text_amount = "#" + translation(temp_amount_tot[0]) + translation(temp_amount_tot[1]) + "#"
      
        def contain_except_zero(temp_amount_tot):
            i = 0
            while i < len(temp_amount_tot):
                if temp_amount_tot[i] != '0':
                    return 1
                i = i + 1
            return 0

        def translation(temp_amount_tot):
            tr = Translator()
            translated_num = tr.translate(nb(temp_amount_tot), dest=destination)
            translated_num = translated_num.text
            translated_num = translated_num.replace(',', '').replace(' ', '')

            return translated_num
