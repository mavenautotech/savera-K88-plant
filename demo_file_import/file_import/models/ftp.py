from odoo import api, models, fields, _


class FTPConfig(models.Model):
    _name = "ftp.config"
    """This model is used for store FTP credential."""
    
    ftp_user_id = fields.Char("FTP User ID", required=True, help="Please Enter ftp User ID carefullly. It is Case Sensitive data.")
    ftp_password = fields.Char("FTP Password", required=True, help="Please Enter ftp Password carefullly. It is Case Sensitive data.")
    ftp_path_testing = fields.Char("FTP Path Testing",help="Please Enter FTP Path.")