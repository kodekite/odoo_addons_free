# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class UserAllowedInv(models.Model):
    _name = 'account.config.settings.inv.user.allowed'

    # user_allowed_ids = fields.Many2many('res.users', 'inv_config_user_relate','user_allowed_id')
    user_allowed_id = fields.Many2one('res.users', string="User")

class InvTreeFilter(models.Model):    
    _inherit = "account.invoice"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        user_login_id = self.env.user.id
        self.env.cr.execute('SELECT ai.id, ai.create_uid, ai.user_id FROM account_invoice ai LEFT JOIN account_config_settings_inv_user_allowed icur ON icur.user_allowed_id = %s WHERE ai.create_uid = %s OR ai.user_id = %s OR icur.user_allowed_id = %s' %(user_login_id,user_login_id,user_login_id,user_login_id))
        invoices_list = []
        for rec in self.env.cr.fetchall():
            invoices_list.append(rec[0])

        domain.extend([['company_id', '=', self.env.user.company_id.id]])        
        domain.extend([['id', 'in', list(set(invoices_list))]])

        return super(InvTreeFilter, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)