from odoo import fields, models, api
from odoo.exceptions import UserError
import datetime
import requests
import json


class ScanQr(models.Model):
    _name = "user.ip.address"
    _description = "User Details"
    _rec_name= 'printer_name'

    printer_name = fields.Char(string='Printer Name')
    printer_ip = fields.Char(string='Printer Ip Address')

