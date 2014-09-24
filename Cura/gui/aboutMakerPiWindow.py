__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx
import platform

class aboutMakerPiWindow(wx.Dialog):
	def __init__(self):
		super(aboutMakerPiWindow, self).__init__(None, title=_("About"))

		wx.EVT_CLOSE(self, self.OnClose)

		p = wx.Panel(self)
		self.panel = p
		s = wx.BoxSizer()
		self.SetSizer(s)
		s.Add(p, flag=wx.ALL, border=15)
		s = wx.BoxSizer(wx.VERTICAL)
		p.SetSizer(s)

		title = wx.StaticText(p, -1, _("MakerPi"))
		title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		s.Add(title, flag=wx.ALIGN_CENTRE|wx.EXPAND|wx.BOTTOM, border=5)

		self.addComponent(_("Website"), "http://www.makerpi.org")
		self.Fit()

	def addComponent(self, name, description):
		p = self.panel
		s = p.GetSizer()
		s.Add(wx.StaticText(p, -1, '%s : %s' % (name, description)), flag=wx.TOP, border=5)
		s.Add(wx.StaticText(p, -1, '' ))
	def OnClose(self, e):
		self.Destroy()
