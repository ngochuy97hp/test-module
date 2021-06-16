from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    name = fields.Char('Title', required=True, help="name of library book")
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    state = fields.Selection([('draft', 'Not Available'),
                            ('available', 'Available'),
                            ('lost', 'Lost')],
                            'State', default="draft", required=True)
    color = fields.Integer()

    def make_available(self):
        self.write({'state': 'available'})

    def make_lost(self):
        self.write({'state': 'lost'})
